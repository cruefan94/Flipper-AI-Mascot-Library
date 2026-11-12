#!/usr/bin/env python3
"""Expand approved Fox keyframes into independently timed 128x64 PNG clips.
Requires Pillow: pip install Pillow
Run: python tools/export_fox.py
"""
from pathlib import Path
from PIL import Image
import base64, json, zlib

ROOT = Path(__file__).resolve().parents[1]
NAMES = ["idle", "smile", "happy", "talk", "chat", "listening", "thinking", "processing", "idea", "scanning", "connected", "sleeping"]
encoded = (ROOT / "characters/AI_Fox/keyframes.zlib.b64").read_text().strip()
data = zlib.decompress(base64.b64decode(encoded))
assert len(data) == len(NAMES) * 1024, "Invalid 128x64 1bpp frame data"
catalog = {"character": "AI_Fox", "size": [128,64], "colors": 2, "clips": {}}
for i, name in enumerate(NAMES):
    img = Image.frombytes("1", (128,64), data[i*1024:(i+1)*1024])
    directory = ROOT / "characters/AI_Fox/clips" / name
    directory.mkdir(parents=True, exist_ok=True)
    timing = [250,180,250,180][i % 4]
    for j, y_shift in enumerate([0,-1,0,1]):
        frame = Image.new("1",(128,64),0)
        frame.paste(img,(0,y_shift))
        frame.save(directory / f"frame_{j:02d}.png")
    meta = {"name":name,"frame_count":4,"frame_duration_ms":timing,"loop":True,"playback":"sequential"}
    (directory / "meta.json").write_text(json.dumps(meta,indent=2)+"\n")
    catalog["clips"][name] = meta
(ROOT / "characters/AI_Fox/manifest.json").write_text(json.dumps(catalog,indent=2)+"\n")
print("Exported 12 independently timed clips, 48 frames total.")

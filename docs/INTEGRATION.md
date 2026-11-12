# Integration notes

This library is **not** merged into any project. Import explicitly after reviewing compatibility.

1. Extract the standalone asset ZIP locally.
2. Select a single clip under `momentum_source/AI_Dolphin/Anims/AI_*`.
3. Respect the clip's `meta.txt` frame timing; play frames in sequence rather than showing a contact sheet.
4. Convert source PNG frames to the `.bm` format required by the target Momentum build, adjust metadata to the exact firmware version, and test on hardware.
5. Keep AI/network event bindings optional. The mascot pack contains artwork and animation metadata, not Bluetooth logic.

Do not install source PNG files as if they were compiled firmware animations.

# Flipper AI Mascot Library

Standalone, opt-in mascot animation layer for Flipper Zero / Momentum experiments. Kept separate from the two Flipper AI firmware projects.

## Current approved mascot
- AI Dolphin, monochrome, designed for a 128 × 64 Flipper display.
- Individual sequential animations (idle, smile, wave, talk, think, scan, celebrate, dance, sleep, alert, connected, wink).
- Animations use individual frames and timing metadata, **not** a simultaneous sprite-grid playback.

## Package status
The existing local v1 package contains source PNG frames, timing metadata, GIF previews and a layer manifest. These binaries have **not yet been published to this repository**. The conversion to Momentum-compatible .bm assets and real-device validation also remain to be done. Do not interpret this repository as a working firmware release.

## Approval policy
**Do not add or commit any new mascot character or newly designed animation unless the owner has reviewed its preview and explicitly approved saving it.** Experimental fox and other ideas remain unapproved.

## Isolation
No firmware source, Bluetooth AI integration, or other Flipper project is modified by this library.

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

## Unified Flipper AI project coordination

This repository is indexed in the [eight-repository Flipper AI ecosystem](https://github.com/cruefan94/Flipper-AI-Integration-Testing/blob/main/PROJECT_ECOSYSTEM.md). The [private project hub and future-ideas ledger](https://github.com/cruefan94/Flipper-AI-Momentum-/blob/main/docs/UNIFIED_PROJECT_HUB.md) records cross-repository priorities, dependencies, deferred concepts and testing boundaries (requires access to private repository).

**Linking a repository does not merge its source or change its integration/approval rules.** Continue to honor this repository's own release, privacy and testing restrictions. The owner's primary ChatGPT project conversation is the coordination point, not an automated chat or GitHub syncing service.

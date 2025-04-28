# iPhone Camera Streaming with Continuity Camera

This module provides functionality to stream video from an iPhone camera to a MacBook using Apple's Continuity Camera feature.

## Prerequisites

1. A MacBook running macOS Ventura or later
2. An iPhone running iOS 16 or later
3. Both devices must be:
   - Signed in to the same Apple ID
   - Have Bluetooth and WiFi enabled
   - Be within range of each other

## Setup

1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Enable Continuity Camera:
   - On your iPhone, go to Settings > General > AirDrop & Handoff
   - Make sure "Continuity Camera" is enabled
   - On your MacBook, go to System Settings > General > AirDrop & Handoff
   - Make sure "Continuity Camera" is enabled

## Usage

Simply run the streaming script:

```bash
python ip_camera_stream.py
```

The script will automatically detect and connect to your iPhone's camera.

## Controls

- Press 'q' to quit the stream

## Troubleshooting

1. Make sure both your iPhone and MacBook are signed in to the same Apple ID
2. Verify that Continuity Camera is enabled on both devices
3. Ensure Bluetooth and WiFi are enabled on both devices
4. Try bringing your iPhone closer to your MacBook if connection issues occur
5. If the camera isn't detected, try disconnecting and reconnecting your iPhone 
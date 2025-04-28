# iPhone Camera Streaming

This module provides functionality to stream video from an iPhone camera to a computer using OpenCV.

## Setup

1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. On your iPhone:
   - Install the "IP Webcam" app from the App Store
   - Connect your iPhone to the same WiFi network as your computer
   - Open the IP Webcam app
   - Tap "Start server" at the bottom of the screen
   - Note the IP address and port shown in the app

## Usage

Run the streaming script with your iPhone's IP address:

```bash
python ip_camera_stream.py --ip YOUR_IPHONE_IP_ADDRESS
```

Optional arguments:
- `--port`: Port number (default: 8080)

Example:
```bash
python ip_camera_stream.py --ip 192.168.1.100 --port 8080
```

## Controls

- Press 'q' to quit the stream

## Troubleshooting

1. Make sure both your iPhone and computer are on the same WiFi network
2. Verify that the IP address and port are correct
3. Check that the IP Webcam app is running on your iPhone
4. If experiencing lag, try adjusting the video quality in the IP Webcam app settings 
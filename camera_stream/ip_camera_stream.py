import cv2
import numpy as np
import time
import argparse
import subprocess
import os
import platform

def create_info_plist():
    """
    Create an Info.plist file with the required Continuity Camera settings
    """
    info_plist_content = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>NSCameraUseContinuityCameraDeviceType</key>
    <true/>
</dict>
</plist>"""
    
    with open('Info.plist', 'w') as f:
        f.write(info_plist_content)

def list_cameras():
    """
    List all available cameras using system_profiler
    """
    try:
        result = subprocess.run(['system_profiler', 'SPCameraDataType'], 
                              capture_output=True, text=True)
        print("\nAvailable cameras:")
        for line in result.stdout.split('\n'):
            if 'Camera' in line and ':' in line:
                print(f"  {line.strip()}")
        print()
    except Exception as e:
        print(f"Warning: Could not list cameras: {e}")

def connect_to_continuity_camera():
    """
    Connect to iPhone camera using Continuity Camera
    Returns:
        cv2.VideoCapture object
    """
    
    create_info_plist() # create info.plist with continuity camera settings
    
    list_cameras()
        
    if platform.system() == 'Darwin':  # macOS; on macOS, try diff approaches to access the continuity camera
        
        backends = [ # try diff backends
            (cv2.CAP_AVFOUNDATION, "AVFoundation"),
            (cv2.CAP_ANY, "Any"),
            (cv2.CAP_V4L2, "V4L2")
        ]
        
        for backend, backend_name in backends:
            print(f"\nTrying {backend_name} backend...")
            
            
            for i in range(10): # try the first 10 camera indices
                print(f"  Trying camera index {i}...")
                cap = cv2.VideoCapture(i, backend)
                
                if cap.isOpened():
                    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
                    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
                    
                    ret, frame = cap.read() # try to read a frame
                    if ret:
                        # try and see if this is the iphone camera, since they usually have higher resolution
                        width = cap.get(cv2.CAP_PROP_FRAME_WIDTH) #
                        height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
                        
                        if width >= 1920 and height >= 1080:
                            print(f"Successfully connected to iPhone camera using {backend_name} backend at index {i}")
                            return cap
                        else:
                            print(f"  Camera {i} opened but might not be iPhone (resolution: {width}x{height})")
                            cap.release()
                    else:
                        print(f"  Camera {i} opened but failed to read frame")
                        cap.release()
                else:
                    print(f"  Failed to open camera {i}")
    
    raise Exception(
        "Could not find iPhone camera. Please ensure:\n"
        "1. Your iPhone is nearby and unlocked\n"
        "2. Continuity Camera is enabled on both devices\n"
        "3. Both devices are signed in to the same Apple ID\n"
        "4. Bluetooth and WiFi are enabled on both devices\n"
        "5. Try bringing your iPhone closer to your MacBook\n"
        "6. Try restarting the Continuity Camera feature on both devices\n"
        "7. Try restarting your iPhone and MacBook"
    )

def main():
    parser = argparse.ArgumentParser(description='Stream video from iPhone using Continuity Camera')
    args = parser.parse_args()
    
    try:
        # Connect to the camera
        cap = connect_to_continuity_camera()
        
        print("Successfully connected to iPhone camera")
        print("Press 'q' to quit")
        
        while True:
            ret, frame = cap.read() # read the frame from the camera stream
            
            if not ret:
                print("Failed to grab frame")
                break
            
            cv2.imshow('iPhone Camera Stream', frame) # display the frame
            
            if cv2.waitKey(1) & 0xFF == ord('q'): # break the loop if 'q' is pressed
                break
                
    except Exception as e:
        print(f"Error: {e}")
    
    finally:
        if 'cap' in locals():
            cap.release()
        cv2.destroyAllWindows()
        # Clean up Info.plist
        if os.path.exists('Info.plist'):
            os.remove('Info.plist')

if __name__ == "__main__":
    main() 
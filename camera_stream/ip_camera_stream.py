import cv2
import numpy as np
import time
import argparse
import subprocess
import os

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

def get_continuity_camera_index():
    """
    Find the index of the Continuity Camera (iPhone) using system_profiler
    Returns:
        int: Index of the Continuity Camera, or None if not found
    """
    try:
        # Use system_profiler to get camera information
        result = subprocess.run(['system_profiler', 'SPCameraDataType'], 
                              capture_output=True, text=True)
        
        # Look for iPhone or Continuity Camera in the output
        for i, line in enumerate(result.stdout.split('\n')):
            if 'iPhone' in line or 'Continuity Camera' in line:
                # The camera index is typically the number of cameras before this one
                return i
    except Exception as e:
        print(f"Warning: Could not detect Continuity Camera: {e}")
    return None

def connect_to_continuity_camera():
    """
    Connect to iPhone camera using Continuity Camera
    Returns:
        cv2.VideoCapture object
    """
    # Create Info.plist with Continuity Camera settings
    create_info_plist()
    
    # First, try to find the Continuity Camera index
    camera_index = get_continuity_camera_index()
    
    if camera_index is not None:
        print(f"Found Continuity Camera at index {camera_index}")
        # Try to use the Continuity Camera specifically
        cap = cv2.VideoCapture(camera_index, cv2.CAP_AVFOUNDATION)
        
        if cap.isOpened():
            # Set properties for better quality
            cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
            cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
            
            # Verify we can read frames
            ret, frame = cap.read()
            if ret:
                print("Successfully connected to iPhone camera")
                return cap
            else:
                print("Failed to read from iPhone camera")
                cap.release()
    
    # If we couldn't find or connect to the Continuity Camera, try all indices
    print("Trying to find iPhone camera...")
    for i in range(10):
        print(f"Trying camera index {i}...")
        cap = cv2.VideoCapture(i, cv2.CAP_AVFOUNDATION)
        
        if cap.isOpened():
            # Set properties for better quality
            cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
            cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
            
            ret, frame = cap.read()
            if ret:
                print(f"Successfully connected to camera at index {i}")
                return cap
            else:
                print(f"Camera {i} opened but failed to read frame")
                cap.release()
        else:
            print(f"Failed to open camera {i}")
    
    raise Exception(
        "Could not find iPhone camera. Please ensure:\n"
        "1. Your iPhone is nearby and unlocked\n"
        "2. Continuity Camera is enabled on both devices\n"
        "3. Both devices are signed in to the same Apple ID\n"
        "4. Bluetooth and WiFi are enabled on both devices\n"
        "5. Try bringing your iPhone closer to your MacBook\n"
        "6. Try restarting the Continuity Camera feature on both devices"
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
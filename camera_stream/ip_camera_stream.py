import cv2
import numpy as np
import time
import argparse

def connect_to_continuity_camera():
    """
    Connect to iPhone camera using Continuity Camera
    Returns:
        cv2.VideoCapture object
    """
    # Note: on macOS, we use the avfoundation backend.  The camera index for Continuity Camera is typically the last available camera, so we'll try to find it automatically
    for i in range(10):  # try first 10 indices
        cap = cv2.VideoCapture(i, cv2.CAP_AVFOUNDATION)
        if cap.isOpened():
            ret, frame = cap.read() # try to read a frame to verify it's working
            if ret:
                print(f"Found Continuity Camera at index {i}")
                return cap
            cap.release()
    
    raise Exception("Could not find Continuity Camera. Make sure your iPhone is connected and Continuity Camera is enabled.")

def main():
    parser = argparse.ArgumentParser(description='Stream video from iPhone using Continuity Camera')
    args = parser.parse_args()
    
    try:
        cap = connect_to_continuity_camera()
        
        print("Successfully connected to Continuity Camera")
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

if __name__ == "__main__":
    main() 
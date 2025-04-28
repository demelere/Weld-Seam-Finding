import cv2
import numpy as np
import time
import argparse

def connect_to_ip_camera(ip_address, port=8080):
    """
    Connect to IP Webcam stream from iPhone
    Args:
        ip_address (str): IP address of the iPhone
        port (int): Port number (default is 8080 for IP Webcam)
    Returns:
        cv2.VideoCapture object
    """
    url = f'http://{ip_address}:{port}/video' # construct the URL for the video stream
    
    cap = cv2.VideoCapture(url)
    
    if not cap.isOpened():
        raise Exception("Could not connect to the camera stream")
    
    return cap

def main():
    parser = argparse.ArgumentParser(description='Stream video from iPhone camera')
    parser.add_argument('--ip', type=str, required=True, help='IP address of the iPhone')
    parser.add_argument('--port', type=int, default=8080, help='Port number (default: 8080)')
    args = parser.parse_args()
    
    try:
        cap = connect_to_ip_camera(args.ip, args.port)
        
        print(f"Successfully connected to camera stream at {args.ip}:{args.port}")
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
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
    # Construct the URL for the video stream
    url = f'http://{ip_address}:{port}/video'
    
    # Create VideoCapture object
    cap = cv2.VideoCapture(url)
    
    if not cap.isOpened():
        raise Exception("Could not connect to the camera stream")
    
    return cap

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Stream video from iPhone camera')
    parser.add_argument('--ip', type=str, required=True, help='IP address of the iPhone')
    parser.add_argument('--port', type=int, default=8080, help='Port number (default: 8080)')
    args = parser.parse_args()
    
    try:
        # Connect to the camera
        cap = connect_to_ip_camera(args.ip, args.port)
        
        print(f"Successfully connected to camera stream at {args.ip}:{args.port}")
        print("Press 'q' to quit")
        
        while True:
            # Read frame from the stream
            ret, frame = cap.read()
            
            if not ret:
                print("Failed to grab frame")
                break
            
            # Display the frame
            cv2.imshow('iPhone Camera Stream', frame)
            
            # Break the loop if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
                
    except Exception as e:
        print(f"Error: {e}")
    
    finally:
        # Release resources
        if 'cap' in locals():
            cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main() 
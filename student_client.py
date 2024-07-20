import cv2
import socket
import numpy as np

# Function to receive frames from the server (invigilator)
def receive_frames():
    # Initialize socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))
    
    while True:
        # Receive frame from the server
        frame_bytes = client_socket.recv(4096)
        
        # Decode frame bytes
        frame_array = np.frombuffer(frame_bytes, dtype=np.uint8)
        
        # Decode frame
        frame = cv2.imdecode(frame_array, flags=cv2.IMREAD_COLOR)
        
        # Display frame
        cv2.imshow('Exam Session', frame)
        
        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Close the connection
    client_socket.close()

if __name__ == "__main__":
    receive_frames()

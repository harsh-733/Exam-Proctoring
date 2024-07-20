import cv2
import socket

# Function to send frames to the client (student)
def send_frames(conn, addr):
    # Initialize video capture object
    cap = cv2.VideoCapture(0)
    
    while True:
        # Capture frame-by-frame
        _, frame = cap.read()
        
        # Convert frame to bytes
        frame_bytes = cv2.imencode('.jpg', frame)[1].tobytes()
        
        # Send frame to the client
        conn.send(frame_bytes)
        
        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Release the capture
    cap.release()
    cv2.destroyAllWindows()

# Main function
def main():
    # Initialize socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)
    
    print("Waiting for a connection...")
    conn, addr = server_socket.accept()
    print("Connected to:", addr)
    
    # Send frames to the client
    send_frames(conn, addr)
    
    # Close the connection
    conn.close()

if __name__ == "__main__":
    main()

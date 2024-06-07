import cv2
import socket
import pickle
import struct

def main():
    # Define the socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Allow reuse of the address
    host_ip = '0.0.0.0'  # Listen on all available interfaces
    port = 9999
    socket_address = (host_ip, port)
    
    # Bind the socket to the address and port
    server_socket.bind(socket_address)
    
    # Start listening for connections
    server_socket.listen(5)
    print("Listening at:", socket_address)
    
    # Accept the connection
    client_socket, addr = server_socket.accept()
    print('Connection from:', addr)
    
    # Open the camera
    cap = cv2.VideoCapture(0)  # 0 is the default camera
    
    # Capture a single frame
    ret, frame = cap.read()
    
    # Check if the frame was captured successfully
    if ret:
        # Serialize the frame
        data = pickle.dumps(frame)
        
        # Send the size of the data first
        message_size = struct.pack("Q", len(data))
        
        # Then send the data
        client_socket.sendall(message_size + data)
    else:
        print("Failed to capture image.")
    
    # Release resources
    cap.release()
    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    main()
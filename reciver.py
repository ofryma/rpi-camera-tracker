import cv2
import socket
import pickle
import struct
import json

def main():
    # Define the socket
    
    with open("sender_host_config.json" , "r") as f:
        sender_info = json.loads(f.read())
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    socket_address = (sender_info["IP"], sender_info["PORT"])

    # Connect to the server
    client_socket.connect(socket_address)
    
    data = b""
    payload_size = struct.calcsize("Q")
    
    while True:
        # Retrieve message size
        while len(data) < payload_size:
            packet = client_socket.recv(4 * 1024)  # 4K chunks
            if not packet:
                break
            data += packet
        
        if len(data) < payload_size:
            break
        
        packed_msg_size = data[:payload_size]
        data = data[payload_size:]
        msg_size = struct.unpack("Q", packed_msg_size)[0]
        
        # Retrieve the entire message data based on message size
        while len(data) < msg_size:
            packet = client_socket.recv(4 * 1024)
            if not packet:
                break
            data += packet
        
        if len(data) < msg_size:
            break
        
        frame_data = data[:msg_size]
        data = data[msg_size:]
        
        # Deserialize the frame
        frame = pickle.loads(frame_data)
        
        # Display the frame
        cv2.imshow("Receiving Video", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    client_socket.close()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

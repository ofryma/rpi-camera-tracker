import cv2
import socket
import pickle
import struct

def main():
    # Define the socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host_ip = '192.168.1.100'  # Replace with the IP address of the Raspberry Pi
    port = 9999
    socket_address = (host_ip, port)
    
    # Connect to the server
    client_socket.connect(socket_address)
    
    data = b""
    payload_size = struct.calcsize("Q")
    
    while True:
        while len(data) < payload_size:
            packet = client_socket.recv(4*1024)  # 4K chunks
            if not packet:
                break
            data += packet
        
        packed_msg_size = data[:payload_size]
        data = data[payload_size:]
        msg_size = struct.unpack("Q", packed_msg_size)[0]
        
        while len(data) < msg_size:
            data += client_socket.recv(4*1024)
        
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

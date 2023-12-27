import socket
import time

def main():
    host = '0.0.0.0'  # Server IP address
    port = 9898       # Server port

    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to the server
        client_socket.connect((host, port))
        print("Connected to server")

        # Send data to the server
        hex_message = '00010000000600050000FF00' # Hex representation
        print("len = ", len(hex_message))
        print(bytes.fromhex(hex_message))
        client_socket.send(bytes.fromhex(hex_message))

        # Receive data from the server
        response = client_socket.recv(1024)  # Receive bytes and convert to hex
        print("Received from server", response)

    except Exception as e:
        print("Error:", e)

    finally:
        # Close the socket connection
        client_socket.close()
        print("Connection closed")

if __name__ == "__main__":
    s = time.time()
    main()
    print("Time: ", time.time() - s)

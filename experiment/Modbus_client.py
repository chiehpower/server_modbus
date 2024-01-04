import socket
import time


def generate_modbus_rtu_message(address, function_code, register_address, data):
    # Convert values to hex strings
    address_hex = format(address, '02x')
    function_code_hex = format(function_code, '02x')
    register_address_hex = format(register_address, '04x')
    data_hex = format(data, '04x')

    # Concatenate the hex strings to form the Modbus RTU message
    modbus_rtu_message = address_hex + \
        function_code_hex + register_address_hex + data_hex

    return modbus_rtu_message


def main():
    host = '0.0.0.0'  # Server IP address
    port = 502       # Server port
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to the server
        client_socket.connect((host, port))
        print("Connected to server")

        # Send data to the server
        # 使用範例
        address = 100         # Modbus 地址
        function_code = 3   # 功能碼：寫單個保持寄存器
        register_address =   # 寄存器地址
        data = 2            # 要寫入的數據

        hex_message = generate_modbus_rtu_message(
            address, function_code, register_address, data)
        print("Hex Message:", hex_message)
        # hex_message = '00010000000600050000FF00' # Hex representation
        print("len = ", len(hex_message))
        print(bytes.fromhex(hex_message))
        client_socket.send(bytes.fromhex(hex_message))

        # Receive data from the server
        # response = client_socket.recv(1024)  # Receive bytes and convert to hex
        # print("Received from server", response)

    except Exception as e:
        print("Error:", e)

    finally:
        # Close the socket connection
        client_socket.close()
        print("Connection closed")

if __name__ == "__main__":

    # for i in range(100):
    s = time.time()
    main()
    print("Time: ", time.time() - s)

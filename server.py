# # Modbus server (TCP)
# from pymodbus.server import StartTcpServer
# from pymodbus.device import ModbusDeviceIdentification
# from pymodbus.datastore import ModbusSequentialDataBlock
# from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext


# def run_async_server():
#     nreg = 200
#     # initialize data store
#     store = ModbusSlaveContext(
#         di=ModbusSequentialDataBlock(0, [15]*nreg),
#         co=ModbusSequentialDataBlock(0, [16]*nreg),
#         hr=ModbusSequentialDataBlock(0, [17]*nreg),
#         ir=ModbusSequentialDataBlock(0, [18]*nreg))
#     context = ModbusServerContext(slaves=store, single=True)

#     # initialize the server information
#     identity = ModbusDeviceIdentification()
#     identity.VendorName = 'APMonitor'
#     identity.ProductCode = 'APM'
#     identity.VendorUrl = 'https://apmonitor.com'
#     identity.ProductName = 'Modbus Server'
#     identity.ModelName = 'Modbus Server'
#     identity.MajorMinorRevision = '3.0.2'

#     # TCP Server
#     StartTcpServer(context=context, host='0.0.0.0',
#                    identity=identity, address=("0.0.0.0", 5020))


# if __name__ == "__main__":
#     print('Modbus server started on localhost port 5020')
#     run_async_server()

import socket


def handle_request(request_data):
    # 在這裡處理收到的請求數據，這部分的邏輯需要根據實際應用和Modbus協議來定義
    # 這裡只是一個簡單的範例，你可能需要根據你的需求修改它

    # 這裡只是回傳一個簡單的確認消息
    return b'Hello from Modbus Server'


def main():
    host = '0.0.0.0'  # Server IP address
    port = 9898       # Server port

    # 創建一個socket對象
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 綁定到指定的IP地址和端口
    server_socket.bind((host, port))

    # 監聽連接
    server_socket.listen(1)
    print(f"Server listening on {host}:{port}")

    while True:
        # 接受客戶端連接
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")

        try:
            # 接收數據
            request_data = client_socket.recv(1024)
            print("Received data from client:", request_data)

            # 處理請求並獲取響應數據
            response_data = handle_request(request_data)

            # 發送響應給客戶端
            client_socket.send(response_data)
            print("Sent response to client")

        except Exception as e:
            print("Error:", e)

        finally:
            # 關閉與客戶端的連接
            client_socket.close()
            print("Connection with client closed")


if __name__ == "__main__":
    main()

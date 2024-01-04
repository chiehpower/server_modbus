"""
Maintainer: Chieh

Work with Modsim3.
Address: 0100
Length: 100
Device ID: 1
03: Holding register
"""

from pymodbus.client.sync import ModbusTcpClient
import random

SERVER_IP = '10.1.2.190'  # aka modbus slave
SERVER_PORT = 502
ADDRESS_START = 100
ADDRESS_LENGTH = 10
DEVICE_ID = 1

client = ModbusTcpClient(host=SERVER_IP, port=SERVER_PORT)
if not client.connect():  # .connect() returns True if connection established
    print("[Error] Fail to connect to modbus slave %s:%d." % (SERVER_IP, SERVER_PORT))
    exit()

res = client.read_holding_registers(address=ADDRESS_START, count=10, unit=DEVICE_ID)
results = res.registers  # shows the result, type: list
print(results)

# ---------------------------
## write an random value
print("[INFO] Now writing a random boolean value to address = {}.".format(ADDRESS_START))
rand_value = random.randint(10, 10000)
print(rand_value)
write_registers_response = client.write_register(
    address=ADDRESS_START, value=rand_value, unit=DEVICE_ID)
write_registers_response.isError()

# ---------------------------
# read the values
res = client.read_holding_registers(address=ADDRESS_START, count=10, unit=DEVICE_ID)
results = res.registers  # shows the result, type: list
print(results)

client.close()

"""
Maintainer: Chieh

Work with Modsim3.
Address: 0100
Length: 100
Device ID: 1
03: Holding register
"""

from pymodbus.client.sync import ModbusTcpClient
import time

UNIT = 0x1

client = ModbusTcpClient('10.1.2.190', port=502, timeout=1)

while True:
   request = client.read_holding_registers(100, 3)
   result = request.registers   # print(result.bits[0])
   print(result)
   print(result[0])
   time.sleep(1)
client.close()

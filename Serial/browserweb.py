import asyncio
import datetime
import random
import websockets
import serial
import io

ser = serial.Serial(
port='/dev/ttyAMA0',\
baudrate=9600,\
parity=serial.PARITY_NONE,\
stopbits=serial.STOPBITS_ONE,\
bytesize=serial.EIGHTBITS,\
timeout=0)

sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))
 
print("connected to: " + ser.portstr)

async def time(websocket, path):
    while True:
        x=sio.readline()
        print(x)
        await websocket.send(x)
        await asyncio.sleep(random.random() * 3)
        #response = await websocket.recv()
        #print(f"<<< {response}")
        #ser.write(b'{response}')
        
async def main():
    async with websockets.serve(time, "localhost", 5678):
        await asyncio.Future()  # run forever
asyncio.run(main())
import asyncio
import os
import websockets

LOG_FILE = "logfile.txt"

async def tail_log(websocket, path):
    last_read_position = 0

    with open(LOG_FILE, "rb") as file:
        file.seek(0, os.SEEK_END)
        file_size = file.tell()
        last_read_position = file_size  # Start tracking from the end

        if file_size > 0:

            file.seek(0, os.SEEK_END)
            buffer = []
            lines_to_send = []
            while file.tell() > 0 and len(lines_to_send) < 10:
                file.seek(-1, os.SEEK_CUR)
                char = file.read(1)
                if char == b'\n':
                    if buffer:
                        lines_to_send.append(b''.join(reversed(buffer)).decode())
                        buffer = []
                else:
                    buffer.append(char)
                file.seek(-1, os.SEEK_CUR)
            if buffer:
                lines_to_send.append(b''.join(reversed(buffer)).decode())

            # Send lines in the correct order
            for line in reversed(lines_to_send):
                print(f"Sending initial line: {line}")
                await websocket.send(line)


    while True:
        await asyncio.sleep(1)
        with open(LOG_FILE, "rb") as file:  # Open the file in binary mode
            file.seek(last_read_position)
            new_data = file.read()
            if new_data:
                new_lines = new_data.decode().splitlines()
                for line in new_lines:
                    if line:
                        print(f"Sending new line: {line}")
                        await websocket.send(line)
                last_read_position = file.tell()

async def main():
    print("Starting WebSocket server on ws://localhost:6789")
    async with websockets.serve(tail_log, "localhost", 6789):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
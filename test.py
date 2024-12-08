#!/usr/bin/env python3

def main():
    import sys
    try:
        with open("/tmp/test.txt", "a") as f:
            f.write(f"Test.py was run: {datetime.now()}\n")
    except Exception as e:
        with open("/tmp/test.txt", "a") as f:
            f.write(f"{datetime.now()} - Error: {str(e)}\n")
            
if __name__ == "__main__":
    main()
    import json
    import struct
    from datetime import datetime

    # def send_message(message):
    try:
    #     sys.stdout.write(json.dumps(message) + "\n")
    #     sys.stdout.flush()

        # # Read the incoming message
        # input_line = sys.stdin.readline()
        # if not input_line:
        #     return
        
        # message = json.loads(input_line.strip())
        # url = message.get("url", "Unknown URL")
        
        # # Write to file for testing purposes
        with open("/tmp/test.txt", "a") as f:
            f.write(f"Test.py was run: {datetime.now()}\n")
            # f.write(f"{datetime.now()} - Received URL: {url}\n")
        # with open("/tmp/test.txt", "a") as f:
        #     raw_length = sys.stdin.read(4)
        #     f.write(f"{datetime.now()} - Raw Length {raw_length}\n")
        #     if raw_length:
        #         message_length = struct.unpack('I', raw_length)[0]
        #         message = sys.stdin.read(message_length)
        #         sys.stdout.write(struct.pack('I', len(message)))
        #         sys.stdout.write(message)
        #         sys.stdout.flush()
        
        # # Send a response back to Chrome extension
        # send_message({"status": "success", "url": url})

    except Exception as e:
        with open("/tmp/test.txt", "a") as f:
            f.write(f"{datetime.now()} - Error: {str(e)}\n")
        # send_message({"status": "error", "message": str(e)})

if __name__ == "__main__":
    main()

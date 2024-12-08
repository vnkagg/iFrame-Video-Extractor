#!/usr/bin/env python3


import urllib.parse
import subprocess
import sys
import json
import struct


def run_chrome_with_url(url):
    # Encode the URL
    encoded_url = urllib.parse.quote(url, safe=':/?&=#')
    # Run Chrome with the encoded URL
    chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    subprocess.run([chrome_path, f'--app={encoded_url}'])
    
# def main():
#     if len(sys.argv) > 1:
#         input_url = sys.argv[1]
#         if input_url:
#             run_chrome_with_url(input_url)
#     else:
#         print("Please provide a URL along with the command.")




def send_message(message):
    message = json.dumps(message)
    encoded_message = message.encode("utf-8")
    sys.stdout.buffer.write(struct.pack("I", len(encoded_message)))
    sys.stdout.buffer.write(encoded_message)
    sys.stdout.buffer.flush()


def read_message():
    raw_length = sys.stdin.buffer.read(4)
    if len(raw_length) == 0:
        sys.exit(0)
    message_length = struct.unpack("I", raw_length)[0]
    message = sys.stdin.buffer.read(message_length).decode("utf-8")
    return json.loads(message)


def main():
    try:
        message = read_message()
        print(f"Received message: {message}")
        # Process the message and respond
        response = {"response": f"Message received; {message}"}
        send_message(response)
        run_chrome_with_url(message['url'])
    except Exception as e:
        # send_message({"error": str(e)})
        return


if __name__ == "__main__":
    main()
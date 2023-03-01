from datetime import datetime
import struct
import sys
import time
import traceback

from nrf24 import *

if __name__ == "__main__":

    address = '1SNSR'

    # Verify that address is between 3 and 5 characters.
    if not (2 < len(address) < 6):
        print(
            f'Invalid address {address}. Addresses must be between 3 and 5 ASCII characters.')
        sys.exit(1)

        # Create NRF24 object.
    # PLEASE NOTE: PA level is set to MIN, because test sender/receivers are often close to each other, and then MIN works better.
    nrf = NRF24(pi, ce=25, payload_size=RF24_PAYLOAD.DYNAMIC, channel=100,
                data_rate=RF24_DATA_RATE.RATE_250KBPS, pa_level=RF24_PA.MIN)
    nrf.set_address_bytes(len(address))

    # Listen on the address specified as parameter
    nrf.open_reading_pipe(RF24_RX_ADDR.P1, address)

    # Display the content of NRF24L01 device registers.
    nrf.show_registers()

    # Enter a loop receiving data on the address specified.
    try:
        print(f'Receive from {address}')
        count = 0
        while True:

            # As long as data is ready for processing, process it.
            while nrf.data_ready():
                # Count message and record time of reception.
                count += 1
                now = datetime.now()

                # Read pipe and payload for message.
                pipe = nrf.data_pipe()
                payload = nrf.get_payload()

                # Resolve protocol number.
                protocol = payload[0] if len(payload) > 0 else -1

                hex = ':'.join(f'{i:02x}' for i in payload)

                # Show message received as hex.
                print(
                    f"{now:%Y-%m-%d %H:%M:%S.%f}: pipe: {pipe}, len: {len(payload)}, bytes: {hex}, count: {count}")

                # If the length of the message is 9 bytes and the first byte is 0x01, then we try to interpret the bytes
                # sent as an example message holding a temperature and humidity sent from the "simple-sender.py" program.
                if len(payload) == 9 and payload[0] == 0x01:
                    values = struct.unpack("<Bff", payload)
                    print(
                        f'Protocol: {values[0]}, temperature: {values[1]}, humidity: {values[2]}')

            # Sleep 100 ms.
            time.sleep(0.1)

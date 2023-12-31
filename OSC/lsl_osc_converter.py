"""Small example OSC client

This program sends 10 random values between 0.0 and 1.0 to the /filter address,
waiting for 1 seconds between each value.
"""
import argparse
import random
import time
from pylsl import StreamInlet, resolve_stream, resolve_bypred

from pythonosc import udp_client


#streams = resolve_stream('name', 'auralsl')
#streams = resolve_stream('name', 'AURA_Power')


if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--ip", default="127.0.0.1",
      help="The ip of the OSC server")
  parser.add_argument("--port", type=int, default=5005,
      help="The port the OSC server is listening on")
  args = parser.parse_args()

  client = udp_client.SimpleUDPClient(args.ip, args.port)

  print("looking for an EEG stream...")
  streams = resolve_stream('name', 'AURA')
  inlet = StreamInlet(streams[0])
  while True:
    sample, timestamp=inlet.pull_sample()
    print(timestamp, sample)
    client.send_message("/eegdata",sample)
#    time.sleep(1)

#  for x in range(10):
#    client.send_message("/filter", random.random())
#    time.sleep(1)



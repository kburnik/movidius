#!/usr/bin/env python3
from mvnc import mvncapi as mvnc
import sys

devices = mvnc.EnumerateDevices()

if len(devices) == 0:
  print("No devices were detected!")
  sys.exit(1)

print("Devices were found!")

for device in devices:
  print("Device", device)

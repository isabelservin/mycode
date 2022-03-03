#!/usr/bin/env python3

ipcheck = input("Enter an IP Address: ")

#test string provided as true
if ipcheck == "192.168.70.1":
    print("Ip address of the Gateway was set: " + ipcheck + " this is NOT recommended!")
elif ipcheck:
    print("Ip address set: " + ipcheck)
else:
    print("No input provided")

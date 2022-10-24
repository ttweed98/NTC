#! /usr/bin/env python

command = "show run"
conf_command = "conf t; int Gig 1; shutdown"

if __name__ == "__main__":
    # the lines below are only executed if called directly; not if this module is imported
    print("Sending 'show' command...")
    print(f"Command sent: \n {command}")

    print("Sending 'config' command...")
    print(f'Commands sent: \n {conf_command}')


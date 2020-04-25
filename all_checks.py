#!/usr/bin/env/ python3

import os
import shutil
import sys

def check_reboot():
	"""Returns True if computer has a pending reboot."""
	return os.path.exists("/run/reboot-required")

def check_disk_full(disk, min_absolute, min_percent):
	pass

def main():
	if check_reboot():
		print("pending reboot")
		sys.exit(1)
	print("Everything ok")
	sys.exit(2)

main()

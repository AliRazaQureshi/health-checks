#!/usr/bin/env/ python3

import os
import shutil
import sys

def check_reboot():
	"""Returns True if computer has a pending reboot."""
	return os.path.exists("/run/reboot-required")

def check_disk_full(disk, min_gb, min_percent):
	"""Return if disk is full or not."""
	du = shutil.disk_usage(disk)
	#Calculate percentage of free space
	free_percent = 100 * du.free / du.total
	gigabytes_free = du.free / 2**30

	if free_percent < min_percent or gigabytes_free < min_gb:
		return True
	return False

def main():
	if check_reboot():
		print("pending reboot")
		sys.exit(1)
	if check_disk_full(disk="/", min_gb=2, min_percent=10):
		print("Insufficient Space")
		sys.exit(1)
	else:
		print("Everything ok")
		sys.exit(1)

main()

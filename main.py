#!/usr/bin/env python3
# main.py - Main entry point for NodePhone

import os
import sys
import signal
import time
from src.tmux_manager import launch_nodephone, is_running_in_tmux

def setup_signal_handlers():
	"""Set up signal handlers for clean exit"""
	def signal_handler(sig, frame):
		print("\nExiting NodePhone...")
		sys.exit(0)
	
	signal.signal(signal.SIGINT, signal_handler)
	signal.signal(signal.SIGTERM, signal_handler)

def check_environment():
	"""Check if the environment is properly set up"""
	# Check if tmux is installed
	if os.system("which tmux > /dev/null") != 0:
		print("Error: tmux is not installed. Please install tmux to use NodePhone.")
		sys.exit(1)
	
	# Check if running inside tmux already
	if is_running_in_tmux():
		print("Warning: Already running inside a tmux session.")
		choice = input("Continue anyway? (y/n): ").strip().lower()
		if choice != 'y':
			sys.exit(0)

def main():
	"""Main function"""
	print("Starting NodePhone...")
	
	# Setup and environment checks
	setup_signal_handlers()
	check_environment()
	
	# Launch the NodePhone tmux session
	launch_nodephone()
	
	print("Thank you for using NodePhone!")

if __name__ == "__main__":
	main()

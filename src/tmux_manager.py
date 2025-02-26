#!/usr/bin/env python3
# src/tmux_manager.py - Manages tmux sessions for NodePhone

import subprocess
import os
import time
import sys

def is_running_in_tmux():
	"""Check if we're already running inside a tmux session"""
	return os.environ.get('TMUX') is not None

def create_tmux_session(session_name="nodephone"):
	"""Create a new tmux session for NodePhone"""
	try:
		# Create a new tmux session named 'nodephone'
		subprocess.run(['tmux', 'new-session', '-d', '-s', session_name])
		print(f"Created new tmux session: {session_name}")
		
		return True
	except Exception as e:
		print(f"Error creating tmux session: {e}")
		return False

def run_python_script_in_tmux(session_name, window_index, script_path, *args):
	"""Run a Python script in the specified tmux session window"""
	try:
		cmd = f"python3 {script_path}"
		if args:
			cmd += " " + " ".join(args)
			
		subprocess.run(['tmux', 'send-keys', '-t', f'{session_name}:{window_index}', 
		               cmd, 'C-m'])
		return True
	except Exception as e:
		print(f"Error running Python script in tmux: {e}")
		return False

def run_python_in_tmux(session_name, window_index, python_command):
	"""Run a Python command in the specified tmux session window"""
	try:
		# Use python -c to execute Python code directly in tmux
		subprocess.run(['tmux', 'send-keys', '-t', f'{session_name}:{window_index}', 
		               f'python3 -c "{python_command}"', 'C-m'])
		return True
	except Exception as e:
		print(f"Error running Python in tmux: {e}")
		return False

def create_new_window(session_name, window_name):
	"""Create a new window in the tmux session"""
	try:
		subprocess.run(['tmux', 'new-window', '-t', session_name, '-n', window_name])
		return True
	except Exception as e:
		print(f"Error creating new window: {e}")
		return False

def setup_app_launcher(session_name="nodephone"):
	"""Set up the app launcher window in the tmux session"""
	try:
		# Clear screen first
		subprocess.run(['tmux', 'send-keys', '-t', f'{session_name}:0', 'clear', 'C-m'])
		
		# Get the path to app_launcher.py
		script_dir = os.path.dirname(os.path.abspath(__file__))
		app_launcher_path = os.path.join(script_dir, 'app_launcher.py')
		
		# Run the app launcher
		return run_python_script_in_tmux(session_name, 0, app_launcher_path)
	except Exception as e:
		print(f"Error setting up app launcher: {e}")
		return False

def attach_to_session(session_name="nodephone"):
	"""Attach to the specified tmux session"""
	try:
		# Attach to the session
		subprocess.run(['tmux', 'attach-session', '-t', session_name])
		return True
	except Exception as e:
		print(f"Error attaching to tmux session: {e}")
		return False

def launch_nodephone():
	"""Launch the NodePhone tmux session with app launcher"""
	if create_tmux_session():
		setup_app_launcher()
		attach_to_session() 
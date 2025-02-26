#!/usr/bin/env python3
# src/apps/settings.py - Settings app for NodePhone

import os

def run():
    """Main entry point for the settings app"""
    try:
        os.system('clear')
        print("\n\n")
        print("="*50)
        print("    NodePhone Settings")
        print("="*50)
        print("\n")
        
        print("Settings categories:")
        print("  1. Display")
        print("  2. Sound")
        print("  3. Network")
        print("  4. System")
        print("\n")
        print("This is a placeholder. Full settings implementation coming soon.")
        print("\n")
        
        input("Press Enter to return to the main menu...")
    except Exception as e:
        print(f"Error in settings app: {e}")
        input("Press Enter to return to the main menu...")

if __name__ == "__main__":
    # Allow the app to be run directly for testing
    run() 
#!/usr/bin/env python3
# src/app_launcher.py - App launcher for NodePhone

import os
import sys
import importlib
import pkgutil

class AppLauncher:
    """Application launcher for NodePhone"""
    
    def __init__(self):
        self.apps = self._discover_apps()
        
    def _discover_apps(self):
        """Discover available applications"""
        # Start with empty app dictionary - welcome is no longer an app option
        apps = {}
        
        # Discover apps in the apps directory
        try:
            # Import the apps package
            from src import apps as apps_package
            
            # Find all modules in the apps package
            for _, name, ispkg in pkgutil.iter_modules(apps_package.__path__):
                try:
                    # Import the module
                    module = importlib.import_module(f'src.apps.{name}')
                    
                    # Check if it has a run function
                    if hasattr(module, 'run') and callable(module.run):
                        # Add it to our apps dictionary
                        apps[name] = module.run
                except ImportError as e:
                    print(f"Error importing app {name}: {e}")
        except ImportError as e:
            print(f"Error importing apps package: {e}")
        
        return apps
    
    def _launch_welcome(self):
        """Launch the welcome screen"""
        os.system('clear')
        print("\n\n")
        print("="*50)
        print("    Welcome to NodePhone!")
        print("    Your terminal-based phone system")
        print("="*50)
        print("\n")
        print("Available commands:")
        print("  - menu: Show the main menu")
        print("  - exit: Return to the app launcher")
        print("\n")
        input("Press Enter to continue...")
    
    def main_menu(self):
        """Display the main application menu"""
        # Show welcome screen on startup
        self._launch_welcome()
        
        while True:
            os.system('clear')
            print("\n\n")
            print("="*50)
            print("    NodePhone Main Menu")
            print("="*50)
            print("\n")
            
            # Display available apps
            for i, app_name in enumerate(sorted(self.apps.keys()), 1):
                print(f"  {i}. {app_name.capitalize()}")
                
            print("\n  q. Exit")
            print("\n")
            
            choice = input("Select an option: ").strip().lower()
            
            if choice == 'q':
                print("Exiting NodePhone...")
                break
                
            try:
                if choice.isdigit() and 1 <= int(choice) <= len(self.apps):
                    app_name = sorted(self.apps.keys())[int(choice)-1]
                    os.system('clear')
                    self.apps[app_name]()
                else:
                    print("Invalid selection. Please try again.")
                    input("Press Enter to continue...")
            except Exception as e:
                print(f"Error launching app: {e}")
                input("Press Enter to continue...")

def run():
    """Run the app launcher"""
    launcher = AppLauncher()
    launcher.main_menu()

if __name__ == "__main__":
    run() 
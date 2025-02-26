#!/usr/bin/env python3
# src/apps/calculator.py - Simple calculator app for NodePhone

import os

def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract b from a"""
    return a - b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def divide(a, b):
    """Divide a by b"""
    if b == 0:
        return "Error: Division by zero"
    return a / b

def run():
    """Main function to run the calculator app"""
    while True:
        os.system('clear')
        print("\n\n")
        print("="*50)
        print("    NodePhone Calculator")
        print("="*50)
        print("\n")
        print("Operations:")
        print("  1. Addition")
        print("  2. Subtraction")
        print("  3. Multiplication")
        print("  4. Division")
        print("\n  q. Return to main menu")
        print("\n")
        
        choice = input("Select an operation: ").strip().lower()
        
        if choice == 'q':
            break
            
        if choice not in ['1', '2', '3', '4']:
            print("Invalid selection. Please try again.")
            input("Press Enter to continue...")
            continue
            
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            
            if choice == '1':
                result = add(a, b)
                op = "+"
            elif choice == '2':
                result = subtract(a, b)
                op = "-"
            elif choice == '3':
                result = multiply(a, b)
                op = "*"
            elif choice == '4':
                result = divide(a, b)
                op = "/"
                
            print(f"\n{a} {op} {b} = {result}")
            input("\nPress Enter to continue...")
        except ValueError:
            print("Error: Please enter valid numbers.")
            input("Press Enter to continue...")
        except Exception as e:
            print(f"Error: {e}")
            input("Press Enter to continue...")

if __name__ == "__main__":
    run() 
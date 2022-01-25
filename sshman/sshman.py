#!/usr/bin/env python3

# Imports
import helpers
import sys
import os

### BEGIN main()
def main():
    # Initialize variables
    userResp = "z"
    runDir = os.path.dirname(os.path.abspath(__file__))
    connFile = helpers.read_config(runDir)
    connData = helpers.read_yaml(connFile)
     
    # Main menu
    print("Welcome to SSHman. What would you like to do?\n")
    while userResp:
        print("\nPress one of the following:\n")
        print("  P: Print defined connections to the screen\n")
        print("  N: New SSH session\n")
        print("  R: Most recent session\n")
        print("  E: Exit the program\n")
        userResp = input("> ").lower()
        
        # Options handling
        # P: PRINT CONNECTIONS 
        if userResp == 'p':
            print(connFile)
            helpers.print_dict(connData)
        # N: NEW SSH SESSION
        elif userResp == 'n':
            print("\nConnection name:\n")
            conn = input("> ").upper()
            helpers.start_session(connData, conn)
            writeString = str("LastUsed: " + conn)
            helpers.write_file(connFile, "LastUsed:", writeString)
            break
        # R: RECENT SESSION
        elif userResp == 'r':
            recent = connData.get('LastUsed', 'No recent connection found')
            print(f"\nStarting new session on {recent}...\n\n")
            helpers.start_session(connData, recent)
            break
        # E: EXIT
        elif userResp == 'e':
            print("\nExiting. Goodbye!")
            break 
        else:
            print("\nInvalid. Please choose a valid option\n")

    sys.exit()

if __name__ == "__main__":
    main()

# TODO:
# Menu options:
#   List connections
#       After each list, option to start one of the connections
#   Manually enter new connection details
#       Offer to save details to file

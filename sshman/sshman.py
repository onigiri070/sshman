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
    # Connection file paths
    custConnFile = helpers.read_config(runDir)
    defaultConnFile = runDir + "/config/connections.yaml"
    # Dictionaries
    defaultConnData = helpers.read_yaml(defaultConnFile) 
    custConnData = helpers.read_yaml(custConnFile)

    # Main menu
    print("Welcome to SSHman. What would you like to do?\n")
    while userResp:
        print("Press one of the following:\n")
        print("  P: Print defined connections information to the screen\n")
        print("  S: Begin SSH session\n")
        print("  E: Exit the program\n")
        userResp = input("> ").lower()
        
        # Options handling
        # P: PRINT CONNECTIONS 
        if userResp == 'p':
            subResp = 'x'
            while subResp:
                print("\nWhich connections would you like to see?\n")
                print("  C: Custom connections file\n")
                print("  D: Default connections file\n")
                print("  B: Go back to main menu\n")
                subResp = input("> ").lower()
                print()
                if subResp == 'c':
                    # Print path to file
                    print(custConnFile)
                    # Print dictionary contents
                    helpers.print_dict(custConnData)
                elif subResp == 'd':
                    # Print path to file
                    print(defaultConnFile)
                    # Print dictionary contents
                    helpers.print_dict(defaultConnData)
                elif subResp == 'b':
                    break
                else:
                    print("Invalid. Please choose a valid option")
        # S: START SSH SESSION
        elif userResp == 's':
            print("\n[C]ustom conenction or [D]efault?\n")
            dict = input("> ").lower()
            print("\nConnection name:\n")
            conn = input("> ").upper()
            if dict == 'c':
                helpers.start_session(custConnData, conn)
                break
            elif dict == 'd':
                helpers.start_session(defaultConnData, conn)
                break
        # E: EXIT
        elif userResp == 'e':
            print("\nExiting. Goodbye!")
            break 
        else:
            print("\nInvalid. Please choose a valid option\n")

    sys.exit()

# __name__ check
if __name__ == "__main__":
    main()

# TODO:
# Menu options:
#   List connections
#       After each list, option to start one of the connections
#   Manually enter new connection details
#       Offer to save details to file

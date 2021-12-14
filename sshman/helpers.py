# Imports
import yaml
import subprocess

# Definition: read_yaml()
# @param path = file path
# Returns a dictionary of the YAML file located at the path
def read_yaml(path):
    with open(path, "r") as f:
        return yaml.safe_load(f)

# Definition: print_dict
# @param dict = dictionary
# Iterates through a two level nested dictionary, printing values of the second level when they exist
def print_dict(dict):
    # Variable for assinging number to connections
    count = 0
    for l1, l2 in dict.items():
        count += 1
        print("\nConnection " + str(count) + ": ", l1)
        for key in l2:
            if l2[key] != None: 
                print("  " + key + ": " + str(l2[key]))
                # Debug
                #print(type(l2[key]))

# Definition: read_config()
# @runDir = Current directory the program is being run in  
# Retrieves the path of a non-default user-defined connections.yaml config file from config.yaml
def read_config(runDir):
    # Read config file into dictionary
    config = read_yaml(runDir + "/config/config.yaml")
    # Read config file parameters
    custConnFile = config.get("CONNECTIONS_FILE")
    return custConnFile

# Definition: start_session()
# @param data = dictionary of connections
# @param conn = string name of a connection
# Retrieves connection details of conn param from data param and starts an SSH session using those details
def start_session(data, conn):
    # Get conneciton info from data and store in variable
    connection = data.get(conn, 'Connection not found')
    user = connection.get('User', 'User not found')
    addr = connection.get('Address', 'Address not found')
    port = connection.get('Port', '22')
    # Print connection info before connecting
    print(f"Connecting to: {addr} on port: {port} as: {user}\n")
    print()
    # Concatenate connection details into @session variable
    session = "ssh " + str(user) + "@" + str(addr) + " -p " + str(port)
    # Start SSH session as a subprocess using the connection information stored in @session
    subprocess.run(session, shell=True)

if __name__ == "__main__":
    pass

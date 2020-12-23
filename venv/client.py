import socket

# Creating a socket
s = socket.socket()

# Host(Address) and port to connect
host = "127.0.0.1"
port = 12345

try:
    # Connect the link
    s.connect((host, port))

    # Get the response from the server
    response = s.recv(1024)
    print(response.decode("utf-8"))

    # Close connection
    s.close()
except socket.error as msg:
    print("[Server not active.] Message:", msg)
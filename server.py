import socket

host = "127.0.0.1"
port = 12345

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("The socket has been created.")

    s.bind((host, port))
    print("The socket is connected to the port {}.".format(port))

    s.listen(5)
    print("socket is resting")
except socket.error as msg:
    print("Error:",msg)

while True:

   # If a connection is established with the client
   c, addr = s.accept()
   print('Created connect:', addr)

   # Let's send a welcome message to the connected client side.
   message = 'Thank you for connect'
   c.send(message.encode('utf-8'))

   # Let's end the connection.
   c.close()
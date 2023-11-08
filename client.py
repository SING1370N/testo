import socket		 	 # Import socket module
import sys
import ipaddress

s = socket.socket() 	  		 # Create a socket object

try:
    # host = str(ipaddress.ip_address(sys.argv[1]))     # Reading IP Address
    host = str(sys.argv[1])
    port = int(sys.argv[2])                           # Reading port number
    s.connect((host, port))                           # Connecting to server
    print("The IP address of the server is:", host)
    print("The port number of the server is:", port)

    while(True):
        equ = input("Вводите: ")
        s.send(equ.encode())
        result = s.recv(1024).decode()

        if result == "Quit":
            print("Closing client connection, goodbye")
            break
        elif result == "ZeroDiv":
            print("You can't divide by 0, try again")
        elif result == "MathError":
            print("There is an error with your math, try again")
        elif result == "SyntaxError":
            print("There is a syntax error, please try again")
        elif result == "NameError":
            print("You did not enter an equation, try again")
        else:
            print("The answer is:", result)

    s.close 				 # Close the socket when done

except (IndexError, ValueError):
    print("You did not specify an IP address and port number")
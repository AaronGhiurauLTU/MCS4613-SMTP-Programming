import socket
from socket import *
import ssl
import base64


#This set of code will use googles mail server, to do this it needs the username and an app password to use an account
#to run this just change the username and password to your account and change the recipient to whatever email you want to use

#Yahoo
#If you want to use yahoo the mailserver is: smtp.mail.yahoo.com and the port will be: 465
#still the same concept for username and password(email@yahoo.com, app password not actual password)

#AOL
#If you want to use yahoo the mailserver is: smtp.aol.com and the port will be: 465
#still the same concept for username and password(email@aol.com, app password not actual password)

'''
username = "" #change with your email
password = "" #change to your email's app password

recipient = "" #change to the target email

subject = "Test For Computer Networking"
body = "\r\n I love computer networks!"
msg = f"subject: {subject}\r\nFrom: {username}\r\nTO: {recipient}\r\n\r\n{body}\r\n"
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = "smtp.gmail.com"
port = 465

context = ssl.create_default_context()
clientSocket = socket.create_connection((mailserver, port))
sslSocket = context.wrap_socket(clientSocket, server_hostname=mailserver)

# Create socket called clientSocket and establish a TCP connection with mailserver
#clientSocket = socket(AF_INET, SOCK_STREAM)
#clientSocket.connect(mailserver)
def recv_expect(sock, code):
    recv = sock.recv(1024).decode()
    print(recv)
    if not recv.startswith(str(code)):
        raise Exception(f"Expected reply {code}, got:\n{recv}")
    return recv
#recv = clientSocket.recv(1024).decode()
#print(recv)
#if not recv.startswith(str(code)):
#    raise print('220 reply not received from server.')
#return recv

def send_cmd(sock, cmd):
    print("C:", cmd.strip())
    sock.send((cmd +"\r\n").encode())

recv_expect(sslSocket,220)

send_cmd(sslSocket, "HELO Alice")
recv_expect(sslSocket, 250)

send_cmd(sslSocket, "AUTH LOGIN")
recv_expect(sslSocket, 334)

# Encode and send username and password
send_cmd(sslSocket, base64.b64encode(username.encode()).decode())
recv_expect(sslSocket, 334)

send_cmd(sslSocket, base64.b64encode(password.encode()).decode())
recv_expect(sslSocket, 235)

# MAIL FROM
send_cmd(sslSocket, f"MAIL FROM:<{username}>")
recv_expect(sslSocket, 250)

# RCPT TO
send_cmd(sslSocket, f"RCPT TO:<{recipient}>")
recv_expect(sslSocket, 250)

# DATA
send_cmd(sslSocket, "DATA")
recv_expect(sslSocket, 354)

# Send email content
sslSocket.send((msg + endmsg).encode())
recv_expect(sslSocket, 250)

# QUIT
send_cmd(sslSocket, "QUIT")
recv_expect(sslSocket, 221)

sslSocket.close()

'''

#This code is used to send it to the command prompt to use comment other section with """ {stuff in here}""" 
    #and remove the """""" around the next set of code
#To use this code you will need to open the command prompt and run pip install aiosmtpd
#after installin you will need to run in one terminal window aiosmtpd -n -l localhost:1025
#Then in another terminal window you will need to go to where you have the code placed and run {codename}.py

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

#Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = ("localhost", 1025)

#Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(mailserver)

recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')

#Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
print("Client:", heloCommand)
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')


#Send MAIL FROM command and print server response.
mailFrom = "MAIL FROM:<test1@gmail.com>\r\n"
print("Client From:", mailFrom)
clientSocket.send(mailFrom.encode())
recv2 = clientSocket.recv(1024).decode()
print(recv2)


#Send RCPT TO command and print server response.
rcptTo = "RCPT TO:<test2@gmail.com>\r\n"
print("Client To:", rcptTo)
clientSocket.send(rcptTo.encode())
recv3 = clientSocket.recv(1024).decode()
print(recv3)


#Send DATA command and print server response.
data = "DATA\r\n"
print("Data:", data)
clientSocket.send(data.encode())
recv4 = clientSocket.recv(1024).decode()
print(recv4)


#Send message data.
clientSocket.send(msg.encode())
print("Client: Sending message")


#Message ends with a single period.
clientSocket.send(endmsg.encode())
recv5 = clientSocket.recv(1024).decode()
print(recv5)


#Send QUIT command and get server response.
quit = "QUIT\r\n"
clientSocket.send(quit.encode())
recv6 = clientSocket.recv(1024).decode()
print(recv6)

clientSocket.close()

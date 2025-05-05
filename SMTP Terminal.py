from socket import *

#This code is used to send it to the command prompt to use comment other section with """ {stuff in here}""" 
    #and remove the """""" around the next set of code
#To use this code you will need to open the command prompt and run pip install aiosmtpd
#after installin you will need to run in one terminal window aiosmtpd -n -l localhost:1025
#Then in another terminal window you will need to go to where you have the code placed and run {codename}.py


msg = (
    "From: test1@gmail.com\r\n"
    "To: test2@gmail.com\r\n"
    "Subject: SMTP Test Message\r\n"
    "\r\n"
    "I love computer networks!"
)
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
mailFrom = "MAIL FROM: test1@gmail.com\r\n"
print("Client From:", mailFrom)
clientSocket.send(mailFrom.encode())
recv2 = clientSocket.recv(1024).decode()
print(recv2)


#Send RCPT TO command and print server response.
recipient = "RCPT TO: test2@gmail.com\r\n"
print("Client To:", recipient)
clientSocket.send(recipient.encode())
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
from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port
    server=("127.0.0.1", 1025)
    # Fill in start
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect(server)
    # Fill in end

    recv = clientSocket.recv(1024).decode()
    

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    
    

    # Send MAIL FROM command and print server response.
    # Fill in start
    mailF = "MAIL FROM:<davisbrandon@outlook.com>\r\n"
    clientSocket.send(mailF.encode())
    recv = clientSocket.recv(1024).decode()
   
    

    # Fill in end

    # Send RCPT TO command and print server response.
    # Fill in start
    mailT = "RCPT TO:<bdavis923@gmail.com>\r\n"
    clientSocket.send(mailT.encode())
    recv = clientSocket.recv(1024).decode()
    
    

    # Fill in end

    # Send DATA command and print server response.
    # Fill in start
    data="DATA\r\n"
    clientSocket.send(data.encode())
    recv = clientSocket.recv(1024).decode()
    
    

    # Fill in end

    # Send message data.
    # Fill in start
    clientSocket.send("From: \"Test\" <davisbrandon@outlook.com>\n".encode())
    clientSocket.send("To: \"Brandon\" <bdavis923@gmail.com>\n".encode())
    clientSocket.send("Date: 11 - 06 - 21\n".encode())
    clientSocket.send("Subject: please work 123\n".encode())
    clientSocket.send(msg.encode())


    # Fill in end

    # Message ends with a single period.
    # Fill in start
    clientSocket.send(endmsg.encode())
    recv = clientSocket.recv(1024).decode()
    
    

    # Fill in end

    # Send QUIT command and get server response.
    # Fill in start
    clientSocket.send("QUIT\r\n".encode())
    recv = clientSocket.recv(1024).decode()
    clientSocket.close()
    # Fill in end


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')

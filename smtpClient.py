from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = (
        "From: <njt4497@nyu.edu>\r\n"
        "To: <jungniteshthapa@gmail.com>\r\n"
        "Subject: SMTP Client Test\r\n"
        "\r\n"
        "My message"
    )
    endmsg = "\r\n.\r\n"

    
    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.settimeout(15)
    clientSocket.connect((mailserver, port))
    # Fill in end
     
    def expect_code(response, expected_code):
        if not response.startswith(expected_code):
            raise RuntimeError(
                f'Expected {expected_code} reply, got: {response.strip()}'
            )

    try:
        recv = clientSocket.recv(1025).decode()
        print(recv)
        expect_code(recv, '220')

        # Send HELO command and print server response.
        heloCommand = 'HELO localhost\r\n'
        clientSocket.sendall(heloCommand.encode())
        recv1 = clientSocket.recv(port).decode()
        print(recv1)
        expect_code(recv1, '250')

        # Send MAIL FROM command and handle server response.
        # Fill in start
        mailFromCommand = 'MAIL FROM:<njt4497@nyu.edu>\r\n'
        clientSocket.sendall(mailFromCommand.encode())
        recv2 = clientSocket.recv(1025).decode()
        print(recv2)
        expect_code(recv2, '250')
        # Fill in end

        # Send RCPT TO command and handle server response.
        # Fill in start
        rcptToCommand = 'RCPT TO:<jungniteshthapa@gmail.com>\r\n'
        clientSocket.sendall(rcptToCommand.encode())
        recv3 = clientSocket.recv(1025).decode()
        print(recv3)
        expect_code(recv3, '250')
        # Fill in end

        # Send DATA command and handle server response.
        
        # Fill in start
        dataCommand = 'DATA\r\n'
        clientSocket.sendall(dataCommand.encode())
        recv4 = clientSocket.recv(1025).decode()
        print(recv4)
        expect_code(recv4, '354')
        # Fill in end

        # Send message data.
        # Fill in start
        clientSocket.sendall(msg.encode())
        # Fill in end

        # Message ends with a single period, send message end and handle server response.
        # Fill in start
        clientSocket.sendall(endmsg.encode())
        recv5 = clientSocket.recv(port).decode()
        print(recv5)
        expect_code(recv5, '250')
        # Fill in end

        # Send QUIT command and handle server response.
        # Fill in start
        quitCommand = 'QUIT\r\n'
        clientSocket.sendall(quitCommand.encode())
        recv6 = clientSocket.recv(port).decode()
        print(recv6)
        expect_code(recv6, '221')
        # Fill in end
    finally:
        clientSocket.close()


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')

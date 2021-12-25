import socket
import time
import datetime
import random


def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    numberIntTemperature = random.randrange(20, 50)
    numberIntHumidity = random.randrange(20, 50)
    numberIntMoisture = random.randrange(20, 50)
    message = str(numberIntTemperature) + ":" + str(numberIntHumidity) + ":" + str(numberIntMoisture);

    while message.lower().strip() != 'bye':
        print(datetime.datetime.now().time()) 
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response

        print('Received from server: ' + data)  # show in terminal
        time.sleep(3)
        numberTemperature = random.randrange(20, 50)
        numberHumidity = random.randrange(20, 50)
        numberMoisture = random.randrange(20, 50)
        message = str(numberTemperature) + ":" + str(numberHumidity) + ":" + str(numberMoisture);

    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()

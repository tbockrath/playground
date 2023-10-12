import socket


def main():
    print("Starting App")
    connect()


def connect():
    print("Connecting Port 30003")
    host = '192.168.2.115'
    port = 30003
    s = socket.socket()
    s.connect((host, port))

    # while True:
    #     print(s.recv(1024).decode())

    message = s.recv(1024).decode('UTF-8')
    print('message', message)

    data = message.split("\n")
    for d in data:
        line = d.split(",")
        if len(line) == 22:
            print('yes')
            Callsign = None if line[10] == '' else line[10]
            Altitude = None if line[11] == '' else line[11]
            GroundSpeed = None if line[12] == '' else line[12]
            Track = None if line[13] == '' else line[13]
            Latitude = None if line[14] == '' else line[14]
            Longitude = None if line[15] == '' else line[15]
            print(Callsign, Altitude, Latitude)
        else:
            print('no')
    s.close()

if __name__ == "__main__":
    main()

from socket import socket, AF_INET, SOCK_STREAM


def request_current_from_ammeter(port: int, command: bytes):
    with socket(AF_INET, SOCK_STREAM) as s:
        s.settimeout(3) # added a timeout of 3 seconds for the socket connection
        s.connect(('localhost', port))
        s.sendall(command)
        data = s.recv(1024)
        if data:
            data_str = float(data.decode('utf-8')) # convert the data to float so we can use it in calculations
            # print(f"Received current measurement from port {port}: {data_str} A")
            return data_str
        else:
            raise ValueError(f"No measurement received from port {port}")

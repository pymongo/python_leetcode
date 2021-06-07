import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 7999
MESSAGE = b"Hello, World!"

if __name__ == '__main__':
    # socket.bind会创建udp_server(端口号固定)
    # socket.socket会创建udp_client(端口号随机)
    sock = socket.socket(socket.AF_INET,  # Internet
                         socket.SOCK_DGRAM)  # UDP
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
    print("read_from_socket", sock.recvfrom(1024))

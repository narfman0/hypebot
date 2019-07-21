"""
Net module to provide connector for talking to livesplit.server
"""
import socket

from hypebot import settings


class LiveSplitClient:
    def __init__(self):
        self.connect()

    def connect(self, host=settings.LIVESPLIT_HOST, port=settings.LIVESPLIT_PORT):
        """ Connect to livesplit.server with the given host.port """
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((host, port))

    def send(self, msg):
        """ Send a message to the livesplit server """
        self.socket.send((msg + "\r\n").encode())

    def recv(self):
        """ Receive a message from the livesplit server """
        self.socket.recv(1024).decode().strip()

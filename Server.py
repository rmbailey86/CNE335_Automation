import os
import paramiko


class Server:
    """ Server class for representing and manipulating servers. """

    def __init__(self, server_ip):
        # TODO -
        self.server_ip = server_ip

    def ping(self):
        # TODO - Use os module to ping the server
        address = self.server_ip
        check = os.system("ping" + address)

        return check

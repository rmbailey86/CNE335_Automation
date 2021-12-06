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

    def connect_and_update(self):
        user_name = 'ubuntu'
        pwd = ""
        server = self.server_ip
        remote = paramiko.SSHClient()
        remote.load_system_host_keys()
        remote.connect(hostname=server, username=user_name, password=pwd)
        if remote.get_transport() is not None:
            is_activ = remote.get_transport().is_active()
            print("transport active:", is_activ)
        cmd_a = "sudo apt-get update -y"
        a_in, a_out, a_err = remote.exec_command(cmd_a)
        a_in.flush()
        data_a = a_out.read().splitlines()
        for line in data_a:
            print(line)

        cmd_b = "sudo apt-get upgrade -y"
        b_in, b_out, b_err = remote.exec_command(cmd_b)
        b_in.flush()
        data_b = b_out.read().splitlines()
        for line in data_b:
            print(line)
        remote.close()

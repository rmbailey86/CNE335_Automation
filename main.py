# This is the template code for the CNA337 Final Project
# Rob Bailey, rmbailey@student.rtc.edu
# Base code template furnished by Zachary Rubin, zrubin@rtc.edu
# With tutoring from TJ Dewey
# CNA 337 Fall 2020
from Server import Server


def print_program_info():
    # TODO - Change your name
    print("Server Automator v0.1 by Rob Bailey")


# This is the entry point to our program
if __name__ == '__main__':
    print_program_info()
    # TODO - Create a Server object
    EC2 = Server("54.188.78.84")
    echo = EC2.ping()
    print(echo)
    EC2.connect_and_update()
    # TODO - Call Ping method and print the results

    # myEC2.connect()

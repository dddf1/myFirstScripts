import paramiko
import sys


host = input("To which IP to connect? ")
username = "root"
password = "aristo1"


def create_ssh(host , username, password ):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        print("creating connection")
        ssh.connect(host, username=username, password=password)
        print("connected")
        #yield ssh
        stdin, stdout, stderr = ssh.exec_command("fstool service status", get_pty=True)

        data = stdout.read()
        print(data)


    finally:
        print("closing connection")
        ssh.close()
        print("closed")


create_ssh(host , username , password)

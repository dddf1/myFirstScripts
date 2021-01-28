# Rafi Maman, 26.10.20

import paramiko

# variables
print("To which IP to connect to remove files and free space before upgrade ?")
host = input()
username = "root"
password = "aristo1"
ssh = paramiko.SSHClient()
directories = ["/usr/local/forescout/rollback/",
               "/usr/local/forescout/plugin/ms/backup",
               "/usr/local/forescout/webapps/portal/wsusscn2.cab",
               "/usr/src/UPGRADES/",
               "/usr/local/forescout/cores/",
               "/usr/local/forescout/backup/",
               "/usr/src/rollback/"]


# open ssh connection
def create_ssh(host, username, password):

    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print("creating connection")
    ssh.connect(host, username=username, password=password)
    print("connected")


def print_stdout(stdout):
    output = ""
    lines = stdout.readlines()
    for line in lines:
        output = output + line
    if output != "":
        print(output)
    else:
        print("There was no files to delete!")


# delete directories before upgrade and print df -h after so you can check free space on disk
def exec_commands_to_free_space():
    for folder in directories:
        print(folder)
        stdin, stdout, stderr = ssh.exec_command(f"rm -rfv {folder}", get_pty=True)
        print_stdout(stdout)

    stdin, stdout, stderr = ssh.exec_command("df -h", get_pty=True)
    print_stdout(stdout)


# close ssh connection
def close_ssh():
    print("closing connection")
    ssh.close()
    print("closed")


# execute code
create_ssh(host, username, password)
exec_commands_to_free_space()
close_ssh()
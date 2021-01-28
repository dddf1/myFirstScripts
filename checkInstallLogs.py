# Rafi Maman, 16.11.20

import paramiko

# variables
print("To which IP to connect to and check Install logs for errors ?")
host = input()
username = "root"
password = "aristo1"
ssh = paramiko.SSHClient()
logs = ["watch_dog.log",
        "daemon/plugin_*.log",
        "install/CounterACT-auto.log",
        "install/CounterACT-install.log",
        "install/CounterACT-syslog.log",
        "install/CounterACT-psql.log"]
words = ["error", "critical", "failure"]
excludes = ["Running java", "inflating","I/O", "adding", "softflowd"]


# open ssh connection
def create_ssh(host, username, password):
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print("creating connection")
    ssh.connect(host, username=username, password=password)
    print("connected")


def print_stdout(stdout):
    lines = stdout.readlines()
    for line in lines:
        if any(wd in line for wd in words):
            if all(ex not in line for ex in excludes):
                print(line)


# check errors in logs
def exec_commands_to_check_logs():
    for log in logs:
        print("***********************************************************************")
        print(f"Log: /usr/local/forescout/log/{log}")
        stdin, stdout, stderr = ssh.exec_command(f"cat -n /usr/local/forescout/log/{log}", get_pty=True)
        stdin.flush()
        print_stdout(stdout)
        print("***********************************************************************")


# close ssh connection
def close_ssh():
    print("closing connection")
    ssh.close()
    print("closed")


# execute code
create_ssh(host, username, password)
exec_commands_to_check_logs()
close_ssh()
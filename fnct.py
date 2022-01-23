from cmath import e
import paramiko
def distrib(host, user, pwd): #détermination de la distribution linux
    ssh_client=paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh_client.connect(hostname=host, username=user, password=pwd, port=22)
        stdin,stdout,stderr=ssh_client.exec_command('lsb_release -i')
        extract_distrib= ''.join(stdout.readlines()).split()[2]
        if extract_distrib in ['Debian','Ubuntu']:
            return 'apt'
        elif extract_distrib in ['CentOS', 'Fedora', 'RedHat']:
            return 'yum'
        else:
            print("Distrib pas géré")
    except paramiko.AuthenticationException as e:
        print('erreur de connection')
        #logging.error(e)
def ssh(host, user, pwd, cmd):
    ssh_client=paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh_client.connect(hostname=host, username=user, password=pwd, port=22)
        stdin,stdout,stderr=ssh_client.exec_command(cmd)
        print(stdout.readlines())
    except paramiko.AuthenticationException as e:
        print('erreur de connection')

def upload_file(remote_server, ssh_user, ssh_password, local_filepath, remote_path):
    sftp = None
    transport = None
    port_number=22
    try:
        # Create transport instance and setup SFTP connection
        transport = paramiko.Transport((remote_server, port_number))
        transport.connect(None, ssh_user, ssh_password)
        sftp = paramiko.SFTPClient.from_transport(transport)

        # Upload file to remote destination
        sftp.put(local_filepath, remote_path)
    except Exception as e:
        print(f'Failed to transfer files: {e}')
        if sftp:
            sftp.close()
        if transport:
            transport.close()

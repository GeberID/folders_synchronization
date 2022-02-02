import paramiko
from page import Page


class Client:
    host = '10.37.168.10'
    port = 22
    username = 'pi'
    passw = 'GE7456!@R842VZ'

    def __init__(self):
        self.ssh = None
        self.ssh_transport = None
        self.transf = None

    def login_transport(self):
        self.ssh_transport = paramiko.Transport((self.host, self.port))
        self.ssh_transport.connect(username=self.username, password=self.passw)

    def login_ssh(self):
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(self.host, self.port, self.username, self.passw)

    def get_files(self, page_from, page_to):
        self.login_transport()
        self.transf = paramiko.SFTPClient.from_transport(self.ssh_transport)
        self.transf.get(page_from, page_to)
        self.transf.close()

    def put_files(self, page_from, page_to):
        self.login_transport()
        self.transf = paramiko.SFTPClient.from_transport(self.ssh_transport)
        self.transf.put(page_from, page_to, confirm=False)
        self.transf.close()

    def list(self, path2):
        self.login_ssh()
        ftp = self.ssh.open_sftp()
        answer = ftp.listdir(path=path2)
        self.ssh.close()
        return answer

import os
from datetime import datetime

class Logs:
    def __init__(self):
        self.log_file_link = None
        self.files_url_list = list()
    def walk_local_page(self, page):
        self.files_url_list = list()
        self.dir_list = list()
        files = list()
        for root, dirs, names in os.walk(page):
            for dir in dirs:
                self.dir_list.append(dir)
            for name in names:
                self.files_url_list.append(os.path.join(root, name))
                files.append(name)
        return files

    # Создание лога и записи в него переданных файлов
    def log_files(self, files,):
        now = datetime.now()
        current_time = now.strftime("%m_%d_%Y_%H_%M_%S")
        file = open(f'logs/log_{current_time}.txt', 'a')
        file.write("Current Time = " + current_time + '\n')
        file.write(files + '\n')
        self.log_file_link = os.getcwd() + f"/logs"
        file.close()

    def delete_log_file(self):
        file = self.walk_local_page(os.getcwd() + "/logs")
        for i in self.files_url_list:
            os.remove(i)

    def send_log_files(self, transfer,current_time):
        self.log_file_link = os.getcwd() + f"/logs"
        try:
            files_list = self.walk_local_page(self.log_file_link)
            for i in files_list:
                transfer.put_files(self.log_file_link + "/" + i,
                                   f'/media/pi/D/share/BACKUPS/logs/log_{current_time}.txt')
        except:
            print('Error send log file')
        self.delete_log_file()



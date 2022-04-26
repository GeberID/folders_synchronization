import os, zipfile
from datetime import datetime
from logs import Logs
log = Logs()
class Page:
    def __init__(self):
        self.page = 'Null'
        self.files_url_list = list()
        self.dir_list = list()
        self.check = 0
        self.current_time = 0
        self.log_file_link = None

#Проверка на существтвание локадьной папки
    def check_local_page(self, page):
        if os.path.exists(page) == True:
            return 1
        else:
            return 0

#Обход всего дерева локальной папки
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

#Создание локальной папки
    def create_local_page(self, page, list_dir_from, list_dir_to):
        if len(list_dir_to) != 0:
            for i in list_dir_from:
                for y in list_dir_to:
                    if str(i) != str(y):
                        self.check = 0
                    else:
                        self.check = 1
                        break
                if self.check == 0:
                    if len(list_dir_to) > 0:
                        os.makedirs(page + '/' + i)
        elif len(list_dir_to) == 0:
            for dir in list_dir_from:
                os.makedirs(page + '/' + dir)

# Открыть локальную папку
    def get_local_page(self, page):
        os.chdir(page)

# # Создание лога и записи в него переданных файлов
#     def log_files(self, files):
#         now = datetime.now()
#         self.current_time = now.strftime("%m_%d_%Y_%H_%M_%S")
#         file = open(f'logs/log_{self.current_time}.txt', 'a')
#         file.write("Current Time = " + self.current_time + '\n')
#         file.write(files+'\n')
#         self.log_file_link = os.getcwd() + f"/logs"
#         file.close()
#
#
#     def delete_log_file(self):
#         file = self.walk_local_page(os.getcwd() + "/logs")
#         for i in self.files_url_list:
#             os.remove(i)
#
#     def send_log_files(self,transfer):
#         try:
#             files_list = self.walk_local_page(self.log_file_link)
#             for i in files_list:
#                 transfer.put_files(self.log_file_link+"/" +i,
#                                    f'/media/pi/D/share/BACKUPS/logs/log_{self.current_time}.txt')
#         except:
#             print('Error send log file')
#         self.delete_log_file()

# Обертка копирования информации с локальной папки на удаленное устройство
    def copy_to_server(self, transfer, page_from, page_to):
        snap_list = self.create_snapshot(page_from)
        remote_file_list = snap_list.replace(page_from,"")
        transfer.put_files(snap_list, page_to + remote_file_list)
        os.remove(snap_list)
        #log = snap_list + " - "+ page_to + '/' + remote_file_list
        #self.log_files(log)

# Обертка копирования информации с удаленного устройства в локальную папку
    def copy_from_server(self, transfer, page_from, page_to):
        answer = transfer.list(page_from)
        for i in answer:
            transfer.get_files(page_from + '/' + i, page_to + '/' + i)
            #log = page_from + '/' + i+ " - " + page_to + '/' + i
            #self.log_files(log)

#Функция создает снапшот папки на компьютере со всеми файлами находящейся в ней.
# Необходима для последующей передачи файла локально на удаленный компьютер (разберри)
    def create_snapshot(self,page_from):
        now = datetime.now()
        self.current_time = now.strftime("%m_%d_%Y_%H_%M_%S")
        snap = zipfile.ZipFile(page_from+f"/snapshot_{self.current_time}.zip",mode='w')
        files_list = self.walk_local_page(page_from)
        for i in files_list:
            if i == f"snapshot_{self.current_time}.zip":
                continue
            else:
                snap.write(page_from+"/"+i)
                log_file = "archivation: "+page_from + '/' + i
                log.log_files(log_file)
        snap.close()
        return page_from+f"/snapshot_{self.current_time}.zip"
import os
class Page:
    def __init__(self):
        self.page = 'Null'
        self.files_url_list = list()
        self.dir_list = list()
        self.check = 0

    def check_local_page(self, page):
        if os.path.exists(page) == True:
            return 1
        else:
            return 0

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
        return  files

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

    def get_local_page(self, page):
        os.chdir(page)

    def log(self):
        pass

    def copy_to_server(self,transfer,page_from,page_to):
        files_list = self.walk_local_page(page_from)
        x=0
        for i in self.files_url_list:
            transfer.put_files(i,page_to +'/'+ files_list[x])
            x=x+1

    def copy_from_server(self, transfer, page_from, page_to):
        files_list = self.walk_local_page(page_from)
        for i in self.files_url_list:
            transfer.get_files(i, page_to)
from client import Client
from page import Page

client = Client()
page = Page()

folder_from = input("Sync folder from:")
folder_to = input('Sync folder to:')
print('''
Sync from server: 0
Sync to server : 1
    ''')
if folder_to == "":
    folder_to =='/media/pi/D/share/BACKUPS'
ans = input()
if int(ans) == 0:
    print('Sync...')
    page.copy_from_server(client, client, folder_to)
    page.send_log_files(client)
elif int(ans) == 1:
    print('Sync...')
    page.copy_to_server(client, folder_from, folder_to)
    page.send_log_files(client)
else:
    print('Close...')


#TODO Сделать функцию по созданию снапшота папки (архивация всех файлов и сжатия архива) и передачи его на удаленное хранилище


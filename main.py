from client import Client
from page import Page

client = Client()
page = Page()
folder_from = input("Sync folder from:")
folder_to = input('Sync folder to:')
while True:
    print('''
Sync from server: 0
Sync to server : 1
    ''')
    ans = input()
    if int(ans) == 0:
        print('Sync...')
        page.copy_from_server(client, folder_from, folder_to)
    elif int(ans) == 1:
        print('Sync...')
        page.copy_to_server(client, folder_from, folder_to)
    else:
        print('Close...')
        break


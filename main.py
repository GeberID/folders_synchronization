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
ans = input()
if int(ans) == 0:
    page.copy_from_server(client, folder_from, folder_to)
    # page.copy_from_server(client, r'/media/pi/D/share/test', r'C:\Users\alexandr.guslyanniko\Documents\IISExpress')
elif int(ans) == 1:
    page.copy_to_server(client, folder_from, folder_to)

# test = client.list(r'/media/pi/D/share/test')
# page.copy_to_server(client,r'C:\Users\alexandr.guslyanniko\Desktop\PTW\доки',r'/media/pi/D/share/test')
# page.copy_from_server(client, folder_from, folder_to)

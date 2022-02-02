
from client import Client
from page import Page
client = Client()
page = Page()

client.list(r'/media/pi/D/share/test')
page.copy_to_server(client,'/home/alexander/Documents/test',r'/media/pi/D/share/test')
#page.copy_from_server(client,r'/media/pi/D/share/test',r'/home/alexander/Documents/testconfig')
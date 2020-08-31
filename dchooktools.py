import requests
import os

banner = """
██████╗  ██████╗██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗    ████████╗ ██████╗  ██████╗ ██╗     ███████╗
██╔══██╗██╔════╝██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
██║  ██║██║     ███████║██║   ██║██║   ██║█████╔╝        ██║   ██║   ██║██║   ██║██║     ███████╗
██║  ██║██║     ██╔══██║██║   ██║██║   ██║██╔═██╗        ██║   ██║   ██║██║   ██║██║     ╚════██║
██████╔╝╚██████╗██║  ██║╚██████╔╝╚██████╔╝██║  ██╗       ██║   ╚██████╔╝╚██████╔╝███████╗███████║
╚═════╝  ╚═════╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝
                                 By 'Raptor Root#1337

--------------------------------
"""

os.system("clear")
print(banner)
print("[1] Discord Webhook Sender")
print("[2] Discord Webhook Spammer")
print("[3] Discord Webhook Deleter")
action = int(input("\nSelect Your Action: "))

if action == 1:
	os.system("clear")
	print(banner)
	url = input("Enter Webhook URL: ")
	uname = input("Enter Username: ")
	avurl = input("Enter Avatar URL: ")
	while True:
		content = input("Enter Message: ")
		data = {
    		"username": uname,
    		"avatar_url": avurl,
    		"content": content
		}
		requests.post(url, data=data)
elif action == 2:
	os.system("clear")
	print(banner)
	how_many_times = 0
	url = input("Enter Webhook URL: ")
	uname = input("Enter Username: ")
	avurl = input("Enter Avatar URL: ")
	content = input("Enter Message: ")
	while True:
		data = {
    		"username": uname,
    		"avatar_url": avurl,
    		"content": content
		}
		requests.post(url, data=data)
		how_many_times = how_many_times + 1
		print(str(how_many_times) + " Messages Sent")
elif action == 3:
	os.system("clear")
	print(banner)
	url = input("Enter Webhook URL: ")
	requests.delete(url)
	print("Webhook Deleted Successfully.")
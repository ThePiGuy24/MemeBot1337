from __future__ import print_function
from oauth2client import file, client, tools
from apiclient.discovery import build
from httplib2 import Http
import random, tkinter
from tkinter import LEFT,RIGHT,TOP,BOTTOM

print("imported")

send = False

cID = 7993359083

SCOPES = 'https://www.googleapis.com/auth/classroom.coursework.students'
store = file.Storage('credentials.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store)
service = build('classroom', 'v1', http=creds.authorize(Http()))
print("set up")

def start():
	global send
	if not send:
		send = True
		print("Starting")
	else:
		print("Already Running")
		
def stop():
	global send
	if send:
		send = False
		print("Stopping")
	else:
		print("Already Stopped")
		
def post(title,description):
	courseWork = {  
		'title': title,  
		'description': description,  
		'workType': 'ASSIGNMENT',  
		'state': 'PUBLISHED',  
	}
	courseWork = service.courses().courseWork().create(  
		courseId=cID, body=courseWork).execute()  
	print('Assignment created with ID {0}'.format(courseWork.get('id')))

top = tkinter.Tk()
startButton = tkinter.Button(top,text = "Start", command = start)
stopButton = tkinter.Button(top,text = "Stop", command = stop)
titleLabel = tkinter.Label(top,text = "Google Classroom Spam Bot Tool Thing")
titleBoxLabel = tkinter.Label(top,text = "Title:")
descriptionBoxLabel = tkinter.Label(top,text = "Description:")
titleBox = tkinter.Entry(top)
descriptionBox = tkinter.Entry(top)

titleLabel.pack(side = TOP)
titleBoxLabel.pack(side = LEFT)
titleBox.pack(side = LEFT)
descriptionBoxLabel.pack(side = LEFT)
descriptionBox.pack(side = LEFT)
stopButton.pack(side = RIGHT)
startButton.pack(side = RIGHT)
top.title("Google Classroom Spam Bot")
top.iconbitmap("favicon.ico")

while True:
	if send:
		post(titleBox.get(),descriptionBox.get())
	top.update_idletasks()
	top.update()

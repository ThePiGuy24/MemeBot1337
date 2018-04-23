from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import random

print("imported")
# Setup the Classroom API
SCOPES = 'https://www.googleapis.com/auth/classroom.coursework.students'
store = file.Storage('credentials.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store)
service = build('classroom', 'v1', http=creds.authorize(Http()))
print("set up")
# Call the Classroom API
##results = service.courses().list(pageSize=10).execute()
##courses = results.get('courses', [])
print("running")
##if not courses:
##    print('No courses found.')
##else:
##    print('Courses:')
##    for course in courses:
##        if course['name'] == "memes":
##            print(course['name'],course['id'])
##            cID = course['id']
cID = 7993359083

for c in range(5):
	courseWork = {  
		'title': 'hello from python',  
		'description': str(random.randint(0,1000000000000000000000000000000000)),  
		'workType': 'ASSIGNMENT',  
		'state': 'PUBLISHED',  
	}
	courseWork = service.courses().courseWork().create(  
		courseId=cID, body=courseWork).execute()  
	print('Assignment created with ID {0}'.format(courseWork.get('id')))

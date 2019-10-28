import pickle
import os.path
from datetime import datetime #,timedelta
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/calendar']

CREDENTIALS_FILE = 'credentials.json'

def get_calendar_service():
	creds = None
	# The file token.pickle stores access/refresh tokens, and is created
	# automatically after completing authorization for the first time.
	if os.path.exists('token.pickle'):
		with open('token.pickle', 'rb') as token:
			creds = pickle.load(token)
	# If there aren't valid credentials present, let user log in.
	if not creds or not creds.valid:
		if creds and creds.expired and creds.refresh_token:
			creds.refresh(Request())
		else:
			flow = InstalledAppFlow.from_client_secrets_file(
				CREDENTIALS_FILE, SCOPES)
			creds = flow.run_local_server(port=0)
		# Save the credentials for the next attempt
		with open('token.pickle', 'wb') as token:
			pickle.dump(creds, token)

	service = build('calendar', 'v3', credentials=creds)
	return service

def create_event():
	# Creates and publishes an event to the calendar
	service = get_calendar_service()

	event_result = service.events().insert(
		calendarId='primary',
		sendUpdates='all',
		body = {
			'summary': 'Test event',
			'description': 'Testing the auto creation of Gcal entry.',
			'start': {'dateTime': '2019-10-31T19:00:00', 'timeZone': 'US/Eastern'},
			'end':   {'dateTime': '2019-10-31T21:00:00', 'timeZone': 'US/Eastern'},
			'attendees': ['butler.421@gmail.com']
			}
		).execute()

	_event_confirm(event_result)

def _event_confirm(event_result):
	# Print items relating to completed calendar entry
	print("Created event.")
	print("EventID: ", event_result['id'])
	print("Summary: ", event_result['summary'])
	print("Start: ", event_result['start']['dateTime'])
	print("End: ", event_result['end']['dateTime'])
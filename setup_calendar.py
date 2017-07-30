from __future__ import print_function
from apiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools
from datetime import date
from dateutil.relativedelta import relativedelta


def get_credentials():

    SCOPES = 'https://www.googleapis.com/auth/calendar'
    store = file.Storage('storage.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
        creds = tools.run_flow(flow, store)
    GCAL = discovery.build('calendar', 'v3', http=creds.authorize(Http()))

    return GCAL


def final_time(number_months):
    """Calculate and returns an especific date, acording with the number of months than receive as parameter"""

    months = date.today() + relativedelta(months=+number_months)
    date_string = str(months)
    return date_string


def create_event(start_time, end_time, name_suscription):

    GCAL = get_credentials()

    GMT_OFF = '-07:00'      # PDT/MST/GMT-7
    EVENT = {
        'summary': 'Remember cancel suscription %s' % name_suscription,
        'start':  {'dateTime': start_time + 'T' + '09:00:00%s' % GMT_OFF},
        'end':    {'dateTime': end_time + 'T' + '10:00:00%s' % GMT_OFF}
    }

    e = GCAL.events().insert(calendarId='primary', sendNotifications=True, body=EVENT).execute()

    return e

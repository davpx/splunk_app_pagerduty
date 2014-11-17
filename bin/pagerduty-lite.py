#!/usr/bin/env python
import json
import requests


SUBDOMAIN='orionhealth'
API_ACCESS_KEY=''

def main():
    description = os.environ.get('SPLUNK_ARG_4', default_description)
    events = extract_events(os.environ.get('SPLUNK_ARG_8'))
    
    trigger_incident()

def trigger_incident(description, events):
    headers = {
        'Authorization': 'Token token={0}'.format(API_ACCESS_KEY),
        'Content-type': 'application/json',
    }
    payload = json.dumps({
      "service_key": "",
      "event_type": "trigger",
      "description": description,
      "client": "Sample Monitoring Service",
      "client_url": "https://monitoring.service.com",
      "details": {
        "ping time": "1500ms",
        "load avg": 0.75
      }
    })
    r = requests.post(
                    'https://events.pagerduty.com/generic/2010-04-15/create_event.json',
                    headers=headers,
                    data=payload,
    )
    print r.status_code
    print r.text
trigger_incident()

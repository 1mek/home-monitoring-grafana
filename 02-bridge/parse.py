

import re 
MQTT_TOPIC = 'i/+/+'  # i/sender/[m] || [battery|status|etc]
MQTT_REGEX = 'i/([^/]+)/([^/]+)'
MQTT_MULTI = '([^/]+)/([^/]+)'
MQTT_SEPARATOR = ';'
topic = 'i/ax22/m' 
payload = 'T/000;F/111;N/222;P/333' 
pay = payload.split (MQTT_SEPARATOR) 

match = re.match(MQTT_REGEX, topic)
if match:
    location = match.group(1)
    if match.group(2) == "m":
     pay = payload.split (MQTT_SEPARATOR) 
     for i in range (0, len (pay)):
        urk = re.match (MQTT_MULTI, pay[i]) 
        if urk  :
                location = match.group (1)
                measurement = urk.group (1)
                value = urk.group (2)
                print (location, measurement, value)
                _send_sensor_data_to_db_multi(location,measurement,value)
    else:
        measurement = match.group(2)
        print(location, measurement, payload)
        _send_sensor_data_to_db_multi(location,measurement,payload)


def _send_sensor_data_to_db_multi(location, measurement, value):
    json_body = [
        {
            'measurement': measurement,
            'tags': {
                'location': location
            },
            'fields': {
                'value': value
            }
        }
    ]
    print(json_body)

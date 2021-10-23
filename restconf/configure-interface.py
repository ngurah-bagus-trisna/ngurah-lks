import requests
import json

from requests.models import Response

# Bypass https
from urllib3.expections import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

# def = defining function / mendefinisikan fungsi
def printBytesAsJSON(bytes):
    print(json.dumps(json.loads(bytes), indent=2))

#inisialisasi Router

response = requests.patch(
    url= 'https://$router-ip/restconf/data/Cisco-IOS-XE-native:native/interface/GigabitEthernet=2',
    auth= ('patah','wait'),
    headers= {
        'Accept': 'application/yang-data+json',
        'Content-Type' : 'application/yang-data+json'
    },

    # inisialisasi interface gi2
    data = json.dumps({
        'Cisco-IOS-XE-native:GigabitEthernet': {
            'ip': {
                'address' :{
                    'primary': {
                        'address': '10.10.10.1',
                        'mask' : '255.255.255.0',
                    }
                }
            }
        }
    }),
    verify= False
)

print('Response Code: ' + str(response.status_code))

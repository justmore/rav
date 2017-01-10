import requests, json

headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

#---LOGIN---
login_url = 'https://cloud.ravellosystems.com/api/v1/login'

#login_req = requests.post(login_url,headers= headers ,auth = ('kunal.morparia@oracle.com','Welcome1#'))
#login_req_json = login_req.json()

#print(json.dumps(login_req_json, indent=4))


#---IMAGES---
get_image_url = 'https://cloud.ravellosystems.com/api/v1/organizations/3/images'

get_req = requests.get(get_image_url, headers=headers, auth = ('kunal.morparia@oracle.com','Welcome1#'))
get_req_json = get_req.json()
#print(json.dumps(get_req_json, indent=4))

for item in get_req_json:
    if item['name'] == 'linux_server2':
        print("VM: linux_server2: baseVmId: " + str(item['baseVmId']))
    elif item['name'] == 'linux_server3':
        print("VM: linux_server3: baseVmId: " + str(item['baseVmId']))
    elif item['name'] == 'linux_lamp1':
        print("VM: linux_lamp1: baseVmId: " + str(item['baseVmId']))
    elif item['name'] == 'linux_lamp2':
        print("VM: linux_lamp2: baseVmId: " + str(item['baseVmId']))
    elif item['name'] == 'linux_lamp3':
        print("VM: linux_lamp3: baseVmId: " + str(item['baseVmId']))


#---APPLICATIONS---
def query_application(appId):
    get_app_url = 'https://cloud.ravellosystems.com/api/v1/applications/' + appId
    #get_app_url = 'https://cloud.ravellosystems.com/api/v1/applications/'

    app_req = requests.get(get_app_url, headers= headers, auth = ('kunal.morparia@oracle.com','Welcome1#'))
    app_req_json = app_req.json()
    print(json.dumps(app_req_json, indent=4))


def update_application(appId,action):
    get_app_url = 'https://cloud.ravellosystems.com/api/v1/applications/' + appId + '/' + action
    print(get_app_url)
    #get_app_url = 'https://cloud.ravellosystems.com/api/v1/applications/'

    app_req = requests.post(get_app_url, headers= headers, auth = ('kunal.morparia@oracle.com','Welcome1#'))

    app_req_json = app_req.json()
    print(json.dumps(app_req_json, indent=4))

def add_vm_to_application(appId, vmId):
    add_vm_url = 'https://cloud.ravellosystems.com/api/v1/applications/' + appId + '/vms'
    payload = {"baseVmId": vmId}
    add_vm_req = requests.post(add_vm_url, headers=headers, auth=('kunal.morparia@oracle.com','Welcome1#'), data=json.dumps(payload))
    add_vm_json = add_vm_req.json()
    print(json.dumps(add_vm_json,indent=4))

#query_application('77237143')
#update_application('77237143','start')
add_vm_to_application('77237143','78307300')
#query_application('77237143')

def publish_application(appId):
    payload = { "preferredRegion": "us-central-1", "optimizationLevel": "PERFORMANCE_OPTIMIZED",
        "startAllVms": "true"}
    pub_url = 'https://cloud.ravellosystems.com/api/v1/applications/' + appId + '/publish'
    pub_req = requests.post(pub_url, headers=headers, auth=('kunal.morparia@oracle.com','Welcome1#'), data=json.dumps(payload))
    print(pub_req)
    #pub_json = pub_req.json()
    #print(json.dumps(pub_json, indent=4))

#publish_application('77237143')

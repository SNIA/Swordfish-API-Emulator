import json
import pprint
import requests
import test_templates
import sys

def send_post(url, payload):
    headers = {'Content-type':'application/json', 'Accept':'text/plain'}
    resp = requests.post (url, data = json.dumps(payload), headers = headers)

    return resp.status_code

def send_get(url):
    resp = requests.get(url)

    return resp.status_code, resp.json()

def send_delete(url):
    resp = requests.delete(url)

    return resp.status_code

def test_create_chassis(url):
    chassis_url = f"{url}/Chassis"
    ret_code = send_post(chassis_url, test_templates.test_chassis)

    if ret_code == 200:
        return True
    else:
        return False

def test_create_computer_system(url):
    # I am assuming we have already created the target Chassis
    system_url = f"{url}/Systems"
    ret_code = send_post(system_url, test_templates.test_system)

    if ret_code == 200:
        return True
    else:
        return False


def test_create_computer_system_duplicate_id():
    # To Be Implemented
    pass


def main():
    url = "http://localhost:5000/redfish/v1"

    print("##### Starting test Suite  #####")
    print()
    print ("Testing creating a Chassis...")
    if test_create_chassis(url):
        print ("PASSED")
    else:
        print ("FAILED")
        sys.exit(1)

    print("Testing creating a ComputerSystem...")
    if test_create_computer_system(url):
        print ("PASSED")
    else:
        print ("FAILED")
        sys.exit(1)


if __name__ == '__main__':
    main()
import requests
import json
import re
import time

def vt_reports(get_resource):
    try:
        reg = re.search('([0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3})', get_resource)
        ip_domain = "ip"
        get_resource = reg.group()
    except:
        ip_domain = "domain"


    url = f"https://api.metadefender.com/v4/{ip_domain}/{get_resource}"
    headers = {
        'apikey': "apikey"
    }

    response = requests.request("GET", url, headers=headers, proxies=proxies, verify=False)

    return response.text



if __name__=='__main__':

    with open('file.csv', 'r') as file:
        csv_data = file.readlines()
    for line in csv_data:
        try:
            json1 = json.loads(vt_reports(line))
            print(json1)
        except:
            json1 = json.loads(vt_reports(line.split('/')[0]))
            print(json1)
        try:
            print("Resource:", json1["address"])
            test1 = json1["lookup_results"]
            for ind in test1["sources"]:
                if ind["assessment"] != '':
                    try:
                        print(ind["provider"], ind["assessment"], ind["category\n"])
                    except:
                        print(ind["provider"], ind["assessment\n"])
        except:
            print("Error\n")
            error_output =  json1["error"]
            print(error_output['messages'])

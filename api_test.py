import requests

def showData():
    try:
        response_1 = requests.get('http://127.0.0.1:8000/readdata') 
        if(response_1.status_code == 200):
            print(response_1.text)
        else:
            print("Status code error")
    except:
        print("failed to load")

try:
    payload = {'query':20}
    response_2 = requests.get('http://127.0.0.1:8000/query',params=payload)
    print(response_2.text)
except:
    print("failed!!")
try:
    payload_1 = {"name":"user_3","age":32}
    reponse_3 = requests.put("http://127.0.0.1:8000/insert",json=payload_1)
    print(reponse_3)
    showData()
except:
    print("Error")

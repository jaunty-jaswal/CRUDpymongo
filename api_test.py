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

def queryParam():
    try:
        payload = {'query':20}
        response_2 = requests.get('http://127.0.0.1:8000/query',params=payload)
        print(response_2.text)
    except:
        print("failed!!")

def insertRequest():
    try:
        payload_1 = {"name":"user_3","age":32}
        reponse_3 = requests.put("http://127.0.0.1:8000/insert",json=payload_1)
        print(reponse_3)
        showData()
    except:
        print("Error")

def tryDelete(name):
    try:
        payload_ = {"name":f"{name}"}
        response_ =requests.delete("http://127.0.0.1:8000/deletedetails",json=payload_)
        print(response_)
    except:
        print("error")

if __name__ == "__main__":
    tryDelete(name="name 4")

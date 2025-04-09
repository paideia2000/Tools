import requests as req
from url import url, headers
from t_logging import error_logs

@error_logs
def method_get_api(ENDPOINT: str)-> list:
    """ get data oh the users to the api JSONPlaceholder"""
    try:
        if ENDPOINT:
            response = req.get(ENDPOINT, timeout=5)
            response.raise_for_status()
            
            if response.status_code == 200:
                print(f"\nRequest successfully to the URL:'{ENDPOINT}'. Status Code:{response.status_code}.")
                return response.json()
            else:
                    print(f"Invalid Status Code: {response.status_code}")
        
        else:
            print("\n¡ERROR! Check the content of the (endpoint).")
    except req.exceptions.HTTPError:
        print("Status Code Invalid")
        raise
    except req.exceptions.JSONDecodeError:
        print("¡JSONDecodeError! Could not be decoded to json format\n")
        raise
    except req.exceptions.ConnectionError:
        print("\n¡ConnectionError! Name or service not know. Please check it.\n")
        raise
    except req.exceptions.Timeout:
        print("\n¡TimeoutError! Too much time has elapsed since the request was made\n")
        raise

def method_post_api(ENDPOINT: str, HEADERS: dict ) ->None:
    """ make a post request to the api """
    
    data = {"name": "soy yoooo", "user": "lo dijo pinedom"}
    try:
        if ENDPOINT and HEADERS :
            response = req.post(ENDPOINT, json=data, headers=HEADERS, timeout=5)
            response.raise_for_status()
            
            if response.status_code == 201:
                print(f"\nThe data was loaded into the API successfully. Status_Code: {response.status_code}")
                print(response.text)
            

        else:
            print("\n¡ERROR! Check the content of the (endpoint) or (headers).")
    
    except req.exceptions.HTTPError as ht:
        print("\n",ht,"\n")
    except req.exceptions.ConnectionError:
        print("\n¡ConnectionError! Name or service not know. Please check it.\n")
    except req.exceptions.Timeout:
        print("\n¡TimeoutError! Too much time has elapsed since the request was made\n")

def method_patch_api(ENDPOINT: str, HEADERS: dict) ->None:
    """ patch de new information from the API """

    data = {"body":"change the body","name":"rene medina", "email": "poencima22@gmail.com"}
    try:
        if ENDPOINT and HEADERS :
            response = req.patch(ENDPOINT+"/1", json=data ,headers=HEADERS, timeout=5)
            response.raise_for_status()
            
            if response.status_code == 200:
                print(f"\nThe data was loaded into the API successfully. Status_Code: {response.status_code}")
                print(response.text)
            
        else:
            print("\n¡ERROR! Check the content of the (endpoint) or (headers).")
        
    except req.exceptions.HTTPError as ht:
        print("\n",ht,"\n")
    except req.exceptions.ConnectionError:
        print("\n¡ConnectionError! Name or service not know. Please check it.\n")
    except req.exceptions.Timeout:
        print("\n¡TimeoutError! Too much time has elapsed since the request was made\n")

def method_delete_api(ENDPOINT: str, HEADERS: dict) -> None:
    """ delete data from dataset API """
    
    params = {"body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"}
    try:
        if ENDPOINT and HEADERS:
            response = req.delete(ENDPOINT, params=params, headers=HEADERS, timeout=5)
            response.raise_for_status()
            
            if response.status_code == 200:
                print(f"\nThe data was deleted successfully. Status_Code: {response.status_code}")
                print(response.text)
            
        else:
            print("\n¡ERROR! Check the content of the (endpoint) or (headers).")
    
    except req.exceptions.HTTPError as ht:
        print("\n",ht,"\n")
    except req.exceptions.ConnectionError:
        print("\n¡ConnectionError! Name or service not know. Please check it.\n")
    except req.exceptions.Timeout:
        print("\n¡TimeoutError! Too much time has elapsed since the request was made\n")

def main():

    ENDPOINT = url()
    HEADERS = headers()
    try:
        
        # method_get_api(ENDPOINT)
        # method_post_api(ENDPOINT,HEADERS)
        # method_patch_api(ENDPOINT,HEADERS)
        # method_delete_api(ENDPOINT,HEADERS)
        pass
    
    except Exception as exp:
        print(exp)

if __name__=="__main__":
    main()
import requests as req
import json
from url import url, headers
from deco_loggi import error_logs

@error_logs()
def get_data_users(ENDPOINT: str)-> list:
    """ get data oh the users to the api JSONPlaceholder"""
    try:
        if ENDPOINT:
            response = req.get(ENDPOINT, timeout=5)
            response.raise_for_status()
            try:
                if response.status_code == 200:

                    print(f"\nRequest successfully to the URL:'{ENDPOINT}'. Status Code:{response.status_code}.")
                    return response.json()
                else:
                    print(f"Invalid Status Code: {response.status_code}")
            except ValueError:
                print(f"Error: The response from '{ENDPOINT}' is not valid JSON. The content might be HTML or another format.")
        else:
            print("\n¡ERROR! Check the content of the (endpoint).")
    
    except req.exceptions.JSONDecodeError:
        print("¡JSONDecodeError! Could not be decoded to json format\n")
    except req.exceptions.ConnectionError:
        print("\n¡ConnectionError! Name or service not know. Please check it.\n")
    except req.exceptions.Timeout:
        print("\n¡TimeoutError! Too much time has elapsed since the request was made\n")

def save_data_jsonfile(data_users: list, name_file: str)-> None:
    """ make file with the data of the users. """
    try:
        if name_file and data_users:
            with open(f"data_user/{name_file}", "w") as f:
                json.dump(data_users, f, indent=4, ensure_ascii=False)
                print("\nThe Information has been added successfully.\n")
        else:
            print("¡ERROR! Please checks the contents of the varibale (or) the name of the file.")
    except IsADirectoryError as isa:
        print(isa)
    except FileNotFoundError as fln:
        print(fln)

def post_new_user(ENDPOINT: str, HEADERS: dict ) ->None:
    """ make a post request to the api """
    
    data = {"name": "soy yoooo", "user": "lo dijo pinedom"}
    try:
        if ENDPOINT and HEADERS :
            response = req.post(ENDPOINT, data=json.dumps(data), headers=HEADERS, timeout=5)
            response.raise_for_status()
            
            if response.status_code == 201:
                print(f"\nThe data was loaded into the API successfully. Status_Code: {response.status_code}")
                print(response.text)
            

        else:
            print("\n¡ERROR! Check the content of the (endpoint) or (headers).")
    
    except req.exceptions.ConnectionError:
        print("\n¡ConnectionError! Name or service not know. Please check it.\n")
    except req.exceptions.Timeout:
        print("\n¡TimeoutError! Too much time has elapsed since the request was made\n")

def patch_new_data_user(ENDPOINT: str, HEADERS: dict) ->None:
    """ patch de new information from the API """

    data = {"body":"change the body","name":"rene medina", "email": "poencima22@gmail.com"}
    try:
        if ENDPOINT and HEADERS :
            response = req.patch(ENDPOINT+"/1", data=json.dumps(data) ,headers=HEADERS, timeout=5)
            response.raise_for_status()
            
            if response.status_code == 200:
                print(f"\nThe data was loaded into the API successfully. Status_Code: {response.status_code}")
                print(response.text)
            
        else:
            print("\n¡ERROR! Check the content of the (endpoint) or (headers).")
    
    except req.exceptions.ConnectionError as cnxe:
        print("\n¡ConnectionError! Name or service not know. Please check it.\n")
    except req.exceptions.Timeout as tm:
        print("\n¡TimeoutError! Too much time has elapsed since the request was made\n")

def delete_data(ENDPOINT: str, HEADERS: dict) -> None:
    """ delete data from dataset API """
    
    params = {"body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"}
    try:
        if ENDPOINT and HEADERS :
            response = req.delete(ENDPOINT + "/svsf", params=params,headers=HEADERS, timeout=5)
            response.raise_for_status()
            
            if response.status_code == 200:
                print(f"\nThe data was deleted successfully. Status_Code: {response.status_code}")
                print(response.text)
            
        else:
            print("\n¡ERROR! Check the content of the (endpoint) or (headers).")
    
    except req.exceptions.ConnectionError:
        print("\n¡ConnectionError! Name or service not know. Please check it.\n")
    except req.exceptions.Timeout:
        print("\n¡TimeoutError! Too much time has elapsed since the request was made\n")

def interface(ENDPOINT: str,PROMTP: str, HEADERS: dict) -> None:
    """ interface user """
    try:
        while True:
            print("BIENVENIDO RENE".center(100))
            print("Enter the number (1) make a GET REQUEST\nEnter the number (2) make a POST REQUEST")
            print("Enter the number (3) make a PATCH REQUEST\nEnter the number (4) make a DELETE REQUEST")
            choise_user = int(input(PROMTP))
            
            if not choise_user or choise_user not in range(1,5):
                print("\n¡ERROR! You only can enter a integer number in the range (1-4): ")
                continue
            else:
                if choise_user == 1:
                    data_users = get_data_users(ENDPOINT)# Call the function (get_data_user) to obtein the users data
                    while True:
                        save_or_not: str = input("\nIf you want to save the information in the file enter (YES) or (No) otherwise. ").strip().lower()
                        if save_or_not == "yes":
                            save_data_jsonfile(data_users, "users.json")
                            break
                        if save_or_not == "no":
                            break
                elif choise_user == 2:
                    post_new_user(ENDPOINT, HEADERS)# Call the function (oost_new_user) send the new user data
                    break
                elif choise_user ==3:
                    patch_new_data_user(ENDPOINT, HEADERS)
                    break
                else:
                    delete_data(ENDPOINT, HEADERS)

            
            
    except ValueError as vl:
        print("rene")

def main():

    ENDPOINT = url()
    PROMPT = "\nWhich option do you want to use: "
    HEADERS = headers()
    try:
        
        interface(ENDPOINT,PROMPT, HEADERS)
    
    except req.exceptions.HTTPError as ht:
        print("\n",ht,"\n")
    except Exception as exp:
        print(exp)

if __name__=="__main__":
    main()

URL = "https://jsonplaceholder.typicode.com/users"

urlbase = "https://jsonplaceholder"

urlpath = ".typicode.com"

user = "/posts"



def url():
    """ endpoint of api """
    return urlbase + urlpath + user


def headers():
    headers = {'Content-type': 'application/json; charset=UTF-8'}
    
    return headers

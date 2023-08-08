import requests

target_input = "google.com"


def make_request(url):
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        pass


with open("subdomainlist.txt","r") as subdomain_list:

   for word in subdomain_list:
       word = word.strip()
       url = "https://" + word + "." + target_input
       response = make_request(url)
       if response != None:
           print("Found Subdomain --->  "+url)



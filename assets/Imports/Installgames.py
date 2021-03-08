import requests

def Install(game):
     if game == 1:
         url= ""
         r = requests.get(url, allow_redirects=True)
         open("1.zip", "wb").write(r.content)
         close("1.zip")
     if game == 2:
         url= ""
         r = requests.get(url, allow_redirects=True)
         open("2.zip", "wb").write(r.content)
         close("2.zip")
     if game == 3:
         url= ""
         r = requests.get(url, allow_redirects=True)
         open("3.zip", "wb").write(r.content)
         close("3.zip")
     if game == 4:
         url= ""
         r = requests.get(url, allow_redirects=True)
         open("4.zip", "wb").write(r.content)
         close("4.zip")
     if game == 5:
         url= ""
         r = requests.get(url, allow_redirects=True)
         open("5.zip", "wb").write(r.content)
         close("5.zip")
         
         
         
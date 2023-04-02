import requests, os, threading
from waiting import wait

os.system("cls")

print("simul's deployhistory client downloader")

host = input("host: ")
target = input("target: ")

ap = ""
if target == "Client" or target == "WindowsPlayer" or target == "MFCStudio":
    ap = "RobloxApp.zip"
elif target == "Studio" or target == "Studio64":
    ap = "RobloxStudio.zip"
elif target == "RccService":
    ap = "RCCService.zip"

deployhistory = requests.get(f"http://{host}/DeployHistory.txt").text
lines = deployhistory.splitlines()
thing = 0

def download(version):
    global thing
    thing = thing + 1
    get = requests.get(f"http://{host}/{version}-{ap}")
    if get.status_code == 200:
        f = open(f"{version}-{ap}", "wb")
        f.write(get.content)
        f.close()
        print(f"{version} downloaded")
    else:
        print(f"{version} could not be downloaded")
    
    thing = thing - 1

for ln in lines:
    if ln.find(target) != -1:
        spl = ln.split(" ")
        version = spl[2]
        
        if thing < 15:
            threading.Thread(target=download, args=(version,)).start()
        else:
            wait(lambda: (thing < 25))
            threading.Thread(target=download, args=(version,)).start()

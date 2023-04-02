import requests, os

host = ""
# hosts: setup.roblox.com | setup.gametest2.robloxlabs.com
target = ""
# targets: Client | WindowsPlayer | RccService | MFCStudio | Studio | Studio64

ap = ""
if target == "Client" or target == "WindowsPlayer" or target == "MFCStudio":
    ap = "RobloxApp.zip"
elif target == "Studio" or target == "Studio64":
    ap = "RobloxStudio.zip"
elif target == "RccService":
    ap = "RCCService.zip"

os.system("cls")

print("simul's deployhistory client downloader")
print(f"host: {host}")
print(f"target: {target}")
print("fetching deployhistory...")

deployhistory = requests.get(f"http://{host}/DeployHistory.txt").text
lines = deployhistory.splitlines()

def download(version):
    get = requests.get(f"http://{host}/{version}-{ap}")
    if get.status_code == 200:
        f = open(f"{version}-{ap}", "wb")
        f.write(get.content)
        f.close()
        print(f"{version} downloaded")
    else:
        print(f"{version} could not be downloaded")

for ln in lines:
    if ln.find(target) != -1:
        spl = ln.split(" ")
        version = spl[2]
        
        download(version)

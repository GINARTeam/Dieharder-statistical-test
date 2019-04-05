from __future__ import unicode_literals
import urllib2
import requests
import json
import thread
from requests.auth import HTTPBasicAuth

########### N THREAD
# N = 2
# url = []
# def thread_get(url_,count,input_f):
#     ticket = requests.get(url_, headers = {'Connection': 'close'}).text

#     if url_ == url[N-1]:
#         for i in range(count - (N - 1)*count / N):
        
#             req = requests.get(('https://test.ginar.io/rng/generate/' + ticket), headers = {'Connection': 'close'})
        
#             print(req.elapsed.total_seconds())

#             response = req.json()
            
#             if response[u'beacon'] == '0xundefined':
#                 print(response)
#             else:
#                 print(response)
#                 beacon = (long(str(response[u'beacon']),16))
#                 input_f.write(format(beacon,'0256b') + '\n')
#                 i += 1
#     else:
#         for i in range(count/N):
            
#             req = requests.get(('https://test.ginar.io/rng/generate/' + ticket), headers = {'Connection': 'close'})

#             print(req.elapsed.total_seconds())

#             response = req.json()
            
#             if response[u'beacon'] == '0xundefined':
#                 print(response)
#             else:
#                 print(response)
#                 beacon = (long(str(response[u'beacon']),16))
#                 input_f.write(format(beacon,'0256b') + '\n')
#                 i += 1

            
#         ticket = str(response[u'sessionKey'])
# def getInput():
#     count = input('Number of requests ( min = 8000 ): ')
#     input_f = open('input.txt','w')
    
    
#     for i in range(N):
#         a = raw_input('Your URL with session-key %d: ' %i)
#         url.append(a)
        
#     for i in range(N):    
#         try:
#             thread.start_new_thread(thread_get,(url[i],count,input_f))
#         except:
#             print ("Error: unable to start thread")
#         finally:
#             pass
# getInput()


################ 1 THREAD
def getInput():
    input_f = open('input.bin','a')
    count = input('Number of requests ( min = 8000 ): ')
    url = raw_input('Your random: ' )
    url = "https://test.ginar.io/rng/initialize/" + url
    ticket = requests.get(url,auth=HTTPBasicAuth('pk_3201545637443695', 'sk_3201545637443700'), headers = {'Connection': 'close'}).text
    for i in range(count):      
        req = requests.get(('https://test.ginar.io/rng/generate/' + ticket), headers = {'Connection': 'close'}, auth=HTTPBasicAuth('pk_3201545637443695', 'sk_3201545637443700'))
        ######## check status code
        print(req.status_code)
        if req.status_code != 200:
            i -= 1
            ticket = requests.get(url,auth=HTTPBasicAuth('pk_3201545637443695', 'sk_3201545637443700'), headers = {'Connection': 'close'}).text
            continue
        
        print(req.elapsed.total_seconds())
        response = req.json()
        
        print(response)
        if response == 'invalid request':
            i -= 1
            ticket = requests.get(url,auth=HTTPBasicAuth('pk_3201545637443695', 'sk_3201545637443700'), headers = {'Connection': 'close'}).text
            continue
        if response[u'beacon'] == u'0xundefined':
            i -= 1
        else:
            beacon = (long(str(response[u'beacon']),16))
            input_f.write(format(beacon,'0256b') + '\n')
            i += 1
        ticket = str(response[u'sessionKey'])

getInput()












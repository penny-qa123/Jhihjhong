import json
import random
import time
import requests
import threading
import uuid
from cryptoJS_PY import signature_body

#deviceid = uuid.uuid1()

#更新設備   update_user_device
with open(file=r'./public.pem') as f:
    pub_key = f.read()
    
data = {"device_id": "6277f88f-af11-11eb-9936-18c04db5476a", "public_key": pub_key, "sms_code": "000000","pushid": ""}
request = {"appid": "BITOLLWALLETDEMO", "sign_type": "SHA256WithRSAClient","phone": "917444002","phone_code": "886",
        "retrieve": "update_user_device","seq": "6","data": data}

sig = signature_body(message=request, rsa_path=r'./private.pem')

body = {"appid": "BITOLLWALLETDEMO", "sign": sig, "sign_type": "SHA256WithRSAClient",
            "phone": "917444002",
            "phone_code": "886", "retrieve": "update_user_device", "seq": "6",
            "data": data}
body = json.dumps(body)
re = requests.session().post(url='https://vk4uikzpgc.execute-api.ap-east-1.amazonaws.com/dev/retrieve', data=body)
print(re.text)

#注冊 register_by_userno

with open(file=r'.\public.pem') as f1:
    pub_key = f1.read()

data = {'nick_name': 'pennynick009', 'name':'penny009',
            'phone': '917444009', 'phone_code': '886', 'sms_code': '000000',
            'captcha_id': '',
            'password': 'welcomeqa1', 'device_id': '0ca4e53f-aee1-11eb-869c-18c04db5476a', 'public_key': pub_key,
            'pushid': ''}
request = {"appid": "BITOLLWALLETDEMO", "sign_type": "SHA256WithRSAClient", "retrieve": "register_by_userno",
               "seq": "6",
               "data": data}  
sig = signature_body(message=request, rsa_path=r'./private.pem')
body = {'appid': 'BITOLLWALLETDEMO', 'sign':sig, 'sign_type': 'SHA256WithRSAClient',
            'retrieve': 'register_by_userno',
            'data': data, 'seq': '6'}
body = json.dumps(body)    

url = 'https://vk4uikzpgc.execute-api.ap-east-1.amazonaws.com/dev/retrieve'
resp = requests.session().post(url=url, data=body, verify=False)
str_re = resp.content.decode()
dict_re = eval(str_re)
print("注册",dict_re['comment'],dict_re['nick_name'])   
 
# 手機密碼登錄 login_by_phone_password
data = {"phone": "917444008", "phone_code": "886", "sms_code": "000000", "nonce": "1",
                "client_type": "android",
                "captcha_id": "", "password": "welcomeqa1", "device_id": "bb8e5f34-af11-11eb-8655-18c04db5476a"}

request = {"appid": "BITOLLWALLETDEMO", "sign_type": "SHA256WithRSAClient",
                   "retrieve": "login_by_phone_password", "data": data, "seq": "6"}		
sig = signature_body(message=request, rsa_path=r'./private.pem')	

body = {"appid": "BITOLLWALLETDEMO", "sign": sig, "sign_type": "SHA256WithRSAClient",
                "retrieve": "login_by_phone_password", "data": data, "seq": "6"}	
body = json.dumps(body)		
re = requests.session().post(url='https://vk4uikzpgc.execute-api.ap-east-1.amazonaws.com/dev/retrieve',data=body)		
str_re = re.content.decode()
dict_re = eval(str_re)
#token = dict_re['token']
print(str_re)
				
#asset_get

#with open(file='newdata', mode='r')as f:
#    s_f = f.readlines()
# token---login後才能拿到
data = {"asset_name": "USDT"}
request = {"appid": "BITOLLWALLETDEMO", "sign_type": "SHA256WithRSAClient", "retrieve": "assets_gen",
        "name": "penny008", "phone": "917444008", "phone_code": "886",
        "token": token,
        "data": data, "seq": "6"}
sig = signature_body(message=request, rsa_path=r'./private.pem')

body = {"appid": "BITOLLWALLETDEMO", "sign": sig, "sign_type": "SHA256WithRSAClient", "retrieve": "assets_gen",
        "name": "penny008", "phone": "917444008", "phone_code": "886",
        "token": token,
        "data": data, "seq": "6"}
body = json.dumps(body)
re = requests.session().post(url='https://vk4uikzpgc.execute-api.ap-east-1.amazonaws.com/dev/retrieve', data=body,verify=False)
# self.user_info(resp=re)

# print('状态码%s\n响应头%s\n响应正文%s' % (re.status_code, re.headers, re.content))
str_re = re.content.decode()
dict_re = eval(str_re)
print("设置账户", dict_re['comment'])
                
# 轉帳 transfer
data = {"asset_name": "USDT", "order_id": "",
                "to_phone": "917444002", "to_phone_code": "886",
                "to_user": "", "amount": "1234", "pin_code": "123456"}
				
request = {"appid": "BITOLLWALLETDEMO", "sign_type": "SHA256WithRSAClient", "retrieve": "transfer",
                   "name": "", "phone": "917444003", "phone_code": "886",
                   "token": token,
                   "data": data, "seq": "6"}

sig = signature_body(message=request, rsa_path=r'./private.pem')

body = {"appid": "BITOLLWALLETDEMO", "sign": sig, "sign_type": "SHA256WithRSAClient", "retrieve": "transfer",
                "name": "", "phone":"917444003", "phone_code": "886",
                "token": token,
                "data": data, "seq": "6"}		 

body = json.dumps(body)		

#re = requests.session().post(url='https://vk4uikzpgc.execute-api.ap-east-1.amazonaws.com/dev/retrieve',data=body)
									 
comment = eval(re.content.decode())["comment"]			

# 登錄 login
data = {"phone": "917444002", "phone_code": "886", "sms_code": "000000", "nonce": "1",
            "client_type": "android",
            "captcha_id": "",
            "password": "welcomeqa1", "device_id": "1cad2226-a63c-11eb-a701-18c04db5476a"}
request = {"appid": "BITOLLWALLETDEMO", "sign_type": "SHA256WithRSAClient", "retrieve": "login", "data": data,
               "seq": "6"}

sig = signature_body(message=request, rsa_path=r'./private.pem')
body = {"appid": "BITOLLWALLETDEMO", "sign": sig, "sign_type": "SHA256WithRSAClient", "retrieve": "login",
            "data": data, "seq": "6"}
body = json.dumps(body)
re = requests.session().post(url='https://vk4uikzpgc.execute-api.ap-east-1.amazonaws.com/dev/retrieve', data=body)		
str_re = re.content.decode()
dict_re = eval(str_re)
token = dict_re['token']
print(str_re)	

#設置或更新支付密碼
data = {'old_pin_code':'', 'new_pin_code':'123456'}

request = {"appid": "BITOLLWALLETDEMO", "sign_type": "SHA256WithRSAClient","name":"penny007","phone":"917444007","phone_code":"000000","token":token
                   ,"retrieve": "update_pin_code", "data": data}		
				   
sig = signature_body(message=request, rsa_path=r'./private.pem')	

body = {"appid": "BITOLLWALLETDEMO", "sign": sig, "sign_type": "SHA256WithRSAClient","name":"penny007","phone":"917444007","phone_code":"000000","token":token
                   ,"retrieve": "update_pin_code", "data": data}	
				   
body = json.dumps(body)	
re = requests.session().post(url='https://vk4uikzpgc.execute-api.ap-east-1.amazonaws.com/dev/retrieve',data=body)		
str_re = re.content.decode()
dict_re = eval(str_re)

#Order_list
request = {"appid": "BITOLLWALLETDEMO", "order_id": "w15991036808", "user_no": "", "user": "", "type": "", "accepted_from": "", "asset": "USDT", "address": "",
            "start_time": 1599097079, "end_time": 0, "page_number": 0, "page_size": 0
}

sig = signature_body(message=request, rsa_path=r'./private.pem')	

body = {"appid": "BITOLLWALLETDEMO", "sign": sig, "sign_type": "SHA256WithRSAClient","retrieve": "order_list", "seq": ""}	
body = json.dumps(body)	                   
re = requests.session().post(url='https://vk4uikzpgc.execute-api.ap-east-1.amazonaws.com/dev/retrieve',data=body)		
str_re = re.content.decode()
dict_re = eval(str_re)                   

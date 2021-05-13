import json
import random
import time
import requests
import threading
import uuid
from cryptoJS_PY import signature_body



def register(c):
    deviceid = uuid.uuid1()
    deviceid = str(deviceid)
    name = "penny"+str(c)[6:9]
    nick_name = "pennynick"+str(c)[6:9]
    phone = str(c)
    print(nick_name)

    with open(file=r'./Key/public.pem') as f1:
        pub_key = f1.read()
    data = {'nick_name': nick_name, 'name':name,
            'phone': phone, 'phone_code': '886', 'sms_code': '000000',
            'captcha_id': '',
            'password': 'welcomeqa1', 'device_id': deviceid, 'public_key': pub_key,
            'pushid': ''}
    request = {"appid": "BITOLLWALLETDEMO", "sign_type": "SHA256WithRSAClient", "retrieve": "register_by_userno",
               "seq": "6",
               "data": data}
    sig = signature_body(message=request, rsa_path=r'.\Key\private.pem')
    body = {'appid': 'BITOLLWALLETDEMO', 'sign':sig, 'sign_type': 'SHA256WithRSAClient',
            'retrieve': 'register_by_userno',
            'data': data, 'seq': '6'}
    body = json.dumps(body)

    url = 'https://vk4uikzpgc.execute-api.ap-east-1.amazonaws.com/dev/retrieve'
    resp = requests.session().post(url=url, data=body, verify=False)
    str_re = resp.content.decode()
    dict_re = eval(str_re)
    print(dict_re)
    if dict_re['comment'] == 'register success':
        print("注册",dict_re['comment'],dict_re['nick_name'])
        str_regiser = {"phone": phone, "name": name, "phone_code": "886", "password": "welcomeqa1", "device_id": deviceid}
        json_regiser = json.dumps(str_regiser)
        with open(file='./Data/RegistedList.txt', mode='a')as fd:
            fd.writelines(
                time.strftime(json_regiser + '\n')
            )
    else:
        print("注册失敗:",dict_re['comment'])

if __name__ == '__main__':
    # 调用方法注意不要重复使用数字范围，递增即可
    for i in range(917444206,917444207):
        #ListRespToken = []
        register(i)
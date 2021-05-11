import json
import random
import time
import requests
import threading
import uuid
from cryptoJS_PY import signature_body

#
class MultiRunner:
    def __init__(self):
        pass

    def login_by_phone_password(self, u_phone, u_name, u_phone_code, u_device_id, u_password):
        # 请求数据签名阶段
        data = {"phone": u_phone, "phone_code": u_phone_code, "sms_code": "000000", "nonce": "1",
                "client_type": "android",
                "captcha_id": "", "password": u_password, "device_id": u_device_id}
        request = {"appid": "BITOLLWALLETDEMO", "sign_type": "SHA256WithRSAClient",
                   "retrieve": "login_by_phone_password", "data": data, "seq": "6"}

        sig = signature_body(message=request, rsa_path=r'.\Key\private.pem')

        body = {"appid": "BITOLLWALLETDEMO", "sign": sig, "sign_type": "SHA256WithRSAClient",
                "retrieve": "login_by_phone_password", "data": data, "seq": "6"}
        body = json.dumps(body)
        re = requests.session().post(url='https://vk4uikzpgc.execute-api.ap-east-1.amazonaws.com/dev/retrieve',data=body)
        # 输出到日志
        self.user_info(resp=re)

    def user_info(self, resp):
        str_re = resp.content.decode()
        with open(file='./DC726_log.txt', mode='a')as fd:
            fd.writelines(
                time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + str_re + '\n')
# 主要程序
    def main_test(self, phone, name, phone_code, password, device_id):
        for j in range(1):
            self.login_by_phone_password( u_phone=phone, u_name=name, u_phone_code=phone_code, u_password=password, u_device_id=device_id)
            transfer_time = random.randrange(0, 1)
            time.sleep(transfer_time)
if __name__ == '__main__':
    list_thread = []
    for i in range(1):
        # 每次循环开辟新的内存，禁止将类示例doa放在循环外面，否则内存混乱
        mt = MultiRunner()
        with open(file='DC726_LoginAccount.txt', mode='r')as f:
            s_f = f.readlines()
            phone = eval(s_f[i])['phone']
            name = eval(s_f[i])['name']
            phone_code = eval(s_f[i])['phone_code']
            password = eval(s_f[i])['password']
            device_id = eval(s_f[i])['device_id']
        # 线程传参并 开始
        T = threading.Thread(target=mt.main_test, name='thread_worker No.%s,Im %s' % (i,name),
                                 args=[phone, name, phone_code, password, device_id])
        T.start()
        thread_time = random.randrange(0, 3)
        time.sleep(thread_time)
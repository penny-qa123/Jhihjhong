import json
import os

from Crypto import Signature
import uuid
import base64
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import MD5, SHA256



# s = 'appid=BITOLLWALLETDEMO&data=map[captcha_id: client_type:andriod device_id: nonce:1 password:a1111111 phone:177880 phone_code:86 sms_code:]&retrieve=login&seq=6&sign_type=SHA256WithRSAClient'
prk = "-----BEGIN RSA PRIVATE KEY-----" \
      "MIIEpgIBAAKCAQEAruqz9+kW12YjNdCvwAsfhDhpvp8ylIDXZI8miW3k7U1/EwDT" \
      "MsDlvn5HiJ8eNOBJ0nj+tHYK1iHmB5reSXQ1hdOwGFc/KHJEIZGabC0+fw1ckQjM" \
      "gwTbIJUQYxANdb6yGHRXMlJl4BJXPDkEubIUSxztELr6+/q3vb5W4/Hjjx0sdfB7" \
      "MDcg0m2Fk7JV9NIBWAnwRPJtlTMuc8ASDABYm2oJ30KDE/BvtyMxY35Z2NwDDO23" \
      "d4P7OReTsuzWJSf8fRgpBw/irnJC6YjPqILJxHaFkbxlGeSnGKdBkO0F+MRdTHbm" \
      "b9nq/q4nduq6ADm3l0vRJgGO35gW34OU95f0YwIDAQABAoIBAQCMUv3OBNCuPOJC" \
      "agiUqFfAWwF6S3zoZfRmV/Eyj1b4iRNIy4CjVtz41ZXNpNk20jhnAWpUm95Vqxw/" \
      "PZ7WjsPheNHstRGWARVnWMfpwOJCSxXXxJdNBLhGi096KYaizzlRJQRO+ouAFzak" \
      "uZlw38wn9iy5H0f6nkiJkAllFMjaJdmQfYMX+i4P27RryfUEOLk0DTMkhjNXp/hh" \
      "18yBcuzklb83d00xQ8wQwccVAuLQIrQeUM7Z5ffTzu3MLqmfp3VxxT8xA2uOnf+j" \
      "yRLJvURZpcQD2as+ryYnK1Z26uXLFhMlAzNM9/oWRFeQGDC7wIftVD4FaWfjlkLy" \
      "PgRKJ2EBAoGBANzFEyi5WQboXVQis9tQlvnP777kyrhs1JOGg9Ay2nWxLgRchoj9" \
      "oOZ1hIN1z40wBYvYC60iiwSgH+sJADsbVHV3C86yLd8aXBLp1yz5/RECLDGXjQiJ" \
      "lsq4iEMLzRtVs+CbNpRzwZEL7OlMFoMu8Ci9THg0NKBej4DrmwI9C0sFAoGBAMrU" \
      "bulXkAJ+WWd4yua01etsViVKr3XAnwiSKX1myMvlZDPg5CdjCyW/cu+SBDl62KBW" \
      "DAuunoF08Rtdl+SrAlMD5Im++n5FWtTW/AEDNMlRvpNYnmHmB0ET1/SJexU4+eci" \
      "4rbfXuZr/BKYmZ/k1e1cvimbwX4ZlUCukTVbcm5HAoGBAMvld/x0srSehxPduR8l" \
      "H0s5sMMtq80JNovKAJOZZAquyUFd8yMynBg9EVYYyMgtQfIWZzJQZPSwrsn0VjJA" \
      "25BhkpYkGhmjzsXpEsKHYCMFTqu+vJLWAF7ab378t0I3tRoMQCx7fJrp2LTfgStH" \
      "fqchri6WiMRUkVUQROmcV4HBAoGBAL4RBYIJ+LwtdFAfBFve15tOIQe/Dd7VSvH4" \
      "LYMCn2VaJ2Tp+ELkcBzGY8kV1nmaoYbWO2FzF7uOPyX6tYylp37tZeqimQ9cpHpQ" \
      "n0O/omaJAIIJCBoLOX8FPlg7wKgphRzQNw1REhfw1v0CHOuVv9Y3E0fgWhh1lsRP" \
      "EWmjsP6fAoGBANPMCXFTTBGMhhB1npebJfqUF28vN4uWZ/X3ee6xqfYf1z8gRg1f" \
      "Mq087lb8ULck+3EyRRVtyFlnd9fU+lW+BYNF2aDwEOKO41MiYhhMM6ovIwmLBD9X" \
      "CL3tJx7XYdHhCDFy15HFAUZJhj7/CMSlh9ykPn7/NTu2sXO6RGlo5IwB" \
      "-----END RSA PRIVATE KEY-----"


pubkey = "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAruqz9+kW12YjNdCvwAsf" \
         "hDhpvp8ylIDXZI8miW3k7U1/EwDTMsDlvn5HiJ8eNOBJ0nj+tHYK1iHmB5reSXQ1" \
         "hdOwGFc/KHJEIZGabC0+fw1ckQjMgwTbIJUQYxANdb6yGHRXMlJl4BJXPDkEubIU" \
         "SxztELr6+/q3vb5W4/Hjjx0sdfB7MDcg0m2Fk7JV9NIBWAnwRPJtlTMuc8ASDABY" \
         "m2oJ30KDE/BvtyMxY35Z2NwDDO23d4P7OReTsuzWJSf8fRgpBw/irnJC6YjPqILJ" \
         "xHaFkbxlGeSnGKdBkO0F+MRdTHbmb9nq/q4nduq6ADm3l0vRJgGO35gW34OU95f0" \
         "YwIDAQAB"

# data = {'phone': '177880', 'phone_code': '63', 'sms_code': '000000', 'nonce': '1', 'client_type': 'andriod',
#         'captcha_id': '',
#         'password': 'a1111111', 'device_id': '9c30691f-35a1-48da-8ed3-ae0b03f7b3f5'}
# request = {'appid': 'BITOLLWALLETDEMO', 'sign': '', 'sign_type': 'SHA256WithRSAClient', 'retrieve': 'login',
#            'data': data, 'seq': '6'}

def datadeal(r):
    # 键的列表
    sr = sorted(r)
    pre_d = []
    for j in sr:
        if type(r[j]) == dict:
            # print('继续追踪', j)
            c = datatrack(r[j])
            pre_d.append(j + '=' + c)

        else:
            pre_d.append('%s=%s' % (j, r[j]))

    newpred = '&'.join(pre_d)
    # print('数据处理格式',newpred)
    return newpred
    # return bytes(newpred,encoding='utf-8')


def datatrack(r={}):
    p = []
    r1 = sorted(r)
    for i in r1:
        if type(r[i]) != dict:
            p.append(i + ':' + r[i])
        else:
            c = datatrack(r[i])
            p.append(i + ":" + c)
    p1 = ' '.join(p)
    conrdi = "map[" + p1 + "]"
    return conrdi

d={'appid': 'DCBOXDEMO', 'order_id': '', 'user_no': 'SM901988', 'type': '', 'accepted_from': '', 'asset': 'USDT', 'address': '', 'start_time': '1607788800', 'end_time': 0, 'page_number': 0, 'page_size': 0}
s = 'appid=BITOLLWALLETDEMO&data=map[captcha_id: client_type:andriod device_id: nonce:1 password:a1111111 phone:177880 phone_code:86 sms_code:]&retrieve=login&seq=6&sign_type=SHA256WithRSAClient'

def datadeal_merchant(c):
    print(sorted(c))
# def hash_handle(d, hashtype):
#     if hashtype == 'MD5':
#         return MD5.new(d.encode('utf-8'))
#     elif hashtype == 'SHA256':
#         digest = SHA256.new()
#         digest.update(d.encode('utf8'))
#         return digest
#
#     else:
#         pass
#
#
# def handle_private_key(key,s,e):
#
#     result = ''
#     # 分割key，每64位长度换一行
#     divide = int(len(key) / 64)
#     divide = divide if (divide > 0) else divide + 1
#     line = divide if (len(key) % 64 == 0) else divide + 1
#     for i in range(line):
#         result += key[i * 64:(i + 1) * 64] + '\n'
#     result_key = s + result + e
#     print(result)
#     return result_key


def sign(p, re):
    # 导入私钥
    key = RSA.import_key(p)
    signer = Signature.PKCS1_v1_5.new(key)
    # 数据处理
    data = datadeal(r=re)
    d = SHA256.new()
    d.update(data.encode('utf8'))
    # 加签
    signed = signer.sign(d)
    print('签名后的数据', signed)
    final_sign = base64.b64decode(signed, '-_')
    print(len(final_sign))
    return final_sign

def verify_sig(sig,pubk,r):

    sig+=b'==='
    print(len(sig))
    base64.b64decode(sig,'-_')
    pk=RSA.import_key(pubk)
    verifyer=PKCS1_v1_5.new(pk)
    d=SHA256.new()
    d.update(r.encode('utf8'))
    v=verifyer.verify(d,sig)
    print(v)

def signature_merchant(message, rsa_path):#用户商户
    '''使用私钥签名'''
    with open(rsa_path) as f:
        key = f.read()
        print(key)
        rsakey = RSA.importKey(key)
        signer = PKCS1_v1_5.new(rsakey)
        digest = SHA256.new()
        # digest.update(message)
        digest.update(message.encode('utf-8'))
        sign = signer.sign(digest)
        signature = base64.b64encode(sign).decode()
        # print('签名生成', type(signature), signature)
        return signature


def signature_body(message, rsa_path):#用于app
    '''使用私钥签名'''
    with open(rsa_path) as f:
        key = f.read()
        rsakey = RSA.importKey(key)
        signer = PKCS1_v1_5.new(rsakey)
        data = datadeal(message)
        digest = SHA256.new()
        digest.update(data.encode())
        sign = signer.sign(digest)
        signature = base64.b64encode(sign).decode()
        # print('签名生成',type(signature),signature)
        return signature

def verify_signature(message, signature, pub_rsa_path):
    '''验证签名'''
    with open(pub_rsa_path) as f:
        key = f.read()

        rsakey = RSA.importKey(key)
        verifier = PKCS1_v1_5.new(rsakey)
        data=datadeal(message)
        digest = SHA256.new()
        digest.update(data.encode())
        is_verify = verifier.verify(digest, base64.b64decode(signature))
        # print('验签是否成功',is_verify)
        return is_verify



if __name__ == '__main__':
    with open(r'C:\Users\janti\public.pem') as f:
    # with open(r'C:\Users\janti\private.pem') as f:
        key = f.read()
        print(key)
    with open(r'C:\Users\janti\private.pem') as f:
        key = f.read()
        print(key)
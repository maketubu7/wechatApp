# -*- coding: utf-8 -*-
# @Time    : 2020/2/11 20:00
# @Author  : Deng Wenxing
# @Email   : dengwenxingae86@163.com
# @File    : UserService.py
# @Software: PyCharm
import hashlib, base64, random,string


class UserService():

    @staticmethod
    def geneAuthCode( user_info ):
        m = hashlib.md5()
        str = "%s-%s-%s-%s"%(user_info.uid,user_info.login_name,user_info.login_pwd,user_info.login_salt)
        m.update(str.encode('utf-8'))
        return m.hexdigest()


    @staticmethod
    def genPwd(pwd, salt):
        m = hashlib.md5()
        str = '%s-%s'%(base64.encodebytes(pwd.encode('utf8')),salt)
        m.update(str.encode('utf-8'))
        return m.hexdigest()

    @staticmethod
    def geneSalt(length = 16):
        key_list = [random.choice(string.ascii_letters + string.digits) for _ in range(length)]
        return ''.join(key_list)

if __name__ == '__main__':
    pass
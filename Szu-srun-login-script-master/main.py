import os
import time
from SzuSrunLogin.LoginManager import LoginManager

import requests


def is_connect_internet(url="http://www.baidu.com", timeout=5):
    """
    检测是否可以连接到指定的URL。

    参数:
    url : str
        要测试连接的URL，默认为http://www.google.com。
    timeout : int
        设置请求超时时间，默认为5秒。

    返回:
    bool
        如果连接成功返回True，否则返回False。
    """
    try:
        # 发送HEAD请求到指定的URL
        requests.head(url, timeout=timeout)
        return True
    except requests.ConnectionError:
        return False
    except requests.Timeout:
        return False
# # 使用示例
# connected = is_connect_internet()
# print("Connected to the internet:", connected)

def always_login(username, password,checkinterval):
    lm = LoginManager()
    login = lambda: lm.login(username=username, password=password)
    timestamp = lambda: print(time.asctime(time.localtime(time.time())))

    timestamp()
    try:
        login()
    except Exception:
        pass
    while 1:
        time.sleep(checkinterval)
        if not is_connect_internet():
            timestamp()
            try:
                login()
            except Exception:
                pass
        else:
            print('already login')


if __name__ == "__main__":
    user_id = os.getenv("USER_ID", "校园卡账号")
    password = os.getenv("PASSWORD", "密码")
    #10s检测一次
    checkinterval = os.getenv("CHECK_INTERVAL", 10)

    always_login(user_id, password,int(checkinterval))

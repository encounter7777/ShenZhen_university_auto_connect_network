# ShenZhen_university_auto_connect_network

This repo is just for Szu students who needs to auto_login in the school network. 

SZU 校园网自动登录脚本 

Reference: [源代码来源](https://github.com/coffeehat/BIT-srun-login-script)。

## 功能介绍

1.该代码实现深大校园网自动登录。

2.死循环逻辑，检测断网就连接，可设置检测时长，建议1h检测一次。

3.可自行修改代码，仅修改main文件的代码即可，其他部分已适配深大校园网登录网页。

4.后面会讲如何将代码打包成.exe可执行文件，直接运行即可，这一点可以省略。

## 使用方法

### 1.补全main文件中校园账号密码部分

```
if __name__ == "__main__":
    user_id = os.getenv("USER_ID", "校园卡账号")
    password = os.getenv("PASSWORD", "密码")
    #10s检测一次
    checkinterval = os.getenv("CHECK_INTERVAL", 10)
    always_login(user_id, password,int(checkinterval))
```

### 2.环境配置和运行

```
pip install requests # 安装requests库
python main.py # 运行脚本
```

### 3.打包成exe可执行文件

```
pip install pyinstaller #依赖包,安装pyinstaller库
cd  \path  #切换到main.py的文件目录下 (path是具体情况)
pyinstaller -F main.py #打包，会在\path目录下生成dist文件夹，dist文件夹里面放的就是exe文件
```

### 4.将exe文件放开机自启动（一般别做）

```
#放开机自启动后，开机即联网，但一般不推荐使用（死循环的程序），推荐可以改成单次login的目的，放自启动

win + r 打开命令行，输入shell:startup，然后回车（此时会打开一个文件夹）,然后将.exe文件放进打开的文件夹里，此时自启动部署完成。

```


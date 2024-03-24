import frida
import sys


# 打开文件（默认以只读方式打开）
def get_script_str(file_name: str):
    with open(file_name, 'r', encoding='utf-8') as file:
        # 读取文件内容
        content = file.read()
        # 输出文件内容
        return content


# 连接手机设备
rdev = frida.get_remote_device()

session = rdev.attach("车智赢+")

script = session.create_script(get_script_str('1.pwd.js'))


def on_message(message, data):
    print(message, data)


script.on("message", on_message)

script.load()
sys.stdin.read()

import hashlib


# md5加密函数
def get_md5(data: str):
    obj = hashlib.md5()
    obj.update(data.encode('utf-8'))
    hex_string = obj.hexdigest()
    return hex_string


"""
明文： 123qwe123
md5加密结果= 
b538c6fd231ef0fbf7f09fe393663cf8
b538c6fd231ef0fbf7f09fe393663cf8
"""
if __name__ == '__main__':
    get_md5("123qwe123")

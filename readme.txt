    爬虫预习第6期
        1、git init
        2、git config user.email "test@qq.com"
        3、git config user.name "test"
        4、git remote add origin https://github.com/sunzhenvip/指定的xx项目.git
        5、git add .
        6、git commit -m "xx提交内容"
        7、修改当前项目代理地址 git config --local http.proxy 127.0.0.1:8889
    安装第三方依赖库
        python版本 python --version => Python 3.7.9
        默认纯净虚拟环境
            执行命令 pip3 list
                Package    Version
                ---------- -------
                pip        21.1.2
                setuptools 57.0.0
                wheel      0.36.2
        1、pip3 install --index-url https://pypi.doubanio.com/simple/ requests==2.31.0
        2、pip3 install --index-url https://pypi.doubanio.com/simple/ pycryptodome==3.20.0( 库名实际是 Crypto )
        2、pip3 install --index-url https://pypi.doubanio.com/simple/ frida==16.0.1
        3、pip3 install --index-url https://pypi.doubanio.com/simple/ frida-tools==12.0.1
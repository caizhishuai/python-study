# python-study
python-study

## 常用命令
```shell
#安装/卸载包
pip install numpy
pip uninstall numpy
```

## pip镜像配置
 ```shell
 #appdata下面创建pip文件夹 创建pip.ini 增加相应命令
cd %APPDATA%
mkdir %APPDATA%/pip
vim %APPDATA%/pip/pip.ini
vim ~/.pip/pip.conf

#内容如下
[global]
index-url=https://mirrors.aliyun.com/pypi/simple/
[install]
trusted-host=mirrors.aliyun.com
 ```

# python-study
python-study

## 格式化代码
```shell
Ctrl+Alt+L
```

## 常用命令
```shell
#安装/卸载包
https://pypi.org/search/?q=urllib
pip install numpy
pip uninstall numpy
pip install selenium

pip install urllib3
pip install httplib2

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

## 采集 谷歌驱动配置
```
## 下载最新的Chrome驱动:http://npm.taobao.org/mirrors/chromedriver/
## chromedriver与chrome版本关系对照表:https://blog.csdn.net/huilan_same/article/details/51896672
## 解压后放到目录下即可:C:\tool\Python36\chromedriver.exe
```

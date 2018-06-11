# python-study
python-study

## 格式化代码
```shell
Ctrl+Alt+L
```

## 网络爬虫学习课程大放送
```shell
Python3.6网络爬虫实战案例(基础+实战+框架+分布式)
网盘地址： https://pan.baidu.com/s/1dGOhvrF 密码：dqd8

大数据实战课程第一季Python基础和网络爬虫数据分析
网盘地址： https://pan.baidu.com/s/1htuV3JQ 密码: pnjc

Scrapy分布式爬虫之ES搜索引擎网站
网盘地址： https://pan.baidu.com/s/1oAsW3Se 密码: tmtx
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

## Python作用域问题
```shell
在局部找不到，便会去局部外的局部找（例如闭包），再找不到就会去全局找，再者去内建中找。

Python 中只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域，其它的代码块（如 if/elif/else/、try/except、for/while等）是不会引入新的作用域的，也就是说这些语句内定义的变量，外部也可以访问

修改变量作用域：
global 和 nonlocal关键字
global关键字用于在函数体内修改全局变量时用到
nonlocal关键字用在inner函数体内修改变量值则外部定义的变量被修改/n没有加nonlocal的，inner内值被修改，外部不起作用
```
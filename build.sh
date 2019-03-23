#!/usr/bin/env bash

#初始化系统依赖库环境
function env_init(){
    wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo
    sudo yum makecache

    sudo yum -y install git
    sudo yum -y install epel-release
    sudo yum -y install python-pip
    sudo yum -y install rpm-build
    sudo yum clean all

    sudo pip install -y setuptools==40.8.0
}

#删除缓存
function del_build_cache(){
    rm -rf ./build/
    rm -rf ./dist/
    rm -rf ./${pkg_name}.egg-info/
}

#初始化环境
env_init

#获取最新代码
git pull

#打包成RPM包
python ./setup.py bdist_rpm

#设置包名和RPM包名
pkg_name='python-study'

rpm_pkg='${pkg_name}-0.0.1-1.noarch.rpm'

#删除已存在的RPM包
rpm -e ${rpm_pkg}

#卸载已经存在的包
pip uninstall -y ${pkg_name}

#RPM方式安装包
rpm -ivh ./dist/${rpm_pkg}

#删除环境
del_build_cache

#测试安装
python -m ${pkg_name}.main

#!/usr/bin/env bash

pkg_name='python-study'

function del_build_cache(){
    rm -rf ./build/
    rm -rf ./dist/
    rm -rf ./${pkg_name}.egg-info/
}

#打包成WHEEL格式
#python ./setup.py bdist_wheel

#windows打包格式
#python setup.py bdist_wininst

#卸载已存在的包
pip uninstall -y ${pkg_name}

#安装新包:/Users/<username>/miniconda2/lib/python2.7/site-packages/smartbooks
pip install ./dist/${pkg_name}-0.0.1-py2-none-any.whl

#删除临时文件
del_build_cache

python -m ${pkg_name}.main
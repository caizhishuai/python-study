# encoding:utf-8

from setuptools import setup, find_packages

setup(
    name="python-study",
    version="0.0.1",
    keywords=("hello", "world"),
    description="hello world test",
    long_description="hello world test for python",
    license="MIT Licence",

    url="https://github.com/caizhishuai/python-study",
    author="caizhishuai",
    author_email="196959783@qq.com",

    platforms="any",
    packages=find_packages(),

    # 'flask>=1.0'
    install_requires=[
        'numpy==1.16.2'
    ],

    include_package_data=True,
    exclude_package_data={'': ['.gitignore']}
)

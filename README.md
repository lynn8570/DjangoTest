---
title: "Growth Django 实战笔记"
date: "2018-03-20"
categories: 
    - "server"
---



# Growth 实践笔记

根据 [growth实战](http://growth-in-action.phodal.com/#%E6%B5%8B%E8%AF%95) 的笔记

## 安装Django

安装Django之前，先用virtualenv工具来创建一个虚拟的python环境。

virtualenv的作用参考 [廖雪峰python](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432712108300322c61f256c74803b43bfd65c6f8d0d0000)

1. 创建virtualenv的步骤
   - 安装virtualenv，`pip3 install virtualenv`
   - 创建项目文件夹，在文件夹下创建`virtualenv --no-site-packages venv` 了一个名为venv的目录，隔离了一个独立的python运行环境，已经安装到系统python上的第三方包都不会复制过来。
   - 使用source命令激活环境 `source vent/bin/activate`，注意，激活后，在命令提示符有个venv的前缀。
   - 使用deactivate退出当前环境。
2. 安装Django，`pip install Django`



## 创建项目

1. 创建名为blog的项目`django-admin startproject blog`
2. 运行项目 `python manage.py runserver`
3. 配置数据库，运行数据迁移脚本 `python manage.py migrate`
4. 创建超级用户`python manage.py createsuperuser`

## 创建app

1. `django-admin startup blogpost`生成blogpost目录结构
2. 创建model，模版，测试

## 持续集成

Jenkins是一个开源软件项目，是基于Java开发的一种持续集成工具，用于监控持续重复的工作，旨在提供一个开放易用的软件平台，使软件的持续集成变成可能

[下载](https://jenkins.io/) 文件，运行`java -jar jenkins.war` 安装，然后[http://0.0.0.0:8080/](http://0.0.0.0:8080/)  点击安装推荐的，等待安装完成。



User?




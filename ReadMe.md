#<center>学生成绩管理系统使用说明书</center>
----
##1.运行环境
- OS X Yosemite, Windows
- Python 2.7.10, Django 1.8.2, MySQL 5.6.25

##2.安装及配置
#### a) 安装Python
OS X下：

    brew install python
Windows下：

登陆`python.org`下载并安装Python

然后配置好python和pip的环境变量
#### b) 安装MySQL
OS X下：

    brew install mysql
Windows下：

登陆`mysql.org`下载并安装MySQL

然后配置好mysql的环境变量
#### c) 安装mysql-python
    sudo pip install mysql-python
*Window下不需要sudo
#### d) 安装Django
    sudo pip install django
*Window下不需要sudo
#### e) 安装项目
将项目文件夹复制到目标路径下

将静态文件（如bootstrap的HTML, CSS, JS, IMAGE等）置于项目文件下的`/static`目录下

将模板文件(.html)置于应用目录 `/scores`下的`/template`目录下
#### f) 启动项目
命令行下`cd`到项目文件夹目录下（存在manage.py的那一层目录）;

输入`python manage.py runserver [ip]:[端口]`在目标ip和端口下启动服务器
#### g) 使用成绩管理系统
i)    在新版本的浏览器输入url： `[ip]:[端口]/scores`(例:`127.0.0.1:8080/scores`) 即可访问系统的登陆界面

ii)   输入用户名和密码，即可登录主界面，根据用户类型分为学生界面、教师界面和管理员界面

iii)  在主界面根据界面功能按钮可以使用查询、新增、修改、删除等功能

# AuthMe-ByFlask
## 项目介绍
本项目为同组织AuthMe的Flask版，基于Flask框架，使用Python语言编写，使用MySQL数据库，实现了基本的登录验证功能。
## 开源声明
本项目由个人开发，项目完全开源，不支持魔改，但欢迎提出建议。本项目可用于商业用途，但请保留原作者信息。不保留原作者信息作侵权处理。
## 安装说明
1.安装python3.X版本

2.安装软件包(运行根目录下的install.bat或者运行以下命令)
```
pip install flask
pip install pymsql
pip install datetime
pip install uuid
pip install requests
```

3.运行根目录下的start.bat或者运行以下命令
```
python app.py
```
## 配置说明
### Mysql配置
mysql配置文件存在于/config/mysql目录下

需要在该目录下建立一个名为mysql.ini的配置文件，并按以下格式填入内容
```
[mysql]
addr = Mysql地址
port = Mysql端口
user = Mysql用户名
passwd = Mysql密码
database = Mysql数据库名
charset = Mysql编码
```

4.配置Mysql用户
在Mysql最高权限账户下执行以下内容：
```/*常规*/
CREATE USER 'authme'@'%' IDENTIFIED BY 'authme';
/*服务器权限设置*/
GRANT SELECT,INSERT,UPDATE,DELETE,CREATE,DROP,RELOAD,PROCESS,REFERENCES,INDEX,ALTER,CREATE TEMPORARY TABLES,LOCK TABLES,EXECUTE,CREATE VIEW,SHOW VIEW,CREATE ROUTINE,ALTER ROUTINE,CREATE USER,EVENT,GRANT OPTION,TRIGGER ON *.* TO 'authme'@'%';
```

5.配置SMTP服务器
SMTP配置文件存在于/config/email目录下

需要在该目录下建立一个名为smtp.ini的配置文件，并按以下格式填入内容
```

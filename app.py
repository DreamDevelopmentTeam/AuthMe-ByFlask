from flask import Flask, request
import pymysql
import configparser
import datetime

app = Flask(__name__)

# 全局变量区
mysql_addr = ''
mysql_port = 3306
mysql_user = ''
mysql_passwd = ''
mysql_database = ''


# 服务层API
@app.route('/')
def hello_world():  # 校验与服务端是否连通
    return 'AuthMe-ByFlask running!'


@app.route('/sys/load')
def load_config():
    # 加载配置文件
    config = configparser.ConfigParser()
    # 读取config文件夹下mysql文件夹下的mysql.ini
    config.read('config/mysql/mysql.ini')
    # 读取mysql.ini中的配置
    global mysql_addr, mysql_port, mysql_user, mysql_passwd, mysql_database, mysql_charset
    mysql_addr = config['mysql']['addr']
    mysql_port = config['mysql']['port']
    mysql_user = config['mysql']['user']
    mysql_passwd = config['mysql']['passwd']
    mysql_database = config['mysql']['database']
    return '配置文件加载成功'


@app.route('/test/mysql')
def test_mysql():  # 测试mysql连接
    # try:
        sql = pymysql.connect(
            host=mysql_addr,
            port=int(mysql_port),
            user=mysql_user,
            passwd=mysql_passwd,
            db=mysql_database,
        )
        sql.close()
        return '数据库连接成功'
    # except:
    #     return '数据库连接失败'


# 用户层API
@app.route('/user/login')
def user_login():  # 用户登录
    user = request.args.get('user')
    passwd = request.args.get('password')
    ip = request.remote_addr
    time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if user is None or passwd is None or user == '' or passwd == '':
        return '用户名或密码不能为空'
    else:
        try:
            sql = pymysql.connect(
                host=mysql_addr,
                port=int(mysql_port),
                user=mysql_user,
                passwd=mysql_passwd,
                db=mysql_database
            )
        except:
            return '数据库连接失败'
        # 使用cursor()方法获取操作游标
        cursor = sql.cursor()
        # 查询数据库中user表下对应user的passwd字段
        sql_com = 'SELECT passwd FROM user WHERE user = "%s"' % user
        # 执行mysql语句
        cursor.execute(sql_com)
        # 获取查询结果
        pwd = cursor.fetchone()
        if pwd is None:
            return '用户不存在'
        elif pwd == passwd:
            # 修改user表下对应user的status为online，login_ip为变量ip的值，login_time为变量time的值
            sql_com = 'UPDATE user SET status = "online", login_ip = "%s", login_time = "%s" WHERE user = "%s"' % (
                ip, time, user)
            # 执行mysql语句
            cursor.execute(sql_com)
            # 提交到数据库执行
            sql.commit()
            # 关闭数据库连接
            sql.close()
            return '登录成功'
        else:
            sql.close()
            return '账号或密码错误'


# 程序运行代码
if __name__ == '__main__':
    app.run()

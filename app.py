from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # 校验与服务端是否连通
    return 'AuthMe-ByFlask running!'


if __name__ == '__main__':
    app.run()

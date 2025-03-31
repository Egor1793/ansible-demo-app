from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from Ansible + Alt Linuxi!!!!!!"

if __name__ == '__main__':
    app.run(host='192.168.1.1', port=5000)

from flask import Flask
from flask import request
from followers import filejson
import telepot
import datetime


app = Flask(__name__)


@app.route('/instagram/username=<username>')
def follow(username):
    
    now = datetime.datetime.now()
    waktu=now.strftime("%Y-%m-%d %H:%M:%S")
    sistem = request.headers.get('User-Agent')
    if sistem is None:
        sistem = 'kosong'
    
    ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    token = '5519356568:AAEFj6No6sTcE-ma_i60rBGmTVIjruC4e70'
    penerimaid = 1769420825
    jsonapi = filejson(username)
    bot = telepot.Bot(token)
    pesan = 'API insta-api-id '+username+' IP: '+ip+' '+'Sistem: '+sistem+' '+waktu
    bot.sendMessage(penerimaid, pesan)
    return jsonapi

if __name__ == '__main__':
    app.run()
   
from flask import Flask, render_template, request

from pythonosc.udp_client import SimpleUDPClient

app = Flask(__name__)

client = SimpleUDPClient("127.0.0.1", 1337)

@app.route('/hello/<voiceInd>', methods=['GET', 'POST'])

def hello_name(voiceInd):
    
        return render_template('kick.html', voice = voiceInd)

@app.route("/kick", methods=['POST', 'GET'])

def kick():
    if request.method == 'POST':
        client.send_message("/kick/trigger", 1)
        return render_template('kick.html', voice = 's')

    elif request.method == 'GET':
        return render_template('kick.html', voice = 's')
    

    return render_template('kick.html', voice = 's')


if __name__ == '__main__':

    app.run(host='0.0.0.0')
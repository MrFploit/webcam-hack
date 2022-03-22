import flask
from threading import Thread

app = flask.Flask(__name__)

@app.route('/')
def main():
    return 'The robot is online'

def run():
  app.run(host="0.0.0.0", port=9010)

def remain_up():
  server = Thread(target=run)
  server.start()

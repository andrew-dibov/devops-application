import os
import socket

from flask import Flask, render_template
from prometheus_flask_exporter import PrometheusMetrics

MESSAGE = os.environ.get('MESSAGE', 'Hello world!')
HOST = os.environ.get('HOST', '0.0.0.0')
PORT = int(os.environ.get('PORT', 5000))

app = Flask(__name__)
metrics = PrometheusMetrics(app, default_labels={"app_name": "application"})
metrics.info('app_info', 'Application info', version='1.0.0')

@app.route('/')
def index():
    return render_template('index.html',
                           hostname=socket.gethostname(),
                           message=MESSAGE)

if __name__ == '__main__':
    app.run(host=HOST, port=PORT)

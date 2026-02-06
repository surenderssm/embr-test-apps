import os
import threading
import time
from datetime import datetime

from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)

app = Flask(__name__)


def background_logger():
    """Background function that logs datetime every 3 seconds."""
    while True:
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f'[Background Log] {current_time}')
        time.sleep(3)


@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/hello', methods=['POST'])
def hello():
   name = request.form.get('name')

   if name:
       print('Request for hello page received with name=%s' % name)
       return render_template('hello.html', name = name)
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return redirect(url_for('index'))


if __name__ == '__main__':
   # Start background logging thread
   logging_thread = threading.Thread(target=background_logger, daemon=True)
   logging_thread.start()
   app.run(port=8080)

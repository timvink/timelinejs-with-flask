
from flask import Flask
from flask import render_template
from flask import g
from flask import Response
from flask import request
from flask import redirect
from flask import url_for, send_from_directory

app = Flask(__name__)

@app.route("/")
def render_timeline():
    return render_template('index.html')

if __name__ == "__main__":	
	app.run(port = 5000, host = '0.0.0.0', use_reloader=True, threaded=True, debug=True)
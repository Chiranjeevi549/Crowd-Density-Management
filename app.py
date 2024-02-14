from flask import Flask, render_template
import subprocess

app = Flask(__name__)
process = None
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detect')
def detect():
    global process
    if process is None:
        process = subprocess.Popen(['python', 'detect.py'])
        return 'Detect script started.'
    else:
        return 'Detect script not started.'

@app.route('/detect/stop')
def stopdetect():
    global process
    if process is not None:
        process.terminate()
        process = None
        return 'Stopped'
    else:
        return 'not stopped'
if __name__ == '__main__':
    app.run(debug=True)

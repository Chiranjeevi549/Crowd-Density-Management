import os
import cv2
from flask import Flask, render_template, request,jsonify,send_file
from PIL import Image
import subprocess
import matplotlib.pyplot as plt
import io
app=Flask(__name__)
UPLOAD_FOLDER = os.path.basename('.')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

process = None
@app.route("/", methods=['GET', 'POST'])
def application():
    file=""
    global process
    if request.method=="POST":
        try:
            file= request.files["video"]
            if file:
                print(file.filename)
                if process is None:
                    f = os.path.join(app.config['UPLOAD_FOLDER'], "video")
                    file.save(f)
                    print(file.filename)
                    process=subprocess.Popen(['python', 'detect1.py'])
                
        except(SyntaxError) as e:
            error ="Could not understand"
            print("Error:" + str(e))
        except Exception as e:
            print(e)
    return render_template('index.html', file=file)
@app.route("/dt1/stop",methods=["GET","POST"])
def dt1stop():
    global process
    if process is not None:
        process.terminate()
        process=None
        return render_template('index.html', file="")
    else:
        print(process)
        return render_template('index.html', file="")
@app.route("/app.py/myfunc",methods=["GET","POST"])
def my_function1():
    global process
    if process is None:
        process=subprocess.Popen(['python','detect.py'])
    return render_template('index.html', file="")
@app.route("/dt/stop", methods=['GET','POST'])
def dt_stop():
    global process
    if process is not None:
        process.terminate()
        process=None
        return render_template('index.html', file="")
@app.route("/line_graph.png",methods=['GET','POST'])
def analysis():
    img_path = 'templates/line_graph.png'
    img = open(img_path, 'rb').read()
    img_io = io.BytesIO(img)
    return send_file(img_io, mimetype='image/png', as_attachment=True, download_name='line_graph.png')
@app.route("/dt/line_graph.png",methods=['GET','POST'])
def analysis1():
    img_path = 'templates/line_graph.png'
    img = open(img_path, 'rb').read()
    img_io = io.BytesIO(img)
    return send_file(img_io, mimetype='image/png', as_attachment=True, download_name='line_graph.png')
@app.route("/dt1/line_graph.png",methods=['GET','POST'])
def analysis2():
    img_path = 'templates/line_graph.png'
    img = open(img_path, 'rb').read()
    img_io = io.BytesIO(img)
    return send_file(img_io, mimetype='image/png', as_attachment=True, download_name='line_graph.png')
if __name__ == "__main__":
    app.run(debug=True)

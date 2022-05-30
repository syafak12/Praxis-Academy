import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/')
def upload_init():
    return render_template('uplod.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_init1():
    file = request.files['file']
    filename = secure_filename(file.filename)
    file.save(os.path.join('uploads', filename))
    return "successfully uploaded file"

if __name__ == '__main__':
    app.run(debug=True)



from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/success/<name>/<alamat>')
def success(name,alamat):
   return f"welcome {name} alamatmu {alamat}"

@app.route('/login.html',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      alamat = request.form['alamat']
      return redirect(url_for('success',name = user,alamat= alamat))
   else:
      user = request.args.get('nm')
      alamat = request.args.get('alamat')
      return redirect(url_for('success',name = user,alamat= alamat))

if __name__ == '__main__':
   app.run(debug = True)
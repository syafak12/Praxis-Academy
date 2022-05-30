
from flask import Flask, flash, redirect, render_template, request, url_for, session
app = Flask(__name__)
app.config["SECRET_KEY"] = "inisecretKeyku2022"

@app.route('/')
def indekku():
   #belajar looping
   hari = ["senin", "selasa", "rabu", "kamis", "jum'at", "sabtu", "minggu"]
   # conditioning / if-else
   suasana = "sedih" # jika senang maka dia juga cinta jika tidak, maka dia sedih
   # set variabel
   return render_template("index.html", value=hari, suasana=suasana)

@app.route("/about")
def aboutku():
   return render_template("about.html")


@app.route('/contact')
def contactku():
   return render_template("contact.html")

# parsing nilai ini, string
@app.route("/parsing/<string:nilaiku>")
def ayo_parsing(nilaiku):
   return "nilainya adlah : {}". format(nilaiku)

#argument parser
@app.route("/parsingargument")
def ayo_argument():
   data = request.args.get("nilai")
   return "nilainya dari argument parser adalah {}".format(data)

# memparsing nilai dari url untuk mengeset nilai session
@app.route("/halaman/<int:lnilai>")
def session_1(nilai):
   session["nilaiku"] = nilai
   return "Berhasil mengeset nilainya"

@app.route("/halaman/lihat")
def view_session_1():
   data = session["nilaiku"]
   return "NIlai yang telah diset adalah = {}".format(data)

if __name__ == "__main__":
   app.run(debug=True)



# @app.route('/')
# def index():
#    if 'username' in session:
#       username = session['username']
#          return 'Logged in as ' + username + '<br>' + \
#          "<b><a href = '/logout'>click here to log out</a></b>"
#    return "You are not logged in <br><a href = '/login'></b>" + \
#       "click here to log in</b></a>"


# # login
# @app.route('/login', methods = ['GET', 'POST'])
# def login():
#    if request.method == 'POST':
#       session['username'] = request.form['username']
#       return redirect(url_for('index'))
#    return '''
	
#    <form action = "" method = "post">
#       <p><input type = text name = username/></p>
#       <p<<input type = submit value = Login/></p>
#    </form>
	
#    '''

# #logout
# @app.route('/logout')
# def logout():
#    # remove the username from the session if it is there
#    session.pop('username', None)
#    return redirect(url_for('index'))


# #secret_key
# from flask import Flask, session, redirect, url_for, escape, request
# app = Flask(__name__)
# app.secret_key = 'any random string’
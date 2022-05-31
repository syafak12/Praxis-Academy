from flask import Flask, render_template
  
app = Flask(__name__)
  
# app name
@app.errorhandler(404)
  
# fungsi bawaan yang mengambil kesalahan sebagai parameter
def not_found(e):
  
# defining function
  return render_template("404.html")
from flask import Flask, render_template, request, redirect, url_for, flash
import psycopg2 #pip install psycopg2 
import psycopg2.extras
 
app = Flask(__name__)
app.secret_key = "cairocoders-ednalan"
 
DB_HOST = "localhost"
DB_NAME = "postgres"
DB_USER = "lorna"
DB_PASS = "password"
 
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
 
@app.route('/')
def Index():
    # return render_template('index.html')
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    s = "SELECT * FROM lorna"
    cur.execute(s) # Execute the SQL
    list_users = cur.fetchall()
    return render_template('index.html', list_users = list_users)
 
@app.route('/baca', methods=['POST'])
def add_lorna():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == 'POST':
        nama = request.form['nama']
        nama_lengkap = request.form['nama_lengkap']
        tanggal_lahir = request.form['tanggal_lahir']
        email = request.form['email']
        cur.execute("INSERT INTO lorna (nama, nama_lengkap, tanggal_lahir, email) VALUES (%s,%s,%s,%s)", (nama, nama_lengkap, tanggal_lahir, email))
        conn.commit()
        flash('Student Added successfully')
        return redirect(url_for('Index'))
 
@app.route('/edit/<id>', methods = ['POST', 'GET'])
def get_employee(id):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
   
    cur.execute('SELECT * FROM lorna WHERE id = %s', (id))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('edit.html', lorna = data[0])
 
@app.route('/update/<id>', methods=['POST'])
def update_lorna(id):
    if request.method == 'POST':
        nama = request.form['nama']
        nama_lengkap = request.form['nama_lengkap']
        tanggal_lahir = request.form['tanggal_lahir']
        email = request.form['email']
         
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("""
            UPDATE lorna
            SET nama = %s,
                nama_lengkap = %s,
                tanggal_lahir = %s,
                email = %s
            WHERE id = %s
        """, (nama, nama_lengkap, tanggal_lahir, email, id))
        flash('Student Updated Successfully')
        conn.commit()
        return redirect(url_for('Index'))
 
@app.route('/delete/<string:id>', methods = ['POST','GET'])
def delete_lorna(id):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
   
    cur.execute('DELETE FROM lorna WHERE id = {0}'.format(id))
    conn.commit()
    flash('Student Removed Successfully')
    return redirect(url_for('Index'))
 
if __name__ == "__main__":
    app.run(debug=True)
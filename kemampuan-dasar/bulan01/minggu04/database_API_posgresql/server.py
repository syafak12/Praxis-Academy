from urllib import response
from flask import Flask, render_template, Response, request, redirect, url_for, flash
import psycopg2 #pip install psycopg2 
import psycopg2.extras
import json
 
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
    s = "SELECT * FROM hasil_penjualan"
    cur.execute(s) # Execute the SQL
    list_users = cur.fetchall()
    return render_template('index.html', list_users = list_users)
 
@app.route('/baca', methods=['POST'])
def add_hasil_penjualan():
    # cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    connection = psycopg2.connect(host="localhost", Database="postgres", user="lorna", password="password")
    # if request.method == 'POST':
    cursor = connection.cursor()
    try:
        payload = json.loads(request.data)
        # nama_barang = payload['nama_barang']
        # harga = payload['harga']
        # merek = payload['merek']
        # keterangan = payload['keterangan']

        # nama_barang = request.form['nama_barang']
        # harga = request.form['harga']
        # merek = request.form['merek']
        # keterangan = request.form['keterangan']
        Response = conn.cursor.hasil_penjualan.insert_one(payload)
        print(Response.inserted_id)
        return Response(
            response=json.dumps(
                {"message": "user sudah terbaca",
                "id":f"{Response.inserted_id}"}),
            status=200,
            mimetype="aplication/json")
            
    except Exception as ex:
        return response.badRequest(f"{ex}", "erorr")

        # cur.execute("INSERT INTO hasil_penjualan (nama_barang, harga, merek, keterangan) VALUES (%s,%s,%s,%s)", (nama_barang, harga, merek, keterangan))
        conn.commit()
        flash('Sukse Memasukkan Data Barang yang terjual')
        return redirect(url_for('Index'))
 
@app.route('/edit/<id>', methods = ['POST', 'GET'])
def get_employee(id):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
   
    cur.execute('SELECT * FROM hasil_penjualan WHERE id = %s', (id))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('edit.html', lorna = data[0])
 
@app.route('/update/<id>', methods=['POST'])
def update_hasil_penjualan(id):
    if request.method == 'POST':
        nama_barang = request.form['nama_barang']
        harga = request.form['harga']
        merek = request.form['merek']
        keterangan = request.form['keterangan']
         
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("""
            UPDATE hasil_penjualan
            SET nama = %s,
                nama_lengkap = %s,
                tanggal_lahir = %s,
                email = %s
            WHERE id = %s
        """, (nama_barang, harga, merek, keterangan, id))
        flash('Barang Sudah Di Update')
        conn.commit()
        return redirect(url_for('Index'))
 
@app.route('/delete/<string:id>', methods = ['POST','GET'])
def delete_hasil_penjualan(id):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
   
    cur.execute('DELETE FROM hasil_penjualan WHERE id = {0}'.format(id))
    conn.commit()
    flash('Barang Sudah Terhapus')
    return redirect(url_for('Index'))
 
if __name__ == "__main__":
    app.run(debug=True)
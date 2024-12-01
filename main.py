from flask import Flask, render_template, request, redirect, url_for, jsonify
import mysql.connector

app = Flask(__name__)

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'bhavani6305580326',
    'database': 'bec',
}

@app.route('/')
def hello_world():
    return render_template('form.html')

@app.route('/Sign Up')
def signup():
    return render_template("signup.html")


@app.route('/Sign In')
def signin():
    return render_template('signin.html')


@app.route('/category')
def category():
    return render_template('category1.html')

@app.route('/sign', methods=['GET', 'POST'])
def sign():
    if request.method == 'POST':
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        try:
            sql = mysql.connector.connect(**db_config)
            cur = sql.cursor()
            insert_query='insert into bec1 (name,email,password) values(%s,%s,%s)'
            data=(name,email,password)
            cur.execute(insert_query,data)
            sql.commit()


            return redirect(url_for('signin'))

        except Exception as e:
            print("Error:", e)

        finally:
            cur.close()
            sql.close()

    return 'invalid request'


@app.route('/bec',methods=['POST'])
def bec():
    if request.method == 'POST':
        email=request.form['email']
        password=request.form['password']
        try:
           sql=mysql.connector.connect(**db_config)
           cur=sql.cursor()
           check='select * from bec.bec1 where email=%s and password=%s'
           data=(email,password)
           cur.execute(check,data)

           user=cur.fetchone()
           if user:
               return jsonify(message="Login successful")
           else:
               return jsonify(message='invalid credential')
        except Exception as e:
            print("Error:", e)



        finally:

            cur.close()

            sql.close()


if __name__ == '__main__':

    app.run(debug=True)

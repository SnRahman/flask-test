from flask import Flask,render_template, request, redirect, url_for
import mysql.connector


# Create a MySQL database connection
connection = mysql.connector.connect(host='localhost',user='root' , password = '', database = 'flask-test' )

app = Flask(__name__)


@app.route('/get-users')
def get_users():
    # Create a cursor object to execute SQL queries
    db = connection.cursor()

    # query = 'SELECT * FROM users'
    # db.execute(query)

    # Execute the SQL query
    db.execute('SELECT * FROM users')

    # Fetch all the results from table
    users = db.fetchall()
    
     # Close the cursor
    db.close()
    return render_template('users.html', active_users = users)

@app.route('/add-user')
def add_user():
    return render_template('form.html')


@app.route('/register',methods=['POST'])

def register():
    fname = request.form['fname']
    lname = request.form['lname']
    email = request.form['email']

    if fname and lname and email:

        # query = 'INSERT INTO users (fname,lname,email) VALUES (%s,%s,%s)'
        # values = (fname,lname,email)
        # db.execute(query,values)

        db = connection.cursor()

        db.execute('INSERT INTO users (fname,lname,email) VALUES (%s,%s,%s)',(fname,lname,email) )
        
        connection.commit()
        db.close()

        return redirect(url_for('get_users'))
    else:
        return redirect(url_for('add_user'))    


@app.route('/update-user/<id>' , methods=['GET', 'POST'])
def update_user(id):
    if request.method == 'GET':
        db = connection.cursor() 
        db.execute(f'SELECT * FROM users WHERE id = {id}')
        user = db.fetchone()
        db.close()
        # return user[0]
        return render_template('update-form.html',user = user)
    else:
        fname = request.form['fname']
        lname = request.form['lname']
        email = request.form['email']

        if fname and lname and email:
            
            db = connection.cursor()
            # query = 'UPDATE users SET fname = %s, lname = %s , email = %s WHERE id = %d '
            # values = (fname,lname,email,id)
            # db.execute(query,values)
            db.execute('UPDATE users SET fname = %s, lname = %s , email = %s WHERE id = %s ',(fname,lname,email,id))

            connection.commit()
            db.close()

            return redirect(url_for('get_users'))
        else:
            return redirect(url_for('update-user',id=id))

if __name__ == '__main__':
    app.debug = True
    app.run()




from flask import Flask, render_template , request

app = Flask(__name__)


@app.route('/signup')
def signup():
    return render_template('form.html')


# submit form
@app.route('/register', methods = ['POST'])
def register():
    fname = request.form['fname']
    lname = request.form['lname']
    uname = request.form['uname']
    email = request.form['email']

    return f'First Name is : {fname} <br> Last Name is : {lname} <br> User Name is : {uname} <br> Email is : {email} '


@app.route('/login', methods= ['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        email = request.form['email']
        # password = request.form['password']
        return render_template('success.html' , email = email)
      
        # return f'Email is : {email} <br> Password: {password} '



if __name__ == '__main__':
    app.debug = True
    app.run()
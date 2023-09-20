from flask import Flask, render_template, request, redirect, flash, url_for

app = Flask(__name__)
app.secret_key = 'flask-test'

@app.route('/form')
def form():
    return render_template('form1.html')


@app.route('/submited' , methods = ['GET','POST'])
def submit():

    # check the request method
    if request.method == 'POST':
        # get input values in post type
        fname = request.form['fname']

        # validation
        if fname == '':
           flash('Please enter you First name', 'error')
           return redirect(url_for('form'))

        lname = request.form['lname']
        uname = request.form['uname']
        email = request.form['email']
        if email == '':
            flash('Plase enter your valid email','error')
            return redirect( url_for('form') )
        
        return render_template('form-data.html',fname = fname, lname = lname, uname = uname ,email = email) 
        return f'First Name is : {fname} <br> Last Name is : {lname} <br> User Name is : {uname} <br> Email is : {email} '

    elif request.method =='GET':

        # get input/ arguments value in get type
        fname = request.args['fname']
        # fname = request.args.get('fname')
        lname = request.args['lname']
        uname = request.args['uname']
        email = request.args['email']
        return f'First Name is : {fname} <br> Last Name is : {lname} <br> User Name is : {uname} <br> Email is : {email} '


@app.route('/products')
def products():
    # make a product dictionary
    products = [
        {
            'name' : 'product 1',
            'price' : 100,
            'Description' : 'THis is product one',
         },
         {
            'name' : 'product 2',
            'price' : 200,
            'Description' : 'THis is product Two',
         },
         {
            'name' : 'product 3',
            'price' : 300,
            'Description' : 'THis is product Three',
         },
         {
            'name' : 'product 4',
            'price' : 400,
            'Description' : 'THis is product Four',
         },
         {
            'name' : 'product 5',
            'price' : 500,
            'Description' : 'THis is product Five',
         }
    ]
    
    # send the product dict to html file for display
    return render_template('products.html', products = products)


if __name__ =='__main__':
    app.run(debug = True)
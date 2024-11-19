from flask import Flask, request, render_template, redirect, session, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Login credentials
ADMIN_USERNAME = "Guru"
ADMIN_PASSWORD = "guru12"

@app.route('/')
def index():
    if 'username' in session:
        return redirect('/admin')  # Redirect to admin panel if already logged in
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        session['username'] = username
        return redirect('/admin')
    else:
        return '', 500  # Return 500 for login failure

@app.route('/admin')
def admin_panel():
    if 'username' not in session:
        return redirect('/')
    return "Welcome to the Admin Panel!"  # Placeholder for admin panel

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('You have been logged out successfully.', 'success')
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

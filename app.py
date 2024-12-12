from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'reemplazar_por_variable_de_entorno'

USERS = {
    'admin': 'password123',
    'user': 'pass456'
}

@app.route('/')
def home():
    if 'username' in session:
        return render_template('login.html', message=f"\u00a1Bienvenido, {session['username']}!", logged_in=True)
    return render_template('login.html', logged_in=False)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()

        if not username or not password:
            flash('Por favor, complete todos los campos.', 'warning')
            return redirect(url_for('login'))

        if username in USERS and USERS[username] == password:
            session['username'] = username
            flash('Inicio de sesión exitoso.', 'success')
            return redirect(url_for('home'))
        else:
            flash('Usuario o contraseña incorrectos.', 'danger')

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()

        if not username or not password:
            flash('Por favor, complete todos los campos.', 'warning')
        elif username in USERS:
            flash('El usuario ya existe.', 'danger')
        else:
            USERS[username] = password
            flash('Usuario registrado exitosamente.', 'success')
            return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('Has cerrado sesión.', 'info')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)

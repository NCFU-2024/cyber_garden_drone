from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Mock data for the drone
drone_state = {
    'connected': False,
    'model': 'DJI Phantom 4',
    'battery': 100,
    'current_task': 'Waiting'
}

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def do_login():
    username = request.form['username']
    password = request.form['password']
    # Simple authentication check (replace with real authentication)
    if username == 'admin' and password == 'password':
        return redirect(url_for('main_menu'))
    return 'Invalid credentials', 401

@app.route('/main_menu')
def main_menu():
    return render_template('main_menu.html', drone_state=drone_state)

@app.route('/combat_operations')
def combat_operations():
    return render_template('combat_operations.html')

@app.route('/patrolling')
def patrolling():
    return render_template('patrolling.html')

@app.route('/shutdown')
def shutdown():
    return render_template('shutdown.html')

@app.route('/log_menu')
def log_menu():
    return render_template('log_menu.html')

@app.route('/monitoring')
def monitoring():
    return render_template('monitoring.html', drone_state=drone_state)

@app.route('/perform_shutdown', methods=['POST'])
def perform_shutdown():
    # Logic to shut down the drone
    drone_state['connected'] = False
    drone_state['current_task'] = 'Shut Down'
    return redirect(url_for('main_menu'))

if __name__ == '__main__':
    app.run(debug=True)

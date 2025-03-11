from flask import Flask
import os
import subprocess
import datetime

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Fetch system username
    system_user = os.getenv("USER") or os.getenv("USERNAME")

    # Fetch htop output
    htop_output = subprocess.getoutput("top -bn1")

    # Server time in IST
    ist_time = datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30)

    # Generate response
    response = f"""
    <h2>Internship Test</h2>
    <p><b>Name:</b> Your Full Name</p>
    <p><b>Username:</b> {system_user}</p>
    <p><b>Server Time (IST):</b> {ist_time.strftime('%Y-%m-%d %H:%M:%S')}</p>
    <pre>{htop_output}</pre>
    """
    
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
import shlex
from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/execute_safe', methods=['POST'])
def execute_command_safe():
    command = request.form.get('cmd')

    # Verwende shlex.split, um die Eingabe sicher zu analysieren
    cmd_args = shlex.split(command)

    try:
        # Verwende os.system mit den sicher analysierten Argumenten
        os.system(" ".join(cmd_args))
        return "Command executed successfully\n"
    except Exception as e:
        return f"Error executing command: {str(e)}"

if __name__ == '__main__':
    # Ändere host auf '127.0.0.1' anstatt '0.0.0.0'
    app.run(debug=False, host='127.0.0.1', port=5000)

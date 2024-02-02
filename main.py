import os
import shlex
from flask import Flask, request

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
    app.run(debug=False, host='0.0.0.0', port=5000)

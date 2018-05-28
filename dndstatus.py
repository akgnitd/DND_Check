
from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/dnd', methods=['POST'])
def check_for_dnd():
    '''
    Returns the dnd status
    '''
    phone_nos = request.form['NUMBER']
    host = "ncprstatus.in"
    endpoint = "/api/v1/status"
    payload = {
        'numbers': set(
            phone_nos.split(',')
        )}
    url = 'http://' + host + endpoint
    result = requests.get(url, payload)
    return render_template('results.html', result=json.loads(result.content))

@app.route('/')
def entry_page():
    return render_template('entry.html',
                           the_title='Welcome to DND Status on the web!')

if __name__ == '__main__':
    app.run(
        host= '0.0.0.0',
        port= '7000',
        debug=True)

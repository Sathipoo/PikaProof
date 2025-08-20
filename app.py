from flask import Flask, render_template, request, redirect, url_for, flash
import json
import datetime as dt

app = Flask(__name__)
app.secret_key = 'change-me'

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    input_type = request.form.get('input_type', 'form')
    data = {}

    if input_type == 'json':
        raw_json = request.form.get('json_data', '').strip()
        try:
            data = json.loads(raw_json)
        except json.JSONDecodeError:
            flash('Invalid JSON input')
            return redirect(url_for('index'))
    else:
        data = {
            'name': request.form.get('name', ''),
            'title': request.form.get('title', ''),
            'start_date': request.form.get('start_date', ''),
            'end_date': request.form.get('end_date', ''),
            'responsibilities': [r.strip() for r in request.form.get('responsibilities', '').split('\n') if r.strip()],
            'issuer_name': request.form.get('issuer_name', ''),
            'issuer_title': request.form.get('issuer_title', '')
        }

    return render_template('certificate.html', data=data, dt=dt)

if __name__ == '__main__':
    app.run(debug=True)

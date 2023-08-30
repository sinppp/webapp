import flask

from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

def validate_data(data):
    # Simplified validation: Check if "Name" column exists
    if "Name" in data.columns:
        return "Data is valid"
    else:
        return "Data is invalid"

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and file.filename.endswith('.xlsx'):
            try:
                data = pd.read_excel(file)
                validation_result = validate_data(data)
                return render_template('result.html', validation_result=validation_result)
            except Exception as e:
                return render_template('error.html', error=str(e))
        else:
            return render_template('error.html', error='Invalid file format')

    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)


app.config['APPINSIGHTS_INSTRUMENTATIONKEY'] = 'a5936978-a242-45b4-ab7e-7fd4d311d24d'

appinsights = AppInsights(app)


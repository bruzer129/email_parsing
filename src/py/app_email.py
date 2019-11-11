"""
Flask App that provides an API to parse raw text email
headers to filter out several fields and their values
"""

from flask import Flask, jsonify, request
import re

app = Flask(__name__)

@app.route('/')
def home():
    return ('You are on the Home Page. Use /api/email to access the Email Parser')

# This is the API url to start the process
@app.route('/api/email')
def email():
    with open('email.html') as fptr:
        html = fptr.read()
    print(html)
    return html

# This is the URL the API will send a POST to with the email headers
@app.route('/parseEmail', methods=['GET', 'POST'])
def parseEmail():
    if request.method == 'POST':
        resDict = {}
        keys = ['To', 'From', 'Subject', 'Date', 'Message-ID']
        regex = [
            F'\s*({keys[0]}: .*)\s',
            F'\s*({keys[1]}: .*)[\r\n]',
            F'\s*({keys[2]}: .*)[\r\n]',
            F'\s*({keys[3]}: .*)[\r\n]',
            F'\s*({keys[4]}: .*)\s',
        ]

        for key in keys:
            resDict[key] = None

        # Get the file object from the request and validate it
        fileObj = request.files.get('emailFile', None)
        if not fileObj:
            # No file to process
            resDict = {'result':'Error receiving file to process'}
            return jsonify(resDict)

        # Not doing anything with the saved file at this time.
        fileObj.save(F'/tmp/{fileObj.filename}')

        # Read the file data from the object stream
        fileObj.seek(0)
        fileData = fileObj.read()
        if hasattr(fileData, 'decode'):
            fileData = fileData.decode()

        # Grep the file data for particular key values
        print(F'fileData type: {type(fileData)}', flush=True)
        for idx, key in enumerate(keys):
            print(F'regex: {regex[idx]}', flush=True)
            match = re.search(F'{regex[idx]}', fileData)
            if match:
                resDict[key] = match.group(1)

        response = jsonify(resDict)
        return response
    else:
        return 'API error, expected POST request'


if __name__ == '__main__':
    # debug=True restart the app on any code change
    app.run()

from flask import Flask, request
import boto3

app = Flask(__name__)
dynamodb = boto3.resource('dynamodb', region_name='ap-south-1')
table = dynamodb.Table('Feedback')

@app.route('/feedback', methods=['POST'])
def save_feedback():
    name = request.form['name']
    message = request.form['message']
    table.put_item(Item={'name': name, 'message': message})
    return "Thank you for your feedback!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

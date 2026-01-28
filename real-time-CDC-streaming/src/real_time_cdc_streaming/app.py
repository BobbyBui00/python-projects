import random

from faker import Faker
from flask import Flask, jsonify
from flask_httpauth import HTTPTokenAuth
from datetime import datetime

app = Flask(__name__)
fake = Faker()
auth = HTTPTokenAuth(scheme='Bearer')

TOKEN = {
    'access_token': 'authorized_user',
    'token_type': 'Bearer'
}

@auth.verify_token
def verify_token(token):
    if token in TOKEN:
        return TOKEN[token]
    return None

@auth.error_handler
def unauthorized():
    response = jsonify({ 'message': 'Unauthorized Access', 'error': 'Invalid or missing Token'})
    response.status_code = 401
    return response

@app.route('/protected', methods=['GET'])
@auth.login_required
def protected():
    return jsonify({ 'message': 'Access Granted', 'user': auth.current_user() }), 200


@app.route('/')
def public():
    return jsonify({ 'message': 'This is a public endpoint' }), 200

@app.route('/retrieve-transactions', methods=['GET'])
@auth.login_required
def generate_transaction():
    user = fake.simple_profile()
    print(user)

    return {
        'transactionId': fake.uuid4(),
        'userId': user['username'],
        'timestamp': datetime.timestamp(datetime.now()),
        'amount': round(random.uniform(10, 100000), 2),
        'currency': random.choice(['USD', 'CAD']),
        'city': fake.city(),
        'country': fake.country(),
        'merchantName': fake.company(),
        'paymentMethod': random.choice(['credit_card', 'debit_card', 'e_transfer']),
        'ipaddress': fake.ipv4(),
        'affiliatedId': fake.uuid4(),
    }


if __name__ == '__main__':
    app.run(debug=True)
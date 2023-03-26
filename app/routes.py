from flask import Flask, request, jsonify, render_template
from .models import ResponseGenerator

app = Flask(__name__)
response_generator = ResponseGenerator()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json()
    message = data['message']
    response = response_generator.generate_response(message)
    return jsonify({'message': response})

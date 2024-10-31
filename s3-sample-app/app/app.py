from flask import Flask, request, jsonify, render_template
import boto3
import os, uuid

app = Flask(__name__)

aws_region = os.getenv('AWS_REGION', 'us-west-2')  # Default to 'us-west-2' if not set
table_name = os.getenv('DYNAMODB_TABLE')

# DynamoDB setup
dynamodb = boto3.resource('dynamodb', region_name=aws_region)  # Change to your region
table = dynamodb.Table(table_name)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/items', methods=['POST'])
def add_item():
    data = request.json
    item_name = data.get('name')
    if not item_name:
        return jsonify({'error': 'Item name is required'}), 400
    id = str(uuid.uuid4())

    response = table.put_item(
        Item={
            'id': id,
            'name': item_name
        }
    )
    return jsonify({'message': 'Item added'}), 201


@app.route('/items', methods=['GET'])
def get_items():
    response = table.scan()
    items = response.get('Items', [])
    return jsonify(items), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data - a list to store items
items = []

# Route to get a list of items
@app.route('/api/items', methods=['GET'])
def get_items():
    return jsonify(items)

# Route to add a new item
@app.route('/api/items', methods=['POST'])
def add_item():
    data = request.get_json()
    if 'name' in data:
        new_item = {'name': data['name']}
        items.append(new_item)
        return jsonify({'message': 'Item added successfully!'}), 201
    else:
        return jsonify({'error': 'Invalid data'}), 400

if __name__ == '__main__':
    app.run(debug=True)


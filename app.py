from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage
items = []

# CREATE
@app.route("/items", methods=["POST"])
def create_item():
    data = request.json
    items.append(data)
    return jsonify({"message": "Item created", "item": data}), 201

# READ ALL
@app.route("/items", methods=["GET"])
def get_items():
    return jsonify(items)

# READ ONE
@app.route("/items/<int:index>", methods=["GET"])
def get_item(index):
    if index < len(items):
        return jsonify(items[index])
    return jsonify({"error": "Item not found"}), 404

# UPDATE
@app.route("/items/<int:index>", methods=["PUT"])
def update_item(index):
    if index < len(items):
        items[index] = request.json
        return jsonify({"message": "Item updated", "item": items[index]})
    return jsonify({"error": "Item not found"}), 404

# DELETE
@app.route("/items/<int:index>", methods=["DELETE"])
def delete_item(index):
    if index < len(items):
        deleted = items.pop(index)
        return jsonify({"message": "Item deleted", "item": deleted})
    return jsonify({"error": "Item not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

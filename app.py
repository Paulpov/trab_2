from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = TreeNode(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert(node.right, key)

    def to_dict(self, node):
        if not node:
            return None
        return {
            'key': node.key,
            'left': self.to_dict(node.left),
            'right': self.to_dict(node.right)
        }

tree = BinaryTree()

@app.route('/insert', methods=['POST'])
def insert():
    key = request.json['key']
    tree.insert(key)
    return jsonify(success=True)

@app.route('/get_tree', methods=['GET'])
def get_tree():
    return jsonify(tree.to_dict(tree.root))

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

class SplayTree:
    def __init__(self):
        self.root = None

    # Aqui ficariam as funções rotate_right, rotate_left, splay e insert com as suas devidas lógicas

    def to_dict(self, node):
        if not node:
            return None
        children = [self.to_dict(node.left), self.to_dict(node.right)] if node.left or node.right else []
        return {'name': str(node.key), 'children': children}

tree = SplayTree()

@app.route('/insert', methods=['POST'])
def insert():
    data = request.get_json()
    key = data.get('key')
    if key is None or not isinstance(key, int):
        return jsonify({'error': 'Key is required and must be an integer.'}), 400
    tree.insert(key)
    return jsonify(tree.to_dict(tree.root))

@app.route('/search', methods=['POST'])
def search():
    data = request.get_json()
    key = data.get('key')
    if key is None or not isinstance(key, int):
        return jsonify({'error': 'Key is required and must be an integer.'}), 400

    # Implementação do splay que atualiza uma lista de caminhos
    path = []
    tree.root = tree.splay(tree.root, key, path=path)
    # Ajuste necessário na função splay para aceitar e atualizar o caminho
    return jsonify({'path': path, 'tree': tree.to_dict(tree.root)})

@app.route('/get_tree', methods=['GET'])
def get_tree():
    return jsonify(tree.to_dict(tree.root))

if __name__ == "__main__":
    app.run(debug=True)

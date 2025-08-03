from flask import Flask, request, jsonify

app = Flask(__name__)

notes = []  # Ye list humari memory wali database hai

# 1. Get All Notes
@app.route('/notes', methods=['GET'])
def get_notes():
    return jsonify(notes)

# 2. Get Note By ID
@app.route('/notes/<int:id>', methods=['GET'])
def get_note(id):
    for note in notes:
        if note['id'] == id:
            return jsonify(note)
    return jsonify({'message': 'Note not found'}), 404

# 3. Create New Note
@app.route('/notes', methods=['POST'])
def add_note():
    data = request.get_json()
    note = {
        'id': len(notes) + 1,
        'title': data['title'],
        'content': data['content']
    }
    notes.append(note)
    return jsonify(note), 201

# 4. Update Note
@app.route('/notes/<int:id>', methods=['PUT'])
def update_note(id):
    data = request.get_json()
    for note in notes:
        if note['id'] == id:
            note['title'] = data.get('title', note['title'])
            note['content'] = data.get('content', note['content'])
            return jsonify(note)
    return jsonify({'message': 'Note not found'}), 404

# 5. Delete Note
@app.route('/notes/<int:id>', methods=['DELETE'])
def delete_note(id):
    for note in notes:
        if note['id'] == id:
            notes.remove(note)
            return jsonify({'message': 'Note deleted'})
    return jsonify({'message': 'Note not found'}), 404

# Server start
if __name__ == '__main__':
    app.run(debug=True)
    from flask import Flask, request, jsonify

app = Flask(_name_)

notes = []  # Memory mein notes rakhnay ke liye list

@app.route('/notes', methods=['POST'])
def create_note():
    data = request.get_json()
    note = {
        'id': len(notes) + 1,
        'title': data['title'],
        'content': data['content']
    }
    notes.append(note)
    return jsonify({'message': 'Note created successfully', 'note': note})

# ✅ GET all notes route (naya add karo)
@app.route('/notes', methods=['GET'])
def get_notes():
    return jsonify(notes)

if _name_ == '_main_':
    app.run(debug=True)
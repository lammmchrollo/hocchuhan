from flask import Flask, jsonify, render_template, request
import json
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/vocab', methods=['GET', 'POST'])
def vocab():
    vocab_path = os.path.join('data', 'vocab.json')
    if request.method == 'POST':
        new_word = request.get_json()
        with open(vocab_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        data.append(new_word)
        with open(vocab_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        return 'Đã thêm từ mới!', 200
    else:
        with open(vocab_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)

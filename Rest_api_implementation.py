from flask import Flask, request, jsonify
from test import generate_answer

app = Flask(__name__)


@app.route('/ask', methods=['POST'])
def ask_question():
    data = request.json
    data_query=data.get('query')
    
    if not user_query:
        return jsonify({"error": "Missing Query"}), 400
    
    answer =generate_answer(user_query)
    
    return jsonify({
        "question":user_query,
        "answer": answer
    })
    
    
if __name__ == "__main__":
    app.run(debug=True)
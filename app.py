from flask import Flask, request, jsonify
import translators as ts

app = Flask(__name__)

@app.route('/translate', methods=['POST'])
def translate():
    data = request.json
    query_text = data.get('text')
    translator = data.get('translator', 'bing')
    from_language = data.get('from_language', 'auto')
    to_language = data.get('to_language', 'en')

    translated_text = ts.translate_text(query_text, translator=translator, from_language=from_language, to_language=to_language)
    return jsonify({'translated_text': translated_text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
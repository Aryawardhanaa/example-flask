from flask import Flask
from g4f.client import Client # type: ignore

client = Client()
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from farhan'


@app.route('/test')
def hellow():
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "explain to me about react js"}]
)
    return response.choices[0].message.content
if __name__ == "__main__":
    app.run()

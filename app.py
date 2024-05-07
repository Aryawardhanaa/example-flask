from flask import Flask
from g4f.client import Client

client = Client()
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Koyeb'


@app.route('/test')
def hello_world():
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Hello"}],
)
    return response.choices[0].message.content
if __name__ == "__main__":
    app.run()

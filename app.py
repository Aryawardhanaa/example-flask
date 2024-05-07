from flask import Flask
from g4f.client import Client

client = Client()
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Koye'


@app.route('/test')
def hellow():
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Can you Help Me?"}]
)
    return response.choices[0].message.content
if __name__ == "__main__":
    app.run()

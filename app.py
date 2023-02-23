from flask import Flask,request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def main():
    print(request.form)
    return 'OK'

if __name__ == '__main__':
    app.run(debug=True)
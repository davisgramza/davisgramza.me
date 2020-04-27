from flask import Flask, render_template, request, send_file

app = Flask(__name__)

if __name__ == '__main__':
    app.run()


@app.route('/', methods=['GET'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

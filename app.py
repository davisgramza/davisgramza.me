from flask import Flask, render_template, request, send_file, redirect, url_for

app = Flask(__name__)

if __name__ == '__main__':
    app.run()


@app.route('/', methods=['GET'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

@app.route('/static/resume.pdf', methods=['GET'])
def resume():
    if request.metho == 'GET':
        return redirect(url_for('index'))
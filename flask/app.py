from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    # return 'Hello Flask'
    return render_template('index.html')

@app.route('/info')
def info():
    #return 'info'
    return render_template('info.html')

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
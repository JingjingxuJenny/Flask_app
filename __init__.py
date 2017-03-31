from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return app.send_static_file("vue_js.html")



@app.route('/css/index.css')
def get_CSS():
    return app.send_static_file("/static/css/index.css")

@app.route('/data')
def data():
    return app.send_static_file("home.html")

if __name__ == "__main__":
    app.run()

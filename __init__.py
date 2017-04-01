from flask import Flask, render_template

app = Flask(__name__)
import json

@app.route('/')
def homepage():
    return app.send_static_file("index1.html")

@app.route('/css/index.css')
def get_CSS():
    return app.send_static_file("/static/css/index.css")

@app.route('/pages')
def data():
    returned_object = {}

    with open('static/home.html') as home:
        returned_object['home'] = "".join(home.readlines())

    with open('static/school.html') as home:
        returned_object['school'] = "".join(home.readlines())

    return json.dumps(returned_object)

if __name__ == "__main__":
    app.run()

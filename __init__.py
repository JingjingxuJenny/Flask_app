from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return app.send_static_file("school.html")



@app.route('/css/index.css')
def get_CSS():
    return app.send_static_file("/static/css/index.css")

@app.route('/worldcloud.png')
def get_image():
    return app.send_static_file("/static/worldcloud.png")

if __name__ == "__main__":
    app.run()

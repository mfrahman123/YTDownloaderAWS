from flask import Flask, render_template, request,redirect, url_for
from pytube import YouTube as Youtube

app = Flask(__name__)

items = []

@app.route("/", methods=['GET','POST'])
def hello_world():
    return render_template('home.html', items=items)

@app.route('/handle_data', methods=['POST'])
def handle_data():
    data = request.form['data']
    yt = Youtube(data).streams.get_highest_resolution()
    print(yt.title)
    items.append(yt.title)
    yt.download()
    return redirect(url_for("hello_world"))


if __name__ == "__main__":
   app.run(host='0.0.0.0', port=5000)

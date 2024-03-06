from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
  return render_template('home.html')

@app.route("/about")
def about():
  return render_template('about.html')

@app.route("/events")
def events():
  return render_template('events.html')

@app.route("/contact")
def contact():
  return render_template('contact.html')


@app.route("/gallery1")
def gallery1():
  return render_template('gallery1.html')

@app.route("/gallery2")
def gallery2():
  return render_template('gallery2.html')

@app.route("/gallery3")
def gallery3():
  return render_template('gallery3.html')


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)


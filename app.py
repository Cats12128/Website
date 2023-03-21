from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
  indexTextFile = open("static/index.txt", "r")
  indextext = indexTextFile.read()
  indexTextFile.close()
  return render_template("index.html",addtitle="Home", indextext=indextext)

@app.route("/gallery")
def gallery():
  return render_template("gallery.html", addtitle="Gallery")

@app.route("/about")
def about():
  return render_template("about.html", addtitle="About")

@app.route("/contact")
def contact():
  return render_template("contact.html", addtitle="Contact")

@app.route("/test")
def test():
  return render_template("test.html", addtitle="Testing")

#if __name__ == "__main__":
app.run(host="0.0.0.0", debug=True)

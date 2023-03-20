from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html",addtitle="Home")

@app.route("/gallery")
def gallery():
  return render_template("gallery.html", addtitle="Gallery")

@app.route("/about")
def about():
  return render_template("about.html", addtitle="About")

@app.route("/contact")
def contact():
  return render_template("contact.html", addtitle="Contact")


#if __name__ == "__main__":
app.run(host="0.0.0.0", debug=True)

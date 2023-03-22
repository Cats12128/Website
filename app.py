from flask import Flask, render_template, request, redirect

app = Flask(__name__)

logo = "static/sun.svg"
facebookUrl = "https://www.google.com" #"https://www.facebook.com/jkiyourscreenguy"
twitterUrl = ""
instagramUrl = ""
previousRequest = dict()



@app.context_processor
def injectVariables():
  return dict(facebookUrl=facebookUrl, twitterUrl=twitterUrl, instagramUrl=instagramUrl)

@app.route("/", methods=["GET", "POST"])
def index():
  #indexTextFile = open("static/index.txt", "r")
  #indextext = indexTextFile.read()
  #indexTextFile.close()
  return render_template("index.html", addtitle="Home", logo=logo)

@app.route("/gallery")
def gallery():
  return render_template("gallery.html", addtitle="Gallery")

@app.route("/about")
def about():
  return render_template("about.html", addtitle="About")

@app.route("/contact")
def contact():
  return render_template("contact.html", addtitle="Contact")

@app.route("/thankyou", methods=["GET", "POST"])
def thankyou():
  if request.method == "POST": #this runs if form was submitted (aka POST)
    storeInfo(request.form)    
    return render_template("thankyou.html", addtitle="Thank You")
  else:
    return redirect("/") #this runs if trying to access page without form

def storeInfo(dict):
  fName=dict.get("inputFirstname")
  lName=dict.get("inputLastname")
  email=dict.get("inputEmail")
  address1=dict.get("inputAddress1")
  address2=dict.get("inputAddress2")
  phone=dict.get("inputPhone")
  city=dict.get("inputCity")
  state=dict.get("inputState")
  zip=dict.get("inputZip")
  print(dict)

#if __name__ == "__main__":
app.run(host="0.0.0.0", debug=True)

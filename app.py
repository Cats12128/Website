from flask import Flask, render_template, request, flash
from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, EmailField, TelField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, Regexp



app = Flask(__name__)
csrf = CSRFProtect(app)

app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key"
    ))

logo = "static/sun.svg"
facebookUrl = "https://www.google.com"  #"https://www.facebook.com/jkiyourscreenguy"
twitterUrl = ""
instagramUrl = ""
business_number = "555-555-5555"
previousRequest = dict()


#Request contact form
class ContactForm(FlaskForm):
  
  fname = StringField('First Name', validators=[DataRequired()], render_kw={'class':"form-control", "placeholder":"First Name"})
  
  lname = StringField('Last Name', validators=[DataRequired()], render_kw={'class':"form-control", "placeholder":"Last Name"})
  
  email = EmailField('Email', validators=[DataRequired(), Email(), Regexp(regex="^.+@.+\..+", message="Invalid Email")], render_kw={'class':"form-control", "placeholder":"Email", "pattern":"^.+@.+\..+"})
  
  phone = TelField('Phone Number',validators=[
    DataRequired(),
    Regexp("\([0-9]{3}\) [0-9]{3}-[0-9]{4}")], render_kw={'class':"form-control", "placeholder":"Phone Number", "pattern":"\([0-9]{3}\) [0-9]{3}-[0-9]{4}"})
  
  address1 = StringField('Address 1', validators=[DataRequired()], render_kw={'class':"form-control", "placeholder":"Address 1"})
  
  address2 = StringField('Address 2', render_kw={'class':"form-control", "placeholder":"Address 2"})
  
  city = StringField('City', validators=[DataRequired()], render_kw={'class':"form-control", "placeholder":"City"})
  
  state = SelectField('State', validators=[DataRequired()], render_kw={"class":"form-select"}, choices=["Alaska", "Alabama", "Arkansas", "Arizona", "California", "Colorado", "Connecticut", "District of Columbia", "Delaware", "Florida", "Georgia", "Hawaii", "Iowa", "Idaho", "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts", "Maryland", "Maine", "Michigan", "Minnesota", "Missouri", "Mississippi", "Montana", "North Carolina", "North Dakota", "Nebraska", "New Hampshire", "New Jersey", "New Mexico", "Nevada", "New York", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Puerto Rico", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Virginia", "Virgin Islands", "Vermont", "Washington", "Wisconsin", "West Virginia", "Wyoming"], )
 
  zip = StringField('Zip', validators=[
    DataRequired(), Regexp('^\d{5}$', message="Please Enter a Valid Zip")], render_kw={'class':"form-control", "placeholder":"Zip", "maxlength":"5", "minlength":"5","pattern":"\d{5}"})
  
  submit = SubmitField('Submit', render_kw={"class":"btn btn-primary"})

@app.context_processor
def injectVariables():
  return dict(facebookUrl=facebookUrl,
              twitterUrl=twitterUrl,
              instagramUrl=instagramUrl)

#Homepage
@app.route("/", methods=["GET", "POST"])
def index():
  form = ContactForm(state="Florida")
  print("below is request.form")
  print(request.form)
  if form.validate_on_submit:
    if request.form.get("state") == "Florida":
      storeInfo(request.form)
      return render_template("thankyou.html")
    elif form.validate_on_submit():
      flash("Sorry, we only service the State of Florida")
    

  return render_template("index.html", addtitle="Home", logo=logo, form=form)
    
  return render_template("thankyou.html", addtitle="Thank You")
  
  return render_template("index.html", addtitle="Home", logo=logo, form=form)


@app.route("/gallery")
def gallery():
  return render_template("gallery.html", addtitle="Gallery")

def storeInfo(dict):
  fname = dict.get("fname")
  lname = dict.get("lname")
  email = dict.get("email")
  address1 = dict.get("address1")
  address2 = dict.get("address2")
  phone = dict.get("phone")
  city = dict.get("city")
  state = dict.get("state")
  zip = dict.get("zip")
  csrfToken = dict.get("csrf_token")
  print("in the storeInfo function")
  print(dict)
  
  request.form = {}
  print("bottom of storeInfo function")
  print(request.form)

  
  


#if __name__ == "__main__":
app.run(host="0.0.0.0", debug=True)

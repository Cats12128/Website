var zipcode = document.getElementById("inputZip").value; // here you get what the end-user typed
if (zipcode != "") {
document.getElementById("inputZip").value = (zipcode.replace(/[^\d]/g, '')); // then you strip off all the spaces

var zipcode1 = document.getElementById("inputZip").value;
document.getElementById("inputZip").value =  zipcode1.substring(0,5) + "-" + zipcode1.substring(5,10);

document.getElementById("inputZip").onchange=zip;

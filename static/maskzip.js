var zipcode = document.getElementById("zip").value; // here you get what the end-user typed
if (zipcode != "") {
document.getElementById("zip").value = (zipcode.replace(/[^\d]/g, '')); // then you strip off all the spaces

var zipcode1 = document.getElementById("zip").value;
document.getElementById("zip").value =  zipcode1.substring(0,5) + "-" + zipcode1.substring(5,10);

document.getElementById("zip").onchange=zip;

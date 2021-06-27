#!/usr/bin/node
// JavaScript script that updates the text of the <header> element
//   to New Header!!! when the user clicks on DIV#update_header
const headercol = $("header").click(function() {
    $.get("https://swapi-api.hbtn.io/api/people/5/?format=json",
function(data) {
    $("#character").html(data.name);
    });
});
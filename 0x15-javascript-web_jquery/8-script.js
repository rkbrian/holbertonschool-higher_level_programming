#!/usr/bin/node
// JavaScript script that fetches the
//   character name from a certain URL.
const headercol = $("#character").click(function() {
    $("character").getJSON("https://swapi-api.hbtn.io/api/people/5/?format=json",
    "name");
});
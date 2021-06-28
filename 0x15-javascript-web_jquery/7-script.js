#!/usr/bin/node
// JavaScript script that fetches the
//   character name from a certain URL.
const headercol = $("header").click(function() {
    $.get("https://swapi-api.hbtn.io/api/people/5/?format=json",
    function(data) {
	$("#character").html(data.name);
    });
});

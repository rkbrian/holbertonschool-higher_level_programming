#!/usr/bin/node
// JavaScript script that fetches and lists the
//   title for all movies by using a certain URL.
// UNFINISHED
const headercol = $("header").click(function() {
    $.get("https://swapi-api.hbtn.io/api/people/5/?format=json",
    function(data) {
        $.each(data.results, )
	("#list_movies").html(data.title);
    });
});

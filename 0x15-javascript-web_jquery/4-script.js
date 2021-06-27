#!/usr/bin/node
// JavaScript script that toggles the class red to the <header>
// element when the user clicks on the tag DIV#toggle_header
const headercol = $("#toggle_header").click(function() {
    $("header").toggleClass("red green");
});
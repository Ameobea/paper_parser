"use strict"
/*
Review Script

Processes input JSON object to generate HTML-based
review mechanism for output from the Python script
*/
$(document).ready(function(){
  $.get("http://ip.ameobea.me:5000/data/results.json", function(parsedJson){
    parsedJson.forEach(function(page){
      var mainTable = $("#mainTable");
      mainTable.append("<tr id='" + page.document + page.page + "'><td>" + page.document + "</td><td><a href='http://ip.ameobea.me:5000/data/raw/" + page.document + "+page-" + page.page + ".txt'>" + page.page + "(txt)</a><br><a href='http://ip.ameobea.me:5000/data/pdf/" + page.document + "+page-" + page.page + ".pdf'>" + page.page + "(pdf)</td>");
      for(var key in page){
        if (page.hasOwnProperty(key) && key != "document" && key != "page") {
          $("#" + page.document + page.page).append("<td><p><b>" + key + "</b></p><table>");
           page[key].forEach(function(match, matchIndex){
            $("#" + page.document + page.page + " table").append("<tr><td style='border-top: 1px solid black'><input type='checkbox' id='" + page.document + "-" + page.page + "-" + matchIndex + "'></td><td style='border-top: 1px solid black'>" + match + "</td></tr>");
           });
           $("#" + page.document + page.page).append("</table></td>");
        }
      }
      mainTable.append("</tr>");
    });
  });
});

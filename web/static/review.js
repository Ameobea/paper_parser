"use strict"
/*
Review Script

Processes input JSON object to generate HTML-based
review mechanism for output from the Python script
*/
$(document).ready(()=>{
  $.get("http://ip.ameobea.me:5000/data/results.json", parsedJson=>{
    parsedJson.forEach(page=>{
      var mainTable = $("#mainTable");
      mainTable.append("<tr id='" + page.document + page.page + "'><td>" + page.document + "</td><td><a href='http://ip.ameobea.me:5000/data/raw/" + page.document + "+page-" + page.page + ".txt'>" + page.page + "(txt)</a><br><a href='http://ip.ameobea.me:5000/data/pdf/" + page.document + "+page-" + page.page + ".pdf'>" + page.page + "(pdf)</td>");
      for(var key in page){
        if (page.hasOwnProperty(key) && key != "document" && key != "page") {
          $("#" + page.document + page.page).append("<td><p><b>" + key + "</b></p><table>");
           page[key].forEach((match, matchIndex)=>{
            $("#" + page.document + page.page + " table").append("<tr><td style='border-top: 1px solid black'><input type='checkbox' class='check' id='" + page.document + "-" + page.page + "-" + key + "-" + matchIndex + "'></td><td style='border-top: 1px solid black'>" + match + "</td></tr>");
           });
           $("#" + page.document + page.page).append("</table></td>");
        }
      }
      mainTable.append("</tr>");
    });
  });

  $("#submitButton").click(()=>{
    $.get("http://ip.ameobea.me:5000/data/results.json", parsedJson=>{
      saveResults(parsedJson);
    });
  })
});

var saveResults = parsedJson=>{
  var checked = [];
  var unchecked = [];

  var checkboxes = $(".check");
  for(var i=0;i<checkboxes.length;i++){
    var split = checkboxes[i].id.split("-"); //format of this is now [document, page, type, index]

    var textObject = parsedJson.filter(page=>{
      return split[0] == page.document && split[1] == page.page;
    });

    var text = textObject[0][split[2]][split[3]];
    var doc = {document: split[0], page: split[1], type: split[2], index: split[3], text: text};

    if(checkboxes[i].checked){
      checked.push(dox);
    }else{
      unchecked.push(doc);
    }
  }
  //TODO: Save checked and unchecked arrays to file
}

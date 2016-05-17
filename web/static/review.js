"use strict";
/*jslint browser: true*/ /*global $*/

/*
Review Script

Processes input JSON object to generate HTML-based
review mechanism for output from the Python script
*/
$(document).ready(()=>{
  $.get("../data/results.json", parsedJson=>{
    //printByDocument(mainTable, parsedJson) //Uncomment this line to enable printing grouped by document
    printByCategory(mainTable, parsedJson)
  });

  $("#submitButton").click(()=>{
    $.get("../data/results.json", parsedJson=>{
      saveResults(parsedJson);
    });
  });
});

/*
This groups the results by document.  They are displayed in a sideways tree fashion
where the document is at the left, which is divided into category, which is divided
into keyword match.
*/
var printByDocument = parse=>{
  parsedJson.forEach(page=>{
    var mainTable = $("#mainTable");

    printPage(mainTable, page);
    mainTable.append("</tr>");
  });
};

var printPage = (mainTable, page)=>{
  mainTable.append("<tr class='page-row' id='" + page.document + page.page + "'><td>" +
    page.document + "</td><td><a href='../data/raw/" + page.document + "+page-" +
    page.page + ".txt'>" + page.page + "(txt)</a><br><a href='../data/pdf/" +
    page.document + "+page-" + page.page + ".pdf'>" + page.page + "(pdf)</td>");
  for(var key in page){
    if (page.hasOwnProperty(key) && key != "document" && key != "page") {
      $("#" + page.document + page.page).append("<td><p><b>" + key + "</b></p><table class='category-table'>");
       page[key].forEach((match, matchIndex)=>{
        $("#" + page.document + page.page + " table").append("<tr>"+
          /*<td style='border-top: 1px solid black'>*/"<input type='checkbox' class='check' id='" +
          page.document + "-" + page.page + "-" + key + "-" + matchIndex + "'></td><td"+
          /*" style='border-top: 1px solid black'*/">" + match + "</td></tr>");
       });
       $("#" + page.document + page.page).append("</table></td>");
    }
  }
};

/*
This groups results globally by category.  Every place where a page matches a
category, it is added to the list of all matches for that category.  That same
page is also added to the sections for all other categories it matches.
*/
var printByCategory = (mainTable, parsedJson)=>{
  var mainTable = $("#mainTable");
  var uniqueCategories = [];
  var justCategories = [];

  parsedJson.forEach(page=>{
    for(var key in page){
      if(justCategories.indexOf(key) == -1 && key != "document" && key != "page"){
        justCategories.push(key);
        uniqueCategories.push({category: key});
      }
    }
  });

  uniqueCategories.forEach(category=>{
    category.pageMatches = parsedJson.filter(page=>{
      var exists = page[category.category];
      return typeof exists != "undefined";
    });

    mainTable.append(`<tr><td><h1 class="category-header">${category.category}</td></tr>`);
    category.pageMatches.forEach(page=>{
      printPage(mainTable, page);
    });
  });
};

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
      checked.push(doc);
    }else{
      unchecked.push(doc);
    }
  }
  //TODO: Save checked and unchecked arrays to file???
};

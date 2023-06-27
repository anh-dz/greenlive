function updateFVatDung() {

  function updateDivText(listData) {
    var divElement = document.getElementById('sodiem');
    divElement.innerHTML = listData[0]; // Replace "0" with the desired index from the list
}

  url = "/diem";

  axios.get(url).then(function(response) {

      // The data will all be returned as a JSON object
      // We can access the data by using the data property of the response object

      updateDivText(response.data);
  })
  .catch(function(error) {
      console.log(error);
  });
}

function updateDiem() {
    
  url = "/diem";

  axios.get(url).then(function(response) {

      // The data will all be returned as a JSON object
      // We can access the data by using the data property of the response object

      document.getElementById('sodiem').innerHTML = response.data.so_diem;
  })
  .catch(function(error) {
      console.log(error);
  });
}

function deleteRow(button) {
  var row = button.parentNode.parentNode;
  row.parentNode.removeChild(row);
}

// This calls the function getRandomNumber() every 2 seconds
var intervalID = window.setInterval(updateDiem, 2000);
updateDiem();

// functionaddRow() {
//   var tableRow = document.getElementById("nhacnho");
//   var row = tableRow.insertRow(0);
//   var cell1 = row.insertCell(0);
//   var cell2 = row.insertCell(1);
//   var cell3 = row.insertCell(2);
//    cell1.innerHTML = "Cell of New Row";
//    cell2.innerHTML = "Cell of New Row";
//    cell3.innerHTML = "Cell of New Row";
// }

// https://linuxhint.com/add-row-to-html-table-using-javascript/#:~:text=Use%20the%20following%20syntax%20for,table%20or%20at%20the%20start.

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

function addRow() {
  var table = document.getElementById("table");
  var newRow = table.insertRow(table.rows.length);
  
  var usernameCell = newRow.insertCell(0);
  var vatdungCell = newRow.insertCell(1);
  var thoigianCell = newRow.insertCell(2);
  var buttonCell = newRow.insertCell(3);
  buttonCell.innerHTML = '<button class="btn text-success my-2 table-delete" onclick="deleteRow(this)"><i class="fa-solid fa-trash"></i></button>';

  usernameCell.contentEditable = true;
  vatdungCell.contentEditable = true;
  thoigianCell.contentEditable = true;
  
  usernameCell.innerHTML = "Bạn cần mua gì?";
  vatdungCell.innerHTML = "Bạn mua vào thời gian nào?";
  thoigianCell.innerHTML = "Bạn mua ở cửa hàng nào?"
}

function copyText() {
  var codeText = document.getElementById("codeText");
  var text = codeText.innerText;

  navigator.clipboard.writeText(text)
    .then(function () {
      
    })
    .catch(function (error) {
      console.error("Copy failed:", error);
    });
}

// https://linuxhint.com/add-row-to-html-table-using-javascript/#:~:text=Use%20the%20following%20syntax%20for,table%20or%20at%20the%20start.

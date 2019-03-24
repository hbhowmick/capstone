import Config from '../../config.py'

let config = new Config();


// function that logs the address info entered in the form
function searchAddress() {
  let street = $('street').val();
  let city = $('city').val();
  let state = $('state').val();
  let zip = $('zip').val();
  console.log(street);
  console.log(city);
  console.log(state);
  console.log(zip);
}

// check to see if the submit button is pressed, if it is, stop the even from refreshing the page, and call searchAddress()
$('submit_Address').click(function(e) {
  e.preventDefault();
  searchAddress();
});

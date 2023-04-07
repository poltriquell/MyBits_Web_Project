// Set up the image object
const img = document.getElementById("rick-astley");

// Wait for the image to load
img.addEventListener("load", () => {
  // Start the animation
  img.classList.add("animated");
});

$(document).ready(function() {
    // Add smooth scrolling to all links
    $("a").on('click', function(event) {
      if (this.hash !== "") {
        event.preventDefault();

        var hash = this.hash;

        $('html, body').animate({
          scrollTop: $(hash).offset().top
        }, 800, function() {
          window.location.hash = hash;
        });
      }
    });
  });

// Get the form element
var form = document.querySelector('.form-signin');

// Add event listener for form submission
form.addEventListener('submit', function(event) {
  event.preventDefault(); // Prevent the form from submitting

  // Get the email and password values
  var email = document.getElementById('inputEmail').value;
  var password = document.getElementById('inputPassword').value;

  // Check if the email and password are valid
  if (email === 'user@example.com' && password === 'password') {
    // Display a success message
    alert('Login successful!');
  } else {
    // Display an error message
    alert('Invalid email or password. Please try again.');
  }
});


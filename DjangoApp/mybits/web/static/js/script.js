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

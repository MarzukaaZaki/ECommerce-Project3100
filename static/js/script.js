var slideIndex = 0;
showSlides();

function showSlides() {
  var i;
  //Fetch the div element by class name from the html file
  var slides = document.getElementsByClassName("mySlides");
  for (i = 0; i < slides.length; i++) {
    // Display none
    slides[i].style.display = "none";
  }
  slideIndex++;
  // If slide ends then start from the beginning
  if (slideIndex > slides.length) {slideIndex = 1}
  // Block display by style property
  slides[slideIndex-1].style.display = "block";
  setTimeout(showSlides, 2000); // Change image every 2 seconds
}
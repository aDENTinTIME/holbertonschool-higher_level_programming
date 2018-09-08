// Swaps the class green with red every time toggle_header is clicked
$('DIV#toggle_header').on('click', function toggleMe () {
  if ($('header').hasClass('green')) {
    $('header').removeClass();
    $('header').addClass('red');
  } else {
    $('header').removeClass();
    $('header').addClass('green');
  }
});

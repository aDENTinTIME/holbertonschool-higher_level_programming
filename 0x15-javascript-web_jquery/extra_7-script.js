// Sets the text of the id character to some the name in some json data
// Also alerts with the date of the character's birth when the page is clicked
$.get('https://swapi.co/api/people/5/?format=json', (data) => {
  $('DIV#character').text(data.name);
  $('body').on('click', () => {
    window.alert(data.birth_year);
  });
});

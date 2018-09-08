// Sets the text of the id character to some the name in some json data
$.get('https://swapi.co/api/people/5/?format=json', (data) => {
  $('DIV#character').text(data.name);
});

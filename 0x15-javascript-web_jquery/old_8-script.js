// Adds all Star Wars movie title to an unorderd list list_movies
$.get('https://swapi.co/api/films/?format=json', (data) => {
  data.results.forEach((movie) => {
    $('UL#list_movies').append('<li>' + movie.title + '</li>');
  });
});

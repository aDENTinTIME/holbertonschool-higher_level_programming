// Adds all Star Wars movie title to an unorderd list list_movies
$.get('https://swapi.co/api/films/?format=json', (data) => {
  $.each(data.results, (i, movie) => {
    $('UL#list_movies').append('<li>' + movie.title + '</li>');
  });
});

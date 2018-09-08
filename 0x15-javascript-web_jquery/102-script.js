// Takes user input city, and returns wind speed
window.onload = () => {
  $('INPUT#btn_search').on('click', function searchNow () {
    let city = encodeURI($('INPUT#city_search').val());
    $.get('https://query.yahooapis.com/v1/public/yql?q=select%20wind%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22' + city + '%22)&format=json', (data) => {
      $('DIV#wind_speed').text(data.query.results.channel.wind.speed);
    });
  });
};

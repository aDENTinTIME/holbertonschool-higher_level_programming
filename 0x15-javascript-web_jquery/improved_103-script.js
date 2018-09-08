// 103 with some error handling and minor aesthetics
window.onload = () => {
  $('INPUT#btn_search').on('click', function searchNow () {
    let city = encodeURI($('INPUT#city_search').val());
    if (!city) {
      city = ':city_name';
    }
    $.get('https://query.yahooapis.com/v1/public/yql?q=select%20wind%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22' + city + '%22)&format=json', (data, textStatus) => {
      if (data.query.results != null) {
        $('DIV#wind_speed').text(data.query.results.channel.wind.speed).toggle().toggle(200);
      } else {
        window.alert('Whoops, can\'t find that one!');
      }
    });
  });
  $(document).on('keypress', 'INPUT#city_search', (e) => {
    if (e.keyCode === 13)
      $('INPUT#btn_search').click();
  });
  $('DIV#wind_speed').css({color: '#f2a446'});
};

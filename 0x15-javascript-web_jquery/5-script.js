// Appends an li element in the my_list tag.
$('DIV#add_item').on('click', function appendMe () {
  $('UL.my_list').append('<li>Item</li>');
});

// Adds, Removes, and Clears items from a list
window.onload = () => {
  $('DIV#add_item').on('click', () => {
    $('UL.my_list').append('<li>Item</li>');
  });
  $('DIV#remove_item').on('click', () => {
    $('UL.my_list > li:first').remove();
  });
  $('DIV#clear_list').on('click', () => {
    $('UL.my_list').empty();
  });
};

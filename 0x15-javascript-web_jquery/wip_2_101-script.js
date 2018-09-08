// A point in my process where I'm confirming my selctors work
// Working with document.querySelector
window.onload = () => {
  document.querySelector('DIV#add_item').onclick = () => {
    $('UL.my_list').append('<li>Item</li>');
  };
  document.querySelector('DIV#remove_item').onclick = () => {
    $('UL.my_list > li:first').remove();
  };
  document.querySelector('DIV#clear_list').onclick = () => {
    $('UL.my_list').empty();
  };
};

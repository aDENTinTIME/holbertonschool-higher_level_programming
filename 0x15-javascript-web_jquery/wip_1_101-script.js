// A point in my process where I'm confirming my selctors work
window.onload = () => {
  document.querySelector('DIV#add_item').onclick = () => {
    window.alert('add');
  };
  document.querySelector('DIV#remove_item').onclick = () => {
    window.alert('remove');
  };
  document.querySelector('DIV#clear_list').onclick = () => {
    window.alert('clear');
  };
};

/* 4-script.js */

$(function() {
  $('#toggle_header').click(function() {
    const currentClass = $('header').attr('class');
    if (currentClass === 'red') {
      $('header').removeClass('red').addClass('green');
    } else if (currentClass === 'green') {
      $('header').removeClass('green').addClass('red');
    }
  });
});

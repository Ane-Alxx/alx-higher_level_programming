/* 9-script.js */

$(function() {
  $.getJSON('https://hellosalut.stefanbohacek.dev/?lang=fr', function(data) {
    $('#hello').text(data.translations.hello);
  });
});

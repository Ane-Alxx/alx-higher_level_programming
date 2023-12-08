/* 102-script.js */

$(function() {
  $('#btn_translate').click(function() {
    const languageCode = $('#language_code').val();
    const url = `https://www.fourtonfish.com/hellosalut/hello/${languageCode}`;
    $.getJSON(url, function(data) {
      $('#hello').text(data.translations.hello);
    });
  });
});

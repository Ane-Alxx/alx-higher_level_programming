/* 103-script.js */

$(function() {
  $('#btn_translate').click(function() {
    fetchTranslation();
  });

  $('#language_code').keyup(function(event) {
    if (event.keyCode === 13) {
      fetchTranslation();
    }
  });

  function fetchTranslation() {
    const languageCode = $('#language_code').val();
    const url = `https://www.fourtonfish.com/hellosalut/hello/${languageCode}`;
    $.getJSON(url, function(data) {
      $('#hello').text(data.translations.hello);
    });
  }
});

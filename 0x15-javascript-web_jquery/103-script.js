$(document).ready(function () {
  function fetchTranslation () {
    const languageCode = $('#language_code').val().trim();
    if (languageCode) {
      $.get('https:/www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}', function (data) {
        $('#hello').text(data.hello);
      }).fail(function () {
        $('#hello').text('Error fetching the translation');
      });
    } else {
      $('#hello').text('Please enter a language code');
    }
  }

  $('#btn_translate').click(fetchTranslation);

  $('#language_code').keyup(function (event) {
    if (event.which === 13) {
      fetchTranslation();
    }
  });
});

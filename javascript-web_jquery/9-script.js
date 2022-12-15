const $ = window.$;
$.get('https://stefanbohacek.com/hellosalut/?lang=fr', function (data, textStatus) {
  $('DIV#hello').text(data.hello);
});

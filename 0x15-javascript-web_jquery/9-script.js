$(document).ready(function () {
    $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (fetcheddata){
    const fetchedval = fetcheddata.hello;
    $('#hello').text(fetchedval)
})
})

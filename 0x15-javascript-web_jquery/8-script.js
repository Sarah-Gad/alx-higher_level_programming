$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (fetcheddata) {
    const allmovies = fetcheddata.results;
    allmovies.forEach(function(onemovie) {
        $('#list_movies').append('<li>' + onemovie.title + '</li>');
    });
});

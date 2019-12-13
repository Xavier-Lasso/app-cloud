function httpRequestMovieId(url) {
    $.ajax({
        url: url,
        type: "get",
        data: 'json',
        success: function(response) {
            $("#s1").html(response);
        },
        error: function(e) {
            console.log(e);
        }
    });
}

function httpRequestMovieYear(url) {
    $.ajax({
        url: url,
        type: "get",
        data: 'json',
        success: function(response) {
            $("#s2").html(response);
        },
        event: function(e) {
            console.log(e);
        }
    });
}

function httpRequestGenreId(url) {
    $.ajax({
        url: url,
        type: "get",
        data: 'json',
        success: function(response) {
            $("#c2").html(response);
        },
        error: function(e) {
            console.log(e);
        }
    });
}

function changeMoviesById() {
    const movieId = document.getElementById('input-movieid').value;
    httpRequestMovieId('/user/movies/' + movieId);
}

function changeYear() {
    const year = document.getElementById('input-year').value;
    if(year)
    {
        httpRequestMovieYear('/user/movies/year/' + year);
    }
}

function changeSexe() {
    const userSex = document.getElementById('select-sexe').value;
    const topNumber = document.getElementById('topNumber').value;
    if(userSex && topNumber)
    {
        httpRequestGenreId('/analyst/genre/' + userSex + '?q=' + topNumber);
    }
}

function changeTopNumber() {
    const userSex = document.getElementById('select-sexe').value;
    const topNumber = document.getElementById('topNumber').value;
    if(userSex && topNumber)
    {
        httpRequestGenreId('/analyst/genre/' + userSex + '?q=' + topNumber);
    }
}

window.onload = function() {
    httpRequestMovieId('/user/movies/1');
    httpRequestMovieYear('/user/movies/year/5');
};

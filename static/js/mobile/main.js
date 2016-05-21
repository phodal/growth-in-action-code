'use strict';
$(document).ready(function () {
    $('#typeahead-input').typeahead({
        source: function (query, process) {
            return $.get('/api/blogpost/?format=json&title=' + query, function (data) {
                return process(data);
            });
        },
        updater: function (item) {
            return item;
        },
        displayText: function (item) {
            return item.title;
        },
        afterSelect: function (item) {
            location.href = 'http://localhost:8000/blog/' + item.slug + ".html";
        },
        delay: 500
    });
});

var responseStream = function (blogId) {
    var url = '/api/blogpost/?format=json';

    if (blogId) {
        url = '/api/blogpost/' + blogId + '?format=json';
    }

    return Rx.Observable.create(function (observer) {
        jQuery.getJSON(url)
            .done(function (response) {
                observer.onNext(response);
            })
            .fail(function (jqXHR, status, error) {
                observer.onError(error);
            })
            .always(function () {
                observer.onCompleted();
            });
    });
};

riot.route.base('#');

riot.route('blog/*', function (id) {
    riot.mount("blogDetail", {id: id})
});

riot.route('blog', function () {
    riot.mount("blog")
});

riot.route.start();

riot.route("blog");

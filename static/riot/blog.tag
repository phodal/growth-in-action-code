<blog class="row">
    <div class="col-sm-4" each={ opts }>
        <h2><a onclick={ parent.click }>{ title }</a></h2>
        { body }
        { posted } - By { author }
    </div>
    <script>
        this.on('update', function () {
            console.log(this.opts) // Succeeds
        })

        click(event)
        {
            var blogId = event.item.id;
            var responseStream = Rx.Observable.create(function (observer) {
                jQuery.getJSON('/api/blogpost/' + blogId + '?format=json')
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
            responseStream.subscribe(function (response) {
                riot.mount("blog", [response]);
            });
        }
    </script>
</blog>

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
            responseStream(1).subscribe(function (response) {
                riot.mount("blog", [response]);
            });
        }
    </script>
</blog>

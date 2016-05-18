<blogDetail class="row">
    <div class="col-sm-4">
        <h2>{ opts.title }</h2>
        { opts.body }
        { opts.posted } - By { opts.author }
    </div>
    <script>
        var self = this;
        this.on('update', function () {
            console.log(this.opts) // Succeeds
        })

        console.log("==========")

        this.on('mount', function () {
            responseStream(1).subscribe(function (response) {
                self.opts = response;
                self.update();
            })
        })
    </script>
</blogDetail>

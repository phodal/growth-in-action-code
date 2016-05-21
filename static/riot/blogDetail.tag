<blogDetail class="row">
    <navbar title="{ opts.title }"></navbar>
    <div class="col-sm-4">
        <h2>{ opts.title }</h2>
        { opts.body }
        { opts.posted } - By { opts.author }
    </div>
    <script>
        var self = this;
        this.on('mount', function (id) {
            responseStream(this.opts.id).subscribe(function (response) {
                self.opts = response;
                self.update();
            })
        })
        clickTitle(event) {
            self.unmount(true);
            riot.route("blog");
        }
    </script>
</blogDetail>

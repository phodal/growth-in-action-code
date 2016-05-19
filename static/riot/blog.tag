<blog class="row">
    <div class="col-sm-4" each={ opts }>
        <h2><a href="#/blogDetail/{id}" onclick={ parent.click }>{ title }</a></h2>
        { body }
        { posted } - By { author }
    </div>
    <script>
        var self = this;
        this.on('update', function () {

        })

        this.on('mount', function (id) {
            responseStream().subscribe(function (response) {
                self.opts = response;
                self.update();
            })
        })

        click(event)
        {
            this.unmount();
            riot.route("blogDetail/" + event.item.id);
        }
    </script>
</blog>

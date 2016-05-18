<blog class="row">
    <div class="col-sm-4" each={ opts }>
        <h2><a href="#blog/{id}" onclick={ parent.click }>{ title }</a></h2>
        { body }
        { posted } - By { author }
    </div>
    <script>
        var self = this;
        this.on('update', function () {
            console.log(this.opts) // Succeeds
        })

        click(event)
        {
            riot.mount("blogDetail");
            self.unmount()
        }
    </script>
</blog>

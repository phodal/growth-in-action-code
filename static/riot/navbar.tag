<navbar class="row">
    <ol class="breadcrumb">
        <li><a onclick={ parent.goHome }>Home</a></li>
    </ol>
    <script>
        var self = this;
        this.on('update', function () {
            console.log(this.opts) // Succeeds
        })

        goHome(event)
        {

        }
    </script>
</navbar>

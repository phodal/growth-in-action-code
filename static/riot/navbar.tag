<navbar>
    <ol class="breadcrumb">
        <li><a href={this.parent.backToHome}>Home</a></li>
    </ol>
    <script>
        this.backToHome = "/"
        this.on('update', function () {

        })

        this.on('mount', function () {
            console.log(this.opts);
        });
    </script>
</navbar>

<navbar>
    <ol class="breadcrumb">
        <li><a href="#/" onclick={parent.clickTitle}>Home</a></li>
        <li if="opts.title">{ opts.title} </li>
    </ol>
    <script>
        this.backToHome = "/"
        this.on('mount', function () {

        });
    </script>
</navbar>

  <blog class="row">
   <div class="col-sm-4" each={ opts }>
        <h2><a onclick={ parent.click }>{ title }</a></h2>
        { body }
        { posted } - By { author }
    </div>
  </blog>

<script>
click = function (event) {
    console.log(event);
}
</script>

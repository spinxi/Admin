
    $(document).on('click','#delete-object', function(event){
    var id = $(this).data("object-id");
    var name = $(this).data("object-name");
    $("#delete-object-a").attr("href", '/trucks/delete/' + id)
    $("#object-name").text(name);
});

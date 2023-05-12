flatpickr(".datetimeinput", {allowInput: true, enableTime: true});

document.addEventListener("DOMContentLoaded", function () {
    new Choices("#id_load_status", { shouldSort: 1 });
    new Choices("#id_load_driver_user", { removeItemButton: !0 });
});
ClassicEditor.create(document.querySelector("#ckeditor-classic")).then(function(e){e.ui.view.editable.element.style.height="100px"}).catch(function(e){console.error(e)});

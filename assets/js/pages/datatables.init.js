$(document).ready(function(){var t=$("#datatable-buttons").DataTable({dom:"tp",ordering:!1,language:{paginate:{previous:'<i class="mdi mdi-chevron-left"></i>',next:'<i class="mdi mdi-chevron-right"></i>'}},buttons:[{extend:"excel",charset:"utf-8",className:"dropdown-item",extension:".xlsx",text:"Export as Excel",filename:"Driver_list",bom:!0,init:function(t,e,n){$(e).removeClass("btn-secondary")},exportOptions:{columns:[0,1,2,4,5]}},{pageSize:"LEGAL",init:function(t,e,n){$(e).removeClass("btn-secondary")},extend:"pdf",text:"Export as PDF",className:"dropdown-item",charset:"utf-8",extension:".pdf",filename:"Driver_list",bom:!0,exportOptions:{columns:[0,1,2,4,5]}}]});t.buttons().container().appendTo($("#datatable_butt")),$(".dt-buttons").removeClass("btn-group"),$("#custom-filter").keyup(function(){t.search(this.value).draw()})});
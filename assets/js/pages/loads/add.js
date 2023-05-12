flatpickr("#id_pickup_date", {allowInput: true});
flatpickr("#id_pickup_time", {time_24hr: true, allowInput: true, noCalendar: true, enableTime: true});
flatpickr("#id_delivery_date", {allowInput: true});
flatpickr("#id_delivery_time", {time_24hr: true, allowInput: true, noCalendar: true, enableTime: true});
flatpickr("#id_cargo_expiration_date", {allowInput: true});
flatpickr("#id_physical_damage_expiration_date", {allowInput: true});

document.addEventListener("DOMContentLoaded", function () {
    new Choices("#id_load_status", { shouldSort: 1 });
    // new Choices("#id_trailer", { shouldSort: 1 });
    // new Choices("#id_truck", { shouldSort: 1 });
    // new Choices("#id_driver", { shouldSort: 1 });
});

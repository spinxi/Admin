flatpickr("#id_registration_start_date", {allowInput: true,  });
flatpickr("#id_registration_expiration_date", {allowInput: true,  });
flatpickr("#id_inspection_expiration_date", {allowInput: true,  });
flatpickr("#id_non_trucking_expiration_date", { allowInput: true, });
flatpickr("#id_cargo_expiration_date", {allowInput: true, });
flatpickr("#id_physical_damage_expiration_date", {allowInput: true,  });

document.addEventListener("DOMContentLoaded", function () {
    
    new Choices("#id_trailer_status", { shouldSort: 1 });
    new Choices("#id_rent", { shouldSort: 1 });
    new Choices("#id_gps", { shouldSort: 1 });
});

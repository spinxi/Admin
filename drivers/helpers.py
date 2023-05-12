from drivers.models import DriversFiles
# from celery import shared_task

# @shared_task
def handle_files(file_dict, driver):
    for field_name, files in file_dict.items():
        for file in files:

            file_instance = DriversFiles(driver_files = driver, **{field_name: file})
            file_instance.save()
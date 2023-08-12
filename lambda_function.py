import json
from s3_helper import create_folder_if_not_exists, folder_names_locator


#Get today's date and extract year, month, and day
today = datetime.now()
year = today.strftime('%Y')
month = today.strftime('%m')
day = today.strftime('%d')

bucket_name = '<your s3 bucket name here>'
raw_folder_path = '<your folder path inside the s3 bucket>' #do not add the s3 bucket again

template_folder_paths = folder_names_locator(bucket_name, raw_folder_path)


for i in range(len(template_folder_paths)):
    # Step 2: Check if the folder with current year exists, if not create it
    year_folder_path = f'{template_folder_paths[i]}{year}/'
    create_folder_if_not_exists(bucket_name, year_folder_path)
    
    # Step 3: Navigate to the folder with current year, check if the folder with current month exists, if not create it
    month_folder_path = f'{year_folder_path}{month}/'
    create_folder_if_not_exists(bucket_name, month_folder_path)
    
    # Step 4: Navigate to the folder with current month, check if the folder with current day exists, if not create it
    day_folder_path = f'{month_folder_path}{day}/'
    create_folder_if_not_exists(bucket_name, day_folder_path)
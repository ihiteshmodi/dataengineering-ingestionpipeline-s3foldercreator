import boto3
from datetime import datetime

s3 = boto3.client('s3')

def folder_names_locator(bucket, raw_data_path):
    #This will give us a list of all folders inside raw data folder, These will be folders for platforms eg - Fb, Snap, Tiktok Etc...
    platform_folder_response = s3.list_objects_v2(Bucket = bucket, Prefix = raw_data_path, Delimiter = "/") #if we do not add Delimeter / then we will end up getting al the objects inside s3 bucket

    platform_folder_list = [folder['Prefix'] for folder in platform_folder_response['CommonPrefixes']] #common prefixes in JSON contains the 
            
    #find templates in second iterations.
    
    templates_paths = []
    
    for i in range(len(platform_folder_list)):
        template_folder_response = s3.list_objects_v2(Bucket = bucket, Prefix = platform_folder_list[i], Delimiter = "/") #iterating through each platform folder to find template folders inside it
        templates_paths = templates_paths + [folder['Prefix'] for folder in template_folder_response['CommonPrefixes']]
    return templates_paths
    
def create_folder_if_not_exists(bucket_name, folder_path):
    s3 = boto3.client('s3')
    try:
        #head object checks for metadata only of an object. If the object is not present there won’t be any metadata as well and the result will be an exception in which case we will run except block.
        #if the head dosent work, we will use get_object
        s3.head_object(Bucket=bucket_name, Key=folder_path)
        print(f"{folder_path} already exists")
    except:
        #put object simply creates object
        s3.put_object(Bucket=bucket_name, Key=folder_path)
        print(f"{folder_path} Created")
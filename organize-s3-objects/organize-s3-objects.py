
import boto3
from datetime import datetime

today = datetime.today()
todays_date = today.strftime("%Y%m%d")

def lambda_handler(event, context):

    # search for boto3 aws s3 in google. find client. this help connect to the s3 bucket
    # connect to the s3 bucket created
    s3_client = boto3.client('s3')


    bucket_name = "chidex-organize-s3-objects"
    #list all objects in the bucket (search boto3 aws list s3 objects)
    list_objects = s3_client.list_objects_v2(Bucket=bucket_name)

    # get the values of the key contents in the bucket
    get_content = list_objects.get("Contents")

    # get the names of all the objects in the bucket 
    get_all_object_names = []

    for item in get_content:
        s3_object_name = item.get("Key")
        
        get_all_object_names.append(s3_object_name)
        
    # create folder format 
    directory_name = todays_date + "/"

    #create a folder for today's date in the s3 bucket
    #first check if the folder exist in the S3 bucket: if statement

    if directory_name not in get_all_object_names:
        s3_client.put_object(Bucket=bucket_name, Key=(directory_name))

    # put all the files in the folder created
    for item in get_content:
        object_creation_date = item.get("LastModified").strftime("%Y%m%d") + "/"
        object_name = item.get("Key")
        
        # next check if each object matches the folder name: condition 
        if object_creation_date == directory_name and "/" not in object_name: 
            s3_client.copy_object(Bucket=bucket_name, CopySource=bucket_name+"/"+object_name, Key=directory_name+object_name)
            s3_client.delete_object(Bucket=bucket_name, Key=object_name)




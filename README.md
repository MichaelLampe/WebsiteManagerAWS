# WebsiteManagerAWS
Easily let me keep version control on my websites on S3.  Single script to update the web.

# Use

To use, follow the example.  The website class takes five arguments.  

Website(Bucket Name, File Location, Access Key, Secret Access Key, Region)

1) Bucket Name: The name of your S3 Bucket  
2) File Location: The directory containing the files you want to be uploaded to your S3 bucket  
3) Access Key: Your user access key with S3 permissions enabled  
4) Secret Access Key: Your secret user access key associated with the above access key  
5) Region: The region your S3 bucket is in  

After creating your website class, just run upload_files_to_amazon()

# Example
Note: I've created a python directory with the fields that I import from aws.Config. You can load these however you want (Or directly encode them).

```
from aws.Config import ACCESS_KEY, SECRET_ACCESS_KEY, BUCKET_NAME, REGION, FILE_LOCATION  
from WebsiteManager import Website  
website = Website(BUCKET_NAME,  
                  FILE_LOCATION,  
                  ACCESS_KEY,  
                  SECRET_ACCESS_KEY,  
                  REGION)  

website.upload_files_to_amazon()  
```

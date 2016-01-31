from aws.Config import ACCESS_KEY, SECRET_ACCESS_KEY, BUCKET_NAME, REGION, FILE_LOCATION
from WebsiteManager import Website
website = Website(BUCKET_NAME,
                  FILE_LOCATION,
                  ACCESS_KEY,
                  SECRET_ACCESS_KEY,
                  REGION)

website.upload_files_to_amazon()
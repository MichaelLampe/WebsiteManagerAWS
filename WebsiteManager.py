from boto3 import Session
import os

class Website:
    def __init__(self, bucket_name, file_location, access_key, secret_access_key, region):
        self.bucket_name = bucket_name
        self.file_location = file_location
        self.session = Session(aws_access_key_id=access_key,
                               aws_secret_access_key=secret_access_key,
                               region_name=region)
        self.s3 = self.session.resource('s3')
        self.bucket = self.s3.Bucket(bucket_name)

    def upload_files_to_amazon(self):
        for root, directory, files in os.walk(self.file_location):
            for f in files:
                file_location = os.path.abspath(os.path.join(root, f))
                file_key = file_location.replace(self.file_location, "")

                # Make sure the documents are correctly presented when they get on the server.
                extra_args = dict()
                if f.endswith(".css"):
                    extra_args["ContentType"] = "text/css"
                elif f.endswith(".json"):
                    extra_args["ContentType"] = "application/json"
                elif f.endswith(".js"):
                    extra_args["ContentType"] = "application/javascript"
                elif f.endswith(".html"):
                    extra_args["ContentType"] = "text/html"
                elif f.endswith(".txt"):
                    extra_args["ContentType"] = "text/plain"
                elif f.endswith(".pdf"):
                    extra_args["ContentType"] = "application/pdf"
                elif f.endswith(".jpeg"):
                    extra_args["ContentType"] = "image/jpeg"
                elif f.endswith(".png"):
                    extra_args["ContentType"] = "image/png"
                elif f.endswith(".bmp"):
                    extra_args["ContentType"] = "image/bmp"
                elif f.endswith(".gif"):
                    extra_args["ContentType"] = "image/gif"

                self.s3.meta.client.upload_file(file_location,
                                                self.bucket_name,
                                                file_key,
                                                extra_args)
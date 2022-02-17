from sys import prefix
import boto3
from datetime import datetime, timedelta

SOURCE_BUCKET = "dsi-hvr-poc"
SOURCE_BUCKET_PREFIX = "archive/"
DESTINATION_BUCKET = "dsi-hvr-poc"
DESTINATION_PREFIX = "archive/"
COPY_ONLY = False

s3_client = boto3.client("s3")

paginator = s3_client.get_paginator("list_objects_v2")

page_iterator = paginator.paginate(Bucket=SOURCE_BUCKET, Prefix=SOURCE_BUCKET_PREFIX)

counter = 0
# Loop through the pages
for page in page_iterator:
    # Loop through the files
    for file in page["Contents"]:
        print(file["LastModified"])

import boto3
from datetime import datetime, timedelta, timezone

# see todo below


def S3_move_copy_delete(
    operation,
    age_threshold_days,
    source_bucket,
    source_prefix,
    destination_bucket,
    destination_prefix,
):
    s3_client = boto3.client("s3")

    paginator = s3_client.get_paginator("list_objects_v2")
    page_iterator = paginator.paginate(Bucket=source_bucket, Prefix=source_prefix)

    counter = 0
    # Loop through the pages
    for page in page_iterator:
        # Loop through the files
        objects = []
        for file in page["Contents"]:
            if file["LastModified"] < datetime.now(timezone.utc) - timedelta(
                days=age_threshold_days
            ):
                objects.append({"Key": file["Key"]})
                # todo: use delete_objects boto3 call to delete the object in the objects list.
                if operation.lower() != "delete":
                    print(f"Copying {file['Key']}")
                    Bucket = destination_bucket
                    Key = file["Key"]
                    s3_client.copy_object(
                        Bucket=Bucket,
                        Key=destination_prefix + Key,
                        CopySource={"Bucket": source_bucket, "Key": Key},
                    )

                if operation.lower() != "copy":
                    print(f"Deleting {file['Key']}")
                    s3_client.delete_object(Bucket=source_bucket, Key=file["Key"])

                counter += 1
                print(f"file count: {counter}")
                print()


if __name__ == "__main__":
    SOURCE_BUCKET = "dsi-hvr-poc"
    SOURCE_PREFIX = "archive/"
    DESTINATION_BUCKET = "dsi-hvr-poc"
    DESTINATION_PREFIX = "archive/"
    OPERATION = "delete"  # copy move delete
    AGE_THRESHOLD_DAYS = 0

    S3_move_copy_delete(
        OPERATION,
        AGE_THRESHOLD_DAYS,
        SOURCE_BUCKET,
        SOURCE_PREFIX,
        DESTINATION_BUCKET,
        DESTINATION_PREFIX,
    )

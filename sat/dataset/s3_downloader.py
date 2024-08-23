import os
import boto3

def download_dataset(s3_bucket, num_files):
    s3 = boto3.client('s3')


    s3_objects = s3.list_objects_v2(Bucket=s3_bucket)

    # Initialize variables for pagination
    continuation_token = None
    all_objects = []

    # List all objects in the S3 bucket using pagination
    while True:
        list_kwargs = {'Bucket': s3_bucket}
        if continuation_token:
            list_kwargs['ContinuationToken'] = continuation_token

        response = s3.list_objects_v2(**list_kwargs)
        all_objects.extend(response.get('Contents', []))

        if not response.get('IsTruncated'):  # At the end of the list?
            break

        continuation_token = response.get('NextContinuationToken')

    for obj in all_objects[:num_files]:

        s3_key = obj['Key']
        local_filename = os.path.basename(s3_key)
        s3.download_file(s3_bucket, s3_key, local_filename)




if __name__ == "__main__":
    s3_bucket = "deepai-research-bucket"
    download_dataset(s3_bucket, 10)
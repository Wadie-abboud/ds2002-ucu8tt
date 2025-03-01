import boto3
import urllib.request
import sys

url, bucket, expires = sys.argv[1], sys.argv[2], int(sys.argv[3])
filename = url.split("/")[-1]

urllib.request.urlretrieve(url, filename)

s3 = boto3.client("s3")
s3.upload_file(filename, bucket, filename)

response = s3.generate_presigned_url(
        "get_object",
        Params={"Bucket": bucket, "Key": filename},
        ExpiresIn=expires,
    )

print(f"Presigned URL: {response}")

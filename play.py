import boto3

try:
    session = boto3.Session(
        aws_access_key_id:="AHjdflhah9875a",
        aws_secret_access_key:="halksdfoa876s8df5a8s5df8a",
        region_name="af-south-1",
    )
    s3 = boto3.client("s3")

    resp = s3.get_object(Bucket="my-bucket", Key="my-file.txt")
    with open("/Users/ferdz/Desktop/workshops/output/my-file.txt") as f:
        f.write(resp["Body"])

except Exception as e:
    print(e)

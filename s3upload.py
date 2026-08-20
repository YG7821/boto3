import boto3
s3 = boto3.resource('s3')
s3.meta.client.upload_file(r"C:\Users\Yogita Gupta\Documents\B44\20thAug\s3upload\boto3", 'yogitagupta-devopsbucket', 'hello.txt')

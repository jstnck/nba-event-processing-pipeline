import boto3
import os
import subprocess

# set aws credentials
session = boto3.Session(profile_name='dataeng-final-proj')
s3 = session.client('s3')

# create videos folder if it doesnt exist
try: 
    os.mkdir('./videos') 
except OSError as error: 
    pass  


# get video file(s) from s3, save to local
video_file = 'bbb_sunflower_1080p_60fps_normal.mp4'
s3_bucket_name = os.environ['S3_BUCKET_NAME']

s3.download_file(s3_bucket_name, video_file, './videos/' + video_file)

# start nginx docker container
subprocess.run(["docker-compose", "up"])
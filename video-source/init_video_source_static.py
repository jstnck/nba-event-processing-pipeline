import boto3
import os, subprocess
import ffmpeg_streaming
from ffmpeg_streaming import Formats, Bitrate, Representation, Size


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



s3.download_file(s3_bucket_name, video_file, './nginx-html/videos/video1.mp4')

# start nginx docker container
subprocess.run(["docker-compose", "up"])


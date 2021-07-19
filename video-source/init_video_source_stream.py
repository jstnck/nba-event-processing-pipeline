import boto3
import os, subprocess, shutil
import ffmpeg_streaming
from ffmpeg_streaming import Formats, Bitrate, Representation, Size


# set aws credentials
session = boto3.Session(profile_name='dataeng-final-proj')
s3 = session.client('s3')

# delete video folder if it exists - always run from having the video in an external source
try: 
    shutil.rmtree('./html-stream/videos', ignore_errors=True)
    os.mkdir('./html-stream/videos')     
except OSError as error: 
    print(error)

# start docker - nginx container(s)
# as the rest of this python script adds files to the docker volume, they will 
# be available for the webserver to play
subprocess.run(["docker-compose", "up", "-d"])


# get video file(s) from s3, save to local
# s3_video_file = 'bbb_sunflower_1080p_60fps_normal_sample_10s.mp4'
s3_video_file = 'bbb_sunflower_1080p_60fps_normal.mp4'
bucket_name = os.environ['S3_BUCKET_NAME']
static_file_location = './videos/video1.mp4'
m3u8_file_location = './html-stream/videos/video1_stream.m3u8'

# download file from s3 to local
s3.download_file(bucket_name, s3_video_file, static_file_location)

# load video from local fs using ffmpeg
video = ffmpeg_streaming.input(static_file_location)

# or, load directly from s3
# video = ffmpeg_streaming.input(s3, bucket_name=s3_bucket_name, key=video_file)

# load the file as an hls stream
hls = video.hls(Formats.h264())
# hls.auto_generate_representations()

# set 1080p as only available representation
_1080p = Representation(Size(1920, 1080), Bitrate(4096 * 1024, 320 * 1024))
hls.representations(_1080p)
print("-----begin hls output-----")
hls.output(m3u8_file_location)

# if this is a long video, it will write .ts files that the .m3u8 file puts together in a playlist
# a user visiting the website can start the video playback before the entire mp4 file is converted to 
# a .m3u8 stream.

# the docker-compose file contains a volume mount, so they're accessible to the nginx container as they
# are written


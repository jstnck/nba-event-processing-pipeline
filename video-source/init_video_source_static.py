import boto3
import os, subprocess
import ffmpeg_streaming
from ffmpeg_streaming import Formats, Bitrate, Representation, Size


# set aws credentials
session = boto3.Session(profile_name='dataeng-final-proj')
s3 = session.client('s3')

# create videos folder if it doesnt exist
try: 
    os.mkdir('./nginx-html/videos') 
except OSError as error: 
    pass  


# get video file(s) from s3, save to local
video_file = 'bbb_sunflower_1080p_60fps_normal.mp4'
s3_bucket_name = os.environ['S3_BUCKET_NAME']

video = ffmpeg_streaming.input(s3, bucket_name=s3_bucket_name, key=video_file)


# s3.download_file(s3_bucket_name, video_file, './nginx-html/videos/video1.mp4')

# # convert file from an .mp4 (static video) to .m3u8 (HLS live stream)
# title = "video1"
# load_location = './nginx-html/videos/' + title + '.mp4'
# save_location =  './nginx-html/videos/' + title + '_stream' + '.m3u8'

# video = ffmpeg_streaming.input(load_location)

print('-----------------------------')
hls = video.hls(Formats.h264())
# hls.auto_generate_representations()
_1080p = Representation(Size(1920, 1080), Bitrate(4096 * 1024, 320 * 1024))
hls.representations(_1080p)
hls.output(save_location)
print('-----------------------------')


# start nginx docker container
subprocess.run(["docker-compose", "up"])


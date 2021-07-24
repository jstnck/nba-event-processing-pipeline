# this script creates a virtual display for the browser/webdriver to use
# it then calls ffmpeg to capture the x11 display (on which selenium is running), and segment the recording/video into 
# multiple .mp4 files of (roughly) fixed length

import subprocess
from pyvirtualdisplay import Display

# # create a virtual display - running on headless ubuntu or docker
# disp = Display()
# disp.start()

# display number - will probaly be :0 if no other display

# print("==================================================")
# # print(disp.new_display_var)
# print("==================================================")

# call ffmpeg to start capturing what's displayed on the (fake) display. The display will be running a selenium browser
# 1824x1026 is 95% of 1920x1080 (my display)
ffmpeg_cmd = "ffmpeg -video_size 1824x1026 -framerate 20 -f x11grab -t 25 -i :0.0+10,10 -f stream_segment -segment_time 10 -segment_format_options movflags=+faststart  -segment_list ./data/playlist.m3u8 ./data/out%03d.mp4"
# ffmpeg_cmd = """ffmpeg -video_size 1024x768 -framerate 25 -f x11grab -t 30 -i :0 -f segment -segment_time 10 -segment_format_options movflags=+faststart -segment_list ./data/playlist.m3u8 ./data/out%03d.mp4"""

# segment vs stream_segment

# make this split command more robust to typos
ffmpeg_subprocess = [cmd for cmd in ffmpeg_cmd.split(" ")]

print(ffmpeg_subprocess)

print("==============before popen===================")

subprocess.run(ffmpeg_subprocess)
# subprocess.Popen(ffmpeg_subprocess)

print("==============after popen====================")



# disp.stop()


"""
ffmpeg -video_size 1919x1079 -framerate 20 -f x11grab -t 25 -i :0.0+0,0 -f stream_segment -segment_time 10 -segment_format_options movflags=+faststart -segment_list playlist.m3u8 out%03d.mp4

"""
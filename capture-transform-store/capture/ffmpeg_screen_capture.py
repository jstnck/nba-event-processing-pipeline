# this script creates a virtual display for the browser/webdriver to use
# it then calls ffmpeg to capture the x11 display (on which selenium is running), and segment the recording/video into 
# multiple .mp4 files of (roughly) fixed length

import concurrent.futures
import subprocess, time
from pyvirtualdisplay import Display
from datetime import datetime



def create_virtual_display(width: int = 1920, height: int = 1080):
    """ creates and starts a virtual display. returns the display number (usually :0 if no other display exists)
    as well as the video capture display dimensions 
    we return virtual_display as well so it can be stopped at the end of the script"""

    display_dimensions = (width, height)
    
    # make the video capture area a little smaller than the display size - seems to cause issues if they are exactly the same
    capture_dimensions = str(int(width*.95)) + "x" + str(int(height*.95))

    virtual_display = Display(size=display_dimensions)

    virtual_display.start()

    display_number = virtual_display.new_display_var

    return virtual_display, capture_dimensions, display_number


def capture_screen( 
    display: str, capture_dimensions: str, timeout: int=0, framerate: int=20, segment_time: int=10, output_path: str="/videos" ):
    """ calls a subprocess that runs ffmpeg. ffmpeg will capture the output of the display and save in video segments
    display = display number,  ie ':0'
    video_size is screen/capture dimensions ie '1824x1026' 
    timeout in seconds. if no time out will run until program is interrupted  
    """ 
    
    # ffmpeg_cmd = f"""ffmpeg \
    # -video_size {capture_dimensions} \
    # -framerate {framerate} \
    # -f x11grab \
    # -t {timeout} \
    # -i {display}.0+1,1 \ 
    # -f stream_segment \
    # -segment_time {segment_time} \
    # -segment_format_options movflags=+faststart \
    # -segment_list {output_path}/playlist.m3u8 \
    # {output_path}/out%03d.mp4
    # """
    
    now = datetime.now()
    ts = datetime.timestamp(now)

    ffmpeg_cmd = f"ffmpeg -video_size {capture_dimensions} -framerate {framerate} -f x11grab -t {timeout} -i {display}.0+1,1 -f stream_segment -segment_time {segment_time} -segment_format_options movflags=+faststart -segment_list {output_path}/playlist.m3u8 {output_path}/out%04d_{ts}.mp4"
    
    # logging.info(ffmpeg_cmd)
    p1 = subprocess.run(ffmpeg_cmd, shell=True, capture_output=True, text=True)

    return p1.returncode


if __name__ == "__main__":

    res = capture_screen(display=":0", capture_dimensions="1824x1026", framerate=10, timeout=25, segment_time=8, output_path=".")

    print(res)

"""
NOTES
ffmpeg -video_size 1919x1079 -framerate 20 -f x11grab -t 25 -i :0.0+0,0 -f stream_segment -segment_time 10 -segment_format_options movflags=+faststart -segment_list playlist.m3u8 out%03d.mp4


ffmpeg -video_size 1824x1026 -framerate 20 -f x11grab -t 25 -i :0.0+10,10 -f stream_segment -segment_time 10 -segment_format_options movflags=+faststart  -segment_list ./data/playlist.m3u8 ./data/out%03d.mp4

1824x1026 is 95% of 1920x1080 (my display)


"""
#  Description:


import time, concurrent.futures
import selenium_video
import ffmpeg_screen_capture 
import subprocess
# import logging


# transform needs to be set up first
# time.sleep(60)

# create and start virtual display
virtual_display, capture_dimensions, display_number = ffmpeg_screen_capture.create_virtual_display(width=960, height=720)

capture_time = 60

# test how long the entire process takes
start_time = time.perf_counter()

# source_url = "http://34.231.243.220:8080/"
source_url = "https://time.is"

# logging.info(source_url)

selenium_video.start_video(source_url)


print(display_number)


with concurrent.futures.ThreadPoolExecutor() as executor:
    
    f1 = executor.submit(ffmpeg_screen_capture.capture_screen, display=display_number, capture_dimensions=capture_dimensions, timeout=capture_time)
    # f1 = executor.submit(ffmpeg_screen_capture.capture_screen, display=display_number, capture_dimensions=capture_dimensions, timeout=capture_time, output_path="./")
    f2 = executor.submit(selenium_video.start_video, source_url)    
    # f2 = executor.submit(wait_test, 5)
    print(f1.result())
    print(f2.result())


finish_time = time.perf_counter()
print(f"Finished in {round(finish_time-start_time, 2)} second(s)")

time.sleep(60)

virtual_display.stop()


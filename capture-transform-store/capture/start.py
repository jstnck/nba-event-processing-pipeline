#  Description:


import time, concurrent.futures
import selenium_video
import ffmpeg_screen_capture 



# create and start virtual display
virtual_display, capture_dimensions, display_number = ffmpeg_screen_capture.create_virtual_display()

capture_time = 60

# test how long the entire process takes
start_time = time.perf_counter()

# source_url = "http://34.231.243.220:8080/"
source_url = "https://time.is"

selenium_video.start_video(source_url)

with concurrent.futures.ThreadPoolExecutor() as executor:
    
    f1 = executor.submit(ffmpeg_screen_capture.capture_screen, display_number, capture_dimensions, capture_time)
    f2 = executor.submit(selenium_video.start_video, source_url)    
    # f2 = executor.submit(wait_test, 5)
    print(f1.result())
    print(f2.result())


finish_time = time.perf_counter()
print(f"Finished in {round(finish_time-start_time, 2)} second(s)")

virtual_display.stop()


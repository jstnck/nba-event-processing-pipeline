import subprocess, time
from selenium.webdriver import Firefox
from selenium.webdriver import Chrome

from pyvirtualdisplay import Display

# create a virtual display
disp = Display()
disp.start()
# display is active

# display number
print(disp.new_display_var)

print("set driver")

# subprocess.run(["pwd"])
# subprocess.run(["ls"])

ffmpeg_cmd = """ffmpeg -video_size 1024x768 -framerate 25 -f x11grab -t 30 -i :0 -f segment -segment_time 10 -segment_format_options movflags=+faststart -segment_list ./data/playlist.m3u8 ./data/out%03d.mp4"""

# ffmpeg_subprocess =  "[" + ffmpeg_cmd.replace(" ", "', '") + "]"

ffmpeg_subprocess = [cmd for cmd in ffmpeg_cmd.split(" ")]




print("before popen")


# subprocess.run(ffmpeg_subprocess)
subprocess.Popen(ffmpeg_subprocess)

print("after popen")


driver_path = "/selenium/geckodriver"

log_path = "/selenium/logs/geckodriver.log"

driver = Firefox(executable_path=driver_path, service_log_path=log_path)


print("driver.get")


driver.get("http://3.236.147.184:8081")
driver.save_screenshot("./data/screenshot1.png")


video = driver.find_element_by_id('video')

print("================================= video click ========================")

video.click()

time.sleep(15)

print("================================= after sleep ========================")

print(str(driver.title))
print(str(driver.current_window_handle))


driver.back()

disp.stop()
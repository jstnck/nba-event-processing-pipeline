import subprocess, time
from selenium.webdriver import Firefox
from selenium.webdriver import Chrome

from pyvirtualdisplay import Display

# create a virtual display
disp = Display()
disp.start()
# display is active


print("set driver")

# subprocess.run(["pwd"])
# subprocess.run(["ls"])


driver_path = "/selenium/geckodriver"

log_path = "/selenium/logs/geckodriver.log"

driver = Firefox(executable_path=driver_path, service_log_path=log_path)


print("driver.get")


driver.get("http://3.236.147.184:8080")
driver.save_screenshot("./data/after pageload.png")


video = driver.find_element_by_id('video')

print("================================= video click ========================")

video.click()
driver.save_screenshot("./data/after-click.png")

time.sleep(15)
driver.save_screenshot("./data/after-sleep.png")

print("================================= after sleep ========================")

print(str(driver.title))
print(str(driver.current_window_handle))


driver.back()

from selenium.webdriver import Firefox


def start_video(url):
    """ loads the url, finds the video player, and clicks on it to start playing. """
        
    # create selenium webdriver
    driver_path = "/capture/geckodriver"
    # log_path = "/capture/logs/geckodriver.log"
    driver = Firefox(executable_path=driver_path)

    driver.get(url)

    try:
        video = driver.find_element_by_id('video')

        # start the video by clicking on it
        # TODO -what if its autoplay and clicking it pauses the video?
        video.click()
        # driver.save_screenshot("./data/after-click.png")
    except:
        pass

    return "video started"


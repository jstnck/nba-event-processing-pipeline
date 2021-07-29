from selenium.webdriver import Firefox


def start_video(url):
    """ loads the url, finds the video player, and clicks on it to start playing. """
        
    # create selenium webdriver
    driver_path = "/capture/geckodriver"
    driver = Firefox(executable_path=driver_path)

    driver.maximize_window()

    driver.get(url)
    # driver.save_screenshot("./pageload.png")
    try:
        video = driver.find_element_by_id('video')

        # start the video by clicking on it
        # TODO -what if its autoplay and clicking it pauses the video?
        video.click()
        # driver.save_screenshot("./after-click.png")
    except:
        pass

    return "video started"

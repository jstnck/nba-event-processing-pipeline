docker build -t jstnck/selenium-ffmpeg:0.1 .




docker run --rm -it -v ~/nba-event-processing-pipeline/video-capture:/selenium --net=host -e DISPLAY jstnck/selenium-ffmpeg:0.1 web.py

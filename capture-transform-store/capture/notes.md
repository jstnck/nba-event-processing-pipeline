docker build -t jstnck/selenium-ffmpeg:0.1 .

docker build -t jstnck/capture .



docker run --rm -it -v /home/think/apps/selenium/repo/nba-event-processing-pipeline/video-capture:/selenium --net=host -e DISPLAY jstnck/selenium-ffmpeg:0.1 start.py

docker run --rm -it -v ~/project/nba-event-processing-pipeline/capture-transform-store/capture:/capture --net=host -e DISPLAY capture start.py

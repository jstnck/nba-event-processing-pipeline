docker build -t jstnck/selenium-ffmpeg:0.1 .

docker build -t jstnck/capture:0.1 .



docker run --rm -it -v /home/think/apps/selenium/repo/nba-event-processing-pipeline/video-capture:/selenium --net=host -e DISPLAY jstnck/selenium-ffmpeg:0.1 start.py

docker run --rm -it -v /home/ubuntu/project/nba-event-processing-pipeline/capture-transform-store/capture:/capture -v /home/ubuntu/project/nba-event-processing-pipeline/capture-transform-store/videos:/videos --net=host -e DISPLAY jstnck/capture:0.1 start.py

FROM python:3

RUN apt-get update
RUN apt-get install -y \
    ffmpeg

WORKDIR /transform
ADD . /transform

RUN pip3 install watchdog opencv-python mysql-connector-python


CMD ["monitor_video_directory.py"]
ENTRYPOINT ["python3"]
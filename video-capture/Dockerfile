FROM ubuntu

RUN apt-get update
RUN apt-get install tzdata

RUN apt-get install -y \
    python3-pip \
    x11-apps \
    firefox \
    ffmpeg \
    xvfb \
    xserver-xephyr \
    tigervnc-standalone-server \
    xfonts-base
    # libxcb

RUN useradd -ms /bin/bash user
WORKDIR /selenium
# ADD . /selenium
RUN mkdir /selenium/logs
RUN touch /selenium/logs/geckodriver.log

RUN pip3 install selenium pyvirtualdisplay pillow

RUN chown -R user:user /selenium
RUN chmod 755 /selenium

USER user
# RUN cd /selenium

CMD ["./error.py"]
ENTRYPOINT ["python3"]
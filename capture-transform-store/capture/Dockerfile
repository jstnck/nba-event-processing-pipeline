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
WORKDIR /capture
ADD . /capture
RUN mkdir /capture/logs
RUN mkdir /capture/data

RUN touch /capture/logs/geckodriver.log

RUN pip3 install selenium pyvirtualdisplay pillow

RUN chown -R user:user /capture
RUN chmod 755 /capture

USER user
# RUN cd /capture

CMD ["start.py"]
ENTRYPOINT ["python3"]
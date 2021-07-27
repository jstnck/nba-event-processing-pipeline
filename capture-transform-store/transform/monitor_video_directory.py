
import time, json, os
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
from opencv_processing import create_frame_data
import db


# create connection to the postgres container
db_name = "postgres"
host_ip = "172.16.57.3"
connection = db.create_connection(db_name=db_name, db_host=host_ip)

# monitor the /videos folder for new mp4 files being added by the capture application
patterns = ["*.mp4"]
my_event_handler = PatternMatchingEventHandler(patterns)

# on file creation, run the opencv processor, which stores to postgres
def on_created(event):
    print(f"hey, {event.src_path} has been created!")

    # the watchdog detects the new file creation, before the file is finished copying, which means opencv
    # tries to read a corrupt file. check every 100ms to see if the filesize has stopped increasing
    historical_file_size = -1
    while (historical_file_size != os.path.getsize(event.src_path)):
        historical_file_size = os.path.getsize(event.src_path)
        time.sleep(0.1)

    # call opencv to create frame metadata and save to postgres db
    create_frame_data(event.src_path, connection)


# configure file creation event handler
my_event_handler.on_created = on_created
video_file_path = "./sample_videos"
go_recursively = True
my_observer = Observer()
my_observer.schedule(my_event_handler, video_file_path, recursive=go_recursively)


# start watching for new files
my_observer.start()
print("watching for new mp4 files")
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    my_observer.stop()
    my_observer.join()



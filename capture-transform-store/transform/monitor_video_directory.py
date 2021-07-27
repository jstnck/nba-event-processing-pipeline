import time, json, os, subprocess
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
from opencv_processing import create_frame_data
import db


import logging
logging.basicConfig(level=logging.DEBUG, filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logging.info('This will get logged to a file')

# need the database to be initalized before we can create a connection
# time.sleep(15)

# create connection to the postgres container
db_name = "postgres"
host_ip = "store"
connection = db.create_connection(db_name=db_name, db_host=host_ip)

# monitor the /videos folder for new mp4 files being added by the capture application
patterns = ["*.mp4"]
my_event_handler = PatternMatchingEventHandler(patterns)

# on file creation, run the opencv processor, which stores to postgres
def on_created(event):
    """ when a video file arrives in the shared volume, this function is called """

    # time.sleep(15)
    logging.info(f'called on created - {event.src_path}')
    logging.info(f'file size before wait {os.path.getsize(event.src_path)}')
    # the watchdog detects the new file creation, before the file is finished copying, which means opencv
    # tries to read a corrupt file. check every 100ms to see if the filesize has stopped increasing
    historical_file_size = -1

    # wait for file to start growing    
    while historical_file_size < 500:
        historical_file_size = os.path.getsize(event.src_path)
        time.sleep(0.25)
 
    # wait for file to stop growing
    while (historical_file_size != os.path.getsize(event.src_path)):
        historical_file_size = os.path.getsize(event.src_path)
        logging.info(f'in wait loop, fs: {os.path.getsize(event.src_path)}')
        time.sleep(0.25)

    logging.info(f'file size after wait {os.path.getsize(event.src_path)}')

    logging.info(f'called on created - done waiting')

    # call opencv to create frame metadata and save to postgres db
    create_frame_data(event.src_path, connection)


# configure file creation event handler
my_event_handler.on_created = on_created
video_file_path = "/videos"
go_recursively = True
my_observer = Observer()
my_observer.schedule(my_event_handler, video_file_path, recursive=go_recursively)


p1 = subprocess.run(["ls", "/videos"], capture_output=True, text=True)

logging.info(f"ls /videos : {p1.stdout}")


# start watching for new files
my_observer.start()
logging.info("watching for new mp4 files")
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    my_observer.stop()
    my_observer.join()



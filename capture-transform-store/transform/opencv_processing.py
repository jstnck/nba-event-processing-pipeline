import cv2, json
import numpy as np
from numpy_array_encoder import NumpyArrayEncoder
import db
import logging

import os

def create_frame_data(file_path: str, connection, table: str):
    """ inputs an mp4 video file, creates a opencv VideoCapture object, 
    loops through each frame, converts to a grayscale array, saves frame
    metadata and array data to postgres database """

    file_info = file_path.split("/")
    file_name = file_info[-1]
    print(f"file info: {file_info}")
    print(f"file name: {file_name}")
    print(f"file path: {file_path}")

    print(f'file size before opencv {os.path.getsize(file_path)}')

    cap = cv2.VideoCapture(file_path)

    # frames per second 
    fps = cap.get(cv2.CAP_PROP_FPS)
    logging.info(f"fps: {fps}")

    total_frame_count= int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    logging.info(f"total frame count: {total_frame_count}")

    frame_count = 0
    # process one out of every n frames - skip a %age of frames for performance improvements
    process_nth_frame = 10

    for _ in range(total_frame_count):
        frame_count += 1

        if frame_count % process_nth_frame != 0:
            # skip this frame
            pass
        else:
            print(frame_count)
            # run processing on 1/6th of the frames (60 fps -> 10 fps)
            # Capture frame-by-frame
            ret, frame = cap.read()

            # convert to grayscale        
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # save the 'gray' frame as json encoded string        
            np_data = { "array": gray}
            encoded_np_data = json.dumps(np_data, cls=NumpyArrayEncoder) 

            # add metadata and frame data to a tuple for insertion into postgres
            data_tuple = (file_name, fps, frame_count, encoded_np_data)
            
            # create the insert query structure
            record = ", ".join(["%s"] * len(data_tuple))
            insert_query = (
                f"INSERT INTO {table} (file_name, fps, frame_num, frame_array) VALUES {data_tuple}"
            )

            # insert single frame data into row in postgres db
            db.insert_query(connection, insert_query, record)
            # res = db.insert_query_v(db_connection, insert_query, record)

            # logging.info()


    return "video processed and frame data added to database"




if __name__ == "__main__":
    print('called main')
    test_file_name = "./sample_videos/sample.mp4"

    create_frame_data(test_file_name, 'dbconn')
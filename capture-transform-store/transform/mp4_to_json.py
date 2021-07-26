import cv2
import numpy as np
import time
import json
from json import JSONEncoder

import db

# create connection to the postgres container
db_name = "postgres"
host_ip = "172.16.57.3"
connection = db.create_connection(db_name=db_name, db_host=host_ip)


# open a video file in opencv
file_name = 'sample.mp4'
cap = cv2.VideoCapture('./' + file_name)

# frames per second of video
fps = cap.get(cv2.CAP_PROP_FPS)

total_frame_count= int(cap.get(cv2.CAP_PROP_FRAME_COUNT))


# create a class for np array to json serialization
# source: https://pynative.com/python-serialize-numpy-ndarray-into-json/
class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)


frame_count = 0
start_time = time.perf_counter()

for _ in range(total_frame_count):
    frame_count += 1

    if frame_count % 10 != 0:
        pass
    else:
        print(frame_count)
        # run processing on 1/6th of the frames (60 fps -> 10 fps)
        # Capture frame-by-frame
        ret, frame = cap.read()
    
        # conversion of BGR to grayscale is necessary to apply this operation
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
        np_data = { "array": gray}
        encoded_np_data = json.dumps(np_data, cls=NumpyArrayEncoder) 

        # print("time stamp current frame:",frame_count / fps)


        data_tuple = (file_name, fps, frame_count, encoded_np_data)
        # create the insert query structure
        record = ", ".join(["%s"] * len(data_tuple))
        insert_query = (
            f"INSERT INTO frame_data (file_name, fps, frame_num, frame_data) VALUES {data_tuple}"
        )

        db.insert_query(connection, insert_query, record)

    #  file_name, "fps": fps, "frame_num": frame_count,
finish_time = time.perf_counter()
print(f"Finished in {round(finish_time-start_time, 2)} second(s)")



# frame_count = 0
# # # Loop until the end of the video
# while (cap.isOpened()):
#     frame_count += 1
    
#     if frame_count % 6 != 0:
#         pass
#     else:
#         # run processing on 1/6th of the frames (60 fps -> 10 fps)
#         # Capture frame-by-frame
#         ret, frame = cap.read()
        
    
#         # conversion of BGR to grayscale is necessary to apply this operation
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
#         np_data = { "array": gray}
#         encoded_np_data = json.dumps(np_data, cls=NumpyArrayEncoder) 

#         # print("time stamp current frame:",frame_count / fps)




#         data_tuple = (file_name, fps, frame_count, encoded_np_data)
#         # create the insert query structure
#         record = ", ".join(["%s"] * len(data_tuple))
#         insert_query = (
#             f"INSERT INTO frame_data (file_name, fps, frame_num, frame_data) VALUES {data_tuple}"
#         )

#         db.insert_query(connection, insert_query, record)

#     #  file_name, "fps": fps, "frame_num": frame_count,
    
    
    
    # cv2.imshow('gray', gray)
    # # define q as the exit button
    # if cv2.waitKey(25) & 0xFF == ord('q'):
    #     break
 

# # release the video capture object
# cap.release()
# # Closes all the windows currently opened.
# cv2.destroyAllWindows()



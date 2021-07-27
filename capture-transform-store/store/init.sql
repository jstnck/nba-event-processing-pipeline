CREATE TABLE frame_data (
    id SERIAL,
    file_name VARCHAR(255),
    fps INT,
    frame_num INT,
    frame_data JSON,
    PRIMARY KEY (file_name, frame_num)
)
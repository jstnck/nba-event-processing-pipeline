CREATE TABLE frame_data (
    id SERIAL,
    file_name VARCHAR(255),
    fps INT,
    frame_num INT,
    frame_array JSONB,
    PRIMARY KEY (file_name, frame_num)
)
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE frame_data (
    id uuid DEFAULT uuid_generate_v4 (),
    file_name VARCHAR(255),
    fps INT,
    frame_num INT,
    frame_array JSONB,
    PRIMARY KEY (file_name, frame_num)
);
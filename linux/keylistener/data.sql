-- create table
CREATE TABLE logger (
	id INT(15) NOT NULL PRIMARY KEY AUTO_INCREMENT,
    uid VARCHAR(20) NOT NULL,
    insert_time DATETIME NOT NULL DEFAULT NOW(),
    modify_time DATETIME,
    left_mouse INT(15) NOT NULL,
    right_mouse INT(15) NOT NULL,
    middle_mouse INT(15) NOT NULL,
    mouse_speed FLOAT(12, 2),
    mouse_distance FLOAT(12, 2) NOT NULL,
    click_position TEXT,
    
    key_stroke INT(15) NOT NULL,
    key_speed FLOAT(12, 2),
    key_map TEXT,
    
    ip CHAR(20),
    mac CHAR(20)
);

DESC logger;

-- INSERT
INSERT INTO logger 
(uid, left_mouse, right_mouse, middle_mouse, mouse_speed, mouse_distance, click_position, key_stroke, key_speed, key_map, ip, mac)
VALUES
('zk4', 2, 2, 2, 12.44, 144.33, '{[12, 34], [123, 444]}', 44, 23.44, '{[\'a\': 5], [\'b\': 4]}', '127.0.0.1', 'ddddddddddd');

-- FindALl
SELECT * FROM devicelogger.logger;

-- FindLast
select left_mouse, right_mouse, middle_mouse, mouse_distance, key_stroke from logger where id=(select max(id) from logger);



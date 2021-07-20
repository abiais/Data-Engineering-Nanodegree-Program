# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS times"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays 
( 
    songplay_id serial NOT NULL PRIMARY KEY, 
    start_time timestamp without time zone NOT NULL, 
    user_id int NOT NULL, 
    level text, 
    song_id text, 
    artist_id text, 
    session_id int, 
    location text, 
    user_agent text 
);
""")

user_table_create = (""" 
CREATE TABLE IF NOT EXISTS users 
( 
    user_id int NOT NULL PRIMARY KEY, 
    first_name text, 
    last_name text, 
    gender text, 
    level text 
);
""")

song_table_create = (""" 
CREATE TABLE IF NOT EXISTS songs 
( 
     song_id text NOT NULL PRIMARY KEY, 
     title text, 
     artist_id text, 
     year int, 
     duration numeric 
); 
""")

artist_table_create = (""" 
CREATE TABLE IF NOT EXISTS artists 
( 
     artist_id text NOT NULL PRIMARY KEY, 
     name text, 
     location text, 
     latitude numeric, 
     longitude numeric 
); 
""")

time_table_create = (""" 
CREATE TABLE IF NOT EXISTS times 
( 
     start_time timestamp without time zone NOT NULL PRIMARY KEY, 
     hour int, 
     day int, 
     week int, 
     month int, 
     year int, 
     weekday int 
); 
""")

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplays 
(
    start_time,
    user_id,
    level,
    song_id,
    artist_id,
    session_id,
    location,
    user_agent
)
    VALUES 
(
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s
)
""")

user_table_insert = ("""
INSERT INTO users 
(
    user_id,
    first_name,
    last_name,
    gender,
    level
) 
VALUES 
(
    %s,
    %s,
    %s,
    %s,
    %s
) 
ON CONFLICT 
    ON CONSTRAINT users_pkey DO UPDATE SET 
        first_name = EXCLUDED.first_name,
        last_name = EXCLUDED.last_name,
        gender = EXCLUDED.gender,
        level = EXCLUDED.level
""")

song_table_insert = ("""
INSERT INTO songs 
(
    song_id, 
    title,
    artist_id,
    year,
    duration
) 
VALUES 
(
    %s,
    %s,
    %s,
    %s,
    %s
) 
ON CONFLICT ON CONSTRAINT 
    songs_pkey DO UPDATE SET 
        title = EXCLUDED.title,
        artist_id = EXCLUDED.artist_id,
        year = EXCLUDED.year,
        duration = EXCLUDED.duration
""")

artist_table_insert = ("""
INSERT INTO artists 
(
    artist_id,
    name,
    location,
    latitude,
    longitude
) 
VALUES 
(
    %s,
    %s,
    %s,
    %s,
    %s
    ) 
ON CONFLICT ON CONSTRAINT artists_pkey DO UPDATE SET 
    name = EXCLUDED.name,
    location = EXCLUDED.location,
    latitude = EXCLUDED.latitude,
    longitude = EXCLUDED.longitude
""")

time_table_insert = ("""
INSERT INTO times 
(
    start_time,
    hour,
    day,
    week,
    month,
    year,
    weekday
) 
VALUES 
(
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s
) 
ON CONFLICT ON CONSTRAINT times_pkey DO NOTHING
""")

# FIND SONGS

song_select =  ("""
SELECT 
    s.song_id,
    s.artist_id 
FROM 
    songs s 
INNER JOIN 
    artists a 
    ON s.artist_id=a.artist_id 
WHERE 
    s.title=%s 
    and a.name=%s 
    and s.duration=%s
""") 

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
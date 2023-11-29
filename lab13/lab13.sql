.read data.sql


CREATE TABLE bluedog AS
  SELECT color, pet FROM students WHERE color = "blue" AND pet = "dog";

CREATE TABLE bluedog_songs AS
  SELECT color, pet, song FROM students WHERE color = "blue" AND pet = "dog";


CREATE TABLE smallest_int_having AS
  SELECT time, smallest 
    FROM students 
    GROUP BY smallest 
    HAVING count(*) < 2;


CREATE TABLE matchmaker AS
  SELECT first.pet, first.song, first.color, second.color
    FROM students as first, students as second
    WHERE first.time != second.time AND
          first.pet = second.pet AND
          first.song = second.song;



CREATE TABLE sevens AS
  SELECT students.seven 
    FROM students, numbers
    WHERE students.time = numbers.time 
          AND numbers.'7' = 'True' 
          AND students.smallest <= 7;

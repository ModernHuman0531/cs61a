.read data.sql


CREATE TABLE bluedog AS
  SELECT color, pet from from students
    where color = 'blue' and pet = 'dog';

CREATE TABLE bluedog_songs AS
  SELECT color, pet, song from students
    where color = 'blue' and 'dog';


CREATE TABLE smallest_int AS
  SELECT time, smallest from students
    where smallest > 2 and order by smallest linit = 20;


CREATE TABLE matchmaker AS
  SELECT a.color, a.music, a.pet, b.color
    from students as a, students as b
      where a.music = b.music and a.pet = b,pet and a.time < b.time;


CREATE TABLE sevens AS
  SELECT a.seven from students as a, numbers as b 
    where a.time = b.time and a.number = 7 and b.'7' = 'True'


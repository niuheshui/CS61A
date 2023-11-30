CREATE TABLE parents AS
  SELECT "abraham" AS parent, "barack" AS child UNION
  SELECT "abraham"          , "clinton"         UNION
  SELECT "delano"           , "herbert"         UNION
  SELECT "fillmore"         , "abraham"         UNION
  SELECT "fillmore"         , "delano"          UNION
  SELECT "fillmore"         , "grover"          UNION
  SELECT "eisenhower"       , "fillmore";

CREATE TABLE dogs AS
  SELECT "abraham" AS name, "long" AS fur, 26 AS height UNION
  SELECT "barack"         , "short"      , 52           UNION
  SELECT "clinton"        , "long"       , 47           UNION
  SELECT "delano"         , "long"       , 46           UNION
  SELECT "eisenhower"     , "short"      , 35           UNION
  SELECT "fillmore"       , "curly"      , 32           UNION
  SELECT "grover"         , "short"      , 28           UNION
  SELECT "herbert"        , "curly"      , 31;

CREATE TABLE sizes AS
  SELECT "toy" AS size, 24 AS min, 28 AS max UNION
  SELECT "mini"       , 28       , 35        UNION
  SELECT "medium"     , 35       , 45        UNION
  SELECT "standard"   , 45       , 60;


-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
  SELECT parents.child
    FROM dogs, parents
    WHERE dogs.name = parents.parent
    ORDER BY dogs.height DESC;



-- The size of each dog
CREATE TABLE size_of_dogs AS
    SELECT dogs.name, sizes.size
      FROM dogs, sizes
      WHERE dogs.height > sizes.min 
        AND dogs.height <= sizes.max;



-- filling out this helper table is optional
create TABLE siblings AS
  SELECT a.parent AS parent, a.child AS child1, b.child AS child2
    FROM parents AS a, parents AS b
    WHERE a.parent = b.parent 
      AND a.child < b.child;

-- sentences about siblings that are the same size
create table sentences as
  SELECT "The two siblings, " || s1.name || " and " || s2.name || ", have the same size: " || s1.size 
    FROM siblings AS ss, size_of_dogs AS s1, size_of_dogs AS s2 
    WHERE ss.child1 = s1.name 
      AND ss.child2 = s2.name 
      AND s1.size = s2.size;


-- height range for each fur type where all of the heights differ by no more than 30% from the average height
create table low_variance as
  select "replace this line with your solution";


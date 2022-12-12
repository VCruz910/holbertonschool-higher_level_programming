-- Cities of California
-- Lists records in a database
SELECT id, name
FROM cities
WHERE state_id = (
  SELECT id
  FROM states
  WHERE name = "California");

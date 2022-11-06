-- Cities by States
-- List records of a table
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id;

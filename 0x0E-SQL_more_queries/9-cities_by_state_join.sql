-- 9. Cities by States
-- Write a script that lists all cities contained in the database hbtn_0d_usa.
SELECT cities.id, cities.name, states.name FROM state INNER JOIN cities ON state.id = cities.state_id ORDER BY cities.id ASC;

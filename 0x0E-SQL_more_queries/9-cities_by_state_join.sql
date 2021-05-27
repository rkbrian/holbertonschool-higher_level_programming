-- 9. Cities by States
-- Write a script that lists all cities contained in the database hbtn_0d_usa.
SELECT cities.id, cities.name, states.name WHERE state.id = cities.state_id ORDER BY cities.id ASC;

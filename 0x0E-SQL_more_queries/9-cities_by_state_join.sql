-- lists all cities contained in the database

SELECT * FROM cities JOIN states ON cities.state_id=states.id ORDER BY id;

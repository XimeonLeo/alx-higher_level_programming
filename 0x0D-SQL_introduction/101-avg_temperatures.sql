-- displays the average temperature (Fahrenheit) by city
-- ordered by temperature (descending).
-- In order to import into a database
-- curl "<link to what you want to import>" -s | mysql -uroot -p <name_of_database>
SELECT city, AVG(value) AS avg_temp FROM temperatures
GROUP BY city ORDER by avg_temp DESC

#--- WRITE YOUR CODE FOR TASK 8-1 ---
%%sql
SELECT name, votes, rating
FROM zomato
WHERE type = 'Delivery'
ORDER BY votes DESC
LIMIT 5;

%%sql
SELECT name, rating, location, type
FROM zomato
WHERE location = 'Banashankari' AND type = 'Delivery'
ORDER BY rating DESC
LIMIT 5;

%%sql
SELECT
  (SELECT rating
   FROM zomato
   WHERE location = 'Indiranagar'
   ORDER BY approx_cost ASC
   LIMIT 1) AS rating1,

  (SELECT rating
   FROM zomato
   WHERE location = 'Indiranagar'
   ORDER BY approx_cost DESC
   LIMIT 1) AS rating2;

%%sql
SELECT type,
COUNT(type) AS number_of_restaurants,
SUM(votes) AS total_votes,
AVG(rating) AS avg_rating
FROM zomato
GROUP BY type
ORDER BY total_votes DESC
LIMIT 10
OFFSET 1;

%%sql
SELECT name, dish_liked, rating, votes
FROM zomato
WHERE online_order = 'Yes' AND type = 'Delivery'
ORDER BY rating DESC, votes DESC
LIMIT 1;

%%sql
SELECT name, online_order, rating, votes
FROM zomato
WHERE rating >= 3 AND votes >= 150 AND online_order = 'No'
ORDER BY votes DESC
LIMIT 15;
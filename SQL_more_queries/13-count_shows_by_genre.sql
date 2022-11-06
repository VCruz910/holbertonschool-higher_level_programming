-- Number of shows by genre
-- Imports database dump
SELECT tv_shows.title AS genre, COUNT(tv_show_genres.genre_id) AS number_of_shows
FROM tv_shows
JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_show_genres.genre_id
ORDER BY number_of_shows DESC, tv_genres.id ASC;

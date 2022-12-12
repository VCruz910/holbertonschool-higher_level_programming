<<<<<<< HEAD
-- Only Comedy
-- Imports database dump
SELECT tv_shows.title
FROM tv_shows
JOIN tv_show_genres
ON tv_show_genres.show_id = tv_shows.id
JOIN tv_genres
ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_genres.name = "Comedy"
ORDER BY tv_shows.title;
=======
-- Lists shows by genre
-- Imports database dump
SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_show_genres.show_id = tv_shows.id
LEFT JOIN tv_genres
ON tv_genres.id = tv_show_genres.genre_id
ORDER BY tv_shows.title, tv_genres.name;
>>>>>>> b0dc061a3c03c00e74efb8781133221b2d9ce949

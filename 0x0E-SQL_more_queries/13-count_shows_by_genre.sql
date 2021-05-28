-- 13. Number of shows by genre
-- Write a script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT tv_genres.name AS genre
    tv_shows_genres.genre_id COUNT(*) AS number_of_shows
    FROM tv_genres INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
    ORDER BY number_of_shows DESC, genre ASC;
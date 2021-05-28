-- 13. Number of shows by genre
-- Write a script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT tv_show_genres.name AS genre
    
    FROM tv_shows LEFT JOIN tv_show_genres
    ON tv_shows.id = tv_show_genres.show_id ORDER BY tv_shows.title ASC,
    tv_show_genres.genre_id ASC;
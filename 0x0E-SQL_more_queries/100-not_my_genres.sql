-- 17. Not my genre
-- Write a script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
SELECT tv_genres.name FROM tv_genres LEFT JOIN
    (tv_shows RIGHT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id)
    ON tv_genres.id = tv_show_genres.genre_id AND tv_shows.title = 'Dexter'
    WHERE tv_shows.title IS NULL
    ORDER BY tv_genres.name ASC;
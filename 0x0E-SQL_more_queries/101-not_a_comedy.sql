-- 18. No Comedy tonight!
-- Write a script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
SELECT tv_shows.title FROM tv_genres RIGHT JOIN
    (tv_shows FULL OUTER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id)
    ON tv_genres.id = tv_show_genres.genre_id AND tv_genres.name = 'Comedy'
    WHERE tv_genres.name IS NULL
    ORDER BY tv_shows.title ASC;
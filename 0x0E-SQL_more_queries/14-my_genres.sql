-- 14. My genres
-- Write a script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
SELECT tv_genres.name FROM tv_shows INNER JOIN tv_show_genres ON tv_shows.title = "Dexter"
    LEFT JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
    ORDER BY tv_genres.name ASC

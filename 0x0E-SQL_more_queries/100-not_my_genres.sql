-- uses the hbtn_0d_tvshows DB to list all genres not linked to the show, Dexter
SELECT name FROM tv_genres
WHERE id NOT IN (
	SELECT DISTINCT tv__show_genre_id
	FROM tv_show_genres
	JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
	WHERE tv_shows.title = 'Dexter'
)
ORDER BY  name ASC;

import pandas as pd

def movie_rating(movies: pd.DataFrame, users: pd.DataFrame, movie_rating: pd.DataFrame) -> pd.DataFrame:
    
    user_ratings = users.merge(movie_rating, on="user_id")

    count_p_user = user_ratings.groupby("name").size().reset_index(name="total_ratings")

    top_user = count_p_user.sort_values(
        by=["total_ratings", "name"],
        ascending=[False, True]
    ).head(1)[["name"]].rename(columns={"name": "results"})

    ratings_feb = movie_rating[
        (movie_rating["created_at"] >= "2020-02-01") &
        (movie_rating["created_at"] <= "2020-02-29")
    ]

    ratings = ratings_feb.merge(movies, on="movie_id")

    avg_r_p_movie = ratings.groupby(["movie_id", "title"])["rating"].mean().reset_index(name="avg_rating")

    top_movie = avg_r_p_movie.sort_values(
        by=["avg_rating", "title"],
        ascending=[False, True]
    ).head(1)[["title"]].rename(columns={"title": "results"})

    final = pd.concat([top_user, top_movie], ignore_index=True)

    return final
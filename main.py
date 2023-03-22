import random

cut_off = 1

m_id = "id"
m_name = "name"
m_ratings = "ratings"


class Movie:
    def __init__(self, identifier, name, ratings):
        self.id_ = identifier
        self.name = name
        self.ratings = ratings
        self.average_rating = self.get_average_rating()

    def get_average_rating(self):
        return sum(self.ratings) / len(self.ratings)


class MovieLibrary:
    def __init__(self, movie_data: list[dict]):

        self.movies = []

        for movie_datum in movie_data:
            movie = Movie(
                identifier=movie_datum[m_id],
                name=movie_datum[m_name],
                ratings=movie_datum[m_ratings],
            )
            self.movies.append(movie)

    def print_movies_rated_at_least(self, cutoff: int):
        good_movies_str = "Movies with {} stars and higher \n".format(cutoff)
        count = 0
        for movie in self.movies:

            if movie.average_rating is None:
                continue

            if movie.average_rating > cut_off:
                count += 1
                good_movies_str += "{}. {} - {} stars\n".format(count, movie.name, movie.average_rating)

        if count == 0:
            good_movies_str = "There are no good movies"

        print(good_movies_str)

    def feeling_lucky(self):
        print("Your lucky movie is: {}🎉:)".format(random.choice(self.movies).name))


sample_movie_data = [
    {m_id: 4, m_name: "A Good Day", m_ratings: [5, 4, 4, 3]},
    {m_id: 5, m_name: "Guardians of the Giant's Castle", m_ratings: [4, 2, 3]},
    {m_id: 6, m_name: "The Train", m_ratings: None},
    {m_id: 7, m_name: "Frying Machine", m_ratings: []}
]

library = MovieLibrary(sample_movie_data)
library.print_movies_rated_at_least(5)
# library.feeling_lucky()

# 3) შექმენი კლასი Movie, რომელსაც ექნება: title, rating, year, შექმენი 3 ფილმი და დაბეჭდე მხოლოდ  ის ფილმები, რომელთა რეიტინგი 8-ზე მეტია.

class Movie:
    def __init__(self, title, rating, year):
        self.title = title
        self.rating = rating
        self.year = year

    def print_rating(self):
        if self.rating > 8:
            return self.title


movie1 = Movie('Gone Girl', 10.0, 2018)
movie2 = Movie('Fight Club', 8.5, 2007)
movie3 = Movie('The Last Samurai', 7.9, 2005)

print(movie1.print_rating())
print(movie2.print_rating())
print(movie3.print_rating())
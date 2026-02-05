# 1) შექმენი კლასი Player: რომელსაც ექნება name, score, level. შექმენი 3 მოთამაშე და დაბეჭდე: რომელი მოთამაშეა ყველაზე მაღალი score-ით

class Player():
    def __init__(self, name, score, level):
        self.name = name;
        self.score = score;
        self.level = level;


player1 = Player('P1', 1200, 120)
player2 = Player('P2', 1340, 130)
player3 = Player('P3', 890, 80)

players_lst = [player1.score, player2.score, player3.score]

print(f'{player1.name} has the biggest score: {player1.score}' if player1.score == max(players_lst) else f'{player2.name} has the biggest score: {player2.score}' if player2.score == max(players_lst) else f'{player3.name} has the biggest score: {player3.score}')
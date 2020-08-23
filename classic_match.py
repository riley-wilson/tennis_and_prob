import numpy as np
import matplotlib.pyplot as plt




class Match:

    def __init__(self, p1): #sets up relevant variables. only takes the probability of player1 winning a point.
        self.p1prob = p1
        self.player1_points = 0
        self.player2_points = 0
        self.game_score = [0,0]
        self.set_score = [0,0]
        self.player1_record = []
        self.player2_record = []

    def play_point(self): #plays a single point
        prob = np.random.random()

        if prob < self.p1prob:
            self.player1_points = self.player1_points+1
        else:
            self.player2_points = self.player2_points+1


    def play_game(self): #plays a full, ad game


        while True:
            self.play_point()
            self.player1_record.append(self.player1_points)
            self.player2_record.append(self.player2_points)

            #print('test')
            if self.player1_points >= 4 and self.player1_points >= self.player2_points +2:
                self.game_score[0] +=1
                self.player1_points = 0
                self.player2_points = 0
                break
            if self.player2_points >=4 and self.player2_points >= self.player1_points +2:
                self.game_score[1] +=1
                self.player1_points = 0
                self.player2_points = 0
                break


    def play_set(self): #plays a set with 7 point tiebreak.

        while True:
            self.play_game()

            if self.game_score[0] == 6 and self.game_score[1] ==6:
                champ = self.play_tiebreaker()
                self.game_score[champ] +=1
                self.set_score[champ] +=1
                break

            if self.game_score[0] >= 6 and self.game_score[0] >= self.game_score[1] +2:
                self.set_score[0] +=1
                break
            if self.game_score[1] >= 6 and self.game_score[1] >= self.game_score[0] +2:
                self.set_score[1] += 1
                break




    def play_3match(self): #plays a 3-setter with a 7-point tiebreaker. Returns 0 if p1 wins and 1 if p2 does.

        winner = 0
        while True:
            self.play_set()
            self.game_score = [0,0]
            if self.set_score[0] == 2:
                winner = 0
                break
            if self.set_score[1] == 2:
                winner =1
                break
        return winner


    def play_tiebreaker(self):

        while True:
            self.play_point()
            #testing
            #print(self.player1_points, self.player2_points)

            if self.player1_points >=7 and self.player1_points >= self.player2_points +2:
                return 0
            if self.player2_points >= 7 and self.player2_points >= self.player1_points +2:
                return 1



###end of class definition



def run_sim(p, n):

    results = []

    for i in range(n):
        m = Match(p)
        results.append(m.play_3match())

    average = np.mean(results)

    return average

def run_sim_range_classic(start, end, n):
    x = np.linspace(start, end, 50)
    output = []
    for i in x:
        output.append(1-run_sim(i,n))

    return output


        #print(self.set_score)

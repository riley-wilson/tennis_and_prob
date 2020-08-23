import numpy as np
import matplotlib.pyplot as plt

#class and functions needed for the choke_match simulation.


class Match_Choke:

    def __init__(self, p1, pc): #sets up relevant variables. only takes the probability of player1 winning a point.
        self.p1prob = p1
        self.p1choke_prob = pc
        self.player1_points = 0
        self.player2_points = 0
        self.game_score = [0,0]
        self.set_score = [0,0]
        self.player1_record = []
        self.player2_record = []



    def play_3match_choke(self): #plays a 3-setter with a 7-point tiebreaker. Returns 0 if p1 wins and 1 if p2 does.

        winner = 0
        while True:
            self.play_set_choke()
            self.game_score = [0,0]
            if self.set_score[0] == 2:
                winner = 0
                break
            if self.set_score[1] == 2:
                winner =1
                break

        return winner


    def play_tiebreaker_choke(self):

        while True:


            self.play_point_choke_tiebreaker()
            #testing
            #print(self.player1_points, self.player2_points)

            if self.player1_points >=7 and self.player1_points >= self.player2_points +2:
                return 0
            if self.player2_points >= 7 and self.player2_points >= self.player1_points +2:
                return 1


    def play_point_choke(self):

        prob = np.random.random()
        #print('test in play_point_choke')
        if self.player1_points == 3 and self.player2_points <=2:
            if prob < self.p1choke_prob:
                self.player1_points +=1
            else:
                self.player2_points +=1

        elif self.player1_points == self.player2_points +1 and self.player1_points >=3:
             if prob < self.p1choke_prob:
                 self.player1_points +=1
             else:
                 self.player2_points +=1

        else:
            if prob < self.p1prob:
                self.player1_points = self.player1_points+1
            else:
                self.player2_points = self.player2_points+1



    def play_game_choke(self):

        while True:
            self.play_point_choke()
            self.player1_record.append(self.player1_points)
            self.player2_record.append(self.player2_points)

            #testing
            #print(self.player1_points, self.player2_points)

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

    def play_set_choke(self):

        while True:

            self.play_game_choke()


            if self.game_score[0] == 6 and self.game_score[1] ==6:
                champ = self.play_tiebreaker_choke()
                self.game_score[champ] +=1
                self.set_score[champ] +=1
                break

            if self.game_score[0] >= 6 and self.game_score[0] >= self.game_score[1] +2:
                self.set_score[0] +=1
                break
            if self.game_score[1] >= 6 and self.game_score[1] >= self.game_score[0] +2:
                self.set_score[1] += 1
                break

        #testing
        #print('game score:', self.game_score)

    def play_point_choke_tiebreaker(self):

        prob = np.random.random()
        #testing
        #print('test in play_point_choke_tiebreaker')
        if self.player1_points == 6 and self.player2_points <=5:
            if prob < self.p1choke_prob:
                self.player1_points +=1
            else:
                self.player2_points +=1

        elif self.player1_points == self.player2_points +1 and self.player1_points >=6:
             if prob < self.p1choke_prob:
                 self.player1_points +=1
             else:
                 self.player2_points +=1

        else:
            if prob < self.p1prob:
                self.player1_points = self.player1_points+1
            else:
                self.player2_points = self.player2_points+1



def run_sim_choke(p, pc, n):

    results = []

    for i in range(n):
        m = Match_Choke(p, pc)
        results.append(m.play_3match_choke())

    average = np.mean(results)

    return average

def run_sim_range_choke(pc, start, end, n): #runs the simulation over a range of p values for a fixed pc.
    x = np.linspace(start, end, 50)
    output = []
    for i in x:
        output.append(1-run_sim_choke(i,pc,n))

    return output

import numpy as np
import matplotlib.pyplot as plt

#class and functions for the streaky match. 


class Match_Switch:

    def __init__(self, p1, p2): #sets up relevant variables. only takes the probability of player1 winning a point.
        self.p1prob = p1
        self.stay_prob = p2
        self.player1_points = 0
        self.player2_points = 0
        self.game_score = [0,0]
        self.set_score = [0,0]
        self.player1_record = []
        self.player2_record = []
        self.last_winner = 0

        #to have the first point be random, I'm keeping play_point_first the same.

    def play_point_first(self): #plays a single point

        prob = np.random.random()

        if prob < self.p1prob:
            self.player1_points = self.player1_points+1
            self.last_winner = 1
        else:
            self.player2_points = self.player2_points+1
            self.last_winner = 2



    def play_point_nonfirst(self):

        prob = np.random.random()

        if self.last_winner == 1:
            if prob < self.stay_prob:
                self.player1_points = self.player1_points+1
                self.last_winner = 1
            else:
                self.player2_points = self.player2_points+1
                self.last_winner = 2
        elif self.last_winner == 2:
            if prob < self.stay_prob:
                self.player2_points = self.player2_points+1
                self.last_winner = 2
            else:
                self.player1_points = self.player1_points +1
                self.last_winner = 1


    def play_game(self): #plays a full, ad game

        self.last_winner = 0

        self.play_point_first()
        self.player1_record.append(self.player1_points)
        self.player2_record.append(self.player2_points)

        #testing
        #print('this is the score after the first point is played: ', self.player1_points, self.player2_points)
        while True:
            self.play_point_nonfirst()

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
            #testing
            #print('score: ', self.player1_points, self.player2_points)


    def play_set(self): #plays a set with 7 point tiebreak. #I will need to change the tiebreak to coincide with staying or switching.

        while True:
            self.play_game()
            #print('this is the game score', self.game_score)
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

            #testing
            #print('game score: ', self.game_score)
        #print('final set score: ', self.game_score)


    def play_3match(self): #plays a 3-setter with a 7-point tiebreaker. Returns 0 if p1 wins and 1 if p2 does.

        winner = 0
        while True:
            self.play_set()
            #print('THIS IS THE SET SCORE ', self.set_score)
            self.game_score = [0,0]

            if self.set_score[0] == 2:
                winner = 0
                #testing
                #print('PLAYER 1 WINS MATCH')
                break
            elif self.set_score[1] == 2:
                winner =1
                #testing
                #print('PLAYER 2 WINS MATCH ')
                break
        return winner


    def play_tiebreaker(self):
        self.last_winner = 0
        self.play_point_first()

        while True:
            self.play_point_nonfirst()
            #testing
            #print(self.player1_points, self.player2_points)

            if self.player1_points >=7 and self.player1_points >= self.player2_points +2:
                return 0
            if self.player2_points >= 7 and self.player2_points >= self.player1_points +2:
                return 1



###end of class defintion



#def run_sim_switchy(p, p1, n):
#    results = []
#
#    for i in range(n):
#        m = Match_Switch(p,p1)
#        results.append(m.play_3match())
#
#    return 1-np.mean(results)

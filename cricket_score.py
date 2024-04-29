#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 21:20:09 2024

@author: vivekchaithayamekarthi
"""

#considering two teams for  a match 
team_1=input('enter the name of first team=')
team_2=input('enter the name of second team=') 

#introducing two variables for scoring of two teams
total_runs_team1 = 0
total_runs_team2 = 0

#accounting total wickets dropped by two teams
wickets_1=0
wickets_2=0

#creating a toss function 
def toss_time():
    print('ok then its time to toss') 
    print(f"{team_1} should have to say either heads or tails")
    toss_chosen=input('enter the toss you want=').lower() 
    #importing a random module for toss 
    import random 
    #creating a list "choices"  
    choices=["heads" , "tails"]
    random_choice=random.choice(choices)
    # making the choices as nonlocal 
    global team_1_choose 
    global team_2_choose
    # initially no toss chosen for both the teams 
    team_1_choose=" "
    team_2_choose=" " 
    if random_choice==toss_chosen:
        print(f'yurrah!! {team_1} won the toss')
        # prompting the user to choose either bat or bowl
        team_1_choose=input('What would you like to choose? Bat or Bowl?').lower() 
        if team_1_choose=="bat":
            print(f'{team_1}  is going to bat, all the best')
            print(f'{team_2} is going to bowl, all the best') 
        elif team_1_choose=="bowl":
            print(f'{team_1} is going to bowl, all the best') 
            print(f'{team_2}  is going to bat, all the best') 
    else:
        print(f'{team_1} lost the toss') 
        print(f'yurrah {team_2} won the toss')
        # prompting the user to choose either bat or bowl
        team_2_choose=input('What would you like to choose? Bat or Bowl?').lower() 
        if team_2_choose=="bat":
            print(f'{team_2}  is going to bat, all the best')
            print(f'{team_1} is going to bowl, all the best')
        elif team_2_choose=="bowl": 
            print(f'{team_2} is going to bowl, all the best')
            print(f'{team_1}  is going to bat, all the best')

# creating a first_innings_team function 
# which is only for determining the winner of the match 
def first_innings_team(): 
    # considering team1 as first batting team not as team_1
    # making it as nonlocal
    global team1
    # considering team2 as first batting team not as team_2
    # making it as nonlocal 
    global team2 
    # deciding team1 and team2 by the toss chosen 
    if team_1_choose=="bat" or team_2_choose=="bowl":
        team1=team_1
        team2=team_2
    elif team_1_choose=="bowl" or team_2_choose=="bat":
        team1=team_2 
        team2=team_1
 
# creating a print_scorecard function which displays the score
# for each ball and overs, scorecard, ...are the arguments 
# passed through the funtion  
def print_scorecard(overs,scorecard,batsman_1, batsman_2, batsman_on_strike, bowler):
    print("SCORECARD:") 
    print("Overs:", overs) 
    # the batsman on strike defined by '*' symbol
    # the non-strike batsman has no symbol 
    if batsman_on_strike == batsman_1:
        print("* " + batsman_1 + "'s runs:", scorecard[batsman_1])
        print("  " + batsman_2 + "'s runs:", scorecard[batsman_2])
    else:
        print("  " + batsman_1 + "'s runs:", scorecard[batsman_1])
        print("* " + batsman_2 + "'s runs:", scorecard[batsman_2])
    print("Total Runs:", scorecard['total_runs'])
    print("Wickets:", scorecard['wickets'])
    print("Bowler:", bowler)
    
    
# creating a first_innings function where the total runs 
# of innings gets accumulated 
def first_innings():
    global total_runs_team1 
    global wickets_1
    # defining total number of overs in the match 
    total_overs = 1 
    # defining number of balls per over which is "6" 
    balls_per_over = 6
    # defining current_over and current_ball 
    current_over = 0
    current_ball = 0
    # entering the name of openers 
    batsman_1 = input("Enter name of batsman 1: ")
    batsman_2 = input("Enter name of batsman 2: ")
    batsman_on_strike = batsman_1
    # entering the name of starting bowler 
    starting_bowler = input("Enter name of starting bowler: ")
    bowler = starting_bowler
    # creating a DICTIONARY where we store the data of the 
    # total_runs,wickets, individual scores of batsmen  
    scorecard = {batsman_1: 0, batsman_2: 0, 'total_runs': 0, 'wickets': 0}
    # creating a conditional loop i.e, while loop with 
    # basic conditions of the game 
    while current_over < total_overs and scorecard['wickets'] < 10:
        # initially displaying the scorecard of the innings
        # this scorecard will display for ball to ball
        print_scorecard(current_over, scorecard, batsman_1, batsman_2, batsman_on_strike, bowler)
        # always displaying the remaing balls 
        print(f"{(total_overs-current_over)*6 - (current_ball)} BALLS REMAINING")  
        # prompts the user to enter the outcome of a ball 
        # like 0/1/2/3/4/6/wide/wicket/noball 
        outcome = input("Enter outcome of the ball (0/1/2/3/4/6/wicket/wide/nb): ").lower()
        # displaying a dot ball
        if outcome == "0":
            pass 
        # displaying a single/triple run(s) ball
        elif outcome in ["1", "3"]:
            runs_scored = 1 if outcome == "1" else 3
            scorecard[batsman_on_strike] += runs_scored
            scorecard['total_runs'] += runs_scored
            # changing the strike rotation for 1,3 runs 
            batsman_on_strike = batsman_2 if batsman_on_strike == batsman_1 else batsman_1
         # displaying a double/four/six run(s) ball
        elif outcome in ["2", "4", "6"]:
            runs_scored = 2 if outcome == "2" else 4 if outcome == "4" else 6
            scorecard[batsman_on_strike] += runs_scored
            scorecard['total_runs'] += runs_scored 
            # there is no need of strike rotation 
         # displaying a wicket taken ball
        elif outcome == "wicket":
            scorecard['wickets'] += 1    
            print("Wicket has fallen!") 
            # displaying the score of out batsman 
            if batsman_on_strike==batsman_1:
                print(f"score of {batsman_1} = {scorecard[batsman_1]}")  
            else:
                print(f"score of {batsman_2} = {scorecard[batsman_2]}")  
            # strike rotation whenever wicket takes 
            batsman_on_strike = batsman_2 if batsman_on_strike == batsman_1 else batsman_1
            # prompts the user to enter new batsman name 
            new_batsman = input("Enter name of new batsman: ")
            print("New batsman:", new_batsman)
   # giving new batsman either batsman_1 or batsman_2 position
            if batsman_on_strike==batsman_2: 
                batsman_1=new_batsman
            if batsman_on_strike==batsman_1:
                batsman_2=new_batsman
            # accumulating the score of new batsman as 0
            scorecard[new_batsman] = 0     
        # displaying the wide ball 
        elif outcome=="wide":
            # asking the user for extra runs taken 
            print("how many runs does batsman taken?")
            # entering the runs taken 
            runs=int(input(('enter the runs '))) 
            # adding these extra runs to the score 
            runs_scored=1+runs 
            scorecard['total_runs'] += runs_scored
            # changing the strike rotation for odd runs 
            if runs==1 or runs==3:
                batsman_on_strike = batsman_2 if batsman_on_strike == batsman_1 else batsman_1 
            # not counting the wide ball 
            current_ball -= 1 
        # displaying the noball which is also an extra run 
        elif outcome=="nb": 
            print("how many runs does batsman taken?")   
            runs=int(input(('enter the runs ')))  
            runs_scored=1+runs 
            scorecard['total_runs'] += runs_scored 
            if runs==1 or runs==3:
                batsman_on_strike = batsman_2 if batsman_on_strike == batsman_1 else batsman_1 
            current_ball -= 1 
        # if the input is not proper then asking to re-enter 
        else: 
            print('no such run is possible in cricket') 
            print('please enter again') 
            # ofcourse not counting the ball 
            current_ball -= 1 
 # for every correct ball the number of balls are increasing 
        current_ball += 1
        # after 6 balls the over is completed and making 
        # the current_ball as 0 and also increasing the overs
        if current_ball == balls_per_over:
            current_over += 1
            current_ball = 0
            print(f"{current_over}overs has been completed")
     # prompts the user to enter the bowler for next over
            bowler = input("Enter name of bowler for next over:")
 # changing the strike rotation for completion of each over 
            batsman_on_strike = batsman_2 if batsman_on_strike == batsman_1 else batsman_1
#giving a caution to batting team if they've got down for 10 wickets
        if scorecard['wickets']==9: 
            print('last batsman') 
    print("First innings has been completed")
    print('the second innings is about to start, please stay tune') 
    print("THE FIRST INNINGS SCORE IS :") 
    # displaying the scorecard for each and every ball 
    print_scorecard(total_overs, scorecard, batsman_1, batsman_2, batsman_on_strike, bowler)
    total_runs_team1= scorecard['total_runs'] 
    wickets_1=scorecard['wickets'] 
    print("-------------------------------") 
    
 
# creating the second_innings function 
# mostly all conditions are similar to first_innings  
def second_innings():
    global total_runs_team2
    global wickets_2
    print("second innings is starting ") 
    total_overs = 1
    balls_per_over = 6
    current_over = 0
    current_ball = 0
    batsman_1 = input("Enter name of batsman 1: ")
    batsman_2 = input("Enter name of batsman 2: ")
    batsman_on_strike = batsman_1
    starting_bowler = input("Enter name of starting bowler: ")
    bowler = starting_bowler
    scorecard = {batsman_1: 0, batsman_2: 0, 'total_runs': 0, 'wickets': 0}
    while current_over < total_overs and scorecard['wickets'] < 10:
        print_scorecard(current_over, scorecard, batsman_1, batsman_2, batsman_on_strike, bowler)
    # always displaying the runs required and ball remaining
        print(f"{team2} NEED {total_runs_team1+1-scorecard['total_runs']} RUNS IN {(total_overs-current_over)*6 - (current_ball)}  BALLS") 
        outcome = input("Enter outcome of the ball (0/1/2/3/4/6/wicket/wide/nb): ").lower()
        if outcome == "0":
            pass 
        elif outcome in ["1", "3"]:
            runs_scored = 1 if outcome == "1" else 3
            scorecard[batsman_on_strike] += runs_scored
            scorecard['total_runs'] += runs_scored
            batsman_on_strike = batsman_2 if batsman_on_strike == batsman_1 else batsman_1
        elif outcome in ["2", "4", "6"]:
            runs_scored = 2 if outcome == "2" else 4 if outcome == "4" else 6
            scorecard[batsman_on_strike] += runs_scored
            scorecard['total_runs'] += runs_scored 
        elif outcome == "wicket":
           scorecard['wickets'] += 1
           batsman_on_strike = batsman_2 if batsman_on_strike == batsman_1 else batsman_1
           print("Wicket has fallen!")
           if batsman_on_strike==batsman_1:
               print(f"score of {batsman_1} = {scorecard[batsman_1]}")  
           else:
               print(f"score of {batsman_2} = {scorecard[batsman_2]}")  
           new_batsman = input("Enter name of new batsman: ")
           print("New batsman:", new_batsman)
           if batsman_on_strike==batsman_2: 
               batsman_1=new_batsman
           if batsman_on_strike==batsman_1:
               batsman_2=new_batsman
           scorecard[new_batsman] = 0 
        elif outcome=="wide":
            print("how many runs does batsman taken?")   
            runs=int(input(('enter the runs ')))  
            runs_scored=1+runs 
            scorecard['total_runs'] += runs_scored 
            if runs==1 or runs==3:
                batsman_on_strike = batsman_2 if batsman_on_strike == batsman_1 else batsman_1 
            current_ball -= 1 
        elif outcome=="nb": 
            print("how many runs does batsman taken?")   
            runs=int(input(('enter the runs ')))  
            runs_scored=1+runs 
            scorecard['total_runs'] += runs_scored 
            if runs==1 or runs==3:
                batsman_on_strike = batsman_2 if batsman_on_strike == batsman_1 else batsman_1 
            current_ball -= 1      
        else: 
            print('no such run is possible in cricket') 
            print('please enter again') 
            current_ball -= 1 
        current_ball += 1
        if current_ball == balls_per_over:
            current_over += 1
            current_ball = 0
            print(f"{current_over}overs has been completed")  
            bowler = input("Enter name of bowler for next over:")
            batsman_on_strike = batsman_2 if batsman_on_strike == batsman_1 else batsman_1
        if "wickets"==9:
            print('last batsman') 
            
# if the second batting team scores the runs required in
# less number of balls than required , break the loop    
        if scorecard['total_runs'] >= total_runs_team1+1:
            break
    print("THE SECOND INNINGS SCORE IS :") 
    print_scorecard(total_overs, scorecard, batsman_1, batsman_2, batsman_on_strike, bowler)  
    total_runs_team2= scorecard['total_runs'] 
    wickets_2=scorecard['wickets'] 
    print("-------------------------------") 
    
def determine_winner(): 
    
    # considering the total runs scored by two teams 
    global total_runs_team1 
    global total_runs_team2 
   

    # Compare total runs to determine the winner
    if total_runs_team1 > total_runs_team2:
        print(f"{team1} won by {total_runs_team1-total_runs_team2} runs") 
    elif total_runs_team2 > total_runs_team1:
        print(f"{team2} won by {10-wickets_2} wickets") 
    else:
        print("It's a tie match!")  


# calling all functions to run the code 
toss_time()
first_innings_team()  
first_innings()  
second_innings()     
determine_winner()  
print("----MATCH FINISHED----")      
    
    
    
    
    
    
    
    
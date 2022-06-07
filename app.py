import streamlit as st
import requests
import time


st.set_page_config(
            page_title="On The Pitch - Betting Strategies",
            page_icon="⚽",
            layout="centered", #'wide' or  'centered'
            initial_sidebar_state="auto") #'auto', 'collapsed' or 'expanded'



'''
# On The Pitch
**World Class Footbal Betting Strategies**
'''



#League selection ----------
countries = [
            '',
            'Belgium',
            'Brazil',
            'England',
            'France',
            'Germany',
            'Greece',
            'Italy',
            'Netherlands',
            'Portugal',
            'Scotland',
            'Spain',
            'Turkey'
            ]

league_option = st.selectbox('First, select a football league:', countries)

if league_option != '':
    st.write(f'You have chosen **{league_option}**!')
    '''**Good choice!**'''



#Betting options ----------
bets = [
        '',
        'Home Team Wins',
        'Away Team Wins',
        'Draw',
        'Over 2.5 Goals in the match',
        'Under 2.5 Goals in the match'
        ]

bet_option = st.selectbox('Now. select on what you want to place a bet:', bets)

if bet_option != '':
    st.write(f'You have chosen **{bet_option}**!')
    if bet_option == 'Over 2.5 Goals in the match':
        '''Wow! You think the match will be filled with goals! Cool!'''
    elif bet_option == 'Under 2.5 Goals in the match':
        '''You think the teams won't score much... Ok!'''
    elif bet_option == 'Home Team Wins':
        '''Goooooo Home Team!'''
    elif bet_option == 'Away Team Wins':
        '''Really? You might be right after all!'''
    elif bet_option == 'Draw':
        '''Well, no winners... Maybe you could be the winner!'''



#Getting the odds from the user ----------
odds = st.number_input('Please, inform the odds on your favorite Booking Platform:', value = 0.0)

'''If you're sure of your choices, let's see if we can make some money!'''



#Making a dictionary for the API request ----------
params = {
        'league_option': 1, #league_option,
        'bet_option': 1, #bet_option,
        'odds': odds
            }



if st.button("LET'S GO"):
    '''# Analyzing the data...'''

    #Requesting the information on the API ----------
    #This is the code for the Taxi Fare Model; Update it!
    url = 'http://0.0.0.0:8080/predict'
    response = requests.get(url, params = params).json()

    bar = st.progress(0)
    for i in range(100):
        bar.progress(i + 1)
        time.sleep(0.05)
    '''# DONE!'''
    time.sleep(2)
    '''According to our experts, your chances of geeting a positive result on
    this bet are **statistically significant**!'''
    '''## Go place that bet!'''

    st.write(response)

#st.markdown('# ' + '$' + str(round(response['fare'], 2)))

import streamlit as st
import requests
import time
from datetime import datetime


st.set_page_config(
            page_title="On The Pitch - Betting Strategies",
            page_icon="⚽",
            layout="centered", #'wide' or  'centered'
            initial_sidebar_state="auto") #'auto', 'collapsed' or 'expanded'


# - - - - - - - - - -
# Page Title
# - - - - - - - - - -
'''
# On The Pitch
**World Class Footbal Betting Strategies**
'''

# - - - - - - - - - -
# Division selection
# - - - - - - - - - -
D1 = 0.0
D2 = 0.0
D3 = 0.0
D4 = 0.0

division = [
            '',
            'D1',
            'D2',
            'D3',
            'D4'
            ]

division_option = st.selectbox("First, select the League's Division:", division)

if division_option == 'D1':
    D1 = 1.0
elif division_option == 'D2':
    D2 = 1.0
elif division_option == 'D3':
    D3 = 1.0
elif division_option == 'D4':
    D4 = 1.0


# - - - - - - - - - -
# Betting options
# - - - - - - - - - -
bets = [
        '',
        'Home Team Wins',
        'Away Team Wins',
        'Draw',
        'Over 2.5 Goals in the match',
        'Under 2.5 Goals in the match'
        ]

bet_option = st.selectbox('Now. select on what you want to place a bet:', bets)


# - - - - - - - - - -
# VIG selection (Will be calculated after the button is pushed)
# - - - - - - - - - -
favor_odds = st.number_input('Please, inform the odds in favor of your bet on your favorite Booking Platform:', value = 0.0)
against_odds = st.number_input('Please, inform the odds against your bet on your favorite Booking Platform:', value = 0.0)


# - - - - - - - - - -
# Market consensus
# - - - - - - - - - -
market_consensus = True
#max_odds = st.number_input('Please, inform the maximum odds offered in the market:', value = 0.0)


# - - - - - - - - - -
# Year
# - - - - - - - - - -
year = datetime.now().year - 2019


# - - - - - - - - - -
# Time of the match
# - - - - - - - - - -
after_4_pm = [
                '',
                'Yes',
                'No'
            ]

match_time = st.selectbox('Will the match take place after 4PM?', after_4_pm)

if match_time == 'Yes':
    match_time_after_4_pm = 1.0
    match_time_before_4_pm = 0.0
else:
    match_time_after_4_pm = 0.0
    match_time_before_4_pm = 1.0


# - - - - - - - - - -
# Odds buckets
# - - - - - - - - - -
odds_1_to_1_5 = 0.0
odds_1_5_to_2_0 = 0.0
odds_2_0_to_3 = 0.0
odds_3_to_10 = 0.0

if favor_odds <= 1.5:
    odds_1_to_1_5 = 1.0
elif 1.5 < favor_odds <= 2:
    odds_1_5_to_2_0 = 1.0
elif 2 < favor_odds <= 3:
    odds_2_0_to_3 = 1.0
elif 3 < favor_odds <= 10:
    odds_3_to_10 = 1.0


'''If you're sure of your choices, let's see if we can make some money! 💰'''


if st.button("LET'S GO"):
    '''# Analyzing the data... 📊'''

    #Calculating the VIG Rate
    vig_rate = (1 - (1 / (1/against_odds + 1/favor_odds)))*100
    if vig_rate > 3.2:
        vig_rate = True
    else:
        vig_rate = False

    #Making a dictionary for the API request
    params = {
            'D1': D1,
            'D2': D2,
            'D3': D3,
            'D4': D4,
            'vig_rate': vig_rate,
            'market_consensus': market_consensus,
            'year': int(year),
            'match_time_after_4_pm': match_time_after_4_pm,
            'match_time_before_4_pm': match_time_before_4_pm,
            'odds_1_to_1_5': odds_1_to_1_5,
            'odds_1_5_to_2_0': odds_1_5_to_2_0,
            'odds_2_0_to_3': odds_2_0_to_3,
            'odds_3_to_10': odds_3_to_10
            }

    #Requesting the information on the API
    url = 'https://apionthepitch-o36oj7hgja-uc.a.run.app/predict'
    response = requests.get(url, params = params).json()

    bar = st.progress(0)
    for i in range(100):
        bar.progress(i + 1)
        time.sleep(0.05)

    '''# DONE! 😎'''

    final_prediction = float(response['result'])

    #This 'print' shows the prediction in the Terminal, so we can compare it
    #with the Streamlit text
    print(final_prediction)

    if final_prediction > 0:
        '''According to our experts, your chances of geeting a positive result on
        this bet are **statistically significant**!'''
        '''## Go place that bet! 🤑'''
    elif final_prediction < 0:
        '''According to our experts, your chances of geeting a positive result on
        this bet **aren't statistically significant**!'''
        '''## Do not place that bet! 💩'''

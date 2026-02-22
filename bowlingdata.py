# Author: Elijah Rades
# File: bowlingdata.py
# Purpose: The purpose of this program
# is to find averages of your bowling scores.
# This is read in from my micrsoft excel spreadsheet
# using pandas. Pandas also helps with row/column work
# to find data. 
# With more of my data, I will write additional algorithms to find
# the most optimal ball weight, ball speed, ball entries, etc
# to maximize my bowling score.

# import pandas
import pandas as pd

# never called in main but helpful for testing
def readfile(filename):
    df = pd.read_excel(filename)
    #df = df.to_string()
    #print(df)

# call is commented out in main, helpful for looking
# at data specifics in rows/columns
def getdata(df):

    row = df.iloc[0]
    print(row)
    print()

# print out our all time averages
def print_averages(df):
    stats = {
        "Scratch ": "Scratch Average",
        "Scratch + Hdcp": "Scratch + HandiCap Average",
        "Open Frames": "Open Frames",
        "Spares": "Spares Average",
        "Strikes": "Strikes Average",
        "Split": "Split Average",
        "Split Conversion": "Split Conversion Average",
        "Fouls": "Foul Average",
        "Gutters": "Gutter Ball Average",
        "1st Ball Average": "1st Ball Average Pins Knocked Down",
        "1st Ball Average Speed (m.p.h)": "1st Ball Average Speed",
        "2nd Ball Average Speed MPH": "2nd Ball Average Speed"
    }

    for column in stats:
        mean = df[column].mean()

        print(stats[column].strip() + ": " + str(mean))
        print()

def print_day_averages(df, date_of_interest):
    stats = {
        "Scratch ": "Scratch Average",
        "Scratch + Hdcp": "Scratch + HandiCap Average",
        "Open Frames": "Open Frames",
        "Spares": "Spares Average",
        "Strikes": "Strikes Average",
        "Split": "Split Average",
        "Split Conversion": "Split Conversion Average",
        "Fouls": "Foul Average",
        "Gutters": "Gutter Ball Average",
        "1st Ball Average": "1st Ball Average Pins Knocked Down",
        "1st Ball Average Speed (m.p.h)": "1st Ball Average Speed",
        "2nd Ball Average Speed MPH": "2nd Ball Average Speed"
    }

    df_day = df[df['Game and Date'].str.contains(date_of_interest)]

    for column, label in stats.items():
        mean = df_day[column].mean()
        print(date_of_interest + " " + label + ": " + str(mean))
        print()


# get the average ball weight for a certain day
def ballweight_mode_date_of_interst(df, date_of_interest):

    df_day = df[df['Game and Date'].str.contains(date_of_interest)]

    ball_weights = df_day['Ball Weght Used (Majority of Time)']

    mode_value = ball_weights.mode().iloc[0]

    print( date_of_interest + " Mode Ball Weight Was: "+ str(mode_value))
    print()

# main function
def main():
    #readfile("BowlingSpreadsheet.xlsx")

 
    df = pd.read_excel("BowlingSpreadsheet.xlsx")
    #getdata(df)

    print_averages(df)

    date_of_interest = "2-19-26"
    print_day_averages(df, date_of_interest)
    ballweight_mode_date_of_interst(df, date_of_interest)

main()
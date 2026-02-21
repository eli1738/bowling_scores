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

# all time scratch average
def scratchtotalaverage(df):

    scratch = df['Scratch ']
    mean = scratch.mean()
    print("Scratch Average: " + str(mean))
    print()

# all time scratch and handicap average
def scratchhndcptotalaverage(df):

    scratch = df['Scratch + Hdcp']
    mean = scratch.mean()
    print("Scratch + HandiCap Average: " + str(mean))
    print()

# all time open frame average
def openframes(df):

    scratch = df['Open Frames']
    mean = scratch.mean()
    print("Open Frames: " + str(mean))
    print()

# all time spare conversion average
def spares(df):

    scratch = df['Spares']
    mean = scratch.mean()
    print("Spares Average: " + str(mean))
    print()

# all time strikes average
def strikes(df):

    scratch = df['Strikes']
    mean = scratch.mean()
    print("Strikes Average: " + str(mean))
    print()

# all time split average
def split(df):

    scratch = df['Split']
    mean = scratch.mean()
    print("Split Average: " + str(mean))
    print()

# all time split conversion average
def splitconversion(df):

    scratch = df['Split Conversion']
    mean = scratch.mean()
    print("Split Conversion Average: " + str(mean))
    print()

# all time fouls average
def fouls(df):

    scratch = df['Fouls']
    mean = scratch.mean()
    print("Foul Average: " + str(mean))
    print()

# all time gutter ball average
def gutters(df):

    scratch = df['Gutters']
    mean = scratch.mean()
    print("Gutter Ball Average: " + str(mean))
    print()

# all time first throw pin knocked down average
def firstaveragescore(df):

    scratch = df['1st Ball Average']
    mean = scratch.mean()
    print("1st Ball Average Pins Knocked Down: " + str(mean))
    print()


# all time first bowl speed average
def firstaveragespeed(df):

    scratch = df['1st Ball Average Speed (m.p.h)']
    mean = scratch.mean()
    print("1st Ball Average Speed: " + str(mean))
    print()

# all time second bowl speed average
def secondaveragespeed(df):

    scratch = df['2nd Ball Average Speed MPH']
    mean = scratch.mean()
    print("2nd Ball Average Speed: " + str(mean))
    print()

# get the average scratch for a certain day
def scratch_average_date_of_interst(df, date_of_interest):

    df_day = df[df['Game and Date'].str.contains(date_of_interest)]

    scratch_scores = df_day['Scratch ']

    average_scratch = scratch_scores.mean()

    print( date_of_interest + " Average Scratch Was: "+ str(average_scratch))
    print()


# get the average scratch handicap for a certain day
def scratch_handicap_average_date_of_interst(df, date_of_interest):

    df_day = df[df['Game and Date'].str.contains(date_of_interest)]

    scratch_scores = df_day['Scratch + Hdcp']

    average_scratch = scratch_scores.mean()

    print( date_of_interest + " Average Scratch + Hdcp Was: "+ str(average_scratch))
    print()

# get the average openframe for a certain day
def openframe_average_date_of_interst(df, date_of_interest):

    df_day = df[df['Game and Date'].str.contains(date_of_interest)]

    openframe_scores = df_day['Open Frames']

    average_openframe = openframe_scores.mean()

    print( date_of_interest + " Average Open Frames Average Was: "+ str(average_openframe))
    print()


# get the average spares for a certain day
def spares_average_date_of_interst(df, date_of_interest):

    df_day = df[df['Game and Date'].str.contains(date_of_interest)]

    spares_scores = df_day['Spares']

    average_spares = spares_scores.mean()

    print( date_of_interest + " Spares Average Was: "+ str(average_spares))
    print()

# get the average strikes  for a certain day
def strikes_average_date_of_interst(df, date_of_interest):

    df_day = df[df['Game and Date'].str.contains(date_of_interest)]

    strikes_scores = df_day['Strikes']

    average_strikes = strikes_scores.mean()

    print( date_of_interest + " Strikes Average Was: "+ str(average_strikes))
    print()


# get the average split for a certain day
def split_average_date_of_interst(df, date_of_interest):

    df_day = df[df['Game and Date'].str.contains(date_of_interest)]

    split_scores = df_day['Split']

    average_split = split_scores.mean()

    print( date_of_interest + " Split Average Was: "+ str(average_split))
    print()

# get the average split conversion for a certain day
def splitconversion_average_date_of_interst(df, date_of_interest):

    df_day = df[df['Game and Date'].str.contains(date_of_interest)]

    splitconversion_score = df_day['Split Conversion']

    average_splitconversion_score = splitconversion_score.mean()

    print( date_of_interest + " Split Conversion Average Was: "+ str(average_splitconversion_score))
    print()

# get the average foul amount for a certain day
def foul_average_date_of_interst(df, date_of_interest):

    df_day = df[df['Game and Date'].str.contains(date_of_interest)]

    foul_scores = df_day['Fouls']

    average_foul_scores = foul_scores.mean()

    print( date_of_interest + " Foul Average Was: "+ str(average_foul_scores))
    print()

# get the average gutter balls for a certain day
def gutters_average_date_of_interst(df, date_of_interest):

    df_day = df[df['Game and Date'].str.contains(date_of_interest)]

    gutters_scores = df_day['Fouls']

    average_gutters_scores = gutters_scores.mean()

    print( date_of_interest + " Gutter Ball Average Was: "+ str(average_gutters_scores))
    print()

# get the average first ball score for a certain day
def firstballscore_average_date_of_interst(df, date_of_interest):

    df_day = df[df['Game and Date'].str.contains(date_of_interest)]

    firstball_score = df_day['1st Ball Average']

    average_firstball_score = firstball_score.mean()

    print( date_of_interest + " 1st Ball Score Average Was: "+ str(average_firstball_score))
    print()

# get the average 1st bowl mph for a certain day
def firstballmph_average_date_of_interst(df, date_of_interest):

    df_day = df[df['Game and Date'].str.contains(date_of_interest)]

    firstmph_score = df_day['1st Ball Average Speed (m.p.h)']

    average_firstmph_score = firstmph_score.mean()

    print( date_of_interest + " 1st Ball MPH Average Was: "+ str(average_firstmph_score))
    print()

# get the average 2nd bowl mph for a certain day
def secondballmph_average_date_of_interst(df, date_of_interest):

    df_day = df[df['Game and Date'].str.contains(date_of_interest)]

    secondmph_scores = df_day['2nd Ball Average Speed MPH']

    average_secondmph_scores = secondmph_scores.mean()

    print( date_of_interest + " 2nd Ball MPH Average Was: "+ str(average_secondmph_scores))
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

    # ----------- all time averages calls ----------
    scratchtotalaverage(df)

    scratchhndcptotalaverage(df)

    openframes(df)

    spares(df)

    strikes(df)

    split(df)

    splitconversion(df)

    fouls(df)

    gutters(df)

    firstaveragescore(df)

    firstaveragespeed(df)

    secondaveragespeed(df)

    #--------- end of all time averages calls -----------

    date_of_interest = "2-19-26"

    scratch_average_date_of_interst(df, date_of_interest)

    scratch_handicap_average_date_of_interst(df, date_of_interest)

    openframe_average_date_of_interst(df, date_of_interest)

    spares_average_date_of_interst(df, date_of_interest)

    strikes_average_date_of_interst(df, date_of_interest)

    split_average_date_of_interst(df, date_of_interest)

    splitconversion_average_date_of_interst(df, date_of_interest)

    foul_average_date_of_interst(df, date_of_interest)

    gutters_average_date_of_interst(df, date_of_interest)

    firstballscore_average_date_of_interst(df, date_of_interest)
    
    firstballmph_average_date_of_interst(df, date_of_interest)

    secondballmph_average_date_of_interst(df, date_of_interest)

    ballweight_mode_date_of_interst(df, date_of_interest)



main()


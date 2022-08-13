#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Project Name: Recode varibles
Date: April 20, 2021
Name: Matthew Fluet
Description:python script that creates new columns entities recoded into Variables

"""
import pandas as pd
#Import Data 
df = pd.read_excel("/Users/matthewfluet/Desktop/Senior_Project_Data.xlsx", sheet_name="Sheet1")

##Create a variable that will take the entity and convert it to a number
#Add the column using the map function Repeat this for all categorical columns

residency_Dummy = {'On-campus resident':1,'Off-campus resident':2,'Commuter from home':3}
df['residency_Dummy'] = df['residency'].map(residency_Dummy)

withdraw_Dummy = {'Yes':1,'No':0}
df['withdraw_Dummy'] = df['withdraw'].map(withdraw_Dummy)

studentAthlete_Dummy = {'Yes':1,'No':0}
df['studentAthlete_Dummy'] = df['studentAthlete'].map(studentAthlete_Dummy)

quarantine_Dummy = {'Yes':1,'No':0}
df['quarantine_Dummy'] = df['quarantine'].map(quarantine_Dummy)


quarantineTimes_Dummy = {0:1,"One-two":2,3:3}
df['quarantineTimes_Dummy'] = df['quarantineTimes'].map(quarantineTimes_Dummy)

academicYear_Dummy = {'First Year':1,'Sophomore':2,'Junior':'3','Senior':'4'}
df['academicYear_Dummy'] = df['academicYear'].map(academicYear_Dummy)

credits_Dummy = {'Less than 12':1,'Twelve-eighteen':2,'More than 18':3}
df['credits_Dummy'] = df['credits'].map(credits_Dummy)

safeInPersonClasses_Dummy = {'Strongly Disagree':1,'Disagree':2,'Neutral':3,'Agree':4,'Strongly Agree':5}
df['safeInPersonClasses_Dummy'] = df['safeInPersonClasses'].map(safeInPersonClasses_Dummy)

topicsAdequatelyCovered_Dummy = {'Strongly Disagree':1,'Disagree':2,'Neutral':3,'Agree':4,'Strongly Agree':5}
df['topicsAdequatelyCovered_Dummy'] = df['topicsAdequatelyCovered'].map(topicsAdequatelyCovered_Dummy)

respectedFreedoms_Dummy = {'Strongly Disagree':1,'Disagree':2,'Neutral':3,'Agree':4,'Strongly Agree':5}
df['respectedFreedoms_Dummy'] = df['respectedFreedoms'].map(respectedFreedoms_Dummy)

caredMentalHealth_Dummy = {'Strongly Disagree':1,'Disagree':2,'Neutral':3,'Agree':4,'Strongly Agree':5}
df['caredMentalHealth_Dummy'] = df['caredMentalHealth'].map(caredMentalHealth_Dummy)

returnToPlaySafety_Dummy = {'Strongly Disagree':1,'Disagree':2,'Neutral':3,'Agree':4,'Strongly Agree':5}
df['returnToPlaySafety_Dummy'] = df['returnToPlaySafety'].map(returnToPlaySafety_Dummy)

adequateResponse_Dummy = {'null':'NaN','Yes':1,'No':0}
df['adequateResponse_Dummy'] = df['adequateResponse'].map(adequateResponse_Dummy)

print(df.head(20))
##Finaly Export the file as a CVS to my desktop to verify if it worked.
#df.to_csv("/Users/matthewfluet/Desktop/dummyData.csv")
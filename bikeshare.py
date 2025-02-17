# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 15:22:22 2022

@author: Abdalmajeed Radwan
"""
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Which city to check ? ").lower()
        try:
            if city == "chicago" or city == "new york city" or city == "washington":
                break
        except  :
            print("invalid input, try agian")


    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Which month ?").lower()
        try:
            #checks if the input is valid for the available months
            #if month == "january" or month == "february" or month == "march" or month =="april" or month =="may" or month =="june" or month =="july" or month == "august " or month == "september" or month == "october" or month == "november" or month == "december" or month == "all":
            if month == "january" or month == "february" or month == "march" or month =="april" or month =="may" or month =="june" or month == "all":
                break
            elif month =="july" or month == "august " or month == "september" or month == "october" or month == "november" or month == "december":
                print("input is out of range, try again")
        except  :
            print("invalid input, try agian")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Which day of the week ?").lower()
        try:
            if day == "sunday" or day == "monday" or day == "tuesday" or day == "wenesday" or day == "thursday" or day == "friday" or day == "saterday" or day == "all" :
                break
        except  :
            print("invalid input, try agian")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    #df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # TO DO: display the most common month
    df['month'] =df['Start Time'].dt.month
    common_month = df['month'].mode()[0]
    print("most common month is :",common_month)

    # TO DO: display the most common day of week
    #df['day'] =df['Start Time'].dt.day
    #common_day = df['day'].mode()[0]
    #print("most common day is :",common_day)

    df['day'] =df['Start Time'].dt.day_name()
    common_day = df['day'].mode()[0]
    print("most common day is :",common_day)

    # TO DO: display the most common start hour
    df['hour'] =df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print("most common hour is :",common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("most common start station is",common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("most common end station is",common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    station_combination = df.groupby(['Start Station','End Station'])
    common_combination = station_combination.size().sort_values(ascending = False).head(1)
    print("most common station combination is",common_combination)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("total travel time is ",total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("average travel time is ",mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def show_sample(df):
    row_start = 0
    row_end = 5
    answer = input("do you want to see a sample of the data (yes or no) ?").lower()

    while True :
        if answer == "yes":
            print(df[row_start:row_end])
            row_start = row_end
            row_end = row_end + 5
            answer = input("do you want to see more ? ").lower()

        elif answer == "no":
            break


def user_stats(df,city):
    """Displays statistics on bikeshare users."""


    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types_counts = df['User Type'].value_counts()
    print("The count of user types is \n",user_types_counts)

    if city != 'washington':

    # TO DO: Display counts of gender
        gender_counts = df['Gender'].value_counts()
        print("The count of user types is \n",gender_counts)

    # TO DO: Display earliest, most recent, and most common year of birth
        earliest_birth = df['Birth Year'].min()
        recent_birth = df['Birth Year'].max()
        common_birth = df['Birth Year'].mode()[0]
        
        print("earliest birth is ",earliest_birth)
        print("recent birth is ",recent_birth)
        print("most common birth",common_birth)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        show_sample(df)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

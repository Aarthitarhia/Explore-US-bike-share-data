import time
import pandas as pd
import numpy as np
import calendar

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
    x = input('Would you like to see data for Chicago, NewYork or  Washington?\n')
    if x=='Chicago' or x=='chicago' or x=='CHICAGO':
        city = 'chicago'
    elif x=='NewYork' or x=='newyork' or x=='Newyork' or x=='newyork':
        city = 'new york city'
    elif x=='Washington' or x=='washington' or x=='WASHINGTON':
        city = 'washington'
    else:
        print("\n I am sorry.Try again.")
        return get_filters()

    # TO DO: get user input for month (all, january, february, ... , june)
    y = input('Would you like to filter by january, february, march, april, may or june? If not, type "na".\n')
        
    if y == 'january' or y == 'January' or y == 'JANUARY':
        month = 'january'
    elif y == 'february' or y == 'February' or y == 'FEBRUARY':
        month = 'february'
    elif y == 'march' or y == 'March' or y == 'MARCH':
        month = 'march'
    elif y == 'april' or y == 'April' or y == 'APRIL':
        month = 'april'
    elif y == 'may' or y == 'May' or y == 'MAY':
        month = 'may'
    elif y == 'june' or y == 'June' or y == 'JUNE':
        month = 'june'
    elif y == 'na' or y == 'Na' or y == 'NA':
        month = 'na'
    else:
        print("\n I am sorry.Try again")
        return get_filters()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    z = input('Would you like to filter by monday, tuesday, wednesday, thursday,  friday, saturday or sunday? If not,  type "na".\n')
    
    if z == 'monday' or z == 'Monday' or z == 'MONDAY':
        day = 'monday'
    elif z == 'tuesday' or z == 'Tuesday' or z == 'TUESDAY':
        day = 'tuesday'
    elif z == 'wednesday' or z == 'Wednesday' or z == 'WEDNESDAY':
        day = 'wednesday'
    elif z == 'thursday' or z == 'Thursday' or z == 'THURSDAY':
        day = 'thursday'
    elif z == 'friday' or z == 'Friday' or z == 'FRIDAY':
        day = 'friday'
    elif z == 'saturday' or z == 'Saturday' or z == 'SATURDAY':
        day = 'saturday'
    elif z == 'sunday' or z == 'Sunday' or z == 'SUNDAY':
        day = 'sunday'
    elif z == 'na' or z == 'Na' or y == 'NA':
        day = 'na'
    else:
        print("\n I am sorry.Try again")
        return get_filters()
    

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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'na':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'na':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def popular_month(df):
    """Dispalys stats about most frequent month """

    print('\nCalculating month with most trips')
    popular_month = df['month'].mode()[0]

    return "Most popular month is " + calendar.month_name[int(popular_month)]

def popular_day(df):
    """Dispalys stats about most frequent day """

    print('\nCalculating day with most trips')
    popular_day = df['day_of_week'].mode()[0]

    return "Most popular day is " + popular_day

def popular_hour(df):
    """Dispalys stats about most frequent hour """
     

    print('\nCalculating hour with most trips')
    popular_hour = df['hour'].mode()[0]

    return "Most popular hour is " + str(popular_hour) + " [24 hr] format"

    


def start_station(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    

    # TO DO: display most commonly used start station
    popular_startstation = df.groupby('Start Station')['Start Station'].count()
    popular_startstation = popular_startstation.sort_values(ascending=False).index[0]
    

    return "\nMost populat start station : {}".format(popular_startstation)
     
    

def end_station(df):
    """Displays statistics on the most popular stations and trip."""

    

    # TO DO: display most commonly used end station
    popular_endstation = df.groupby('End Station')['End Station'].count()
    popular_endstation = popular_endstation.sort_values(ascending = False).index[0]
    return "\nMost popular Endstation : " + str(popular_endstation)

    
def popular_station(df):
    """Displays statistics on the most popular stations and trip."""


    # TO DO: display most frequent combination of start station and end station trip
    popular_trips = df.groupby(['Start Station', 'End Station'])['Start Time'].count()
    popular_trips = popular_trips.sort_values(ascending = False)
    return "\nMost popular trip:" + "\n" + "Start Station: " + str(popular_trips.index[0][0]) + '\n'+"End Station:" + str(popular_trips.index[0][1])


  


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    
    return "\nTotal trip time = " + str(df['Trip Duration'].sum()) + "\n" + "Average trip time = " + str(df['Trip Duration'].mean())

   


def user_stats(df):
    """Displays counts of usertype on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    userdata = df.groupby('User Type')['User Type'].count()
    
    return userdata
    
    
def gender(df):
    """Displays counts of gender on bikeshare users."""

    print('\nCalculating Gender....\n')
    # TO DO: Display counts of gender
    gender = df.groupby('Gender')['Gender'].count()

    return gender

def birthyear(df):
     """Displays counts of birthyear details of bikeshare users."""
     print('\nCalculating birth year....\n')

    # TO DO: Display earliest, most recent, and most common year of birth


     return "\nEarliest birth year : " + str(int(df['Birth Year'].min())) + "\nRecent birth year : " + str(int(df['Birth Year'].max())) + "\nMost common birth year : " + str(int(df['Birth Year'].mode()[0]))
    
def raw_data(df,line):
     """Displays five lines of raw data"""

     d = input('\n Would you like to view five lines of trip data? \n Type "yes" or "no" \n')
    
     
     if d == 'yes' or d == 'Yes' or d == 'YES' or d == 'y':
          print(df.iloc[line:line+5])
          line+= 5
          return raw_data(df,line)
     if d =='no' or d =='No' or d =='NO' or d == 'n':
          return
     else:
          print('\n Try again, with "yes" or "no" \n')
          return raw_data(df)

    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        if month == 'na':
            print(popular_month(df))

        if day == 'na':
            print(popular_day(df))
            
        print(popular_hour(df))
        print(start_station(df))
        print(end_station(df))
        print(popular_station(df))
        print(trip_duration_stats(df))
        print(user_stats(df))
        
        if city != 'washington':
            print(gender(df))
        if city != 'washington':
             print(birthyear(df)) 

        print(raw_data(df,0))

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()


import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH_DATA = ['all','january','february','march','april','may','june']
              
DAY_DATA = [ 'all','monday', 'tuesday','wednesday','thursday','friday','saturday']
              
              
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    while True:
        city = input("\nwhich city would you like to filter by? chicago, new york city or washington\n").lower()
        if city not in ('chicago', 'new york city', 'washington'):          
               print("Sorry, I didn't catch that. try again.")
               continue
        else:
              break
          
    while True:
       month = input("\nwhich month would you like to filter by? january,february,...,june\n").lower()
       if month not in ('all','january','february','march','april','may','june'):
            print("Sorry, I didn't catch that. try again")
            continue
       else:
            break
              
    while True:
        day = input("\nwhich day would you like to filter by?monday,tuesday,....,sunday\n").lower()
        if day not in ('all','monday','tuesday','wednesday','thursday','friday','saturday','sunday'):
            print("Sorry, I didn't catch that. try again")
            continue
        else:
            break
                        
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
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time']. dt.month 
    df['hour'] = df['Start Time'].dt.hour
    df['day_of_week'] = df['Start Time'].dt.day_name()
    if month != 'all':
       months = ['january', 'february', 'march', 'april', 'may', 'june']
       month = months.index(month) +1        
       df = df[df['month'] == month]
    if day != 'all':
       df = df[df['day_of_week'] == day.title()]
        
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    popular_month = df['month'].mode() [0]
    print('Most Common Month:', popular_month)
    popular_day = df['day_of_week'].mode() [0]
    print('Most Common Day:', popular_day)
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode() [0]
    print('Most Common Hour:', popular_hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    Start_Station = df['Start Station'].value_counts()
    print('Most Commonly used start station:', Start_Station)
    End_Station = df['End Station'].value_counts()
    print('Most Commonly used end station:', End_Station)
    Combination_Station = df.groupby(['Start Station', 'End Station']).count()
    print('Most Commonly used combination of start station and end station trip:', Start_Station,"&",End_Station)
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    Total_Travel_Time = sum(df['Trip Duration'])
    print('Total Travel Time:',Total_Travel_Time/86400, "Days")
    Mean_Travel_Time = df['Trip Duration'].mean()
    print('Mean Travel Time:', Mean_Travel_Time/60, "Minutes")
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    
    user_types = df['User Type'].value_counts()
    #print(user_types)
    print('User Types:\n', user_types)
    gender_types = df['Gender'].value_counts()
    print('\nGender Types:\n', gender_types)
    Earliest_Year = df['Birth Year'].min()
    print('\nEaliest Year:', Earliest_Year)
    Most_Recent_Year = df['Birth Year'].max()
    print('\nMost Recent Year:', Most_Recent_Year)
    Most_Common_Year = df['Birth Year']. value_counts()
    print('\nMost Common Year:', Most_Common_Year)
                           

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_raw_data(df):
    """Displays raw data on user request."""
    print(df.head())
    next = 0
    while True:
        view_raw_data = input('\nwould you like to view next five row of raw data?Enter yes or no.\n')
        if view_raw_data.lower() != 'yes':
            return
        next = next + 5
        print(df.iloc[next:next+5])
    
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
       
  
             
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

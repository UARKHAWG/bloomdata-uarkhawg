'''helper functions'''
import random
import numpy as np
import pandas as pd


# Part 2 Functions===============================================

adjectives = ['blue', 'large', 'grainy', 'substantial', 'potent', 'thermonuclear']

nouns = ['food', 'house', 'tree', 'bicycle', 'toupee', 'phone']

def random_phrase():
    '''When called the function should return a single string containing
      a randomly selected adjective and noun pair'''
    adj = random.choice(adjectives)
    noun = np.random.choice(nouns)
    # random_index = random.randint(0, len(nouns)-1)
    # noun = nouns(random_index)
    # noun = random.sample(nouns, 1)[0] = ['house']

    return adj + ' ' + noun

print(random_phrase())
print(random_phrase())
print(random_phrase())

list1 = [1, 2, 3]
list2 = [4, 5, 6]
'''ex lists'''
def random_phrase2(list1, list2):
    '''random phrase gen2'''
    item1 = random.choice(list1)
    item2 = random.choice(list2)
    
    return str(item1) + ' ' + str(item2)

if __name__ == '__main__':
    print(random_phrase2(list1, list2))

def random_float(min_val, max_val):
    '''returns a random float sampled from a uniform distribution 
    with a minimum value of min_val and a maximum value of max_val.'''
    return random.uniform(min_val, max_val)

print(random_float(2,4))
print(random_float(2,4))
print(random_float(2,4))


def random_bowling_score():
    '''returns a random integer between 0 and 300'''
    return random.randint(0, 300)

print(random_bowling_score())
print(random_bowling_score())
print(random_bowling_score())


def silly_tuple():
    '''returns a tuple that contains three items. the first should
      be a random adjective-noun string, the second should be a float
        representing a star-rating between 1 and 5 - rounded to one
          decimal place. And the third item should be a random bowling score
          between 0 and 300.'''
    return (random_phrase(), round(random_float(1,5),1), random_bowling_score())

print(silly_tuple())
print(silly_tuple())
print(silly_tuple())

def silly_tuple_list(num_tuples):
    '''returns a list filled with a designated number of silly tuples'''
    tuple_list = []
    for item in range(num_tuples):
        tuple_list.append(silly_tuple())
    return tuple_list
print(silly_tuple_list(10))


# Part 3 Functions===============================================

test_df = pd.DataFrame(np.array([[0,1,2,3],[4,5,6,8.5],[7,8,9,10]]))
null_df = pd.DataFrame(np.array([[0,1,np.nan,3],[np.nan,5,6,7.7],[np.nan,8,np.nan,0]]))
def null_count(df):
    '''Check a dataframe for nulls and return the number of missing values.'''
    return df.isna().sum().sum()

print(null_count(test_df))
print(null_count(null_df))

def train_test_split(df, frac=0.8):
    '''Create a Train/Test split function for a dataframe and
      returns both the Training and Testing sets. Frac referes 
      to the precent of data you would like to set aside for training.'''
    train = df.sample(frac=frac)
    test = df.drop(train.index).sample(frac=1.0)
    return train, test

print(train_test_split(test_df))

def randomize(df, seed):
    '''Develop a randomization function that randomizes all
      of a dataframes cells then returns that randomized dataframe.
        This function should also take a random seed for reproducible randomization.'''
    randomized_df = df.sample(frac=1.0, random_state=seed)
    return randomized_df

print(randomize(test_df, 21))

address_df = pd.DataFrame({'address': ['890 Jennifer Brooks\nNorth Janet, WY 24785',
                                       '8394 Kim Meadow\nDarrenville, AK 27389',
                                       '379 Cain Plaza\nJosephburgh, WY 06332',
                                       '5303 Tina Hill\nAudreychester, VA 97036']})

def addy_split(addy_series):
    '''Split addresses into three columns (df['city'], df['state'], and df['zip'])
      - you can use regex to detect the format and pull out important pieces.'''
    #blank dataframe
    df = pd.DataFrame()
    city_list = []
    state_list = []
    zip_list = []
    for addy in addy_series:
        #find the values in the strings
        second_half = addy.split('\n')[1]
        city = second_half.split(',')[0]
        state = second_half.split()[-2]
        zip = second_half.split()[-1]
        # add the strings to lists
        city_list.append(city)
        state_list.append(state)
        zip_list.append(zip)
    #add list as new columns on df
    df['city']=city_list
    df['state']=state_list
    df['zip']=zip_list

    return df

print(addy_split(address_df['address']))



def abbr_2_st(state_series, abbr_2_st=True):
    '''Return a new column with the full name from a
      State abbreviation column. An input of FL would
        return Florida. This function should also take
          a boolean (abbr_2_state) and when False takes
            full state names and return state abbreviations.
              An input of Florida would return Fl.'''
    states_dict = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}
    def abbrev_replace(abbrev):
        '''replace state name with abbrev'''
        return states_dict[abbrev]

    def state_replace(state_name):
        '''replace abbrev with state name'''
        reverse_state_dict = dict((v, k) for k, v in states_dict.items())
        return reverse_state_dict[state_name]

    if abbr_2_st:
        return state_series.apply(abbrev_replace)
    return state_series.apply(state_replace)

addy_states = addy_split(address_df['address'])['state']

full_states_names_col = abbr_2_st(addy_states)

print(abbr_2_st(full_states_names_col, abbr_2_st=False))


def list_2_series(list_2_series, df):
    '''Single function to take a list and
      dataframe then turn the list into a series
        and add it to the inputted dataframe as a new column.'''
    new_column = pd.Series(list_2_series)
    return pd.concat([df, new_column],axis=1)

print(list_2_series([20,40,60,80], test_df))

outlier_df = pd.DataFrame(np.array([[0,10000000,2,3],[4,5,6,8.5],[7,8000008,9,10]]))

def rm_outlier(df):
    '''A 1.5*Interquartile range outlier detection/removal
      function that gets rid of outlying rows and returns
        that outlier cleaned dataframe.'''
    cleaned_df = pd.DataFrame()
    
    for (columnName, columnData) in df.items():
        Q1 = columnData.quantile(0.25)
        Q3 = columnData.quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5*IQR
        upper_bound = Q3 + 1.5*IQR
        print(lower_bound, upper_bound)

        mask = columnData.between(lower_bound,upper_bound, inclusive='both')
        cleaned = columnData.loc[mask]
        
        
        cleaned_df[columnName] = cleaned
    
    return cleaned_df

print(rm_outlier(outlier_df))

def split_dates(date_series):
    '''Function to split dates of format "MM/DD/YYYY"
      into multiple columns (df['month'], df['day'], df['year'])
        and then return the same dataframe with those additional columns.'''
    df = pd.DataFrame()

    # MM/DD/YYYY
    month_list = []
    day_list = []
    year_list = []


    for date in date_series:
        month = month_list.append(date.split('/')[0])
        day = day_list.append(date.split('/')[1])
        year = year_list.append(date.split('/')[2])
        
    df['month'] = month_list
    df['day'] = day_list
    df['year'] = year_list

    return df
print(split_dates(pd.Series(['01/01/2023','02/10/2022','03/21/2021','04/30/2020'])))
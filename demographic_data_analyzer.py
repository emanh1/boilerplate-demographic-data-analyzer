import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    cols = [
        "age",
        "workclass",
        "fnlwgt","education",
        "education-num",
        "marital-status","occupation","relationship","race","sex","capital-gain",
        "capital-loss","hours-per-week","native-country","salary"
    ]
    df = pd.read_csv(
        'adult.data.csv',
        usecols=cols
        )

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    races = {}
    for race in df['race']:
        races[race] = races.get(race, 0) + 1
    race_count = pd.Series(data=races, index=races.keys())

    # What is the average age of men?
    average_age_men = round(df.loc[df['sex'] == 'Male', 'age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round(df.loc[df['education'] == "Bachelors"].shape[0]/df.shape[0]*100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df.loc[(df['education'] == 'Bachelors') | 
                              (df['education'] == 'Masters') | 
                              (df['education'] == 'Doctorate')]

    lower_education = df.loc[(df['education'] != 'Bachelors') & 
                              (df['education'] != 'Masters') & 
                              (df['education'] != 'Doctorate')]

    # percentage with salary >50K
    higher_education_rich = round(higher_education.loc[higher_education['salary'] == '>50K'].shape[0]/higher_education.shape[0]*100, 1)
    lower_education_rich = round(lower_education.loc[lower_education['salary'] == '>50K'].shape[0]/lower_education.shape[0]*100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df.loc[(df['hours-per-week'] == min_work_hours )].shape[0]

    rich_percentage = df.loc[(df['salary'] == '>50K') & (df['hours-per-week'] == min_work_hours)].shape[0]/num_min_workers*100

    # Calculate the number of people earning >50K for each country
    high_earners = df[df['salary'] == '>50K']['native-country'].value_counts()

    # Calculate the total number of people for each country
    total_population = df['native-country'].value_counts()

    # Compute the percentage of high earners in each country
    percentage_high_earners = (high_earners / total_population) * 100

    # Find the country with the highest percentage of high earners
    highest_earning_country = percentage_high_earners.idxmax()
    highest_earning_country_percentage = round(percentage_high_earners.max(),1)


    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df.loc[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts().index[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

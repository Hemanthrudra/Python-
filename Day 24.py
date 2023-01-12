# Data munging or Data wrangling
# Import pandas package
# import pandas as pd
#
# # Assign data
# data = {'Name': ['Jai', 'Princi', 'Gaurav',
#                  'Anuj', 'Ravi', 'Natasha', 'Riya'],
#         'Age': [17, 17, 18, 17, 18, 17, 17],
#         'Gender': ['M', 'F', 'M', 'M', 'M', 'F', 'F'],
#         'Marks': [90, 76, 'NaN', 74, 65, 'NaN', 71]}
#
# # Convert into DataFrame
# df = pd.DataFrame(data)
#
# # Display data
# print(df)
#
#
# # Compute average
# c = avg = 0
# for ele in df['Marks']:
#     if str(ele).isnumeric():
#         c += 1
#         avg += ele
# avg /= c
#
# # Replace missing values
# df = df.replace(to_replace="NaN",
#                 value=avg)
#
# # Display data
# print(df)
#
# # Categorize gender
# df['Gender'] = df['Gender'].map({'M': 0,'F': 1, }).astype(float)
#
# # Display data
# print(df)
#
# # Filter top scoring students
# df = df[df['Marks'] >= 75]
#
# # Remove age row
# df = df.drop(['Age'], axis=1)
#
# # Display data
# print(df)


# Data Merging
# First Data set for merging
# import module
# import pandas as pd
#
# # creating DataFrame for Student Details
# details = pd.DataFrame({
#     'ID': [101, 102, 103, 104, 105, 106,
#            107, 108, 109, 110],
#     'NAME': ['Jagroop', 'Praveen', 'Harjot',
#              'Pooja', 'Rahul', 'Nikita',
#              'Saurabh', 'Ayush', 'Dolly', "Mohit"],
#     'BRANCH': ['CSE', 'CSE', 'CSE', 'CSE', 'CSE',
#                'CSE', 'CSE', 'CSE', 'CSE', 'CSE']})
#
# # printing details
# print(details)
#
# # Second data set for merging
#
# # Import module
# import pandas as pd
#
# # Creating Dataframe for Fees_Status
# fees_status = pd.DataFrame(
#     {'ID': [101, 102, 103, 104, 105,
#             106, 107, 108, 109, 110],
#      'PENDING': ['5000', '250', 'NIL',
#                  '9000', '15000', 'NIL',
#                  '4500', '1800', '250', 'NIL']})
#
# # Printing fees_status
# print(fees_status)
# # Merging the details and fee status  data frames
# print(pd.merge(details,fees_status,on='ID'))

# Wrangling data using grouping method
# Cars selling data

# Import module
# import pandas as pd
#
# # Creating Data
# car_selling_data = {'Brand': ['Maruti', 'Maruti', 'Maruti',
#                               'Maruti', 'Hyundai', 'Hyundai',
#                               'Toyota', 'Mahindra', 'Mahindra',
#                               'Ford', 'Toyota', 'Ford'],
#                     'Year': [2010, 2011, 2009, 2013,
#                              2010, 2011, 2011, 2010,
#                              2013, 2010, 2010, 2011],
#                     'Sold': [6, 7, 9, 8, 3, 5,
#                              2, 8, 7, 2, 4, 2]}
#
# # Creating Dataframe of car_selling_data
# df = pd.DataFrame(car_selling_data)
#
# # printing Dataframe
# print(df)
#
# # Group the data for year 2010
# grouped=df.groupby('Year')
# print(grouped.get_group(2010))


# Wrangling data by removing duplication
# Syntax : DataFrame.duplicated(subset=None,keep='first')

# Import module
import pandas as pd

# Initializing Data
student_data = {'Name': ['Amit', 'Praveen', 'Jagroop',
                         'Rahul', 'Vishal', 'Suraj',
                         'Rishab', 'Satyapal', 'Amit',
                         'Rahul', 'Praveen', 'Amit'],

                'Roll_no': [23, 54, 29, 36, 59, 38,
                            12, 45, 34, 36, 54, 23],

                'Email': ['xxxx@gmail.com', 'xxxxxx@gmail.com',
                          'xxxxxx@gmail.com', 'xx@gmail.com',
                          'xxxx@gmail.com', 'xxxxx@gmail.com',
                          'xxxxx@gmail.com', 'xxxxx@gmail.com',
                          'xxxxx@gmail.com', 'xxxxxx@gmail.com',
                          'xxxxxxxxxx@gmail.com', 'xxxxxxxxxx@gmail.com']}

# Creating Dataframe of Data
df = pd.DataFrame(student_data)

# Printing Dataframe
print(df)

# Here df.duplicated() list duplicate  Entries in ROllno.23
# So that ~(NOT) is placed in order to get non duplicate values.
non_duplicate = df[~df.duplicated('Roll_no')]

# printing non-duplicate values
print(non_duplicate)

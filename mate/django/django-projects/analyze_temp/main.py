import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

# authorize access to Google Sheets API
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('test-381421-7af234c5c1f6.json', scope)
client = gspread.authorize(creds)

# open the Google Sheet by URL
url = 'https://docs.google.com/spreadsheets/d/1M7ZxmkYGBI0N8GryjwBlYQmhmWsc4W9VUX2W1OyX134/edit#gid=1646210190'
sheet = client.open_by_url(url).sheet1

# get all values from the sheet
data = sheet.get_all_values()

# create a DataFrame from the data
headers = data[0]
rows = data[1:]
df = pd.DataFrame(rows, columns=headers)

# filter the DataFrame to only include employees who work 2/2
df_filtered = df[df['График'] == '2/2 день']

# convert the 'Дата' column to a datetime object
df_filtered['Дата'] = pd.to_datetime(df_filtered['Дата'], dayfirst=True)

# group the DataFrame by employee and day of the week, and count the number of days worked
df_grouped = df_filtered.groupby(['ФИО', df_filtered['Дата'].dt.day_name()]).size().reset_index(name='Count')

# pivot the DataFrame to create a table with employees as rows, days of the week as columns, and the count of working days as values
df_pivot = df_grouped.pivot(index='ФИО', columns='Дата', values='Count')

# create a bar chart for each employee showing the number of working days for each day of the week
for employee in df_pivot.index:
    chart_data = gspread_dataframe_to_array(df_pivot.loc[[employee]])
    chart_title = employee + ' - Количество рабочих дней по дням недели'
    chart = sheet.new_chart('BAR', chart_title, 10, 10, 500, 300, 5, 5)
    chart.add_data_series(chart_data, False)
    chart.set_legend_position('bottom')
    chart.set_x_axis_title('День недели')
    chart.set_y_axis_title('Количество рабочих дней')
    chart.insert_into_sheet('A1')

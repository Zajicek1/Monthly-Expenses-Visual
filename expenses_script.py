from datetime import datetime
from plotly.graph_objs import Bar, Layout
from plotly import offline
import pandas as pd


MONTHS = (
    'January', 'February', 'March',
    'April', 'May', 'June',
    'July', 'August', 'September',
    'October', 'November', 'December',
)

now = datetime.now()

print('Please enter the filename with the correct file pathing and make sure '
      'the file is saved as a ".csv" file extension.\n'
      'If wanting to quit, please enter "n".\n')

while True:
    try:
        filename = input(str('Filename with path: '))
        if filename == 'n':
            print('Exiting program.')
            break
        else:
            df = pd.read_csv(filename)

            # Run two for loops to enter the dates and costs into a list.
            individual_cost = []
            individual_dates = []
            for date in df['Date']:
                individual_dates.append(date)

            for cost in df['Amount']:
                individual_cost.append(cost)

            # Create the visualization but not yet display it.
            x_values = individual_dates
            y_values = individual_cost
            data = [Bar(x=x_values, y=y_values)]

            # Visualize the results with bar chart.
            x_axis_config = {'title': 'Dates', 'dtick': 1}
            y_axis_config = {'title': 'Cost'}
            for month in MONTHS:
                if month == now.strftime("%B"):
                    my_layout = Layout(title=f'{month} Expenses ' + now.strftime('%Y'), xaxis=x_axis_config,
                                       yaxis=y_axis_config)
                    offline.plot({'data': data, 'layout': my_layout}, filename=f'{month}_Expenses_Visual.html')

            print('Program complete.')
            break

    except FileNotFoundError:
        print('The path or file was not found. Please try again.')
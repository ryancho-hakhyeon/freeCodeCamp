import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
  
    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    # Create first line of best fit
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_pred = pd.Series([i for i in range(1880, 2051)])
    y_pred = x_pred*res.slope + res.intercept
    plt.plot(x_pred, y_pred, 'r')

    # Create second line of best fit
    new_df = df.loc[df['Year'] >= 2000]
    new_res = linregress(new_df['Year'], new_df['CSIRO Adjusted Sea Level'])
    new_x_pred = pd.Series([i for i in range(2000, 2051)])
    new_y_pred = new_x_pred*new_res.slope + new_res.intercept
    plt.plot(new_x_pred, new_y_pred, 'green')
    
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
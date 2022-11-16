import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    xcol=df["Year"]
    ycol=df["CSIRO Adjusted Sea Level"]
    plt.scatter(xcol, ycol) 

    # Create first line of best fit
    line_eq= linregress(xcol, ycol)
    print(line_eq)
    x_pred=pd.Series([i for i in range(1880,2051)])
    y_pred=line_eq.slope*x_pred + line_eq.intercept
    plt.plot(x_pred, y_pred,"r")

    # Create second line of best fit
    new_df=df.loc[df["Year"]>=2000]
    new_xcol=new_df["Year"]
    new_ycol=new_df["CSIRO Adjusted Sea Level"]
    line_eq2= linregress(new_xcol,new_ycol)
    x_pred_new= pd.Series([i for i in range(2000,2051)])
    y_pred_new= line_eq2.slope*x_pred2 + line_eq2.intercept
    plt.plot(x_pred_new, y_pred_new,"r")

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
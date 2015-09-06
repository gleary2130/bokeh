
from bokeh.charts import Scatter, output_file, show, vplot, hplot
from bokeh.sampledata.autompg import autompg as df
from bokeh.sampledata.olympics2014 import data
from bokeh.charts.utils import df_from_json
import pandas as pd

scatter0 = Scatter(
    df, x='mpg', title="x='mpg'", xlabel="Miles Per Gallon")

scatter1 = Scatter(
    df, x='mpg', y='hp', title="x='mpg', y='hp'",
    xlabel="Miles Per Gallon", ylabel="Horsepower", legend='top_right')

scatter2 = Scatter(
    df, x='mpg', y='hp', color='cyl', title="x='mpg', y='hp', color='cyl'",
    xlabel="Miles Per Gallon", ylabel="Horsepower", legend='top_right')

scatter3 = Scatter(
    df, x='mpg', y='hp', color='origin', title="x='mpg', y='hp', color='origin'",
    xlabel="Miles Per Gallon", ylabel="Horsepower", legend='top_right')

scatter4 = Scatter(
    df, x='mpg', y='hp', color='cyl', marker='origin', title="x='mpg', y='hp', color='cyl', marker='origin'",
    xlabel="Miles Per Gallon", ylabel="Horsepower", legend='top_right')

# Example with nested json/dict like data, which has been pre-aggregated and pivoted
df2 = df_from_json(data)
df2 = df2.sort('medals.total', ascending=False)
df2 = df2.head(10)
df2 = pd.melt(df2, id_vars=['abbr', 'name'])

scatter5 = Scatter(
    df2, x='value', y='name', color='variable', title="x='value', y='name', color='variable'",
    xlabel="Medals", ylabel="Top 10 Countries", legend='bottom_right')

output_file("scatter.html")

show(vplot(
    hplot(scatter0, scatter1),
    hplot(scatter2, scatter3),
    hplot(scatter4, scatter5)))

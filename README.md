# SparkRestAPI

Use the API <br />
https://rapidapi.com/eec19846/api/investors-exchange-iex-trading/<br />
to download data for 100 stocks and save in separate csv files for each stock.<br />
<br />
Create Spark data frames by reading the csv files and do following analysis
<br />
 On each of the days find which stock has moved maximum %age wise in both directions (+ve, -ve)<br />
Which stock was most traded stock on each day<br />
Which stock had the max gap up or gap down opening from the previous day close price I.e. (previous day close -  current day open price )<br />
Which stock has moved maximum from 1st Day data to the latest day Daya<br />
Find the standard deviations for each stock over the period<br />
Mind the mean  and median prices for each stock<br />
Find the average volume over the period<br />
Find which stock has higher average volume<br />
Find the highest and lowest prices for a stock over the period of time<br />

Create REST APIs to query the data for above questions as you could query from the website.<br />

For Spark you can use Scala or Pyspark.<br />
For API again you can use Scala or Python.<br />


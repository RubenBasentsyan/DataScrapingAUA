import quandl

data = quandl.get("WIKI/TSLA", start_date="2015-12-31", end_date = "2018-12-31")
op_percent_change = data['Open'].pct_change()
average_oppc = op_percent_change.mean()

range = data['High'] - data['Low']
range_percent_change = range.pct_change()
median_rpc = range_percent_change.median()

print("The average daily percentage change of the opening price is " +  str(average_oppc))
print("The median daily percentage change of range between highest and lowest daily prices is " + str(median_rpc))
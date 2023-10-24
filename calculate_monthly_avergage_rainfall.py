def calculate_monthly_average_rainfall(list_of_annual_values):
    total_rainfall = sum(list_of_annual_values)
	
    average = total_rainfall / 12

    return average

rainfall_values =   [10, 12, 8, 15, 10, 6, 9, 11, 13, 14, 9, 7]
monthly_average = calculate_monthly_average_rainfall(rainfall_values)
print('Average monthly rainfall: ', "{:.2f}".format(monthly_average))

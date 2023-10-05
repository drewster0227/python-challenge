import csv

# Specify the path to the CSV file and the output text file
pybank_csv = 'C:/Users/dreww/Desktop/DataAnalysisWork/Assignments/python-challenge/PyBank/Resources/budget_data.csv'
final_report = 'C:/Users/dreww/Desktop/DataAnalysisWork/Assignments/python-challenge/PyBank/Analysis/budget_analysis.txt'

# Open the CSV file for reading
with open(pybank_csv) as csv_file:
    pybank = csv.reader(csv_file)
    next(pybank)  # Skip the header row
    
    # Initialize variables to store various metrics
    numMonths = 0
    total = 0
    total_diff = 0
    i = 0
    greatestIncrease = 0
    greatestDecrease = 0
    monthly_diff = 0
    dateIncrease = ""
    dateDecrease = ""
    
    # Loop through each row in the CSV file
    for row in pybank:
        # Increment the count of months
        numMonths += 1
        
        # Get the monthly profit as a float
        monthly_profit = float(row[1])
        
        # Accumulate the total profit
        total += monthly_profit
        
        if i == 0:  
            last_month = monthly_profit
        else:
            monthly_diff = monthly_profit - last_month
            last_month = monthly_profit
            total_diff += monthly_diff
        # Find the greatest increase in profit and corresponding date
        if monthly_diff > greatestIncrease:
            greatestIncrease = monthly_diff
            dateIncrease = row[0]

        # Find the greatest decrease in profit and corresponding date
        if monthly_diff < greatestDecrease:
            greatestDecrease = monthly_diff
            dateDecrease = row[0]
        
        # Calculate the monthly difference and accumulate for average calculation
        
        i += 1

# Calculate the average monthly change and round it to 2 decimal points
average_diff = round(total_diff / (numMonths - 1), 2)

# Format the total with a dollar sign and comma separator
total_formatted = "${:,.0f}".format(total)

# Format the output for greatest increase and decrease in profits
formatted_increase = f"Greatest Increase in Profits: {dateIncrease} (${int(greatestIncrease)})"
formatted_decrease = f"Greatest Decrease in Profits: {dateDecrease} (${int(greatestDecrease)})"

# Add a dollar sign to the average monthly change
average_diff_formatted = "${:.2f}".format(average_diff)

# Print the results to the terminal
print("Total Months:", numMonths)
print("Total:", total_formatted)
print("Average Monthly Change:", average_diff_formatted)
print(formatted_increase)
print(formatted_decrease)

# Export the results to a text file
with open(final_report, 'w') as text_file:
    text_file.write("Financial Analysis\n")
    text_file.write("-------------------------\n")
    text_file.write(f"Total Months: {numMonths}\n")
    text_file.write(f"Total: {total_formatted}\n")
    text_file.write(f"Average Monthly Change: {average_diff_formatted}\n")
    text_file.write(f"{formatted_increase}\n")
    text_file.write(f"{formatted_decrease}\n")

print(f"Results exported to {final_report}")




        
       
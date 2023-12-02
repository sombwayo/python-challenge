import os

import csv





budget_csv = os.path.join("..", "PyBank", "Resources", "budget_data.csv")

output_file=os.path.join("Analysis", "main_analysis.txt")





months=0

previous_month_profit_losses=0

current_month_profit_losses=0

total_profit_losses=0

profit_losses=0

month_change=[]

profit_losses_change=[]



with open(budget_csv, encoding='UTF-8') as csvfile:

    csv_reader = csv.reader(csvfile)

    csv_header = next(csvfile)

    

    for row in csv_reader:

        

        months=months+1

        current_month_profit_losses= int(row[1])

        total_profit_losses=total_profit_losses+ current_month_profit_losses

        

        if months==1:

            previous_month_profit_losses=current_month_profit_losses



        else:

             profit_losses=current_month_profit_losses-previous_month_profit_losses

                         

             month_change.append(row[0])

             profit_losses_change.append(profit_losses)

        

             previous_month_profit_losses=current_month_profit_losses  

                                     

    sum_profit_losses=sum(profit_losses_change)

    average_profit_losses= round(sum_profit_losses/(len(month_change)),2)

    Greatest_increase=max(profit_losses_change)

    Greatest_decrease=min(profit_losses_change)

       

    Greatest_increase_index=profit_losses_change.index (Greatest_increase)

    Greatest_decrease_index=profit_losses_change.index (Greatest_decrease)

      

    best_month=month_change[Greatest_increase_index]

    worse_month=month_change[Greatest_decrease_index]

                                      

print("Financial Analysis")                                      

print("----------------------------")                                                   

print(f"Total Months:  {months}")

print(f"Total:  ${total_profit_losses}")                                            

print(f"Average Change:  ${average_profit_losses}")                                         

print(f"Greatest Increase in Profits:  {best_month} (${Greatest_increase})")                     

print(f"Greatest Decrease in Losses:  {worse_month} (${Greatest_decrease})")                         



with open(output_file, "w", encoding='UTF-8') as txt_file:

    

    txt_file.write("Financial Analysis") 

    txt_file.write("\n")

    txt_file.write("----------------------------") 

    txt_file.write("\n")

    txt_file.write(f"Total Months:  {months}") 

    txt_file.write("\n")

    txt_file.write(f"Total:  ${total_profit_losses}") 

    txt_file.write("\n")

    txt_file.write(f"Average Change:  ${average_profit_losses}")    

    txt_file.write("\n")                          

    txt_file.write(f"Greatest Increase in Profits:  {best_month} (${Greatest_increase})") 

    txt_file.write("\n")

    txt_file.write(f"Greatest Decrease in Losses:  {worse_month} (${Greatest_decrease})") 

    

    


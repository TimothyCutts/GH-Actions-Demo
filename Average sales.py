##Need to have a function for: Main, Avervage Sale, Above average sales, and the highest sale.
##Average sale function should add up the array and find the average and return it to main.  Nees one parameter
##Above average function should sort using a loop to find the total sales above the average sale and return that to main. Needs two parameters
##Highest sale function should sort using a loop to find the highest sale in the array and return that to main.  Needs one parameter
##Main function needs to declare variables and call all remaing functions and print to screen the average and highest sales, along with the amount of sales above the average.
##No inputs required from the user
##sales are given to us to preload the array


#Funtion to find average sale with in the array
def AverageSale(sales):
    #declare variables
    average_sale = float()
    total_sales = float()
    total_sales = 0
    #loop for finding total sales
    for index in range(0, len(sales)):
        total_sales = total_sales + sales[index]
        #end loop
    #find average from total sales
    average_sale = total_sales/len(sales)
    #returning the average
    return average_sale

 #function to find the total sales above the average sale       
def AboveAverage(sales, average_sale):
    #declare variables
    total_above = int()
    index = int()
    total_above = 0
    #loop to find the total of sales above average
    for index in range(0,len(sales)):
        if sales[index] > average_sale:
            total_above = total_above + 1
        else:
            total_above = total_above + 0
            #end  loop
    #returning the total above average
    return total_above

#function to sort the list for the highest sale
def HighestSale(sales):
    #delcare variables
    hightest = int()
    highest_index = int()
    index = int()
    highest = sales[0]
    #loop to find the highest sale
    for index in range(0,len(sales)):
        if sales[index] > highest:
            highest = sales[index]
        #end loop
    #returning the highest sale
    return highest

#main function to declare variables and print to screen.
def main():
    #declare variables and set array
    sales = [3578, 5136, 7835, 10385, 12384, 11350, 11284, 10590, 2739, 1638, 648, 4358]
    average_sale = float()
    sales_above_average = int()
    highest_sale = int()
    #call averagesale function with sales array
    average_sale = AverageSale(sales)
    #print to screen the average sale rounded to the 2nd decimal
    print("The average sale amount is: $", round(average_sale, 2))
    #call the above average sales with array and average sale
    sales_above_average = AboveAverage(sales, average_sale)
    #print to screen the total number of sales above the average sale
    print("The total number of sales above the average sale is: ", sales_above_average)
    #call the highest sale function with the array
    highest_sale = HighestSale(sales)
    #print to screen the highest sale of the array
    print("The highest sale amount was: $", highest_sale)


#calling main
main()

    
    

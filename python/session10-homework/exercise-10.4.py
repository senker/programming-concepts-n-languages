gtg_sales = [('Coffee', 2018, 525.05),
             ('Juice', 2021, 526.03),
             ('Apple', 2020, 525.12),
             ('Green Tea', 2019, 525.02),
             ('Banana', 2022, 524.08)]
sorted_sales = sorted(gtg_sales, key=lambda x: x[1])
print(sorted_sales)

''' In the code above, key=lambda x: x[1] specifies that we want to sort 
    the gtg_sales list based on the second element of each tuple, which is the year. '''
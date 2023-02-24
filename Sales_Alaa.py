import csv
AlaaFile = open('Sales.txt', 'r')
reader = csv.reader(AlaaFile)

header = next(reader)
rows = []
for row in reader:
    rows.append (row)

#print(header)
#print(rows)

#A- make small lists from rows list
#list for all dayes
date = ( (rows[0][0]), (rows[1][0]), (rows[2][0]), (rows[3][0]), (rows[4][0]), (rows[5][0]),
       (rows[6][0]), (rows[7][0]), (rows[8][0]), (rows[9][0]))

photoCopys =((rows[0][1]), (rows[1][1]), (rows[2][1]), (rows[3][1]), (rows[4][1]), (rows[5][1]),
       (rows[6][1]), (rows[7][1]), (rows[8][1]), (rows[9][1]))

Charge =((rows[0][2]),(rows[1][2]), (rows[2][2]), (rows[3][2]), (rows[4][2]), (rows[5][2]),
       (rows[6][2]), (rows[7][2]), (rows[8][2]), (rows[9][2]))

ExtraFee =((rows[0][3]), (rows[1][3]), (rows[2][3]), (rows[3][3]), (rows[4][3]), (rows[5][3]),
       (rows[6][3]), (rows[7][3]), (rows[8][3]), (rows[9][3]))

profit =((rows[0][4]), (rows[1][4]), (rows[2][4]), (rows[3][4]), (rows[4][4]), (rows[5][4]),
         (rows[6][4]), (rows[7][4]), (rows[8][4]), (rows[9][4]))

#print(" show the Date:" , date)
#print(" sales of Photo copys:" , photoCopys)
#print(" total of charge:" , Charge)
#print(" Estra fee :" , ExtraFee)
#print(" Total (Charge + Extra_fee) :" , profit)

Day1= ( date[0]+" :" ,"photoCopys: " + (photoCopys [0]) ,"Charge: " + Charge [0] ,"Extra_fee: "+ ExtraFee [0] ,"Total: "+ profit [0])
Day2 = ( date [1] +" :" ,"photoCopys: " + photoCopys [1] ,"Charge: " + Charge [1] ,"Extra_fee: "+ ExtraFee [1] ,"Total: "+ profit [1])
Day3 = ( date [2] +" :" ,"photoCopys: " + photoCopys [2] ,"Charge: " + Charge [2] ,"Extra_fee: "+ ExtraFee [2] ,"Total: "+ profit [2])
Day4 = ( date [3] +" :" ,"photoCopys: " + photoCopys [3] ,"Charge: " + Charge [3] ,"Extra_fee: "+ ExtraFee [3] ,"Total: "+ profit [3])
Day5 = ( date [4] +" :" ,"photoCopys: " + photoCopys [4] ,"Charge: " + Charge [4] ,"Extra_fee: "+ ExtraFee [4] ,"Total: "+ profit [4])
Day6 = ( date [5] +" :" ,"photoCopys: " + photoCopys [5] ,"Charge: " + Charge [5] ,"Extra_fee: "+ ExtraFee [5] ,"Total: "+ profit [5])
Day7 = ( date [6] +" :" ,"photoCopys: " + photoCopys [6] ,"Charge: " + Charge [6] ,"Extra_fee: "+ ExtraFee [6] ,"Total: "+ profit [6])
Day8 = ( date [7] +" :" ,"photoCopys: " + photoCopys [7] ,"Charge: " + Charge [7] ,"Extra_fee: "+ ExtraFee [7] ,"Total: "+ profit [7])
Day9 = ( date [8] +" :" ,"photoCopys: " + photoCopys [8] ,"Charge: " + Charge [8] ,"Extra_fee: "+ ExtraFee [8] ,"Total: "+ profit [8])
Day10 = ( date [9] +" :" ,"photoCopys: " + photoCopys [9] ,"Charge: " + Charge [9] ,"Extra_fee: "+ ExtraFee [9] ,"Total: "+ profit [9])

#print (Day1)
#print (Day2)
#print (Day3)
#print (Day4)
#print (Day5)
#print (Day6)
#print (Day7)
#print (Day8)
#print (Day9)
#print (Day10)


#B- Serching by number of day
x= input("Enter Number of day 1-10 : ")
if x == '10':
    print(Day10)
elif x == '9':
    print(Day9)
elif x == '8':
    print(Day8)
elif x == '7':
    print(Day7)
elif x == '6':
    print(Day6)
elif x == '5':
    print(Day5)
elif x == '4':
    print(Day4)
elif x == '3':
    print(Day3)
elif x == '2':
    print(Day2)
elif x == '1':
    print(Day1)
else:
    print("there no data for your number")

# c- Accounting
#here I am casting data from str to int/float to calculte

tuple_of_integers_photo = tuple(float(item) for item in photoCopys)
#print(tuple_of_integers_photo)

total_cost = [i * 5 for i in tuple_of_integers_photo]
print("total cost each day:", total_cost)

tuple_of_integers_charge = tuple(float(item) for item in Charge)
#print(tuple_of_integers_charge)

tuple_of_integers = tuple(float(item) for item in ExtraFee)
#print(tuple_of_integers)

tuple_of_integers_profit = tuple(float(item) for item in profit)
print(tuple_of_integers_profit)
print("=============\n"
      " The total Profit for each day ( Sales profits - costs ): \n"
      "============= ")
Total_profit = [tuple_of_integers_profit [0] - total_cost [0],
                tuple_of_integers_profit [1] - total_cost [1],
                tuple_of_integers_profit [2] - total_cost [2],
                tuple_of_integers_profit [3] - total_cost [3],
                tuple_of_integers_profit [4] - total_cost [4],
                tuple_of_integers_profit [5] - total_cost [5],
                tuple_of_integers_profit [6] - total_cost [6],
                tuple_of_integers_profit [7] - total_cost [7],
                tuple_of_integers_profit [8] - total_cost [8],
                tuple_of_integers_profit [9] - total_cost [9]]

print(Total_profit)

AlaaFile.close()

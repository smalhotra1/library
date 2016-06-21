import csv
import collections


#CSV file for Library books for kids
a = open('Libraries_-_Popular_Kids_Titles_at_the_Chicago_Public_Library.csv', 'r+')
csvReader = csv.reader(a)
bookkids= []
for row in csvReader:
   bookkids.append(row[1])
    

#CSV file for Library books for teens
b = open('Libraries_-_Popular_Teen_Titles_at_the_Chicago_Public_Library.csv', 'r+')
csvReader2 = csv.reader(b)
bookteen= []

for row in csvReader2:
   bookteen.append(row[1])
   
print bookkids
print bookteen

# an input of year is needed to know how many books are published in that year in diffrent sections        
def main():
    print ('/n give an input below ')
    year = int(input('Please enter year between 2007-2013: '))
    if  year== 2007:
        count1()
        
    elif year == 2008:
        count2()
    elif year == 2009:
        count3()
    elif year == 2010:
        count4()
    elif year == 2011:
        count5()
    elif year == 2012:
        count6()
    elif year == 2013:
        count7()
        exit()
    else:
        print('this year does not exisit in the list.')

    


#Counts  years 2007 if in row
def count1():
    a = open('Libraries_-_Popular_Kids_Titles_at_the_Chicago_Public_Library.csv', 'r+')
    csvReader = csv.reader(a)


    var1 = 0
    for row in csvReader:
        if row[3]== '2007':
            var1 = var1 + 1
              
           
    print('\nNumber of books published for kids: ', var1)
    
    
    b = open('Libraries_-_Popular_Teen_Titles_at_the_Chicago_Public_Library.csv', 'r+')
    csvReader2 = csv.reader(b)


    var2 = 0
    for row in csvReader2:
        if row[3]== '2007':
            var2 = var2 + 1       
              
            
    print('\nNumber of books published for teens: ', var2)
    
    main()

#Counts the number books published in 2008

def count2():
    a = open('Libraries_-_Popular_Kids_Titles_at_the_Chicago_Public_Library.csv', 'r+')
    csvReader = csv.reader(a)


    var11 = 0
    for row in csvReader:
        if row[3]== '2007':
            var11 = var11 + 1
              
    print('\nNumber of books published for kids : ', var11)
    
    
    b = open('Libraries_-_Popular_Teen_Titles_at_the_Chicago_Public_Library.csv', 'r+')
    csvReader22 = csv.reader(b)

    var22 = 0
    for row in csvReader2:
        if row[3]== '2007':
            var22 = var22 + 1       
              
            
    print('\nNumber of books published for teens: ', var22)
    main()


#Counts  years 2009 
def count3():
    a = open('Libraries_-_Popular_Kids_Titles_at_the_Chicago_Public_Library.csv', 'r+')
    csvReader = csv.reader(a)


    var33 = 0
    for row in csvReader:
        if row[3]== '2009':
            var33 = var33 + 1
              
            
    print('\nNumber of books published for kids: ', var33)
    
    
    b = open('Libraries_-_Popular_Teen_Titles_at_the_Chicago_Public_Library.csv', 'r+')
    csvReader2 = csv.reader(b)


    var44 = 0
    for row in csvReader2:
        if row[3]== '2009':
            var44 = var44 + 1       
              
           
    print('\nNumber of books published for teens: ', var44)
    
    main()

#Counts  years 2010 
def count4():
    a = open('Libraries_-_Popular_Kids_Titles_at_the_Chicago_Public_Library.csv', 'r+')
    csvReader = csv.reader(a)


    var5 = 0
    for row in csvReader:
        if row[3]== '2010':
            var5 = var5 + 1
              
           
    print('\nNumber of books published for kids: ', var5)
    
    
    b = open('Libraries_-_Popular_Teen_Titles_at_the_Chicago_Public_Library.csv', 'r+')
    csvReader2 = csv.reader(b)


    var6 = 0
    for row in csvReader2:
        if row[3]== '2010':
            var6 = var6 + 1       
              
           
    print('\nNumber of books published for teens: ', var6)
    
    main()
#Counts  years 2011 
def count5():
    a = open('Libraries_-_Popular_Kids_Titles_at_the_Chicago_Public_Library.csv', 'r+')
    csvReader = csv.reader(a)


    var7 = 0
    for row in csvReader:
        if row[3]== '2011':
            var7 = var7 + 1
              
           
    print('\nNumber of books published for kids: ', var7)
    
    
    b = open('Libraries_-_Popular_Teen_Titles_at_the_Chicago_Public_Library.csv', 'r+')
    csvReader2 = csv.reader(b)


    var9 = 0
    for row in csvReader2:
        if row[3]== '2011':
            var9 = var9 + 1       
            
    print('\nNumber of books published for teens: ', var9)
    
    main()
#Counts  years 2012
def count6():
    a = open('Libraries_-_Popular_Kids_Titles_at_the_Chicago_Public_Library.csv', 'r+')
    csvReader = csv.reader(a)


    var10 = 0
    for row in csvReader:
        if row[3]== '2012':
            var10 = var10 + 1
              
            
    print('\nNumber of books published for kids: ', var10)
    
    
    b = open('Libraries_-_Popular_Teen_Titles_at_the_Chicago_Public_Library.csv', 'r+')
    csvReader2 = csv.reader(b)


    var00 = 0
    for row in csvReader2:
        if row[3]== '2012':
            var00 = var00 + 1       
              
            
    print('\nNumber of books published for teens: ', var00)
    
    main()
#Counts  years 2013
def count7():
    a = open('Libraries_-_Popular_Kids_Titles_at_the_Chicago_Public_Library.csv', 'r+')
    csvReader = csv.reader(a)


    varr = 0
    for row in csvReader:
        if row[3]== '2013':
            varr = varr + 1
              
            
    print('\nNumber of books published for kids: ', varr)
    
    
    b = open('Libraries_-_Popular_Teen_Titles_at_the_Chicago_Public_Library.csv', 'r+')
    csvReader2 = csv.reader(b)


    varr0 = 0
    for row in csvReader2:
        if row[3]== '2013':
            varr0 = varr0 + 1       
              
        
    print('\nNumber of books published for teens: ', varr0)
    
main()



    

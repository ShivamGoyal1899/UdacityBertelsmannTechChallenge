f= open("README.md","w+")

f.write('# 60 Days of Udacity\n\n')
f.write('Here is my detailed analysis of *#60DaysofUdacity* for Bertelsmann Scholarship Challenge\n\n')

f.write('| Day Number 	|   Link to detailed file   	|\n')
f.write('|:----------:	|:-------------------------:	|\n')

for i in range(1, 61):
    i=str(i)
    f.write('|      '+i+'    	| [day'+i+'.md](./day'+i+'/day'+i+'.md) 	|\n')

f.close() 
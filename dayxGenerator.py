import os

for i in range(3, 61):
    i=str(i)
    
    path = 'day' + i
    if not os.path.exists(path):
        os.makedirs(path)
    
    f=open('day'+i+'/day'+i+'.md','w')

    f.write('# Day '+i+' #60DaysofUdacity\n\n')

    f.write('Today I completed Lesson X and revised the previous concepts till Lesson X as well.\n\n')

    f.write('### Concepts Studied Today:\n')
    f.write('- \n')
    f.write('- \n')
    f.write('- \n')
    f.write('- \n')
    f.write('- \n\n')

    f.write('### Material Referred:\n')
    f.write('- []()\n')
    f.write('- []()\n')
    f.write('- []()\n')
    f.write('- []()\n')
    f.write('- []()\n\n')

    f.write('### Progress: XYZ%\n')
    f.close() 
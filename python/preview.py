import csv

food_price_pairs=[['pear',0.80],['celery',0.50],['apple',0.50]]

with open('food.csv','w') as out_file
    for item in food_price_pairs:   
        line_str='{0},{1}'.format(item[0],item[1])
        line_str=line_str+'\n'
        out_file.write(line_str)
out_file.close()
print('Saved in food.csv')

# should convert the file (was .py before) to a csv (current)

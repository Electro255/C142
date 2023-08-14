import os
import csv

with open('movies.csv') as f:
    reader = csv.reader(f)
    data = list(reader)
    allmovies = data[1:]
    headers = data[0]
    headers.append('poster_link')

with open('final.csv', 'a+') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)

with open('poster_link.csv') as f:
    reader = csv.reader(f)  
    data = list(reader)
    allmovielinks = data[1:]  

for movieitem in allmovies:
    posterfound = any(movieitem[8] in movielinkitems for movielinkitems in allmovielinks)
    if posterfound:
        for movielinkitems in allmovielinks:
            if movieitem[8] == movielinkitems[0]:
                movieitem.append(movielinkitems[1])
                if len(movieitem) == 28:
                    with open('final.csv', 'a+') as f:
                        csvwriter = csv.writer(f)
                        csvwriter.writerow(headers)
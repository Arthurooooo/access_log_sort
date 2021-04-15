import csv
import operator



with open('weblog.csv') as inf,\
     open('output.csv', 'wb') as outf:
    reader = csv.reader(inf, delimiter=',')
    # sort the original data by the `points` column

    header = ['IP', 'Time', 'URL', 'Status']
    writer = csv.DictWriter(outf, fieldnames=header)
    userslist = []
    next(reader)
    #writer.writeheader()  # writes in the fieldnames
    for row in reader:
        #try:
            if row[0] != "":
                #print(row[2])
                tmp = [row[0], ]
                i = 0
                while(i < len(userslist)):
                    {
                        if userslist[0] == row[0]:
                        {
                            print("issa new one")
                        }
                        i += 1;
                    }
                if (tmp not in userslist) and (row[0][0] == "1"): #si on ne connait pas cet user
                    print("added to userslist")

                    userslist.append(tmp) #on l'enregistre
                    #print(userslist)
                userslist[userslist.index(tmp)].append(row[2])
                print(userslist[userslist.index(tmp)])
        #except:
            #print("fail", row)

    #print(userslist[0])
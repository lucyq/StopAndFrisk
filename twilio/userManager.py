import csv

file_path = "../data/users.csv"

users = []

def loadData():
    with open(file_path, 'rb') as csvfile:
        rdr = csv.reader(csvfile)
        for row in rdr:
            users.append(row[0])

def getAllUsers():
    return users


def addUser(phone_num):
    with open(file_path, 'wb') as csvfile:
        wrtr = csv.writer(csvfile)
        if phone_num not in users:
            wrtr.writerow([phone_num])
        
    
    users.append(phone_num);

def isUser(phone_num):
    if phone_num in users:
        return True
    else: 
        return False


#TODO:
# def removeUser(phone_num);



        
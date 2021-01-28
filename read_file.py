import csv

def read():

def get_user_id(user_id):
    user_id = str(user_id)
    res = []
    with open('ratings.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            user_list = row[0].split(",")
            if user_list[0] == user_id:
                dic = {
                    "userId": user_list[0],
                    "movieId": user_list[1],
                    "rating": user_list[2],
                    "timestamp": user_list[3],
                }
                res.append(dic)
            # print(', '.join(row))
    
    return res

def get_rating(user_id):
    user_id = str(user_id)
    rating = []
    with open('ratings.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            user_list = row[0].split(",")
            if user_list[0] == user_id:
                dic = {
                    "userId": user_list[0],
                    "movieId": user_list[1],
                    "rating": user_list[2],
                    "timestamp": user_list[3],
                }
                rating.append(user_list[2])
            # print(', '.join(row))
            plt.figure(figsize=[5,10]); # Set dimensions for figure
    plt.plot(rating)
    plt.title("")
    plt.show()
    plt.savefig('../static/1.svg', format='svg', dpi=1200)
    return rating




import pymysql
myconn = pymysql.connect(host = "localhost", 
                                 user = "root",
                                 port=3306,
                                 password = "shalini12%",
                                 db="login" 
                                 )  
  
#printing the connection object   
# print(myconn)  

# user = os.environ.get('USER_NAME')
# print(user)

mycursor = myconn.cursor()


def getcred(user, password):
    
    query = "SELECT * FROM details WHERE username = %s AND password = %s"
    values = (user, password)


    mycursor.execute(query, values)
    result = mycursor.fetchone()
    print(result)
    if result:
        return True 
    else:
        False
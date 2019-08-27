import sys
import mysql.connector


class CreateNewAccount:
    totalUser = 0
    insta = []

    def __init__(self,):

        self.id = CreateNewAccount.totalUser
        self.followers = []
        self.following = []
        CreateNewAccount.totalUser = CreateNewAccount.totalUser+1

    def createAccount(self):
        self.username = input("*Enter Your username :")
        self.name = input("Enter Your Name: ")
        self.password = input("Enter Your password :")
        self.age = input("Enter Your Age :")
        sql = "INSERT INTO user (username,name, password,age) VALUES (%s, %s, %s, %s)"
        val = (self.username, self.name, self.password, self.age)
        mydb = DbConnect().connect()
        mycursor = mydb.cursor()
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")
        mydb.disconnect()


class UserProfile:
    userObj = None

    def __init__(self, userObj):
        self.userObj = userObj

    def follow(self):
        if(self.userObj == None):
            print("Please login before proceed")
            return
        username = input("Enter your Friends username:")
        sql = "select id,name from user where username = %s"

        val = (username,)
        mydb = DbConnect().connect()
        mycursor = mydb.cursor()
        mycursor.execute(sql, val)
        myresult = mycursor.fetchall()
        try:
            id = myresult[0][0]
            print("Your friend name is ", myresult[0][1])
            followCursor = mydb.cursor()
            sql = "insert into tbl_follow (follower_id, following_id) values(%s, %s)"
            val = (self.userObj[0], id)
            followCursor.execute(sql, val)
            mydb.commit()
            print("Relationship added, ID:", followCursor.lastrowid)
        except:
            print("Entered username not exist")
        finally:
            mydb.disconnect()
            print("Closing connection")

    def i_am_following(self):
        sql = "select name from user where id in (select following_id from tbl_follow where follower_id = %s)"
        val = (self.userObj[0],)
        mydb = DbConnect().connect()
        mycursor = mydb.cursor()
        mycursor.execute(sql, val)
        myresult = mycursor.fetchall()
        if(len(myresult)==0):
            print("You r not following any one, follow now press F ")
            choice = input()
            if(choice == 'F' or choice == 'f'):
                self.follow()    
            return
        print("You r following ")
        for x in myresult:
            print(x[0])
        mydb.close()

    def myFollowers(self):
        sql = "select name from user where id in (select follower_id from tbl_follow where  following_id = %s)"
        val = (self.userObj[0],)
        mydb = DbConnect().connect()
        mycursor = mydb.cursor()
        mycursor.execute(sql, val)
        myresult = mycursor.fetchall()
        if(len(myresult)==0):
            print("You r dont have any follower, do you want")    
            return
        print("My followers ")
        for x in myresult:
            print(x[0])
        mydb.close()


class Login:

    def details(self):
        self.username = input("*Enter Your username :")
        self.password = input("*Enter Your password :")
        sql = "select * from user where username=%s and password=%s"
        val = (self.username, self.password)
        mydb = DbConnect().connect()
        mycursor = mydb.cursor()
        mycursor.execute(sql, val)
        myresult = mycursor.fetchall()
        mydb.disconnect()

        if 1 > len(myresult):
            print("invalid ID ")
            return
        else:
            userObj = myresult[0]
            user = UserProfile(userObj)
            while True:
                print("Welcome ", userObj[1])
                print("\n1.Change User Name .")
                print("2.Following.")
                print("3.Followers.")
                print("4.Follow new person.")
                print("5.Log Out .")
                ch = int(input("Enter Your Choice :"))

                if ch == 1:
                    user.name = input("Enter Your New User Name:")
                elif ch == 2:
                    user.i_am_following()
                elif ch == 3:
                    user.myFollowers()
                elif ch == 4:
                    user.follow()
                elif ch == 5:
                    break
                else:
                    print("Invalid Choice.")


class DbConnect:
    def connect(self):
        mydb = mysql.connector.connect(
            host="remotemysql.com",
            user="lM6U0FCrpf",
            passwd="uSAUr4iZyO",
            database="lM6U0FCrpf"
        )
        return mydb


if __name__ == '__main__':

    while True:
        print("1.Create New Account:")
        print("2.Log In")
        print("3.Exit")
        ch = int(input("Enter Your Choice :"))

        if ch == 1:
            obj = CreateNewAccount()
            obj.createAccount()
            # CreateNewAccount.insta.append(obj)
        elif ch == 2:
            ob = Login()
            ob.details()
        elif ch == 3:
            sys.exit(0)
        elif ch == 4:
            dbObj = DbConnect()
            print(dbObj.connect())
        else:
            print("Invalid Choice:")


# Username: lM6U0FCrpf

# Database name: lM6U0FCrpf

# Password: uSAUr4iZyO

# Server: remotemysql.com

# Port: 3306

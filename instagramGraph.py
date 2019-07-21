import sys
class CreateNewAccount:
    totalUser = 0
    insta = []

    def __init__(self,):
        self.name=input("Enter Your Name :")
        self.id=CreateNewAccount.totalUser
        self.followers=[]
        self.following=[]
        CreateNewAccount.totalUser=CreateNewAccount.totalUser+1

    def follow(self):
        dest=int(input("Enter your Friends Id:"))
        if dest>=len(CreateNewAccount.insta):
            print("User Not Exist with This ID ")
            return
        CreateNewAccount.insta[self.id].following.append(CreateNewAccount.insta[dest])
        CreateNewAccount.insta[dest].followers.append(CreateNewAccount.insta[self.id])

    def i_am_following(self):
        print("%s is Following =="%(CreateNewAccount.insta[self.id].name),end="")
        for i in CreateNewAccount.insta[self.id].following:
            print(i.name+"--->",end="")

    def myFollowers(self):
        print("Followers of %s  ==" % (CreateNewAccount.insta[self.id].name), end="")
        for i in CreateNewAccount.insta[self.id].followers:
            print(i.name + "--->", end="")


class Login:

    def details(self):
        iden=int(input("Enter your Id :"))
        if iden>=len(CreateNewAccount.insta):
            print("invalid ID ")
            return
        else:
            user=CreateNewAccount.insta[iden]
            print(user.id)
            while True:
                print("\n1.Change User Name .")
                print("2.Following.")
                print("3.Followers.")
                print("4.Follow .")
                print("5.Log Out .")
                ch=int(input("Enter Your Choice :"))

                if ch==1:
                    user.name=input("Enter Your New User Name:")
                elif ch==2:
                     user.i_am_following()
                elif ch==3:
                    user.myFollowers()
                elif ch==4:
                    user.follow()
                elif ch==5:
                    break
                else:
                    print("Invalid Choice.")





if __name__=='__main__':

    while True:
        print("1.Create New Account:")
        print("2.Log In")
        print("3.Exit")
        ch=int(input("Enter Your Choice :"))

        if ch==1:
            obj=CreateNewAccount()
            CreateNewAccount.insta.append(obj)
        elif ch==2:
            ob=Login()
            ob.details()
        elif ch==3:
            sys.exit(0)
        else:
            print("Invalid Choice:")

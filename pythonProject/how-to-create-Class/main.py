'''class User:
    pass


user_1 = User()
user_1.id = "001" #adding Attribute
user_1.username = "niyanta"

print(user_1.username) #Result : niyanta    '''

#Constructor :
'''insted of using this again 
user_2 = User()
user_2.id = "002"
user_2.username = "nishant"
So we use 
class Car:
    def __init__(self):
    #initialise attributes.'''

'''class User2:
    def __init__(self):# Use for inserting starting values for attribute.
    print("New user being created....")
    user_1 = User2()
    user_1.id = "001"
    user_1.username = "niyanta"

    print(user_1.username)
    Result : New user being created....
             niyanta'''

'''class User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username


user_1 = User("001", "Niyanta")
user_2 = User("002", "Nishant")
print(user_1.id, user_1.username)
Result : 001 Niyanta'''

'''class User:              #instagram

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.follower = 0


user_1 = User("001", "Niyanta")
user_2 = User("002", "Nishant")
print(user_1.follower)
Result : 0'''

#Adding Metods in Class:

class User:              #instagram

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "Niyanta")
user_2 = User("002", "Nishant")

user_1.follow(user_2)

print(f" {user_1.username} followers: {user_1.followers}, following : {user_1.following}")
print(f" {user_2.username} followers: {user_2.followers}, following : {user_2.following}")

# Result :
# Niyanta followers: 0, following : 1
# Nishant followers: 1, following : 0
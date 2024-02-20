import pyodide
import js
import pyscript
from pyscript import document

def testUser (event):
    try:
       # user = document.querySelector("#user")
        #password = document.querySelector("#password")
        f = open('UserPasswords.txt', 'w')
        
        f.close()
        #output_div = document.querySelector("#label")
        #output_div.innerText = "works"
    except:
        f = open('UserPasswords.txt', 'w')
        f.close()
        output_div = document.querySelector("#label")
        output_div.innerText = "Sorry, you don't have a saved user"
        




class user:
    def __init__ (self, username, password):
        self.username = username
        self.password = password

    def createUser(self, user, password):
        try:
            f = open('UserPasswords.txt', 'r')
            UserPWsDictStr = f.read()
            UserPWsDict = eval(UserPWsListStr)
            f.close()
            if user in UserPWsDict.keys():
                print("Sorry, user is taken.")
            
                
            else:
                UserPWsDict[user] = password

            # Finding the file if it DOES exists
        except:
            f = open('UserPasswords', 'w')
            # Creates the file
            UserPWsDict = {}
            UserPWsDict[user] = password
            f.close()
        finally:
            UserPWsDict[self.user] = self.password
            
            
    

    

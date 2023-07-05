"""
Copyright (c) 2023 Dauwt

Licensed under the MIT License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.opensource.org/licenses/mit-license.php

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

password = str(input("Insert a password: "))
new_password = "D" * len(password)  # This variable is used to encrypt the text or password, we put a number of D defined by the length of the password
order = ["A","B","C","D","E","F","G","H","I","J","Q","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","Ç","0","1","2","3","4","5","6","7","8","9","!","#","$","%","&","/","?","@","£","§","_","*",".","-"]
encrypt = []  # Put the character corresponding to the letter in order[] (put the characters separated by commas and between quotes).
num_encrypt = len(encrypt)  # The number of characters in the text/password

print(new_password)

def encrypt_password():  # Used to encrypt the password/text defined in the variable "password"
    global password
    global new_password
    password = password.upper()  # Puts the password/text in capital letters
    for x in range(len(password)):  # For every character in "password"
        for y in range(num_encrypt):  # For every character in "encrypt"
            if password[x] == order[y]:  # If the x(defined by "num_encrypt" from 0 to the number of characters - 1) of the password is equal to the character in the "order"
                new_password = new_password[:x] + str(encrypt[y]) + new_password[x+1:]  # Substitutes the D in the x by the encrypted character in "encrypt"
                print(new_password)

def run():  # Used to run the code as many times as the user wants
    global password
    global new_password
    new_password = "D" * len(password)
    encrypt_password()
    print(new_password)
    while True:
        continuing = str(input("Continue(y/n): "))  # Ask the user if he wants to encrypt more password/text
        if continuing.lower() == "n":
            break
        if continuing.lower() == "y":
            password = ""  # Redefines the "password" to None
            password = str(input("Insert a password: "))
            run()
        else:  # If the user didn't use n/N or y/Y then says to enter the answer with n/N or y/Y
            print("Please answer with y(yes) or n(no)!")

if __name__ == "__main__":
    run()


import string
import getpass
from colorama import Fore,Back,Style,init
from termcolor import colored
import time
import random

def comlexity_chechker():
    
    init(convert=True)
    print(Fore.BLUE+'''\n\n \______   \_____    ______ ________  _  _____________  __| _/ |    |    ____   ____ |  | ____ ________  
 |     ___/\__  \  /  ___//  ___/\ \/ \/ /  _ \_  __ \/ __ |  |    |   /  _ \ /  _ \|  |/ /  |  \____ \ 
 |    |     / __ \_\___ \ \___ \  \     (  <_> )  | \/ /_/ |  |    |__(  <_> |  <_> )    <|  |  /  |_> >
 |____|    (____  /____  >____  >  \/\_/ \____/|__|  \____ |  |_______ \____/ \____/|__|_ \____/|   __/ 
                \/     \/     \/                          \/          \/                 \/     |__|    \n\n''')
    print(Fore.BLUE+"\n                             *****Welocme to complexity checker*****                     ")
    print(Fore.GREEN+"\n\n 1- To check passowrd complexity")
    print(Fore.RED+"\n 2- To generate random passowrd")
    print(Fore.YELLOW+"\n 3- to exit\n")
    user_imput=int(input(">>>>>>:"))
    if user_imput==1:
        password=Fore.CYAN+input("Enter the Pawword to Check comlexity:")
        strengt=0
        remarks=''
        lower_count=uper_count=num_count = wspace_count = special_count =0

        for char in list(password):
            if char in string.ascii_lowercase:
                lower_count+=1
            elif char in string.ascii_uppercase:
                uper_count+=1
            elif char in string.digits:
                num_count+=1
            elif char ==' ':
                wspace_count+=1
            else:
                 special_count+=1
        
        if lower_count>=1:
            strengt+=1
        if uper_count>=1:
            strengt+=1
        if num_count>=1:
            strengt+=1
        if wspace_count>=1:
            strengt+=1
        if special_count>=1:
            strengt+=1
    
        if strengt==1:
            remarks="Chnage your password Easily Hacked "
        elif strengt==2:
            remarks="Better but not recomend"
        elif strengt==3:
            remarks="Average good for initilay"
        elif strengt==4:
            remarks="Diffulct to hack"
        elif strengt==5:
            remarks="Hard to hack Best possword"


        print(f"YOUR PASSWORD IS :{password}")
        for j in range(1, 101):
            time.sleep(0.03)

      
            downloading = colored("Complexity Check", 'green', 'on_black', attrs=['reverse', 'bold'])

      
            percentage = colored(f"[{j}%]", 'blue', attrs=['bold'])

        
            if j <= 33:
                bar = colored('|' * (j // 2), 'red', attrs=['bold'])  
            elif 33 < j <= 66:
                bar = colored('|' * (j // 2), 'yellow', attrs=['bold', 'underline'])  
            else:
                bar = colored('|' * (j // 2), 'red', attrs=['bold', 'reverse']) 

        
            color = downloading + percentage + bar
            print(color, end="\r")
        print()

        print(Fore.RED + "\nDetailed About your chosen password \n")
        print(Fore.YELLOW + f'Your password length is {len(password)}')
        print(Fore.BLUE + f'{lower_count} Lowercase chars')
        print(Fore.CYAN + f'{uper_count} Upper chars')
        print(Fore.GREEN + f'{num_count} Number chars')
        print(Fore.MAGENTA + f'{wspace_count} Spaces chars')
        print(Fore.LIGHTYELLOW_EX + f'{special_count} Special chars')

        print(f"Password strength is {strengt}")
        print(f"\n Hint!: {remarks}")

# Open a file to save the password details without color codes  

        with open("password_details.txt", "w") as file:
            file.write("\nDetailed About your chosen password \n")
            file.write(f'Your password is {password}\n')
            file.write(f'Your password length is {len(password)}\n')
            file.write(f'{lower_count} Lowercase chars\n')
            file.write(f'{uper_count} Upper chars\n')
            file.write(f'{num_count} Number chars\n')
            file.write(f'{wspace_count} Spaces chars\n')
            file.write(f'{special_count} Special chars\n')
            file.write(f"Password strength is {strengt}\n")
            file.write(f"\n Hint!: {remarks}\n")
            print("Password report \n save password_detailed.txt")

        return comlexity_chechker()
    if user_imput == 2:
        print(Fore.GREEN + '''\n\n
  ____                             _                _                
 / ___|  ___  ___ _   _ _ __ ___  | |    ___   ___ | | ___   _ _ __  
 \___ \ / _ \/ __| | | | '__/ _ \ | |   / _ \ / _ \| |/ / | | | '_ \ 
  ___) |  __/ (__| |_| | | |  __/ | |__| (_) | (_) |   <| |_| | |_) |
 |____/ \___|\___|\__,_|_|  \___| |_____\___/ \___/|_|\_\\__,_| .__/ 
                                                              |_|     \n\n''')
    
        print(Fore.BLUE + "Enter the length of your password (eg: 8-15): ", end="")
        
        
        try:
            length = int(input().strip())
            for j in range(1, 101):
                time.sleep(0.01)

        
                downloading = colored("Genetarting Password", 'green', 'on_black', attrs=['reverse', 'bold'])

        
                percentage = colored(f"[{j}%]", 'blue', attrs=['bold'])

        
                if j <= 33:
                    bar = colored('|' * (j // 2), 'yellow', attrs=['bold']) 
                elif 33 < j <= 66:
                    bar = colored('|' * (j // 2), 'blue', attrs=['bold', 'underline'])  
                else:
                    bar = colored('|' * (j // 2), 'red', attrs=['bold', 'reverse'])  

      
                color = downloading + percentage + bar
                print(color, end="\r")
            print()
            
            if length < 8 or length > 15:
                print(Fore.RED + "Password length should be between 8 and 15 characters.")
                

           
            lower = random.choice(string.ascii_lowercase)
            upper = random.choice(string.ascii_uppercase)
            digit = random.choice(string.digits)
            special = random.choice(string.punctuation)

           
            remaining_length = length - 4
            combined = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
            
           
            random_chars = ''.join(random.choices(combined, k=remaining_length))
            
            password = upper + lower + digit + special + random_chars
            password_list = list(password)
            random.shuffle(password_list) 
            final_password = ''.join(password_list)

            # Save the generated password to a text file
            with open("generated_password.txt", "w") as file:
                file.write(final_password)

            print(Fore.GREEN + f"Generated Password: {final_password}")
            print(Fore.YELLOW + "Password saved to 'generated_password.txt'")

        except ValueError:
            print(Fore.RED + "Please enter a valid number for the password length.")
        comlexity_chechker()
    if user_imput==3:
        for j in range(1, 101):
            time.sleep(0.01)

        
            downloading = colored("Clear all Passwords", 'green', 'on_black', attrs=['reverse', 'bold'])

        
            percentage = colored(f"[{j}%]", 'blue', attrs=['bold'])

        
            if j <= 33:
                bar = colored('|' * (j // 2), 'red', attrs=['bold']) 
            elif 33 < j <= 66:
                bar = colored('|' * (j // 2), 'yellow', attrs=['bold', 'underline'])  
            else:
                bar = colored('|' * (j // 2), 'red', attrs=['bold', 'reverse'])  

      
            color = downloading + percentage + bar
            print(color, end="\r")
        print()
        print("\n Thanks for using this Tool \n Regard,\n MrSecurityAnalyst\n ")
        exit






comlexity_chechker()



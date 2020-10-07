#Electoral System
import pandas as pd

print("Welcome to Dummy Electoral Registration Desk")

election_dict={'Voter_ID':[],'Name':[], 'Age':[] , 'Party':[] }

n=int(input("Please enter the number of candidates you would like to fill in the data: "))

parties=['BJP', 'CONGRESS', 'JDU','SP','BSP', 'CPI']

p=100000
c=1
while c<=n:
    print(f"\nPlease enter the details of {c} candidate!")
    
    try:
        age = int(input("Please enter you Age in Numbers: "))
        if type(age)==int and int(age)>=18:
            age=age
            name = input("Please enter your name: ").upper() 
            party = input("Please enter your preferred party: ").upper()
            
        elif type(age)==int and int(age)<18:
            print(f"Candidate {c} please try when you reach 18 years age")
            pass
        
    except ValueError:
        age=int(input("Please enter your Age in Numbers AGAIN: "))
    election_dict['Voter_ID'].append(p+c)
    if int(age>=18):
        election_dict['Age'].append(int(age))
        if name !="":
            election_dict['Name'].append(name)
        
        
        if party !="" and party in parties:
            election_dict['Party'].append(party)
        else:
            print('\n You are adding a new party!!')
            parties.append(party)
            election_dict['Party'].append(party)
    c+=1

print(election_dict)

election_df=pd.DataFrame(election_dict)
print(election_df)
election_df.to_csv('Electoral Registration.csv', index =False)
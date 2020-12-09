'''
[+]The new "Avengers" movie has just been released!
There are a lot of people at the cinema box office standing in a huge line.

[+]Each of them has a single 100, 50 or 25 dollar bill. An "Avengers" ticket costs 25 dollars.

Vasya is currently working as a clerk. He wants to sell a ticket to every single person in this line.

Can Vasya sell a ticket to every person and give change if he initially has no money and sells the tickets strictly in the order people queue?

Return YES, if Vasya can sell a ticket to every person and give change with the bills he has at hand at that moment. Otherwise return NO.

[+]Examples:
tickets([25, 25, 50]) # => YES 
tickets([25, 100]) # => NO. Vasya will not have enough money to give change to 100 dollars
tickets([25, 25, 50, 50, 100]) # => NO. Vasya will not have the right bills to give 75 dollars of change (you can't make two bills of 25 from one of 50)
'''

#solution:
def tickets(people):
    print(people)
    #the profit Vasya has
    profit = 0
    #list of dollar bill types Vasya having
    vasya = []
    for money in people:
        if money == 25:
            #add 25$ to list, raise the profit
            vasya.append(25)
            profit += 25
        else:
            #check if Vasya has enough money to return
            if (money - 25) > profit:
                return "NO"
                break
            else:
                #the customer give 100$
                if money == 100:
                    #add 100$ and raise the profit 
                    vasya.append(100)
                    profit += 25
                    #check if Vasya has enough papers of each type of dollar bills
                    #which need to be returned
                    try:
                        vasya.pop(vasya.index(25))
                        #got 25$ missing 50$ to return, so just check
                        try:
                            vasya.pop(vasya.index(50))
                            continue
                        except:
                            #Vasya doesn't have 50$ paper, finding 25$ paper instead
                            try:
                                vasya.pop(vasya.index(25))
                                #Got 1, find another
                                try:
                                    vasya.pop(vasya.index(25))
                                    continue
                                except:
                                    return "NO"
                                    break
                            except:
                                return "NO"
                                break
                    except:
                        return "NO"
                        break
                else:
                #the customer give 50$
                    #add 50$ and raise the profit 
                    vasya.append(50)
                    profit += 25
                    #finding 25$ paper to return
                    try:
                        vasya.pop(vasya.index(25))
                        continue
                    except:
                        return "NO"
                        break
    #confirm Vasya has enough money and papers of dollar to return
    return "YES"

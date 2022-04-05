#!/usr/bin/env python3 

import sys

# These are my clients
clients = [
    'andrew@gmail.com', 
    'jessica@gmail.com', 
    'ted@mosby.com', 
    'john@snow.is', 
    'bill_gates@live.com', 
    'mark@facebook.com', 
    'elon@paypal.com', 
    'jessica@gmail.com']

# These are my participants from the event
participants = [
    'walter@heisenberg.com', 
    'vasily@mail.ru', 
    'pinkman@yo.org', 
    'jessica@gmail.com', 
    'elon@paypal.com', 
    'pinkman@yo.org', 
    'mr@robot.gov', 
    'eleven@yahoo.com']

# These have viewed my promotion email
recipients = [
    'andrew@gmail.com',
    'jessica@gmail.com',
    'john@snow.is']




def call_center(c=set(clients), p=set(participants), r=set(recipients)):
    """
        A list of those who have not seen my promotion yet. 
        Send them to the call centre.
    """
    print('# A list of those who have not seen my promotion yet')
    return list((c | p) - r)

def potential_clients(c=set(clients), p=set(participants), r=set(recipients)):
    """
        Participants that are not my clients. 
        Send them an introductory memo
    """
    print('# Participants that are not my clients')
    return list(p - c)
    

def loyalty_program(c=set(clients), p=set(participants), r=set(recipients)):
    """
        Clients that didn't join the event. 
        Send them a link
    """
    print("# Clients that didn't join the event")
    return list(c - p)


def dispatch_tasks(task: callable):
    
    if task not in TASKS:
        raise Exception("Unknown task!")
    
    return TASKS[task]()


TASKS = {
    'call_center': call_center,
    'potential_clients': potential_clients,
    'loyalty_program': loyalty_program
}

if __name__ == '__main__':

    argc = len(sys.argv)
    if argc != 2:
        print("Wrong number of arguments")
        exit()
    
    try:
        print(*dispatch_tasks(sys.argv[1]), sep='\n')
    except Exception as e:
        print(e)
        exit()
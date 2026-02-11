'''Your Amazonian team is responsible for maintaining a monetary transaction service. The transactions are tracked in a log file.

A log file is provided as a string array where each entry represents a transaction to service. Each transaction consists of:

sender_user_id: Unique identifier for the user that initiated the transaction. It consists of only digits with at most 9 digits.

recipient_user_id: Unique identifier for the user that is receiving the transaction. It consists of only digits with at most 9 digits.

amount_of_transaction: The amount of the transaction. It consists of only digits with at most 9 digits.

The values are separated by a space. For example, "sender_user_id recipient_user_id amount_of_transaction".

Users that perform an excessive amount of transactions might be abusing the service so you have been tasked to identify the users that have a number of transactions over a threshold. The list of user ids should be ordered in ascending numeric value.'''

#I need a dictionary to count the transactions for each user. Then, I need to compare them with the threshold and return the list of 
#users.

def processLogs(logs, threshold):
    dict_users = {}
    abusing_users = []
    for log in logs:
        sender, recipient, _ = log.split() #El amount no nos interesa, no es necesario pero esta bueno poner _
        #No matter the role, I need to take the user in the dictionary, so I can use the set method to create a variable and add 
        # the sender and recipient.
        all_users = set([sender, recipient])
        #I need to iterate through all users to add them to the dictionary and count their transactions. It is not inefficient because
        # the number of users is not greater than the number of transactions, so it is O(n) of time and O(n) of space.
        for user in all_users:
            dict_users[user] = dict_users.get(user, 0) + 1
    for user, transactions in dict_users.items():
        if transactions >= threshold:
            abusing_users.append(user)
    return sorted(abusing_users, key=int)

if __name__ == "__main__":
    logs = ["345366 89921 45", "029021 38239 23", "38239 345366 15", "029021 345366 77"]
    threshold = 2

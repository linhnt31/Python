import time

class SMS_store:
   
    #Class Object attribute
    book = 'harry porter'
    
    def __init__(self):
        self.list_of_messages = []
        
    def add_new_arrival(self):
        """
            Makes new SMS tuple, inserts it after other messages
            in the store. When creating this message, its
            has_been_viewed status is set False.
        """
  
        has_been_viewed = bool(input("Have you seen this message ? True or False ? "))
        from_number = str(input("What number are you sending this message from ?"))
        text_of_SMS = str(input("What message would you like to send ?"))
        time_arrived = time.asctime()
        
        message = (has_been_viewed, from_number, text_of_SMS, time_arrived)
        self.list_of_messages.append(message)
    
    def message_count(self):
        """Returns the number of sms messages in my_inbox """ 
        return len(self.list_of_messages)

    def get_unread_indexes(self):
        """ Returns list of indexes of all not-yet-viewed SMS messages """

        unread_indexes = []
        for i in range(0, len(self.list_of_messages)):
            if not self.list_of_messages[i][0]:
                unread_indexes.append(i)
        return "unread messages: {}".format(unread_indexes)

    def to_string(self):
        if len(self.list_of_messages) == 0:
            return 'Nothing here'
        return "{}".format(self.list_of_messages)
    

#Object
my_inbox = SMS_store()
my_inbox.add_new_arrival()
print("Number of messages in my inbox is {}".format(my_inbox.message_count()))
print(my_inbox.get_unread_indexes())
print(my_inbox.to_string())
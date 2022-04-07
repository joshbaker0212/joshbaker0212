import re

#asks user how many cards he wants to enter
for totalcards in range(int(input('Enter number of credit cards to check'))):
    
    #ask user to enter each credit card
    ccnumber = input('Enter credit card numbers one at a time').strip()

    #pattern used to search for first digit, 16 total digits with our without hyphon and
    #ending with ? to ensure no letters at the end.
    pre_match = re.search(r'^[456]\d{3}-?\d{4}-?\d{4}-?\d{4}$',ccnumber)
    
    
    if pre_match:

        #
        processed_string = "".join(pre_match.group(0).split('-'))

        #checks for four consecutive numbers
        final_match = re.search(r'(\d)\1{3,}',processed_string)
        if final_match:
            print('Invalid')
        else :
            print('Valid')
    else:
        print('Invalid')
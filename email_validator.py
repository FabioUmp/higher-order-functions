def clean_email_list(emails):
    cleaned = map(lambda email: email.lower().strip(), emails)
    
    valid_emails = filter(lambda email: 
        email.count('@') == 1 and        
        email.index('@') > 0 and        
        email.index('@') < len(email)-1,
        cleaned
    ) 
    
    return list(valid_emails)
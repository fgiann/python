def response(hey_bob):
    s = hey_bob.strip()

    if s == '' or s.isspace():
        bob_response = 'Fine. Be that way!'
    elif s.isupper() and not s[:-1].isnumeric():
        if s[-1] == '?':
            bob_response = 'Calm down, I know what I\'m doing!'
        else:
            bob_response = 'Whoa, chill out!'
    elif s[-1] == '?':
        bob_response = 'Sure.'
    else:
        bob_response = 'Whatever.'
    
    return bob_response

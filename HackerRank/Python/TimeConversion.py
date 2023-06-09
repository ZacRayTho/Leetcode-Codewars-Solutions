# Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.
# A single string  that represents a time in -hour clock format (i.e.: hh:mm:ssAM or hh:mm:ssPM ).
def timeConversion(s):
    if s[8] == 'A':
        if s[0:2] == '12':
            new = s.replace(s[0:2], '00')
            new = new.replace(s[8:], "")  
        else:
            new = s.replace(s[8:], "")        
    else:
        if s[0:2] == '12':
            new = s.replace(s[8:], "") 
        else:
            new = s.replace(s[0:2], str(int(s[0:2]) + 12))
            new = new.replace(s[8:], "")
    return new
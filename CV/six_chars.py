def six_chars(data):
    if data[0]<0 or data[1]<0:
        word=['a','f','f','f','f','f','f','f']
        return word
    aye=int(data[0]/100)+48
    bee=int((data[0]%100)/10)+48
    cee=int(data[0]%10)+48
    dee=int(data[1]/100)+48
    eee=int((data[1]%100)/10)+48
    eff=int(data[1]%10)+48
    word=['a',chr(aye),chr(bee),chr(cee),chr(dee),chr(eee),chr(eff),'f']
    return word

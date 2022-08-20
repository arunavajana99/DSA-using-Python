def ReplaceChar(s,a,b):
    if len(s)==0:
        return s
    SmallOutput=ReplaceChar(s[1:],a,b)
    if s[0]==a:
        return b+SmallOutput
    else:
        return s[0]+SmallOutput
print(ReplaceChar('dacdxcd','c','x'))
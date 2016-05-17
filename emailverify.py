###Email Identifier###

def ObtainEmailAddress():
    EmailAddress = input("Please Enter Your Email Address: ")
    return EmailAddress
    
def FindDomain(EmailAddress):
    SplitEmail = EmailAddress.split("@")
    Domain = SplitEmail[-1]
    return Domain
    
def FindLocal(EmailAddress):
    SplitEmail = EmailAddress.split("@")
    SplitEmail.pop()
    unsplit = "@"
    Local = unsplit.join(SplitEmail)
    return Local
    
def AuthenticateDomain(Domain):
    AllowedDomain = ["edu", "com", "gov", "net", "org", "mil", "int"]
    Domain = Domain.lower()
    CheckDomain = Domain.split(".")
    if CheckDomain[1] in AllowedDomain:
        ValidDomain1 = True
    else:
        ValidDomain1 = False
    DomainList = list(CheckDomain[0])
    for Character in DomainList:
        if Character >= "a" and Character <= "z" or  Character >= "0" and Character <= "9" or Character == "-":
            pass
        else:
            ValidDomain0 = False
            break
        if DomainList[0] == "-" or DomainList[-1] == "-":
            ValidDomain0 = False
            break
    ValidDomain0 = True
    if ValidDomain0 == True and ValidDomain1 == True:
        AuthenticDomain = True
    else:
        AuthenticDomain = False
    return AuthenticDomain
   
def AuthenticateLocal(Local):
    Local = Local.lower()       
    LocalList = list(Local)
    for Character in LocalList:
        if Character >= "a" and Character <= "z" or  Character >= "0" and Character <= "9" or Character in ["!", "#", "$", "%", "&", "'", "*", "+", "-", "/", "=", "?", "^", "_", "`", "{", "|", "}", "~", "."]:
            pass
        else:
            ValidLocal = False
            break
        ValidLocal = True
    if ".." in Local:
        ValidLocal = False
    if LocalList[0] == "." or LocalList[-1] == ".":
        ValidLocal = False
    return ValidLocal
            
def DisplayResult(EmailAddress, ValidLocal, AuthenticDomain):
    if ValidLocal == True and AuthenticDomain == True:
        print(EmailAddress,"is a Valid Email Address.")
    else:
        print(EmailAddress,"is NOT a Valid Email Address.")
    
def RunCode():
    EmailAddress = ObtainEmailAddress()
    Domain = FindDomain(EmailAddress)
    Local = FindLocal(EmailAddress)
    AuthenticDomain = AuthenticateDomain(Domain)
    ValidLocal = AuthenticateLocal(Local)
    DisplayResult(EmailAddress, ValidLocal, AuthenticDomain)
#################################################################

RunCode()


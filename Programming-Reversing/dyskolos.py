import base64
def club(s1,s2):
    return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s1,s2))

def Aληθινόςθησαυρός():
    userinput = input("Enter the password: ") 
    key = "greekgreekgreekgreekgreekgreekgreekgr"
    a = club(key,userinput)
    b = str.encode(a)
    result = base64.b64encode(b, altchars=None)
    if result == b'NzAmMS0cM1INWAlGOgNbVx5WATQSLRJUDzgFF1UFUS0DCV8ADw==':
        return True
    else:
        return False

def Πάρτετoνθησαυρό():
    access = Aληθινόςθησαυρός()
    if access == True:
        print("Συγχαρητήρια! Βρήκατε έναν θησαυρό!")
        print("Δεν νικήσατε την Αθηνά. Περισσότερα ελληνικά για εσάς")
        print("Ο κωδικός πρόσβασης δεν είναι η σημαία")
        Πάρτετoνθησαυρό()
    else:
        print("Είναι καλύτερο να σταματήσετε να προσπαθείτε και να φύγετε από εδώ")
        Πάρτετoνθησαυρό()

def Πάρτετονθησαυρό():
    access = Αληθινόςθησαυρός()
    if access == True:
        print("Συγχαρητήρια! Βρήκατε έναν θησαυρό!")
        print("Νικήσατε την Αθηνά. Όχι πια ελληνικά για εσάς")
        print("Ο κωδικός πρόσβασης είναι η σημαία")
        exit()
    else:
        print("Λάθος κωδικός!")
        print("Δεν θα πάρετε τη σημαία τόσο εύκολο")
        Πάρτετoνθησαυρό()

def Αληθινόςθησαυρός():
    userinput = input("Enter the password: ")
    key = "greekgreekgreekgreekgreekgreekgreekgr"
    a = club(key,userinput)
    b = str.encode(a)
    result = base64.b64encode(b, altchars=None)
    if result == b'NzAmMS0cKFYQXjgWVAEFUC0VURgULVINWhQtBg1fCx5WCwxUDw==':
        return True
    else:
        return False


access=False
Πάρτετονθησαυρό()
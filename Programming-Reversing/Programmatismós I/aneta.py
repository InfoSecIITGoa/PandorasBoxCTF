def ελέγξτετηνπρoσβαση():
  userinput = input("Enter the password: ")
  if userinput == "PBCTF{y0u_b3tT3r_l34rn_Gr33k}":
      return True
  else:
      return False

def ελέγξτετηvπρoσβαση():
  userinput = input("Enter the password: ")
  if userinput == "PBCTF{1t_c4m3_fr0m_ph03n1c14n}":
      return True
  else:
      return False

def ελέγξτετηνπpόσβαση():
  userinput = input("Enter the password: ")
  if userinput == "PBCTF{h3r3s_7h3_t1ck37_T0_CypRu5}":
      return True
  else:
      return False

def ελέγξτετηvπpoσβαση():
  userinput = input("Enter the password: ")
  if userinput == "PBCTF{h3r3s_7h3_t1ck37_T0_4th3n5}":
      return True
  else:
      return False

def ελέγξτετηνπρόσβαση():
  userinput = input("Enter the password: ")
  if userinput == "PBCTF{Gr33k_i5_n07_7h4T_5impl3}":
      return True
  else:
      return False

def ελέγξτετηvπpόσβαση():
  userinput = input("Enter the password: ")
  if userinput == "PBCTF{tH1s_i5_4_R3aL_fLaG_t0TalLy}":
      return True
  else:
      return False
    
def ελέγξτετηvπρόσβαση():
  userinput = input("Enter the password: ")
  if userinput == "PBCTF{1_7h1nk_y0u_L0v3_Gr3ec3}":
      return True
  else:
      return False

def Βρεςτοκλειδι():
    access = ελέγξτετηνπρόσβαση()
    if access == True:
        print("Συγχαρητήρια! Βρήκατε ένα κλειδί !")
        print("Ξέρω ότι είναι πολύ απλό για εσάς.")
        print("Ο κωδικός πρόσβασης είναι η σημαία")
        exit()
    else:
        print("Λάθος κωδικός!")
        print("Δεν ξέρω τι συμβαίνει με εσάς. Είναι πολύ απλό!")
        Βρεςτoκλειδι()

def Βρεςτoκλειδι():
    access = ελέγξτετηvπρόσβαση()
    if access == True:
        print("Συγχαρητήρια! Βρήκατε ένα κλειδί !")
        print("Ξέρω ότι είναι πολύ απλό για εσάς.")
        print("Ο κωδικός πρόσβασης δεν είναι η σημαία")
        exit()
    else:
        print("Λάθος κωδικός!")
        print("Είστε απόλυτη αποτυχία. Αντε χάσου")
        Βρεςτoκλειδι()


access = False
Βρεςτοκλειδι()

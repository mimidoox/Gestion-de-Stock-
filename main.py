import pyodbc
from tkinter import *
from tkcalendar import DateEntry

global idproduit
global idfour
global idop
global iduser

#la connexion à la base de données
conn = pyodbc.connect("Driver={SQL Server Native Client 11.0};Server=Vostro3558\SQLEXPRESS;Database=master;Trusted_Connection=yes;")

#Login form
def Loginform():
    global login_screen
    login_screen = Tk()
    login_screen.title("GStock")
    login_screen.geometry("400x200+400+200")


    global  message
    global username
    global password
    username = StringVar()
    password = StringVar()
    message  = StringVar()
    Label(login_screen,width="300", text="Authentification", bg="orange",fg="white").pack()
    Label(login_screen, text="Identifiant").place(x=40,y=40)
    Entry(login_screen, textvariable=username).place(x=150,y=42)
    Label(login_screen, text="Mot de passe").place(x=40,y=80)
    Entry(login_screen, textvariable=password ,show="*").place(x=150,y=82)
    Label(login_screen, text="",textvariable=message).place(x=95,y=100)
    Button(login_screen, text="Créer un compte", width=15, height=1, bg="orange", command=inscriremenu).place(x=200, y=130)
    Button(login_screen, text="Login", width=10, height=1, bg="orange",command=login).place(x=105,y=130)
    login_screen.mainloop()
#fonction du bouton login
def login():
    cursor = conn.cursor()
    cursor.execute("SELECT id,typecpt FROM  UTILISATEUR where username=? and password=? ",username.get(),password.get())

    row=cursor.fetchone()


    if password.get()=='' or username.get()=='':
        message.set("Tous les champs sont obligatoires !")
    if row==None:
        message.set("votre identitfiant ou mot de passe est incorrecte")

    else:
        login.var = row[0]
        login.var2 = row[1]
        login_screen.destroy()
        Menuform()
        message.set("connexion bien établie")
#Form creation compte utilisateur
def inscriremenu():
    if checkwindow(login_screen)=='true':
        login_screen.destroy()
    global signup_screen
    signup_screen =Tk()
    signup_screen.title("GStock")

    signup_screen.geometry("400x320+400+200")

    global message
    global nom
    global prenom
    global username
    global password
    global repassword
    nom= StringVar()
    prenom =StringVar()
    username = StringVar()
    password = StringVar()
    message = StringVar()
    repassword = StringVar()
    Label(signup_screen, width="300", text="Inscription", bg="orange", fg="white").pack()
    Label(signup_screen, text="Prénom").place(x=20, y=40)
    Entry(signup_screen, textvariable=prenom).place(x=170, y=40)
    Label(signup_screen, text="Nom").place(x=20, y=80)
    Entry(signup_screen, textvariable=nom).place(x=170, y=80)
    Label(signup_screen, text="Identifiant").place(x=20, y=120)
    Entry(signup_screen, textvariable=username).place(x=170, y=120)
    Label(signup_screen, text="Mot de passe").place(x=20, y=160)
    Entry(signup_screen, textvariable=password, show="*").place(x=170, y=160)
    Label(signup_screen, text="Retaper le mot de passe").place(x=20, y=200)
    Entry(signup_screen, textvariable=repassword, show="*").place(x=170, y=200)
    Label(signup_screen, text="", textvariable=message).place(x=95, y=225)
    Button(signup_screen, text="Créer votre compte", width=15, height=2, bg="orange",command=inscrire).place(x=80, y=250)
    Button(signup_screen, text="se connecter", width=15, height=2, bg="orange",command=ret).place(x=220, y=250)
    signup_screen.mainloop()
#fonction créer compte
def inscrire():

    if(nom.get()=="" or prenom.get()=="" or username.get()=="" or password.get()=="" or repassword.get()==""):
        message.set(" Vous devez remplir tous les champs !")
    else:
        if password.get()!=repassword.get():
            message.set(" Resaisir le mot de passe correcetement !")
        else:
            cur = conn.cursor()
            cur.execute("SELECT * FROM UTILISATEUR WHERE username=?",username.get())
            row=cur.fetchone()
            if row==None:
                cur1 = conn.cursor()
                cur1.execute("INSERT INTO UTILISATEUR(nom,prenom,username,password,typecpt) values(?,?,?,?,?)",nom.get(),prenom.get(),username.get(),password.get(),'user')
                cur1.commit()
                message.set("Utilisateur crée ")
            else:
                message.set("Identifiant déja utilisé, veuillez choisir un autre !")
#fonction se connecter après la creation du compte
def ret():
        signup_screen.destroy()
        Loginform()
#la page principale
def Menuform():
    global menu_screen
    menu_screen = Tk()
    menu_screen.title("GStock")
    menu_screen.geometry("700x550+300+100")


    Label(menu_screen,width="300", text="Menu", bg="#B90E0E",fg="black").pack()
    Button(menu_screen, text="Gestion du compte", width=40, height=4, bg="#B90E0E",command=Menuform1).place(x=200,y=50)
    Button(menu_screen, text="Gestion des produits", width=40, height=4, bg="#B90E0E",command=gererprod).place(x=200,y=150)
    Button(menu_screen, text="Gestion des fournisseurs", width=40, height=4, bg="#B90E0E",command=gestionfournisseur).place(x=200,y=250)
    Button(menu_screen, text="Gestion des opérations", width=40, height=4, bg="#B90E0E",command=gererop).place(x=200,y=350)
    Button(menu_screen, text="Déconnexion", width=40, height=4, bg="orange",command=deco).place(x=200, y=450)
    menu_screen.mainloop()
#GESTION DU COMPTE
#Form Menu Compte
def Menuform1():
    try:
        menu_screen.destroy()
    except:
        pass
    global menu_compte
    menu_compte = Tk()
    menu_compte.title("GStock")
    menu_compte.geometry("700x550+300+100")


    Label(menu_compte, width="300", text="Menu", bg="#B90E0E", fg="black").pack()
    Button(menu_compte, text="Modifier votre identifiant ", width=40, height=4, bg="#B90E0E",command=Modifieruser).place(x=200, y=50)
    Button(menu_compte, text="Changer mot de passe", width=40, height=4, bg="#B90E0E",command=Modifiermdp).place(x=200, y=150)
    Button(menu_compte, text="Supprimer votre compte", width=40, height=4, bg="#B90E0E",command=suppcompte).place(x=200, y=250)
    if login.var2=='admin':
        Button(menu_compte, text="Supprimer un utilisateur", width=40, height=4, bg="red", command=gereruser).place(x=200, y=350)
        Button(menu_compte, text="Page principal", width=40, height=4, bg="orange", command=retour).place(x=200, y=450)
    else:
        Button(menu_compte, text="Page principal", width=40, height=4, bg="orange",command=retour).place(x=200, y=350)
    menu_compte.mainloop()
#Form modifier identifiant
def Modifieruser():
    menu_compte.destroy()
    global modifier_compte
    modifier_compte = Tk()
    modifier_compte.title("GStock")
    modifier_compte.geometry("600x350+300+200")


    global message
    global username
    global password
    global new
    username = StringVar()
    new = StringVar()
    password = StringVar()
    message = StringVar()
    Label(modifier_compte, width="300", text="Modification d'identifiant", bg="#B90E0E", fg="black").pack()
    Label(modifier_compte, text="Votre nouveau identifiant").place(x=100, y=100)
    Entry(modifier_compte, textvariable=new).place(x=300, y=100)
    Label(modifier_compte, text="Votre mot de passe").place(x=100, y=150)
    Entry(modifier_compte, textvariable=password,show="*").place(x=300, y=150)
    Label(modifier_compte, text="", textvariable=message).place(x=100, y=200)
    Button(modifier_compte, text="Valider", width=20, height=1, bg="orange", command=validerusername).place(x=100,y=250)
    Button(modifier_compte, text="Annuler", width=20, height=1, bg="orange", command=deco13).place(x=300, y=250)
    modifier_compte.mainloop()
def deco13():
    modifier_compte.destroy()
    Menuform1()
#fonction modifier identifiant
def validerusername():
    global cur
    if password.get() == '' or new.get() == '':
        message.set("Vous devez remplir tous les champs !")
    else:
        cur = conn.cursor()
        cur1 = conn.cursor()
        cur.execute("SELECT * FROM  UTILISATEUR where username like ?  ", new.get())
        cur1.execute("SELECT * FROM  UTILISATEUR where id like ? and password=? ", login.var,password.get())
        row1 = cur.fetchone()
        row2=cur1.fetchone()
        if row1==None:
            res='true'
        else:
            res='false'
        if row2==None:
            res='false'
        else:
            res='true'
        if res=='true':
            cur2 = conn.cursor()
            cur2.execute("UPDATE UTILISATEUR SET username=? WHERE id=?   ", new.get(), login.var)
            cur2.commit()
            message.set(" Identifiant est mis à jour !")
            new.set("")
            password.set("")
        else:
            message.set("cet identifiant déja pris ou bien le mot de passe est incorrecte !")
#Form changer mot de passe
def Modifiermdp():
            menu_compte.destroy()
            global modifier_compte
            modifier_compte = Tk()
            modifier_compte.title("GStock")
            modifier_compte.geometry("600x350+300+200")


            global message
            global password
            global newpassword
            global newpassword1
            password = StringVar()
            newpassword = StringVar()
            newpassword1 = StringVar()
            message = StringVar()
            Label(modifier_compte, width="300", text="Changement de mot de passe", bg="#B90E0E", fg="black").pack()
            Label(modifier_compte, text="Votre ancien mot de passe").place(x=100, y=100)
            Entry(modifier_compte, textvariable=password, show="*").place(x=300, y=100)
            Label(modifier_compte, text="Taper votre nouveau mot de passe").place(x=100, y=150)
            Entry(modifier_compte, textvariable=newpassword, show="*").place(x=300, y=150)
            Label(modifier_compte, text="Retaper votre nouveau mot de passe").place(x=100, y=200)
            Entry(modifier_compte, textvariable=newpassword1, show="*").place(x=300, y=200)
            Label(modifier_compte, text="", textvariable=message).place(x=100, y=250)
            Button(modifier_compte, text="Valider", width=20, height=1, bg="orange", command=mdp).place(x=100, y=300)
            Button(modifier_compte, text="Annuler", width=20, height=1, bg="orange", command=deco13).place(x=300, y=300)
            modifier_compte.mainloop()
#fonction changer mot de passe
def mdp():
    global cur
    if password.get() == "" or newpassword.get() == "" or newpassword1.get() == "":
        message.set("Vous devez remplir tous les champs !")
    elif newpassword.get() != newpassword1.get():
        message.set("Retapez votre nouveau mot de passe !")
    else:
        cur = conn.cursor()
        cur1 = conn.cursor()
        cur.execute("SELECT * FROM UTILISATEUR WHERE id=? and password=? ",login.var,password.get())
        row = cur.fetchone()
        if row==None:
            res = 'false'
        else:
            res = 'true'
        if res == 'true':
            cur1.execute("UPDATE UTILISATEUR SET password=? where id=? ", newpassword.get(), login.var)
            cur1.commit()
            message.set("Mot de passe bien changé !")
        else:
            message.set("Impossible votre ancien mot de passe est incorrecte !!")
#fonction supprimer compte
def suppcompte():
    from tkinter.messagebox import askyesno, showinfo, WARNING
    answer = askyesno(title='Confirmation',message='Vous risquez de perdre votre compte. Etes vous sûre ?',icon=WARNING)
    if answer:
        if checkwindow(menu_compte)=='true':
            menu_compte.destroy()
        cur = conn.cursor()
        cur.execute("DELETE FROM UTILISATEUR WHERE id=?", login.var)
        cur.commit()
        #showinfo(title='Compte supprimé',message='votre compte a été supprimé avec succés.')
        Loginform()
    else:
        if checkwindow(menu_compte)!='true':
            Menuform1()
# apres la suppression du compte on deconnecte l'utilisateur
def deco1():
            if checkwindow(menu_compte) == 'true':
                menu_compte.destroy()
                Loginform()
#retourner à la page principale depuis Menu Compte
def retour():
        menu_compte.destroy()
        Menuform()



#GESTION DES PRODUITS
#Form produit
def gererprod():
    menu_screen.destroy()
    global ajoutprod
    ajoutprod = Tk()
    ajoutprod.title("GStock")
    ajoutprod.geometry("600x350+300+200")


    global message
    global ref
    global nom
    global poids
    global fournisseur
    global message
    global variable
    global qte
    qte = StringVar()
    ref = StringVar()
    nom = StringVar()
    poids = StringVar()
    fournisseur = StringVar()
    message = StringVar()
    cur1 = conn.cursor()
    cur1.execute("SELECT distinct nomf FROM  FOURNISSEUR ")
    ans = []
    for row in cur1:
        for f in row:
            ans.append(f)

    variable = StringVar(ajoutprod)
    variable.set(ans[0])  # default value
    w = OptionMenu(ajoutprod, variable, *ans)
    w.place(x=150, y=250)
    if login.var2=='admin':

        Button(ajoutprod, text="Rechercher", width=15, height=1, bg="orange", command=rechercherprod).place(x=400, y=30)
        Button(ajoutprod, text="Ajouter", width=15, height=1, bg="orange", command=ajoutbd).place(x=400, y=70)
        Button(ajoutprod, text="Modifier", width=15, height=1, bg="orange",command=modifierprod).place(x=400, y=110)
        Button(ajoutprod, text="Supprimer", width=15, height=1, bg="orange",command=supprimerprod).place(x=400, y=150)
        Button(ajoutprod, text="Afficher tout", width=15, height=1, bg="orange",command=affpro).place(x=400, y=190)
        Button(ajoutprod, text="Annuler", width=15, height=1, bg="orange",command=retourprod).place(x=400, y=230)
    else:
        Button(ajoutprod, text="Rechercher", width=15, height=1, bg="orange", command=rechercherprod).place(x=400, y=30)
        Button(ajoutprod, text="Ajouter", width=15, height=1, bg="orange", command=ajoutbd).place(x=400, y=70)
        Button(ajoutprod, text="Afficher tout", width=15, height=1, bg="orange", command=affpro).place(x=400, y=110)
        Button(ajoutprod, text="Annuler", width=15, height=1, bg="orange", command=retourprod).place(x=400, y=150)

    Label(ajoutprod, text="Référence").place(x=50, y=50)
    Entry(ajoutprod, textvariable=ref).place(x=150, y=50)
    Label(ajoutprod, text="Designation").place(x=50, y=100)
    Entry(ajoutprod, textvariable=nom).place(x=150, y=100)
    Label(ajoutprod, text="Quantité").place(x=50, y=150)
    Entry(ajoutprod, textvariable=qte).place(x=150, y=150)
    Label(ajoutprod, text="Poids").place(x=50, y=200)
    Entry(ajoutprod, textvariable=poids).place(x=150, y=200)
    Label(ajoutprod, text="Fournisseur").place(x=50, y=250)
    Label(ajoutprod, textvariable=message).place(x=50, y=300)
    ajoutprod.mainloop()
#fonction ajouter produit
def ajoutbd():
    if  nom.get()=="" or poids.get()=="" or qte.get()=="":
        message.set("les champs suivants sont obligatoires à remplir : (Designation,Quantité,Poids,Fournisseur) !")
    else:
        if ref.get()!="":

            cur1=conn.cursor()
            cur1.execute("SELECT * FROM PRODUIT WHERE ref=?",ref.get())
            row1=cur1.fetchone()
            if row1==None:
                cur = conn.cursor()
                cur2 = conn.cursor()
                cur2.execute("SELECT idf FROM FOURNISSEUR WHERE nomf like ?", variable.get())
                row = cur2.fetchone()
                cur.execute("SET IDENTITY_INSERT dbo.PRODUIT ON INSERT INTO PRODUIT(ref,designation,qte,poids,fournisseur) VALUES (?,?,?,?,?) ",ref.get(), nom.get(),qte.get(),poids.get(), row[0])
                cur.commit()
                message.set("Produit ajouté avec succés")
            else:
                message.set("Produit déja existe avec cette réference !")
        else:
            cur = conn.cursor()
            cur2 = conn.cursor()
            cur2.execute("SELECT idf FROM FOURNISSEUR WHERE nomf like ?", variable.get())
            row = cur2.fetchone()
            cur.execute("INSERT INTO PRODUIT(designation,qte,poids,fournisseur) VALUES (?,?,?,?) ",nom.get(),qte.get(),poids.get(), row[0])
            cur.commit()
            message.set("Produit ajouté avec succés")
#fonction rechercher produit
def rechercherprod():
    cur = conn.cursor()
    cur.execute("SELECT p.ref,p.designation,p.poids,p.qte,f.nomf FROM  PRODUIT p inner join FOURNISSEUR f on p.fournisseur=f.idf where ref=? ",ref.get())
    if cur == None:
        res = 'false'
    else:
        res = 'true'
    if ref.get() == "":
        message.set("Vous devez entrer la reference de votre produit")
    if res == 'true':
        my_w = Tk()
        a = Entry(my_w, width=30, fg='red')
        a.grid(row=0, column=0)
        a.insert(END, "REF")
        a = Entry(my_w, width=30, fg='red')
        a.grid(row=0, column=1)
        a.insert(END, "DESIGNATION")
        a = Entry(my_w, width=30, fg='red')
        a.grid(row=0, column=2)
        a.insert(END, "POIDS")
        a = Entry(my_w, width=30, fg='red')
        a.grid(row=0, column=3)
        a.insert(END, "QUANTITE")
        a = Entry(my_w, width=30, fg='red')
        a.grid(row=0, column=4)
        a.insert(END, "FOURNISSEUR")
        i = 1
        for student in cur:
            for j in range(len(student)):
                e = Entry(my_w, width=30, fg='blue')
                e.grid(row=i, column=j)
                e.insert(END, student[j])
            i = i + 1
        my_w.mainloop()
    else:
        message.set("Produit introuvable ! ")
#fonction modifier produit
def modifierprod():
    message.set("")
    if ref.get()=="":
        message.set("Vous devez saisir la réference du produit !")
    else:
        cur = conn.cursor()
        cur.execute("SELECT * FROM  PRODUIT where ref=? ",ref.get())
        row = cur.fetchone()
        if row == None:
            message.set("Aucun produit avec cette reference !")
        else:
            cur1 = conn.cursor()
            cur2 = conn.cursor()
            cur2.execute("SELECT idf FROM FOURNISSEUR WHERE nomf=?",variable.get())
            row1=cur2.fetchone()
            cur1.execute("UPDATE PRODUIT SET designation=? ,qte=?,poids=? ,fournisseur=? WHERE ref=?",nom.get(),qte.get(),poids.get(),row1[0],ref.get())
            cur1.commit()
            message.set("Produit modifié avec succes !")
#fonction supprimer produit
def supprimerprod():
    message.set("")
    if ref.get()=="":
        message.set("Vous devez saisir la réference du produit !")
    else:
        cur = conn.cursor()
        cur.execute("SELECT * FROM  PRODUIT where ref=? ",ref.get())
        row = cur.fetchone()
        if row == None:
            message.set("Aucun produit avec cette reference !")
        else:
            cur1 = conn.cursor()
            cur1.execute("DELETE FROM PRODUIT WHERE ref=?",ref.get())
            cur1.commit()
            message.set("Produit supprimé avec succes !")
#fonction afficher tout les produits
def affpro():
    cur = conn.cursor()
    cur.execute("SELECT p.ref,p.designation,p.poids,p.qte,f.nomf FROM  PRODUIT p inner join FOURNISSEUR f on p.fournisseur=f.idf  ")
    my_w = Tk()
    a = Entry(my_w, width=30, fg='red')
    a.grid(row=0, column=0)
    a.insert(END, "REF PROD")
    a = Entry(my_w, width=30, fg='red')
    a.grid(row=0, column=1)
    a.insert(END, "DESIGNATION")
    a = Entry(my_w, width=30, fg='red')
    a.grid(row=0, column=2)
    a.insert(END, "POIDS")
    a = Entry(my_w, width=30, fg='red')
    a.grid(row=0, column=3)
    a.insert(END, "QUANTITE")
    a = Entry(my_w, width=30, fg='red')
    a.grid(row=0, column=4)
    a.insert(END, "FOURNISSEUR")
    i=1
    for student in cur:
        for j in range(len(student)):
            e = Entry(my_w, width=30, fg='blue')
            e.grid(row=i, column=j)
            e.insert(END, student[j])
        i = i + 1
    my_w.mainloop()
#retourner à la page principale depuis form de produit
def retourprod():
    ajoutprod.destroy()
    Menuform()


#GESTION DES FOURNISSEURS
#Form fournisseur
def gestionfournisseur():
    menu_screen.destroy()
    global ajoutprod
    ajoutprod = Tk()
    ajoutprod.title("GStock")
    ajoutprod.geometry("600x350+300+200")


    global message
    global ref
    global nom
    global fournisseur
    global message
    global variable
    global id_f
    global pays
    id_f = StringVar()
    nom = StringVar()
    pays = StringVar()
    fournisseur = StringVar()
    message = StringVar()
    Label(ajoutprod, text="ID Fournisseur").place(x=50, y=50)
    Entry(ajoutprod, textvariable=id_f).place(x=150, y=50)
    Label(ajoutprod, text="Nom").place(x=50, y=100)
    Entry(ajoutprod, textvariable=nom).place(x=150, y=100)
    Label(ajoutprod, text="Pays").place(x=50, y=150)
    Entry(ajoutprod, textvariable=pays).place(x=150, y=150)
    Label(ajoutprod, text="", textvariable=message).place(x=50, y=200)
    if login.var2 == 'admin':
        Button(ajoutprod, text="Rechercher", width=15, height=1, bg="orange",command=rchfour).place(x=400, y=30)
        Button(ajoutprod, text="Ajouter", width=15, height=1, bg="orange",command=ajouterfour).place(x=400, y=70)
        Button(ajoutprod, text="Modifier", width=15, height=1, bg="orange",command=modifierfour).place(x=400, y=110)
        Button(ajoutprod, text="Supprimer", width=15, height=1, bg="orange",command=supprimerfour).place(x=400, y=150)
        Button(ajoutprod, text="Afficher tout", width=15, height=1, bg="orange",command=afft).place(x=400, y=190)
        Button(ajoutprod, text="Annuler", width=15, height=1, bg="orange", command=retourprod).place(x=400, y=230)
    else:
        Button(ajoutprod, text="Rechercher", width=15, height=1, bg="orange", command=rchfour).place(x=400, y=30)
        Button(ajoutprod, text="Ajouter", width=15, height=1, bg="orange", command=ajouterfour).place(x=400, y=70)
        Button(ajoutprod, text="Afficher tout", width=15, height=1, bg="orange", command=afft).place(x=400, y=110)
        Button(ajoutprod, text="Annuler", width=15, height=1, bg="orange", command=retourprod).place(x=400, y=150)

    ajoutprod.mainloop()
#fonction afficher tout les fournisseurs
def afft():
    cur = conn.cursor()
    cur.execute("SELECT * FROM  Fournisseur  ")
    my_w = Tk()
    a = Entry(my_w, width=30, fg='red')
    a.grid(row=0, column=0)
    a.insert(END, "id fournisseur")
    a = Entry(my_w, width=30, fg='red')
    a.grid(row=0, column=1)
    a.insert(END, "nom fournisseur")
    a = Entry(my_w, width=30, fg='red')
    a.grid(row=0, column=2)
    a.insert(END, "pays")
    i = 1
    for student in cur:
        for j in range(len(student)):
            e = Entry(my_w, width=30, fg='blue')
            e.grid(row=i, column=j)
            e.insert(END, student[j])
        i = i + 1
    my_w.mainloop()
#fonction rechercher fournisseur
def rchfour():
    cur = conn.cursor()
    cur.execute("SELECT * FROM  Fournisseur where idf=? ",id_f.get())
    my_w = Tk()
    a = Entry(my_w, width=30, fg='red')
    a.grid(row=0, column=0)
    a.insert(END, "id fournisseur")
    a = Entry(my_w, width=30, fg='red')
    a.grid(row=0, column=1)
    a.insert(END, "nom fournisseur")
    a = Entry(my_w, width=30, fg='red')
    a.grid(row=0, column=2)
    a.insert(END, "pays")
    i = 1
    for student in cur:
        for j in range(len(student)):
            e = Entry(my_w, width=30, fg='blue')
            e.grid(row=i, column=j)
            e.insert(END, student[j])
        i = i + 1
    my_w.mainloop()
#fonction ajouter fournisseur
def ajouterfour():
    if   nom.get()=="" or pays.get()=="":
        message.set(" Tous les champs sont obligatoires à remplir  !")
    else:
        if id_f.get()!="":

            cur1=conn.cursor()
            cur1.execute("SELECT * FROM FOURNISSEUR WHERE idf=?",id_f.get())
            row1=cur1.fetchone()
            if row1==None:
                cur = conn.cursor()
                cur.execute("SET IDENTITY_INSERT dbo.FOURNISSEUR ON INSERT INTO FOURNISSEUR(idf,nomf,pays) VALUES (?,?,?) ",id_f.get(), nom.get(), pays.get())
                cur.commit()
                message.set("Fournisseur ajouté avec succés")
            else:
                message.set("Fournisseur déja existe avec cet id !")
        else:
            cur = conn.cursor()
            cur.execute("INSERT INTO FOURNISSEUR(nomf,pays) VALUES (?,?) ",nom.get(),pays.get())
            cur.commit()
            message.set("Fournisseur ajouté avec succés")
#fonction modifier fournisseur
def modifierfour():
    message.set("")
    if id_f.get() == "" or nom.get()=="" or pays.get()=="":
        message.set("Vous devez saisir l'identifiant du fournisseur !")
    else:
        cur = conn.cursor()
        cur.execute("SELECT * FROM  FOURNISSEUR where idf=? ", id_f.get())
        row = cur.fetchone()
        if row == None:
            message.set("Aucun Fournisseur avec cet id !")
        else:
            cur1 = conn.cursor()
            cur1.execute("UPDATE FOURNISSEUR SET nomf=? ,pays=?  WHERE idf=?", nom.get(), pays.get(),id_f.get())
            cur1.commit()
            message.set("Fournisseur modifié avec succes !")
#fonction supprimer fournisseur
def supprimerfour():
    message.set("")
    if id_f.get()=="":
        message.set("Vous devez saisir l'identifiant du fournisseur !")
    else:
        cur = conn.cursor()
        cur.execute("SELECT * FROM  FOURNISSEUR where idf=? ",id_f.get())
        row = cur.fetchone()
        if row == None:
            message.set("Aucun fournisseur avec cet id !")
        else:
            cur1 = conn.cursor()
            cur1.execute("DELETE FROM FOURNISSEUR WHERE idf=?",id_f.get())
            cur1.commit()
            message.set("Fournisseur supprimé avec succes !")

#bouton deconnexion
def deco():
    if checkwindow(menu_screen)=='true':
        menu_screen.destroy()
        Loginform()



#fonction pour savoir si une form est ouverte ou pas
def checkwindow(name):
    if name.state()=='normal':
        return 'true'
    else:
        return 'false'

#Form d'admin pour supprimer un user
def gereruser():
    menu_compte.destroy()
    global supp_usr
    supp_usr = Tk()
    supp_usr.title("GStock")
    supp_usr.geometry("600x350+300+200")

    global message
    global username
    username=StringVar()
    message = StringVar()
    Label(supp_usr, width="300", text="Suppression d'un utilisateur", bg="#B90E0E", fg="black").pack()
    Label(supp_usr, text="Identifiant de l'utilisateur").place(x=100, y=100)
    Entry(supp_usr, textvariable=username).place(x=300, y=100)
    Label(supp_usr, text="", textvariable=message).place(x=100, y=200)
    Button(supp_usr, text="Supprimer", width=20, height=1, bg="orange", command=deletehim).place(x=100, y=250)
    Button(supp_usr, text="Retour", width=20, height=1, bg="orange", command=retourmenu).place(x=300,y=250)
    supp_usr.mainloop()
#fonction pour supprimer un user
def deletehim():
    if username.get()=="":
        message.set("Vous devez remplir tous l'identifiant de l'utilisateur' !")
    else:
        cur =conn.cursor()
        cur.execute("SELECT typecpt FROM UTILISATEUR WHERE username=?",username.get())
        row = cur.fetchone()
        if row==None:
            message.set("Aucun utilisateur avec cet identifiant !")
        else:
            if row[0]=="user":
                cur1=conn.cursor()
                cur1.execute("DELETE FROM UTILISATEUR WHERE username=?",username.get())
                cur1.commit()
                message.set("Utilisateur supprimé avec succes ")
            else:
                message.set("Vous n'avez pas le droit pour supprimer cet utilisateur ! ")
def retourmenu():
    supp_usr.destroy()
    Menuform1()


#GESTION DES OPERATIONS
#form operation
def gererop():
    from tkinter import ttk
    menu_screen.destroy()
    global op_menu
    op_menu = Tk()
    op_menu.title("GStock")
    op_menu.geometry("600x400+300+200")


    global message
    global ref
    global idop
    global date
    global qte
    global prix
    global excombo
    global call
    global com
    com = StringVar()
    qte = IntVar()
    ref = StringVar()
    nom = StringVar()
    idop = StringVar()
    prix = StringVar()
    message = StringVar()
    call = StringVar()
    Button(op_menu, text="Ajouter", width=15, height=1, bg="orange",command=ajouterop).place(x=400, y=100)
    Button(op_menu, text="Afficher entrées", width=15, height=1, bg="orange", command=afficherentr).place(x=400, y=140)
    Button(op_menu, text="Afficher sorties", width=15, height=1, bg="orange", command=affichersor).place(x=400, y=180)
    Button(op_menu, text="Afficher tout", width=15, height=1, bg="orange", command=afficherop).place(x=400, y=220)
    Button(op_menu, text="Annuler", width=15, height=1, bg="orange",command=retourop).place(x=400, y=260)



    Label(op_menu, text="Id Operation").place(x=50, y=50)
    Entry(op_menu, textvariable=idop).place(x=150, y=50)
    Label(op_menu, text="Réference").place(x=50, y=100)
    Entry(op_menu, textvariable=ref).place(x=150, y=100)
    Label(op_menu, text="Quantité").place(x=50, y=150)
    Entry(op_menu, textvariable=qte).place(x=150, y=150)
    Label(op_menu, text="Prix").place(x=50, y=200)
    Entry(op_menu, textvariable=prix).place(x=150, y=200)
    Label(op_menu, text="Date").place(x=50, y=250)
    cal = DateEntry(op_menu, width=12, year=2022, month=5, day=27,background='darkblue', foreground='white', borderwidth=2,textvariable=call).place(x=150,y=250)
    Label(op_menu, text=" Type opération").place(x=50, y=300)
    excombo=ttk.Combobox(op_menu,values=["entrée","sortie"],textvariable=com,state="readonly").place(x=150,y=300)
    Label(op_menu, textvariable=message).place(x=50, y=350)
    op_menu.mainloop()
#retourner à la page principale
def retourop():
    op_menu.destroy()
    Menuform()
#ajouter operation
def ajouterop():
    if ref.get() == "" or qte.get() == "" or prix.get() == "" or com.get()=="":
        message.set("les champs suivants sont obligatoires à remplir : (reference,Quantité,prix,type operation) !")
    else:
        if ref.get() != "":
            cur = conn.cursor()
            cur.execute("SELECT * FROM PRODUIT WHERE ref=?", ref.get())
            row1 = cur.fetchone()
            if row1 == None:
                message.set("Produit n'existe pas")
            else:
                cur1 = conn.cursor()
                cur1.execute("SELECT qte FROM PRODUIT WHERE ref=?", ref.get())
                row2 = cur1.fetchone()
                if com.get() == "entrée":
                    cur3 = conn.cursor()
                    cur4 = conn.cursor()
                    cur4.execute("INSERT INTO OPERATIONS (ref,dateop,qte,prix,typeop) VALUES (?,?,?,?,?) ", ref.get(),call.get(), qte.get(), prix.get(), com.get())
                    cur4.commit()
                    cur3.execute("UPDATE PRODUIT SET qte= qte + ? WHERE ref=?   ", qte.get(), ref.get())
                    cur3.commit()
                    message.set("Opération bien ajouté")
                if com.get() == "sortie" and qte.get() <= row2[0]:
                    cur2 = conn.cursor()
                    cur3 = conn.cursor()
                    cur2.execute("INSERT INTO OPERATIONS (ref,dateop,qte,prix,typeop) VALUES (?,?,?,?,?) ", ref.get(),call.get(), qte.get(),prix.get(), com.get())
                    cur2.commit()
                    cur3.execute("UPDATE PRODUIT SET qte= qte - ? WHERE ref=?   ", qte.get(), ref.get())
                    cur3.commit()
                    message.set("Opération bien ajouté")
                if com.get() == "sortie" and qte.get() > row2[0]:
                    message.set("quantite indisponible ")
#afficher toutes les operations
def afficherop():
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM OPERATIONS  ")
    my_w = Tk()
    a = Entry(my_w, width=30, fg='red')
    a.grid(row=0, column=0)
    a.insert(END, "ID OPERATION")
    a = Entry(my_w, width=30, fg='red')
    a.grid(row=0, column=1)
    a.insert(END, "REFERENCE")
    a = Entry(my_w, width=30, fg='red')
    a.grid(row=0, column=2)
    a.insert(END, "DATE OPERATION")
    a = Entry(my_w, width=30, fg='red')
    a.grid(row=0, column=3)
    a.insert(END, "QUANTITE")
    a = Entry(my_w, width=30, fg='red')
    a.grid(row=0, column=4)
    a.insert(END, "PRIX")
    a = Entry(my_w, width=30, fg='red')
    a.grid(row=0, column=5)
    a.insert(END, "TYPE OPERATION")
    i = 1
    for student in cur:
        for j in range(len(student)):
            e = Entry(my_w, width=30, fg='blue')
            e.grid(row=i, column=j)
            e.insert(END, student[j])
        i = i + 1
    my_w.mainloop()
#afficher les entrées
def afficherentr():
    cur = conn.cursor()
    cur.execute( "SELECT o.dateop,o.idop,p.designation,o.qte,o.prix FROM OPERATIONS o inner join PRODUIT p on o.ref=p.ref where typeop='entrée' order by o.dateop desc")
    my_w = Tk()
    a = Entry(my_w, width=30, fg='red')
    a.grid(row=0, column=0)
    a.insert(END, "DATE OPERATION")
    a = Entry(my_w, width=30, fg='red')
    a.grid(row=0, column=1)
    a.insert(END, "ID OPERATION")
    a = Entry(my_w, width=30, fg='red')
    a.grid(row=0, column=2)
    a.insert(END, "PRODUIT")
    a = Entry(my_w, width=30, fg='red')
    a.grid(row=0, column=3)
    a.insert(END, "QUANTITE")
    a = Entry(my_w, width=30, fg='red')
    a.grid(row=0, column=4)
    a.insert(END, "PRIX")
    i = 1
    for student in cur:
        for j in range(len(student)):
            e = Entry(my_w, width=30, fg='blue')
            e.grid(row=i, column=j)
            e.insert(END, student[j])
        i = i + 1
    my_w.mainloop()
#afficher les sorties
def affichersor():
    cur = conn.cursor()
    cur.execute( "SELECT o.dateop,o.idop,p.designation,o.qte,o.prix FROM OPERATIONS o inner join PRODUIT p on o.ref=p.ref where typeop='sortie' order by dateop desc")
    my_w = Tk()
    a = Entry(my_w, width=30, fg='red')
    a.grid(row=0, column=0)
    a.insert(END, "DATE OPERATION")
    a = Entry(my_w, width=30, fg='red')
    a.grid(row=0, column=1)
    a.insert(END, "ID OPERATION")
    a = Entry(my_w, width=30, fg='red')
    a.grid(row=0, column=2)
    a.insert(END, "PRODUIT")
    a = Entry(my_w, width=30, fg='red')
    a.grid(row=0, column=3)
    a.insert(END, "QUANTITE")
    a = Entry(my_w, width=30, fg='red')
    a.grid(row=0, column=4)
    a.insert(END, "PRIX")
    i = 1
    for student in cur:
        for j in range(len(student)):
            e = Entry(my_w, width=30, fg='blue')
            e.grid(row=i, column=j)
            e.insert(END, student[j])
        i = i + 1
    my_w.mainloop()

#lancement du programme
Loginform()





import pymysql.cursors
import webbrowser
import requests
from google_drive_downloader import GoogleDriveDownloader as gdd
import sys



# Connect to the database.
####################################
connection = pymysql.connect(host='',
                             user='',
                             password='',
                             db='',
                             charset='',
                             cursorclass=pymysql.cursors.DictCursor)



mycursor = connection.cursor()



#### Συναρτήσεις που δίνουν την δυνατότητα στον χρήστη να αναζητήσει ΑΜΕΣΑ δλδ πληκτρολογώντας το ονομα αυτού που ψάχνει
##===================================================================================================================##
def key_words():
    print("Δώσε μας τη λέξη κλειδί για αναζήτηση σε τίτλο άρθρου")
    s1="select `ΤΙΤΛΟΣ`, `ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ` FROM `ΕΠΙΣΤΗΜΟΝΙΚΟ ΑΡΘΡΟ` where `ΤΙΤΛΟΣ` LIKE '%s' " %("%"+input()+"%")
    mycursor.execute(s1)
    a=mycursor.fetchall()
    while True:
        if len(a)>1:
            c1=[]
            c2=[]
            for i in a:
                
                b=i.get('ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ')
                c1.append(b)
                d=i.get('ΤΙΤΛΟΣ')
                c2.append(i.get('ΤΙΤΛΟΣ'))
            what_to_do_with_article(c1,c2)
            break
        elif len(a)==1:
            c1=[]
            c2=[]
            for i in a:
                b=i.get('ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ')
                c1.append(b)
                d=i.get('ΤΙΤΛΟΣ')
                c2.append(i.get('ΤΙΤΛΟΣ'))
            what_to_do_with_article(c1,c2)
            break
        else:
            print("Η αναζήτηση που κάνατε δεν οδήγησε σε κάποιο άρθρο. Προσπαθήστε ξανά...:")
            s1="select `ΤΙΤΛΟΣ`, `ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ` FROM `ΕΠΙΣΤΗΜΟΝΙΚΟ ΑΡΘΡΟ` where `ΤΙΤΛΟΣ` LIKE '%s' " %("%"+input()+"%")
            mycursor.execute(s1)
            a=mycursor.fetchall()




def author_search():
    print("Όνοματεπώνυμο συγγραφέα για αναζήτηση:")
    b = input()
    b = b.split()
    b = ''.join(b)
    sql = """   SELECT `ΣΥΓΓΡΑΦΕΑΣ`.`ΟΝΟΜΑ` , `ΣΥΓΓΡΑΦΕΑΣ`.`ΕΠΩΝΥΜΟ` 
                FROM (select `ΣΥΓΓΡΑΦΕΑΣ`.`ΚΩΔΙΚΟΣ ΣΥΓΓΡΑΦΕΑ` AS `ΚΩΔΙΚΟΣ ΣΥΓΓΡΑΦΕΑ`,concat(`ΣΥΓΓΡΑΦΕΑΣ`.`ΟΝΟΜΑ`,`ΣΥΓΓΡΑΦΕΑΣ`.`ΕΠΩΝΥΜΟ`) AS `flname` from `ΣΥΓΓΡΑΦΕΑΣ`) AS A1
                JOIN `ΣΥΓΓΡΑΦΕΑΣ` ON A1.`ΚΩΔΙΚΟΣ ΣΥΓΓΡΑΦΕΑ` = `ΣΥΓΓΡΑΦΕΑΣ`.`ΚΩΔΙΚΟΣ ΣΥΓΓΡΑΦΕΑ`
                WHERE flname LIKE '%s'""" %("%"+b+"%")
    mycursor.execute(sql)
    a=mycursor.fetchall()

    while True:
        if len(a)>1:
            j=1
            print("\nΗ ΑΝΑΖΗΤΗΣΗ ΣΑΣ ΟΔΗΓΗΣΕ ΣΤΟΥΣ ΑΚΟΛΟΥΘΟΥΣ ΣΥΓΓΡΑΦΕΙΣ:")
            print("=======================================================")
            for i in a:
                print(j,i.get("ΟΝΟΜΑ"), i.get("ΕΠΩΝΥΜΟ"))
                j=j+1
            while True:
                b = (input("ΠΛΗΚΤΡΟΛΟΓΗΣΤΕ ΤΟΝ ΑΡΙΘΜΟ ΠΟΥ ΑΝΤΙΣΤΟΙΧΕΙ ΣΤΟΝ ΣΥΓΓΡΑΦΕΑ ΠΟΥ ΑΝΑΖΗΤΗΣΑΤΕ:"))
                if b.isdigit()==True and int(b)!=0:
                    if int(b)-1 < (j-1):break
                    else:print("\nΔώστε έγκυρο αριθμό...")
                else:print("\nΔώστε έγκυρο αριθμό...")
            string = [a[int(b)-1].get("ΟΝΟΜΑ"),a[int(b)-1].get("ΕΠΩΝΥΜΟ")]
            print(string[0],string[1])
            print("\nΤο προφίλ του συγγραφέα που αναζητήσατε είναι το εξής:")
            print("=======================================================")
            fa = """SELECT `ΟΝΟΜΑ`, `ΕΠΩΝΥΜΟ`, `ΧΩΡΑ ΚΑΤΑΓΩΓΗΣ`
                    FROM `ΣΥΓΓΡΑΦΕΑΣ`
                    WHERE `ΟΝΟΜΑ` LIKE '%s' AND `ΕΠΩΝΥΜΟ` LIKE '%s'""" %(string[0],string[1])
            mycursor.execute(fa)
            info2 = mycursor.fetchall()
            info22=[]
            for i in info2:
                info22.append(list(i.values()))
            for i in range(len(info22)) :
                print("ΟΝΟΜΑ:",info22[i][0],", ΕΠΩΝΥΜΟ:",info22[i][1], ", ΧΩΡΑ ΚΑΤΑΓΩΓΗΣ:", info22[i][2])
            print("=======================================================")
            print('\nοκ, ... Αναζήτηση άρθρων του συγγραφέα:', string[0], string[1])
            sql="select `ΚΩΔΙΚΟΣ ΣΥΓΓΡΑΦΕΑ` FROM `ΣΥΓΓΡΑΦΕΑΣ` WHERE `ΟΝΟΜΑ` LIKE '%s' AND `ΕΠΩΝΥΜΟ` LIKE '%s'" %(string[0],string[1])
            mycursor.execute(sql)
            result=mycursor.fetchall()
            break
        elif len(a)==1:
            print("\nΟ ΣΥΓΓΡΑΦΕΑΣ ΠΟΥ ΒΡΕΘΗΚΕ ΕΙΝΑΙ Ο ΑΚΟΛΟΥΘΟΣ:")
            print("==============================================")
            for i in a:
                s1=i.get("ΟΝΟΜΑ")
                s2=i.get("ΕΠΩΝΥΜΟ")
                print(i.get("ΟΝΟΜΑ"), i.get("ΕΠΩΝΥΜΟ"))
                
            print("\nΤο προφίλ του συγγραφέα που αναζητήσατε είναι το εξής:")
            print("=======================================================")
            fa = """SELECT `ΟΝΟΜΑ`, `ΕΠΩΝΥΜΟ`, `ΧΩΡΑ ΚΑΤΑΓΩΓΗΣ`
                    FROM `ΣΥΓΓΡΑΦΕΑΣ`
                    WHERE `ΟΝΟΜΑ` LIKE '%s' AND `ΕΠΩΝΥΜΟ` LIKE '%s'""" %(s1,s2)
            mycursor.execute(fa)
            info2 = mycursor.fetchall()
            info22=[]
            for i in info2:
                info22.append(list(i.values()))
            for i in range(len(info22)) :
                print("ΟΝΟΜΑ:",info22[i][0],", ΕΠΩΝΥΜΟ:",info22[i][1], ", ΧΩΡΑ ΚΑΤΑΓΩΓΗΣ:", info22[i][2])
            print("=======================================================")
            print('\nοκ, ... Αναζήτηση άρθρων του συγγραφέα:', s1, s2)
            sql="select `ΚΩΔΙΚΟΣ ΣΥΓΓΡΑΦΕΑ` FROM `ΣΥΓΓΡΑΦΕΑΣ` WHERE `ΟΝΟΜΑ` LIKE '%s' AND `ΕΠΩΝΥΜΟ` LIKE '%s'" %(s1,s2)
            mycursor.execute(sql)
            result=mycursor.fetchall()
            break
        else:
            print("Ο συγγραφέας που αναζητάτε δεν υπάρχει. Προσπαθήστε ξανά...:")
            b = input()
            b = b.split()
            b = ''.join(b)
            sql ="""SELECT `ΣΥΓΓΡΑΦΕΑΣ`.`ΟΝΟΜΑ` , `ΣΥΓΓΡΑΦΕΑΣ`.`ΕΠΩΝΥΜΟ` 
                    FROM (select `ΣΥΓΓΡΑΦΕΑΣ`.`ΚΩΔΙΚΟΣ ΣΥΓΓΡΑΦΕΑ` AS `ΚΩΔΙΚΟΣ ΣΥΓΓΡΑΦΕΑ`,concat(`ΣΥΓΓΡΑΦΕΑΣ`.`ΟΝΟΜΑ`,`ΣΥΓΓΡΑΦΕΑΣ`.`ΕΠΩΝΥΜΟ`) AS `flname` from `ΣΥΓΓΡΑΦΕΑΣ`) AS A1
                    JOIN `ΣΥΓΓΡΑΦΕΑΣ` ON A1.`ΚΩΔΙΚΟΣ ΣΥΓΓΡΑΦΕΑ` = `ΣΥΓΓΡΑΦΕΑΣ`.`ΚΩΔΙΚΟΣ ΣΥΓΓΡΑΦΕΑ`
                    WHERE flname LIKE '%s' """ %("%"+b+"%")
            mycursor.execute(sql)
            a=mycursor.fetchall()


    if mycursor.rowcount>0:
        a=result[0]['ΚΩΔΙΚΟΣ ΣΥΓΓΡΑΦΕΑ']
        sql="select DISTINCT `ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ` FROM συγγράφει where `ΚΩΔΙΚΟΣ ΣΥΓΓΡΑΦΕΑ`='%s'"%a
        mycursor.execute(sql)
        result=mycursor.fetchall()
        result2=[]
        c1=[]
        for i in range(len(result)):
            b=result[i]['ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ']
            c1.append(b)
            sql="select `ΤΙΤΛΟΣ` from `ΕΠΙΣΤΗΜΟΝΙΚΟ ΑΡΘΡΟ` where `ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ`='%s'"%b
            mycursor.execute(sql)
            result2.append(mycursor.fetchall())
        if len(result2) !=0:
            c2=[]
            for i in range(len(result2)):
                c2.append(result2[i][0]['ΤΙΤΛΟΣ'])
            what_to_do_with_article(c1,c2)
        else:print("\nΛυπούμαστε αλλά δεν υπάρχουν άρθρα του συγκεκριμένου συγγραφέα!!\n\n")            
        
    elif mycursor.rowcount==0:
        print("Το όνομα που πληκτρολογήσατε δεν υπάρχει στην λίστα. Προσπαθήστε ξανά..")
        author_search()

def magazine_search():
    print("'Ονομα περιοδικού για αναζήτηση:")
    magaz_name="select `ΟΝΟΜΑ` FROM ΠΕΡΙΟΔΙΚΟ where `ΟΝΟΜΑ` LIKE '%s' " %("%"+input()+"%")
    mycursor.execute(magaz_name)
    a=(mycursor.fetchall())
    while True:
        if len(a)>1:
            j=1
            print("\nΗ ΑΝΑΖΗΤΗΣΗ ΣΑΣ ΟΔΗΓΗΣΕ ΣΤΑ ΑΚΟΛΟΥΘΑ ΠΕΡΙΟΔΙΚΑ:")
            print("==============================================")
            for i in a:
                print(j,i.get("ΟΝΟΜΑ"))
                j=j+1
            while True:
                b = (input("ΠΛΗΚΤΡΟΛΟΓΗΣΤΕ ΤΟΝ ΑΡΙΘΜΟ ΠΟΥ ΑΝΤΙΣΤΟΙΧΕΙ ΣΤΟ ΠΕΡΙΟΔΙΚΟ ΠΟΥ ΑΝΑΖΗΤΗΣΑΤΕ:"))
                if b.isdigit()==True and int(b)!=0:
                    if int(b)-1 < (j-1):break
                    else:print("\nΔώστε έγκυρο αριθμό ...")
                else:print("\nΔώστε έγκυρο αριθμό ...")
            string = a[int(b)-1].get("ΟΝΟΜΑ")
            print("\nΤο προφίλ του περιοδικού που αναζητήσατε είναι το εξής:")
            print("=======================================================")
            fm = """SELECT `ΟΝΟΜΑ`, `ΕΚΔΟΤΗΣ`
            FROM `ΠΕΡΙΟΔΙΚΟ`
            WHERE `ΟΝΟΜΑ` LIKE %s"""
            mycursor.execute(fm,(string,))
            info1 = mycursor.fetchall()
            info11=[]
            for i in info1:
                info11.append(list(i.values()))
            for i in range(len(info11)) :
                print(info11[i][0],", ΕΚΔΟΤΗΣ:",info11[i][1])
            print("=======================================================")
            print('\nοκ, ... Αναζήτηση άρθρων του περιοδικού:', string)
            sql="select `ΚΩΔΙΚΟΣ ΠΕΡΙΟΔΙΚΟΥ` FROM ΠΕΡΙΟΔΙΚΟ where `ΟΝΟΜΑ` LIKE '%s' " %string
            mycursor.execute(sql)
            result=mycursor.fetchall()
            break
        elif len(a)==1:
            print("ΤΟ ΠΕΡΙΟΔΙΚΟ ΠΟΥ ΒΡΕΘΗΚΕ ΕΙΝΑΙ ΤΟ ΑΚΟΛΟΥΘΟ:")
            print("==============================================")
            for i in a:
                string=i.get("ΟΝΟΜΑ")
                print(string)
            ## ΠΛΗΡΟΦΟΡΙΕΣ ΓΙΑ ΤΟ ΠΕΡΙΟΔΙΚΟ ΠΟΥ ΒΡΕΘΗΚΕ
            print("\nΤο προφίλ του περιοδικού που αναζητήσατε είναι το εξής:")
            print("=======================================================")
            fm = """SELECT `ΟΝΟΜΑ`, `ΕΚΔΟΤΗΣ`
            FROM `ΠΕΡΙΟΔΙΚΟ`
            WHERE `ΟΝΟΜΑ` LIKE %s"""
            mycursor.execute(fm,(string,))
            info1 = mycursor.fetchall()
            info11=[]
            for i in info1:
                info11.append(list(i.values()))
            for i in range(len(info11)) :
                print(info11[i][0],", ΕΚΔΟΤΗΣ:",info11[i][1])
            print("=======================================================")
            print('\nοκ, ... Αναζήτηση άρθρων του περιοδικού:', string)
            sql="select `ΚΩΔΙΚΟΣ ΠΕΡΙΟΔΙΚΟΥ` FROM ΠΕΡΙΟΔΙΚΟ where `ΟΝΟΜΑ` LIKE '%s' " %string
            mycursor.execute(sql)
            result=mycursor.fetchall()
            break
        else:
            print("Το περιοδικό που αναζητάτε δεν υπάρχει. Προσπαθήστε ξανά...:")
            magaz_name="select `ΟΝΟΜΑ` FROM ΠΕΡΙΟΔΙΚΟ where `ΟΝΟΜΑ` LIKE '%s' " %("%"+input()+"%")
            mycursor.execute(magaz_name)
            a=(mycursor.fetchall())
        
    if mycursor.rowcount>0:
        a=result[0]['ΚΩΔΙΚΟΣ ΠΕΡΙΟΔΙΚΟΥ']
        sql="select `ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ` FROM περιλαμβάνεται where `ΚΩΔΙΚΟΣ ΠΕΡΙΟΔΙΚΟΥ`='%s'"%a
        mycursor.execute(sql)
        result=mycursor.fetchall()
        result2=[]
        global c1
        c1=[]
        for i in range(len(result)):
            b=result[i]['ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ']
            c1.append(b)
            sql="select `ΤΙΤΛΟΣ` from `ΕΠΙΣΤΗΜΟΝΙΚΟ ΑΡΘΡΟ` where `ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ`='%s'"%b
            mycursor.execute(sql)
            result2.append(mycursor.fetchall())
        if len(result2):
            c2=[]
            for i in range(len(result2)):
                c2.append(result2[i][0]['ΤΙΤΛΟΣ'])
            what_to_do_with_article(c1,c2)
        else:print("\nΛυπούμαστε αλλά δεν υπάρχουν άρθρα του συγκεκριμένου περιοδικού!!\n\n")

        
    elif mycursor.rowcount==0:
        print("Το όνομα που πληκτρολογήσατε δεν υπάρχει στην λίστα. Προσπαθήστε ξανά..")
        magazine_search()


def episthmoniko_pedio_search():
    print("Επιστημονικό πεδίο για αναζήτηση:")      
    subj_name="select `ΟΝΟΜΑ` FROM `ΕΠΙΣΤΗΜΟΝΙΚΟ ΠΕΔΙΟ` where `ΟΝΟΜΑ` LIKE '%s' " %("%"+input()+"%")
    mycursor.execute(subj_name)
    a=(mycursor.fetchall())
    while True:
        if len(a)>1:
            j=1
            print("Η ΑΝΑΖΗΤΗΣΗ ΣΑΣ ΟΔΗΓΗΣΕ ΣΤΑ ΑΚΟΛΟΥΘΑ ΕΠΙΣΤΗΜΟΝΙΚΑ ΠΕΔΙΑ:")
            print("=======================================================")
            for i in a:
                print(j,i.get("ΟΝΟΜΑ"))
                j=j+1
            while True:
                b = (input("ΠΛΗΚΤΡΟΛΟΓΗΣΤΕ ΤΟΝ ΑΡΙΘΜΟ ΠΟΥ ΑΝΤΙΣΤΟΙΧΕΙ ΣΤΟ ΕΠΙΣΤΗΜΟΝΙΚΟ ΠΕΔΙΟ ΠΟΥ ΑΝΑΖΗΤΗΣΑΤΕ:"))
                if b.isdigit()==True and int(b)!=0:
                    if int(b)-1 < (j-1):break
                    else:print("\nΔώστε έγκυρο αριθμό...")
                else:print("\nΔώστε έγκυρο αριθμό...")
            string = a[int(b)-1].get("ΟΝΟΜΑ")
            print(string)
            sql="select `ΚΩΔΙΚΟΣ ΕΠΙΣΤΗΜΟΝΙΚΟΥ ΠΕΔΙΟΥ` FROM `ΕΠΙΣΤΗΜΟΝΙΚΟ ΠΕΔΙΟ` where `ΟΝΟΜΑ` LIKE '%s' " %string
            mycursor.execute(sql)
            result=mycursor.fetchall()
            break
        elif len(a)==1:
            print("ΤΟ ΕΠΙΣΤΗΜΟΝΙΚΟ ΠΕΔΙΟ ΠΟΥ ΒΡΕΘΗΚΕ ΕΙΝΑΙ ΤΟ ΑΚΟΛΟΥΘΟ:")
            print("==============================================")
            for i in a:
                string=i.get("ΟΝΟΜΑ")
                print(string)
            sql="select `ΚΩΔΙΚΟΣ ΕΠΙΣΤΗΜΟΝΙΚΟΥ ΠΕΔΙΟΥ` FROM `ΕΠΙΣΤΗΜΟΝΙΚΟ ΠΕΔΙΟ` where `ΟΝΟΜΑ` LIKE '%s' " %string
            mycursor.execute(sql)
            result=mycursor.fetchall()
            break
        else:
            print("Το πεδίο που αναζητάτε δεν υπάρχει. Προσπαθήστε ξανά...:")
            subj_name="select `ΟΝΟΜΑ` FROM `ΕΠΙΣΤΗΜΟΝΙΚΟ ΠΕΔΙΟ` where `ΟΝΟΜΑ` LIKE '%s' " %("%"+input()+"%")
            mycursor.execute(subj_name)
            a=(mycursor.fetchall())
    if mycursor.rowcount>0:
        a=result[0]['ΚΩΔΙΚΟΣ ΕΠΙΣΤΗΜΟΝΙΚΟΥ ΠΕΔΙΟΥ']
        sql="select `ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ` FROM αναφέρεται where `ΚΩΔΙΚΟΣ ΕΠΙΣΤΗΜΟΝΙΚΟΥ ΠΕΔΙΟΥ`='%s'"%a
        mycursor.execute(sql)
        result=mycursor.fetchall()
        result2=[]
        global c1
        c1=[]
        for i in range(len(result)):
            b=result[i]['ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ']
            c1.append(b)
            sql="select `ΤΙΤΛΟΣ` from `ΕΠΙΣΤΗΜΟΝΙΚΟ ΑΡΘΡΟ` where `ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ`='%s'"%b
            mycursor.execute(sql)
            result2.append(mycursor.fetchall())
        if len(result2)!=0:
            c2=[]
            for i in range(len(result2)):
                c2.append(result2[i][0]['ΤΙΤΛΟΣ'])
            what_to_do_with_article(c1,c2)
        else:print("\nΛυπούμαστε αλλά δεν υπάρχουν άρθρα του συγκεκριμένου επιστημονικού πεδίου!!\n\n")


    elif mycursor.rowcount==0:
        print("Το όνομα που πληκτρολογήσατε δεν υπάρχει στην λίστα. Προσπαθήστε ξανά..")
        episthmoniko_pedio_search()

def foreas():
    print("Φορέας για αναζήτηση:")      
    foreas_name="select `ΟΝΟΜΑ` FROM `ΦΟΡΕΑΣ` where `ΟΝΟΜΑ` LIKE '%s' " %("%"+input()+"%")
    mycursor.execute(foreas_name)
    a=(mycursor.fetchall())
    while True:
        if len(a)>1:
            j=1
            print("Η ΑΝΑΖΗΤΗΣΗ ΣΑΣ ΟΔΗΓΗΣΕ ΣΤΟΥΣ ΑΚΟΛΟΥΘΟΥΣ ΦΟΡΕΙΣ:")
            print("=======================================================")
            for i in a:
                print(j,i.get("ΟΝΟΜΑ"))
                j=j+1
            while True:
                b = (input("ΠΛΗΚΤΡΟΛΟΓΗΣΤΕ ΤΟΝ ΑΡΙΘΜΟ ΠΟΥ ΑΝΤΙΣΤΟΙΧΕΙ ΣΤΟΝ ΦΟΡΕΑ ΠΟΥ ΑΝΑΖΗΤΗΣΑΤΕ:"))
                if b.isdigit()==True and int(b)!=0:
                    if int(b)-1 < (j-1):break
                    else:print("\nΔώστε έγκυρο αριθμό...")
                else:print("\nΔώστε έγκυρο αριθμό...")
            string = a[int(b)-1].get("ΟΝΟΜΑ")
            print(string)
            print("\nΤο προφίλ του φορέα που αναζητήσατε είναι το εξής:")
            print("=======================================================")

            fi = """SELECT `ΟΝΟΜΑ`, `ΚΑΤΗΓΟΡΙΑ ΦΟΡΕΑ`, `ΧΩΡΑ`
            FROM `ΦΟΡΕΑΣ`
            WHERE `ΟΝΟΜΑ` = %s"""
            mycursor.execute(fi,(string,))
            info3 = mycursor.fetchall()
            info33=[]
            for i in info3:
                info33.append(list(i.values()))
            for i in range(len(info33)) :
                print("ΟΝΟΜΑ:",info33[i][0],", ΚΑΤΗΓΟΡΙΑ ΦΟΡΕΑ:",info33[i][1], ", ΧΩΡΑ ΦΟΡΕΑ:", info33[i][2])

            print("=======================================================")
            sql="select `ΚΩΔΙΚΟΣ ΦΟΡΕΑ` FROM `ΦΟΡΕΑΣ` where `ΟΝΟΜΑ` LIKE '%s' " %string
            mycursor.execute(sql)
            result=mycursor.fetchall()
            break
        elif len(a)==1:
            print("Ο ΦΟΡΕΑΣ ΠΟΥ ΒΡΕΘΗΚΕ ΕΙΝΑΙ Ο ΑΚΟΛΟΥΘΟΣ:")
            print("==============================================")
            for i in a:
                string=i.get("ΟΝΟΜΑ")
                print(string)

            print("\nΤο προφίλ του φορέα που αναζητήσατε είναι το εξής:")
            print("=======================================================")
            fi = """SELECT `ΟΝΟΜΑ`, `ΚΑΤΗΓΟΡΙΑ ΦΟΡΕΑ`, `ΧΩΡΑ`
            FROM `ΦΟΡΕΑΣ`
            WHERE `ΟΝΟΜΑ` = %s"""
            mycursor.execute(fi,(string,))
            info3 = mycursor.fetchall()
            info33=[]
            for i in info3:
                info33.append(list(i.values()))
            for i in range(len(info33)) :
                print("ΟΝΟΜΑ:",info33[i][0],", ΚΑΤΗΓΟΡΙΑ ΦΟΡΕΑ:",info33[i][1], ", ΧΩΡΑ ΦΟΡΕΑ:", info33[i][2])

            print("=======================================================")
            print('\nοκ, ... Αναζήτηση άρθρων του φορέα:', string)
            
            sql="select `ΚΩΔΙΚΟΣ ΦΟΡΕΑ` FROM `ΦΟΡΕΑΣ` where `ΟΝΟΜΑ` LIKE '%s' " %string
            mycursor.execute(sql)
            result=mycursor.fetchall()
            break
        else:
            print("Ο φορέας που αναζητάτε δεν υπάρχει. Προσπαθήστε ξανά...:")
            foreas_name="select `ΟΝΟΜΑ` FROM `ΦΟΡΕΑΣ` where `ΟΝΟΜΑ` LIKE '%s' " %("%"+input()+"%")
            mycursor.execute(foreas_name)
            a=(mycursor.fetchall())

            
    if mycursor.rowcount>0:
        a=result[0]['ΚΩΔΙΚΟΣ ΦΟΡΕΑ']
        sql="select DISTINCT `ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ` FROM συγγράφει where `ΚΩΔΙΚΟΣ ΦΟΡΕΑ`='%s'"%a
        mycursor.execute(sql)
        result=mycursor.fetchall()
        result2=[]
        global c1
        c1=[]
        for i in range(len(result)):
            b=result[i]['ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ']
            c1.append(b)
            sql="select `ΤΙΤΛΟΣ` from `ΕΠΙΣΤΗΜΟΝΙΚΟ ΑΡΘΡΟ` where `ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ`='%s'"%b
            mycursor.execute(sql)
            result2.append(mycursor.fetchall())
        if len(result2)!=0:
            c2=[]
            for i in range(len(result2)):
                c2.append(result2[i][0]['ΤΙΤΛΟΣ'])
            what_to_do_with_article(c1,c2)
        else:print("\nΛυπούμαστε αλλά δεν υπάρχουν άρθρα του συγκεκριμένου επιστημονικού φορέα!!\n\n")
 
    elif mycursor.rowcount==0:
        print("Το όνομα που πληκτρολογήσατε δεν υπάρχει στην λίστα. Προσπαθήστε ξανά..")
        foreas()

##==============================================================================##
        
#### Συναρτήσεις που δημιουργούν τις αντίστοιχες λίστες από όπου ξεκινάμε για την εύρεση ενός άρθρου
##==============================================================================##
##Συνάρτηση που δημιουργεί μία λίστα με τα ονόματα όλων των επιστημονικών πεδίών
def create_subject():
    subjects= "SELECT `ΟΝΟΜΑ` FROM `ΕΠΙΣΤΗΜΟΝΙΚΟ ΠΕΔΙΟ`"
    mycursor.execute(subjects)
    result = mycursor.fetchall()
    subject = []
    for a in result:
        subject=subject+(list(a.values()))
    return subject
##Συνάρτηση που δημιουργεί μία λίστα με τα ονόματα από όλους τους συγγραφείς
def create_author():
    authors="SELECT `ΟΝΟΜΑ`, `ΕΠΩΝΥΜΟ` FROM `ΣΥΓΓΡΑΦΕΑΣ`"
    mycursor.execute(authors)
    result1 = mycursor.fetchall()
    author=[]
    for i in result1:
        author.append(list(i.values()))
    return author
##Συνάρτηση που δημιουργεί μία λίστα με τα ονόματα όλων των φορέων
def create_institutions():
    institutions = "SELECT `ΟΝΟΜΑ` FROM `ΦΟΡΕΑΣ`"
    mycursor.execute(institutions)
    result2 = mycursor.fetchall()
    institution = []
    for i in result2:
        institution.append(list(i.values()))
    return institution
##Συνάρτηση που δημιουργεί μία λίστα με τα ονόματα όλων των περιοδικών
def create_magazines():
    magazines = "SELECT `ΟΝΟΜΑ` FROM `ΠΕΡΙΟΔΙΚΟ`"
    mycursor.execute(magazines)
    result3 = mycursor.fetchall()
    magazine = []
    for i in result3:
        magazine.append(list(i.values()))
    return magazine

##==============================================================================##
## Βρίσκει πληροφορίες για ένα περιοδικό
def full_magaz(specific_magazine):
    maglen=len(specific_magazine)
    if maglen==1 and specific_magazine!="9":
        p = "10000"
    elif maglen==2 or specific_magazine =="9": p = "1000"
    kod_per = p + str(int(specific_magazine)+1)
    fm = """SELECT `ΟΝΟΜΑ`, `ΕΚΔΟΤΗΣ`
            FROM `ΠΕΡΙΟΔΙΚΟ`
            WHERE `ΚΩΔΙΚΟΣ ΠΕΡΙΟΔΙΚΟΥ` = %s"""
    mycursor.execute(fm,(kod_per,))
    info1 = mycursor.fetchall()
    info11=[]
    for i in info1:
        info11.append(list(i.values()))
    for i in range(len(info11)) :
        print(info11[i][0],", ΕΚΔΟΤΗΣ:",info11[i][1])
    
## Βρίσκει πληροφορίες για ένα συγγραφέα
def full_auth(specific_author):
    autlen=len(specific_author)

    if autlen==1 and specific_author!="9":
        st = "20000"
    elif autlen == 2 or specific_author=="9": st = "2000"
    kod_sygg = st + str(int(specific_author)+1)
    fa = """SELECT `ΟΝΟΜΑ`, `ΕΠΩΝΥΜΟ`, `ΧΩΡΑ ΚΑΤΑΓΩΓΗΣ`
            FROM `ΣΥΓΓΡΑΦΕΑΣ`
            WHERE `ΚΩΔΙΚΟΣ ΣΥΓΓΡΑΦΕΑ` = %s"""
    mycursor.execute(fa,(kod_sygg,))
    info2 = mycursor.fetchall()
    info22=[]
    for i in info2:
        info22.append(list(i.values()))
    for i in range(len(info22)) :
        print("ΟΝΟΜΑ:",info22[i][0],", ΕΠΩΝΥΜΟ:",info22[i][1], ", ΧΩΡΑ ΚΑΤΑΓΩΓΗΣ:", info22[i][2])
## Βρίσκει πληροφορίες για ένα πεδίο

def full_inst(specific_inst):
    instlen=len(specific_inst)
    if instlen==1 and specific_inst!="9":
        f = "30000"
    elif instlen==2 or specific_inst=="9": f = "3000"
    kod_forea = f + str(int(specific_inst)+1)
    fi = """SELECT `ΟΝΟΜΑ`, `ΚΑΤΗΓΟΡΙΑ ΦΟΡΕΑ`, `ΧΩΡΑ`
            FROM `ΦΟΡΕΑΣ`
            WHERE `ΚΩΔΙΚΟΣ ΦΟΡΕΑ` = %s"""
    mycursor.execute(fi,(kod_forea,))
    info3 = mycursor.fetchall()
    info33=[]
    for i in info3:
        info33.append(list(i.values()))
    for i in range(len(info33)) :
        print("ΟΝΟΜΑ:",info33[i][0],", ΚΑΤΗΓΟΡΙΑ ΦΟΡΕΑ:",info33[i][1], ", ΧΩΡΑ ΦΟΡΕΑ:", info33[i][2])

## Βρίσκει αναλυτικές πληροφορίες για ένα άρθρο
def information(kod_arthrou):


    titlos = """ SELECT `ΕΠΙΣΤΗΜΟΝΙΚΟ ΑΡΘΡΟ`.`ΤΙΤΛΟΣ`
                 FROM `ΕΠΙΣΤΗΜΟΝΙΚΟ ΑΡΘΡΟ`
                 WHERE `ΕΠΙΣΤΗΜΟΝΙΚΟ ΑΡΘΡΟ`.`ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ` = %s"""

    glwssa = """SELECT `ΕΠΙΣΤΗΜΟΝΙΚΟ ΑΡΘΡΟ`.`ΓΛΩΣΣΑ`
                 FROM `ΕΠΙΣΤΗΜΟΝΙΚΟ ΑΡΘΡΟ`
                 WHERE `ΕΠΙΣΤΗΜΟΝΙΚΟ ΑΡΘΡΟ`.`ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ` = %s"""
    
    syggrafeas= """ SELECT DISTINCT `ΣΥΓΓΡΑΦΕΑΣ`.`ΟΝΟΜΑ`, `ΣΥΓΓΡΑΦΕΑΣ`.`ΕΠΩΝΥΜΟ`
                    FROM `συγγράφει`
                    JOIN `ΣΥΓΓΡΑΦΕΑΣ` ON `συγγράφει`.`ΚΩΔΙΚΟΣ ΣΥΓΓΡΑΦΕΑ` = `ΣΥΓΓΡΑΦΕΑΣ`.`ΚΩΔΙΚΟΣ ΣΥΓΓΡΑΦΕΑ`
                    WHERE `συγγράφει`.`ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ` = %s"""

    foreas = """SELECT DISTINCT `ΦΟΡΕΑΣ`.`ΟΝΟΜΑ`
                FROM `συγγράφει`
                JOIN `ΦΟΡΕΑΣ` ON `συγγράφει`.`ΚΩΔΙΚΟΣ ΦΟΡΕΑ` = `ΦΟΡΕΑΣ`.`ΚΩΔΙΚΟΣ ΦΟΡΕΑ`
                WHERE `συγγράφει`.`ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ` = %s"""

    im_ekdosis= """SELECT `ΕΠΙΣΤΗΜΟΝΙΚΟ ΑΡΘΡΟ`.`ΗΜΕΡΟΜΗΝΙΑ ΕΚΔΟΣΗΣ`
                   FROM `ΕΠΙΣΤΗΜΟΝΙΚΟ ΑΡΘΡΟ`
                   WHERE `ΕΠΙΣΤΗΜΟΝΙΚΟ ΑΡΘΡΟ`.`ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ` = %s"""

    periodiko="""SELECT `ΠΕΡΙΟΔΙΚΟ`.`ΟΝΟΜΑ` , `ΤΕΥΧΟΣ`.`VOLUME`, `ΤΕΥΧΟΣ`.`ISSUE`, `περιλαμβάνεται`.`ΣΕΛΙΔΕΣ`
                 FROM  `ΤΕΥΧΟΣ`
                 JOIN `περιλαμβάνεται` ON `ΤΕΥΧΟΣ`.`ΚΩΔΙΚΟΣ ΠΕΡΙΟΔΙΚΟΥ` = `περιλαμβάνεται`.`ΚΩΔΙΚΟΣ ΠΕΡΙΟΔΙΚΟΥ` AND `ΤΕΥΧΟΣ`.`VOLUME` = `περιλαμβάνεται`.`VOLUME` AND `ΤΕΥΧΟΣ`.`ISSUE` = `περιλαμβάνεται`.`ISSUE`
                 JOIN `ΠΕΡΙΟΔΙΚΟ` ON `ΤΕΥΧΟΣ`.`ΚΩΔΙΚΟΣ ΠΕΡΙΟΔΙΚΟΥ` = `ΠΕΡΙΟΔΙΚΟ`.`ΚΩΔΙΚΟΣ ΠΕΡΙΟΔΙΚΟΥ`
                 WHERE `περιλαμβάνεται`.`ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ` = %s"""

    pedio= """SELECT `ΕΠΙΣΤΗΜΟΝΙΚΟ ΠΕΔΙΟ`.`ΟΝΟΜΑ`
              FROM `ΕΠΙΣΤΗΜΟΝΙΚΟ ΠΕΔΙΟ`
              JOIN `αναφέρεται` ON `ΕΠΙΣΤΗΜΟΝΙΚΟ ΠΕΔΙΟ`.`ΚΩΔΙΚΟΣ ΕΠΙΣΤΗΜΟΝΙΚΟΥ ΠΕΔΙΟΥ` = `αναφέρεται`.`ΚΩΔΙΚΟΣ ΕΠΙΣΤΗΜΟΝΙΚΟΥ ΠΕΔΙΟΥ`
              WHERE `αναφέρεται`.`ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ`= %s"""
    mycursor.execute(titlos,(kod_arthrou,))
    t = mycursor.fetchall()
    mycursor.execute(glwssa,(kod_arthrou,))
    g = mycursor.fetchall()
    mycursor.execute(syggrafeas,(kod_arthrou,))
    s = mycursor.fetchall()
    mycursor.execute(foreas,(kod_arthrou,))
    f = mycursor.fetchall()
    mycursor.execute(im_ekdosis,(kod_arthrou,))
    im = mycursor.fetchall()
    mycursor.execute(periodiko,(kod_arthrou,))
    per = mycursor.fetchall()
    mycursor.execute(pedio,(kod_arthrou,))
    ped = mycursor.fetchall()

    print("\nΑναζήτηση πληροφοριών του άρθρου ...")
    T=[]
    print("\nΤΙΤΛΟΣ")
    print("===========")
    for i in t:
        T.append(list(i.values()))
    for i in range(len(T)) :
        print(T[i][0])
    print("\n")

    print("ΓΛΩΣΣΑ")
    print("=======")
    print(g[0].get("ΓΛΩΣΣΑ"))
    print("\n")
    
    S=[]
    print("ΣΥΓΓΡΑΦΕΙΣ")
    print("===========")
    for i in s:
        S.append(list(i.values()))
    for i in range(len(S)) :
        print(S[i][0],S[i][1])
    print("\n")
    
    F=[]
    print("ΦΟΡΕΑΣ")
    print("===========")
    for i in f:
        F.append(list(i.values()))
    for i in range(len(F)) :
        print(F[i][0])
    print("\n")

    IM=[]
    print("ΗΜΕΡΟΜΗΝΙΑ ΕΚΔΟΣΗΣ")
    print("==================")
    for i in im:
        IM.append(list(i.values()))
    for i in range(len(IM)) :
        print(IM[i][0])
    print("\n")

    PER=[]
    print("ΠΕΡΙΟΔΙΚΟ")
    print("==================")
    for i in per:
        PER.append(list(i.values()))
    for i in range(len(PER)) :
        print(PER[i][0],", volume:",PER[i][1],", issue:",PER[i][2],", σελίδες:",PER[i][3])
    print("\n")

    PED=[]
    print("ΕΠΙΣΤΗΜΟΝΙΚΟ ΠΕΔΙΟ")
    print("==================")
    for i in ped:
        PED.append(list(i.values()))
    for i in range(len(PED)) :
        print(PED[i][0])
    print("\n")
    print("\nΕπιστροφή στο μενού άρθρου...")

## ΠΑΡΑΠΟΜΠΕΣ

def parapompes(kod_arthrou):

    par_ektos = """ SELECT concat_ws(', ',`ΕΠΩΝΥΜΟ ΣΥΓΓΡΑΦΕΑ`, CONCAT("(",`ΕΤΟΣ ΚΥΚΛΟΦΟΡΙΑΣ`,")"), `ΤΙΤΛΟΣ ΑΡΘΡΟΥ`, `ΟΝΟΜΑ ΤΕΚΜΗΡΙΟΥ`,CONCAT("pp.",`ΣΕΛΙΔΕΣ`), `ΕΚΔΟΤΗΣ`)  as par_ektos
                    FROM `ΠΑΡΑΠΟΜΠΗ`
                    JOIN (select `ΣΥΓΓΡΑΦΕAΣ ΠΑΡΑΠΟΜΠΗΣ`.`ΚΩΔΙΚΟΣ ΠΑΡΑΠΟΜΠΗΣ` AS `ΚΩΔΙΚΟΣ ΠΑΡΑΠΟΜΠΗΣ`,group_concat(`ΣΥΓΓΡΑΦΕAΣ ΠΑΡΑΠΟΜΠΗΣ`.`ΕΠΩΝΥΜΟ ΣΥΓΓΡΑΦΕΑ` separator ', ') AS `ΕΠΩΝΥΜΟ ΣΥΓΓΡΑΦΕΑ` from `ΣΥΓΓΡΑΦΕAΣ ΠΑΡΑΠΟΜΠΗΣ`
                    group by `ΣΥΓΓΡΑΦΕAΣ ΠΑΡΑΠΟΜΠΗΣ`.`ΚΩΔΙΚΟΣ ΠΑΡΑΠΟΜΠΗΣ`) AS syggr ON `ΠΑΡΑΠΟΜΠΗ`.`ΚΩΔΙΚΟΣ ΠΑΡΑΠΟΜΠΗΣ`=syggr.`ΚΩΔΙΚΟΣ ΠΑΡΑΠΟΜΠΗΣ`
                    JOIN `παραπέμπει εκτός` ON `ΠΑΡΑΠΟΜΠΗ`.`ΚΩΔΙΚΟΣ ΠΑΡΑΠΟΜΠΗΣ` = `παραπέμπει εκτός`.`ΚΩΔΙΚΟΣ ΠΑΡΑΠΜΠΗΣ`
                    WHERE `παραπέμπει εκτός`.`ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ`=%s""" %kod_arthrou
    mycursor.execute(par_ektos)
    ektos=mycursor.fetchall()
    par_entos =  """SELECT kod_deuterou, titlos, concat_ws(', ',eponimo, xronos, titlos, onoma, CONCAT("pp.",selides), CONCAT('vol: ', vol), CONCAT('iss :' , iss),`ΕΚΔΟΤΗΣ` ) as par_entos
                    FROM (SELECT GROUP_CONCAT(DISTINCT CONCAT(`ΕΠΩΝΥΜΟ`,' ',SUBSTRING(`ΣΥΓΓΡΑΦΕΑΣ`.`ΟΝΟΜΑ`,1,1),". ")) as eponimo, CONCAT("(",YEAR(`ΕΠΙΣΤΗΜΟΝΙΚΟ ΑΡΘΡΟ`.`ΗΜΕΡΟΜΗΝΙΑ ΕΚΔΟΣΗΣ`),")") as xronos,
                          `ΕΠΙΣΤΗΜΟΝΙΚΟ ΑΡΘΡΟ`.`ΤΙΤΛΟΣ` as titlos, `ΠΕΡΙΟΔΙΚΟ`.`ΟΝΟΜΑ` as onoma, `ΤΕΥΧΟΣ`.`VOLUME` as vol, `ΤΕΥΧΟΣ`.`ISSUE` as iss, `περιλαμβάνεται`.`ΣΕΛΙΔΕΣ` as selides, `ΠΕΡΙΟΔΙΚΟ`.`ΕΚΔΟΤΗΣ`,
                          `παραπέμπει εντός`.`ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ ΔΕΥΤΕΡΟΥ` as kod_deuterou
                    FROM `συγγράφει`
                    JOIN `ΣΥΓΓΡΑΦΕΑΣ` ON `συγγράφει`.`ΚΩΔΙΚΟΣ ΣΥΓΓΡΑΦΕΑ` = `ΣΥΓΓΡΑΦΕΑΣ`.`ΚΩΔΙΚΟΣ ΣΥΓΓΡΑΦΕΑ`  
                    JOIN `ΕΠΙΣΤΗΜΟΝΙΚΟ ΑΡΘΡΟ` ON `συγγράφει`.`ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ` = `ΕΠΙΣΤΗΜΟΝΙΚΟ ΑΡΘΡΟ`.`ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ`
                    JOIN `παραπέμπει εντός` on`συγγράφει`.`ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ` = `παραπέμπει εντός`.`ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ ΔΕΥΤΕΡΟΥ`
                    JOIN `περιλαμβάνεται` ON `ΕΠΙΣΤΗΜΟΝΙΚΟ ΑΡΘΡΟ`.`ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ` = `περιλαμβάνεται`.`ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ`
                    JOIN `ΤΕΥΧΟΣ` ON `περιλαμβάνεται`.`ΚΩΔΙΚΟΣ ΠΕΡΙΟΔΙΚΟΥ` = `ΤΕΥΧΟΣ`.`ΚΩΔΙΚΟΣ ΠΕΡΙΟΔΙΚΟΥ` AND `περιλαμβάνεται`.`VOLUME` = `ΤΕΥΧΟΣ`.`VOLUME` AND `περιλαμβάνεται`.`ISSUE` = `ΤΕΥΧΟΣ`.`ISSUE`
                    JOIN `ΠΕΡΙΟΔΙΚΟ` ON `ΤΕΥΧΟΣ`.`ΚΩΔΙΚΟΣ ΠΕΡΙΟΔΙΚΟΥ` = `ΠΕΡΙΟΔΙΚΟ`.`ΚΩΔΙΚΟΣ ΠΕΡΙΟΔΙΚΟΥ`
                    WHERE `παραπέμπει εντός`.`ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ ΠΡΩΤΟΥ` = %s
                    GROUP BY `ΕΠΙΣΤΗΜΟΝΙΚΟ ΑΡΘΡΟ`.`ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ`) as what""" %kod_arthrou
    mycursor.execute(par_entos)
    entos=mycursor.fetchall()
 
    
    print("\nΑναζήτηση παραπομπών του άρθρου ...")
    j=1
    if len(ektos)!=0 or len(entos) !=0 :
        print("\nΠΑΡΑΠΟΜΠΕΣ")
        print("==========================")
        if len(ektos) != 0:
            for i in ektos:
                print(j,i.get("par_ektos"))
                j=j+1
                print("\n")
        if len(entos) !=0:
            c1=[]
            c2=[]
            c3=[]
            for i in entos:
                c1.append(i.get("kod_deuterou"))
                c2.append(i.get("titlos"))
                c3.append(i.get("par_entos"))
                print(j,i.get("par_entos"))
                j=j+1
                print("\n")
            print("==========================\n")
            if len(c2) == 1:
                print("\nΗ παρακάτω παραπομπή υπάρχει στην βάση δεδομένων μας\n")
                print("=========================================================")
                print(c3[0])
                print("=========================================================")
                print("\nΑν θέλετε να την επιλέξετε πατήστε 1.")
                print("Αν δεν θέλετε να την επιλέξετε πατήστε 2.")
            else:
                print("\nΟι παρακάτω παραπομπές υπάρχουν στην βάση δεδομένων μας\n")
                print("=========================================================")
                for i in c3:print(i)
                print("=========================================================\n")
                print("Αν θέλετε να επιλέξετε κάποια απο αυτές πατήστε 1.")
                print("Αν δεν θέλετε να επιλέξετε κάποια πατήστε 2.")
            ans=str(input())
            if ans=="1":what_to_do_with_article(c1,c2)
        
    else:print("\nΛυπούμαστε αλλά δεν υπάρχουν παραπομπές του συγκεκριμένου άρθρου!!\n\n")
    print("\nΕπιστροφή στο μενού άρθρου...")

    
    
    
##Συνάρτηση που δίνει την δυνατότηα στον χρήστη να αποφασίσει τι θέλει να κάνει με το άρθρο που βρήκε
def what_to_do_with_article(lista_kod_arthr, lista_titlwn):
    while True:
        print("\n\nΕΠΙΣΤΗΜΟΝΙΚΑ ΑΡΘΡΑ")
        print("====================\n")
        j=1
        for i in lista_titlwn:
            print(j,i)
            j=j+1
            print("\n")
        print("=========================\n")
        m=0
        while len(lista_kod_arthr)!=1:
            print("--Πληκτρολογείστε τον αριθμό του άρθρου που θέλετε να επιλέξετε:")
            print("--(Enter) για να πάτε πίσω")
            b = input()
            if b.isdigit()==True:
                if int(b)-1 < len(lista_kod_arthr) and int(b)!=0:break
                else:print("\nΔώστε έγκυρο αριθμό άρθρου...")
            elif b=="":break
            else:print("\nΔώστε έγκυρο αριθμό άρθρου...")
        if len(lista_kod_arthr)!=1 and b=="": break        
        if len(lista_kod_arthr)==1:
            b="1"
            m=1

        add_to_history(lista_kod_arthr[int(b)-1])
        while True:
            if len(lista_kod_arthr)!=1:
                print("\nΤο άρθρο που επιλέξατε ειναι το:\n")
                print("====================================")
                print(lista_titlwn[int(b)-1])
                print("====================================")
            print("\nΜΕΝΟΥ ΑΡΘΡΟΥ")
            print("===============")
            print("1: Πρόσθεση-Αφαίρεση άρθρου από τα αγαπημένα.")
            print("2: Άνοιγμα άρθρου σε μορφή .pdf.")
            print("3: Αναλυτικές πληροφορίες άρθρου.")
            print("4: Παραπομπές άρθρου.")
            print("5: Αναζήτηση μέσω του συγκεκριμένου άρθρου.")
            print("6: Κατέβασμα του συγκεκριμένου άρθρου.")
            print("(ENTER): Για να πάτε πίσω.")    
            

            c = input()
            if c=="1":add_to_favourites(lista_kod_arthr[int(b)-1])
            elif c=="2":open_art(lista_kod_arthr[int(b)-1])
            elif c=="3":information(lista_kod_arthr[int(b)-1])
            elif c=="4":parapompes(lista_kod_arthr[int(b)-1])
            elif c=="5":
                
                print("\nΕΠΙΛΟΓΕΣ ΑΝΑΖΗΤΗΣΗΣ")
                print("=====================")
                print("1: Αναζήτηση άρθρων που αναφέρονται στο πεδίο του επιλεγμένου άρθρου.")
                print("2: Αναζήτηση άρθρων που έχουν συγγραφεί από τον συγγραφέα του επιλεγμένου άρθρου.")
                print("3: Αναζήτηση άρθρων που έχουν εκδοθεί από τους φορεις του επιλεγμένου άρθρου.")
                print("4: Αναζήτηση άρθρων που έχουν εκδοθεί από το περιοδικό του επιλεγμένου άρθρου.")
                print("5: Για να πάτε πίσω.")
                so = input()
                if so == "1":ep_pedio(lista_kod_arthr[int(b)-1])
                elif so == "2":syggr(lista_kod_arthr[int(b)-1])
                elif so == "3":ep_foreas(lista_kod_arthr[int(b)-1])
                elif so == "4":ep_per(lista_kod_arthr[int(b)-1])
                elif so == "5":c =""
                else:print("\nΠροσπαθήστε ξανά...\n")
            elif c=="":
                break
            elif c=="6":
                download_article(lista_kod_arthr[int(b)-1])
            else:print("\nΠροσπαθήστε ξανά...\n")
        if c=="" and m==1:break
    
        
def download_article(kod_arthrou):
    sql = """SELECT DOWNLOAD_URL
            FROM`ΕΠΙΣΤΗΜΟΝΙΚΟ ΑΡΘΡΟ`
            WHERE `ΕΠΙΣΤΗΜΟΝΙΚΟ ΑΡΘΡΟ`.`ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ` = %s""" %kod_arthrou
    mycursor.execute(sql)
    a = mycursor.fetchall()
    url = a[0].get('DOWNLOAD_URL')
    print("\n\nΠεριμένετε να κατέβει το άρθρο...\n\n\n")
    gdd.download_file_from_google_drive(url,'./downloads/%s.pdf'%kod_arthrou)
    print("Το άρθρο κατέβηκε επιτυχώς!!")
    print("=============================")
        
## Συνάρτηση που ανοίγει pdf files από το google drive
def open_art(kod_arthrou):
    sql = """SELECT OPEN_URL
            FROM`ΕΠΙΣΤΗΜΟΝΙΚΟ ΑΡΘΡΟ`
            WHERE `ΕΠΙΣΤΗΜΟΝΙΚΟ ΑΡΘΡΟ`.`ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ` = %s""" %kod_arthrou
    mycursor.execute(sql)
    a = mycursor.fetchall()
    url = a[0].get('OPEN_URL')
    
    print(url)
    
    print("\nΆνοιγμα του άρθρου ...")
    print("\nΕπιστροφή στο μενού άρθρου...")
    webbrowser.open_new(url)

    
####Συναρτήσεις που τυπώνουν άρθρα ίδιου φίλτρου
##Ιδιου επιστημονικου πεδιου
##====================================================
def ep_pedio(kod_arthrou):
    sql ="""SELECT DISTINCT `αναφέρεται`.`ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ`, `ΕΠΙΣΤΗΜΟΝΙΚΟ ΑΡΘΡΟ`.`ΤΙΤΛΟΣ`,`ΕΠΙΣΤΗΜΟΝΙΚΟ ΠΕΔΙΟ`.`ΟΝΟΜΑ`
            FROM `αναφέρεται`
            JOIN `ΕΠΙΣΤΗΜΟΝΙΚΟ ΑΡΘΡΟ` ON `αναφέρεται`.`ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ`=`ΕΠΙΣΤΗΜΟΝΙΚΟ ΑΡΘΡΟ`.`ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ`
            JOIN `ΕΠΙΣΤΗΜΟΝΙΚΟ ΠΕΔΙΟ` ON `αναφέρεται`.`ΚΩΔΙΚΟΣ ΕΠΙΣΤΗΜΟΝΙΚΟΥ ΠΕΔΙΟΥ`=`ΕΠΙΣΤΗΜΟΝΙΚΟ ΠΕΔΙΟ`.`ΚΩΔΙΚΟΣ ΕΠΙΣΤΗΜΟΝΙΚΟΥ ΠΕΔΙΟΥ`
            WHERE `αναφέρεται`.`ΚΩΔΙΚΟΣ ΕΠΙΣΤΗΜΟΝΙΚΟΥ ΠΕΔΙΟΥ` IN (SELECT `αναφέρεται`.`ΚΩΔΙΚΟΣ ΕΠΙΣΤΗΜΟΝΙΚΟΥ ΠΕΔΙΟΥ`
                                                                FROM `αναφέρεται`
                                                                WHERE `αναφέρεται`.`ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ`=%s)
            AND `αναφέρεται`.`ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ`!=%s""" %(kod_arthrou,kod_arthrou)
    c1=[]
    c2=[]
    mycursor.execute(sql)
    result=mycursor.fetchall()
    sql1 ="""SELECT DISTINCT `ΕΠΙΣΤΗΜΟΝΙΚΟ ΠΕΔΙΟ`.`ΟΝΟΜΑ`
            FROM `αναφέρεται`
            JOIN `ΕΠΙΣΤΗΜΟΝΙΚΟ ΠΕΔΙΟ` ON `αναφέρεται`.`ΚΩΔΙΚΟΣ ΕΠΙΣΤΗΜΟΝΙΚΟΥ ΠΕΔΙΟΥ`=`ΕΠΙΣΤΗΜΟΝΙΚΟ ΠΕΔΙΟ`.`ΚΩΔΙΚΟΣ ΕΠΙΣΤΗΜΟΝΙΚΟΥ ΠΕΔΙΟΥ`
            WHERE `αναφέρεται`.`ΚΩΔΙΚΟΣ ΕΠΙΣΤΗΜΟΝΙΚΟΥ ΠΕΔΙΟΥ` IN (SELECT `αναφέρεται`.`ΚΩΔΙΚΟΣ ΕΠΙΣΤΗΜΟΝΙΚΟΥ ΠΕΔΙΟΥ`
                                                                FROM `αναφέρεται`
                                                                WHERE `αναφέρεται`.`ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ`=%s)""" %(kod_arthrou)
    mycursor.execute(sql1)
    a=mycursor.fetchall()
    if len(a)>1:
        print("\n\n============================================================")
        print("Το άρθρο αναφέρεται στα ακόλουθα επιστημονικά πεδία:")
        for i in a:
            print(i.get("ΟΝΟΜΑ"))
        print("\n\nΟκ, αναζήτηση άλλων σχετικών με τα συγκεκριμένα πεδία άρθρων...\n")
        print("============================================================")
    elif len(a)==1:
        print("\n\n============================================================")
        print("Το άρθρο αναφέρεται στο ακόλουθο επιστημονικό πεδίο:")
        for i in a:
            print(i.get("ΟΝΟΜΑ"))
        print("\n\nΟκ, αναζήτηση άλλων σχετικών με το συγκεκριμένο πεδίο άρθρων...\n")
        print("============================================================")
    if len(result)!=0:
        for i in result:
            c1.append(i.get("ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ"))
            c2.append(i.get("ΤΙΤΛΟΣ"))
        
        what_to_do_with_article(c1,c2)
    else:print("\nΛυπούμαστε αλλά δεν υπάρχουν άλλα άρθρα του συγκεκριμένου πεδίου!!\n\n")


def syggr(kod_arthrou):
    sql ="""SELECT DISTINCT `συγγράφει`.`ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ`, `ΕΠΙΣΤΗΜΟΝΙΚΟ ΑΡΘΡΟ`.`ΤΙΤΛΟΣ` 
            FROM `συγγράφει`
            JOIN `ΕΠΙΣΤΗΜΟΝΙΚΟ ΑΡΘΡΟ` ON `συγγράφει`.`ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ`=`ΕΠΙΣΤΗΜΟΝΙΚΟ ΑΡΘΡΟ`.`ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ`
            JOIN `ΣΥΓΓΡΑΦΕΑΣ` ON `συγγράφει`.`ΚΩΔΙΚΟΣ ΣΥΓΓΡΑΦΕΑ` = `ΣΥΓΓΡΑΦΕΑΣ`.`ΚΩΔΙΚΟΣ ΣΥΓΓΡΑΦΕΑ`
            WHERE `συγγράφει`.`ΚΩΔΙΚΟΣ ΣΥΓΓΡΑΦΕΑ` IN (SELECT  `συγγράφει`.`ΚΩΔΙΚΟΣ ΣΥΓΓΡΑΦΕΑ`
                                                                FROM `συγγράφει`
                                                                WHERE `συγγράφει`.`ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ`=%s)
            AND `συγγράφει`.`ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ`!=%s""" %(kod_arthrou,kod_arthrou)
    c1=[]
    c2=[]
    mycursor.execute(sql)
    result=mycursor.fetchall()
    sql1 ="""SELECT DISTINCT `ΣΥΓΓΡΑΦΕΑΣ`.`ΟΝΟΜΑ`,`ΣΥΓΓΡΑΦΕΑΣ`.`ΕΠΩΝΥΜΟ`
            FROM `συγγράφει`
            JOIN `ΣΥΓΓΡΑΦΕΑΣ` ON `συγγράφει`.`ΚΩΔΙΚΟΣ ΣΥΓΓΡΑΦΕΑ` = `ΣΥΓΓΡΑΦΕΑΣ`.`ΚΩΔΙΚΟΣ ΣΥΓΓΡΑΦΕΑ`
            WHERE `συγγράφει`.`ΚΩΔΙΚΟΣ ΣΥΓΓΡΑΦΕΑ` IN (SELECT  `συγγράφει`.`ΚΩΔΙΚΟΣ ΣΥΓΓΡΑΦΕΑ`
                                                                FROM `συγγράφει`
                                                                WHERE `συγγράφει`.`ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ`=%s)""" %(kod_arthrou)
    
    mycursor.execute(sql1)
    a=mycursor.fetchall()
    if len(a)>1:
        print("\n\n============================================================")
        print("Το άρθρο έχει συγγραφεί από τους ακόλουθους συγγραφείς:")
        for i in a:
            print(i.get("ΟΝΟΜΑ"),i.get("ΕΠΩΝΥΜΟ"))
        print("\n\nΟκ, αναζήτηση άρθρων των συγκεκριμένων συγγραφέων...\n")
        print("============================================================")
    elif len(a)==1:
        print("\n\n============================================================")
        print("Το άρθρο έχει συγγραφεί από τον ακόλουθο συγγραφέα:")
        for i in a:
            print(i.get("ΟΝΟΜΑ"),i.get("ΕΠΩΝΥΜΟ"))
        print("\n\nΟκ, αναζήτηση άρθρων του συγκεκριμένου συγγραφέα...\n")
        print("============================================================")
    if len(result)!=0:
        for i in result:
            c1.append(i.get("ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ"))
            c2.append(i.get("ΤΙΤΛΟΣ"))
        what_to_do_with_article(c1,c2)
    else:print("\nΛυπούμαστε αλλά δεν υπάρχουν άλλα άρθρα του συγκεκριμένου συγγραφέα!!\n\n")

def ep_foreas(kod_arthrou):
    sql ="""SELECT DISTINCT `συγγράφει`.`ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ`, `ΕΠΙΣΤΗΜΟΝΙΚΟ ΑΡΘΡΟ`.`ΤΙΤΛΟΣ` 
            FROM `συγγράφει`
            JOIN `ΕΠΙΣΤΗΜΟΝΙΚΟ ΑΡΘΡΟ` ON `συγγράφει`.`ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ`=`ΕΠΙΣΤΗΜΟΝΙΚΟ ΑΡΘΡΟ`.`ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ`
            WHERE `συγγράφει`.`ΚΩΔΙΚΟΣ ΦΟΡΕΑ` IN (SELECT  `συγγράφει`.`ΚΩΔΙΚΟΣ ΦΟΡΕΑ`
                                                                FROM `συγγράφει`
                                                                WHERE `συγγράφει`.`ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ`=%s)
            AND `συγγράφει`.`ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ`!=%s""" %(kod_arthrou,kod_arthrou)
    c1=[]
    c2=[]
    mycursor.execute(sql)
    result=mycursor.fetchall()
    sql1 ="""SELECT DISTINCT `ΦΟΡΕΑΣ`.`ΟΝΟΜΑ` 
            FROM `συγγράφει`
            JOIN `ΦΟΡΕΑΣ` ON `συγγράφει`.`ΚΩΔΙΚΟΣ ΦΟΡΕΑ`=`ΦΟΡΕΑΣ`.`ΚΩΔΙΚΟΣ ΦΟΡΕΑ`
            WHERE `συγγράφει`.`ΚΩΔΙΚΟΣ ΦΟΡΕΑ` IN (SELECT  `συγγράφει`.`ΚΩΔΙΚΟΣ ΦΟΡΕΑ`
                                                                FROM `συγγράφει`
                                                                WHERE `συγγράφει`.`ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ`=%s)""" %(kod_arthrou)
    mycursor.execute(sql1)
    a=mycursor.fetchall()
    if len(a)>1:
        print("\n\n============================================================")
        print("Το άρθρο εκδόθηκε σε συνεργασια με τους ακόλουθους φορείς:")
        for i in a:
            print(i.get("ΟΝΟΜΑ"))
        print("\n\nΟκ, αναζήτηση άρθρων των συγκεκριμένων φορέων...\n")
        print("============================================================")
    elif len(a)==1:
        print("\n\n============================================================")
        print("Το άρθρο εκδόθηκε σε συνεργασια με τον ακόλουθο φορέα:")
        for i in a:
            print(i.get("ΟΝΟΜΑ"))
        print("\n\nΟκ, αναζήτηση άρθρων του συγκεκριμένου φορέα...\n")
        print("============================================================")
    if len(result)!=0:
        for i in result:
            c1.append(i.get("ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ"))
            c2.append(i.get("ΤΙΤΛΟΣ"))
        what_to_do_with_article(c1,c2)
    else:print("\nΛυπούμαστε αλλά δεν υπάρχουν άλλα άρθρα του συγκεκριμένου φορέα!!\n\n")

def ep_per(kod_arthrou):
    sql ="""SELECT DISTINCT `περιλαμβάνεται`.`ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ`, `ΕΠΙΣΤΗΜΟΝΙΚΟ ΑΡΘΡΟ`.`ΤΙΤΛΟΣ` 
            FROM `περιλαμβάνεται`
            JOIN `ΕΠΙΣΤΗΜΟΝΙΚΟ ΑΡΘΡΟ` ON `περιλαμβάνεται`.`ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ`=`ΕΠΙΣΤΗΜΟΝΙΚΟ ΑΡΘΡΟ`.`ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ`
            WHERE `περιλαμβάνεται`.`ΚΩΔΙΚΟΣ ΠΕΡΙΟΔΙΚΟΥ` IN (SELECT  `περιλαμβάνεται`.`ΚΩΔΙΚΟΣ ΠΕΡΙΟΔΙΚΟΥ`
                                                                FROM `περιλαμβάνεται`
                                                                WHERE `περιλαμβάνεται`.`ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ`=%s)
            AND `περιλαμβάνεται`.`ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ`!=%s""" %(kod_arthrou,kod_arthrou)
    c1=[]
    c2=[]
    mycursor.execute(sql)
    result=mycursor.fetchall()
    sql1 ="""SELECT DISTINCT `ΠΕΡΙΟΔΙΚΟ`.`ΟΝΟΜΑ`
            FROM `περιλαμβάνεται`
            JOIN `ΠΕΡΙΟΔΙΚΟ` ON `περιλαμβάνεται`.`ΚΩΔΙΚΟΣ ΠΕΡΙΟΔΙΚΟΥ` = `ΠΕΡΙΟΔΙΚΟ`.`ΚΩΔΙΚΟΣ ΠΕΡΙΟΔΙΚΟΥ`
            WHERE `περιλαμβάνεται`.`ΚΩΔΙΚΟΣ ΠΕΡΙΟΔΙΚΟΥ` IN (SELECT  `περιλαμβάνεται`.`ΚΩΔΙΚΟΣ ΠΕΡΙΟΔΙΚΟΥ`
                                                                FROM `περιλαμβάνεται`
                                                                WHERE `περιλαμβάνεται`.`ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ`=%s)""" %(kod_arthrou)
    mycursor.execute(sql1)
    a=mycursor.fetchall()

    print("\n\n============================================================")
    print("Το άρθρο εκδόθηκε από το ακόλουθο περιοδικό:")
    for i in a:
        print(i.get("ΟΝΟΜΑ"))
    print("\n\nΟκ, αναζήτηση άλλων άρθρων του συγκεκριμένου περιοδικού...\n")
    print("============================================================")
    if len(result)!=0:
        for i in result:
            c1.append(i.get("ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ"))
            c2.append(i.get("ΤΙΤΛΟΣ"))
        what_to_do_with_article(c1,c2)
    else:print("\nΛυπούμαστε αλλά δεν υπάρχουν άλλα άρθρα του συγκεκριμένου περιοδικού!!\n\n")

##====================================================


def add_to_history(kod_arthrou):
    
    try:
        file = open("history.txt","r+")
    except IOError:
        file = open("history.txt","w+")

    
    data = file.read().splitlines()
    file.close()
    a=len(data)
    if a == 0:
        hist = open("history.txt","a")
        hist.write(kod_arthrou)
        hist.write("\n")
        hist.close()
    elif a!=0 and kod_arthrou!=data[-1]:
        hist = open("history.txt","a")
        hist.write(kod_arthrou)
        hist.write("\n")
        hist.close()
        
def open_history():
    hist = open("history.txt","r+")
    data = hist.read().splitlines()
    hist.close()
    c1=[]
    c2=[]
    if len(data)!=0:
        for i in data:
            if i != "":
                c1.append(i)
        for i in c1:
            sql ="""SELECT `ΤΙΤΛΟΣ`
                    FROM `ΕΠΙΣΤΗΜΟΝΙΚΟ ΑΡΘΡΟ`
                    WHERE `ΕΠΙΣΤΗΜΟΝΙΚΟ ΑΡΘΡΟ`.`ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ` = %s """%i
            mycursor.execute(sql)
            result=mycursor.fetchall()
            c2.append(result[0].get("ΤΙΤΛΟΣ"))
        what_to_do_with_article(c1,c2)
    else:print("\nΤΟ ΙΣΤΟΡΙΚΟ ΑΝΑΖΗΤΗΣΕΩΝ ΣΑΣ ΕΙΝΑΙ ΚΕΝΟ !!")
        
    

def add_to_favourites(kod_arthrou):
    try:
        fav = open("favourites.txt","r+")
    except IOError:
        fav = open("favourites.txt","w+")
        
    data = fav.read().splitlines()
    fav.close()

    if (kod_arthrou in data):
        print("\n\nΤΟ ΣΥΓΚΕΚΡΙΜΕΝΟ ΑΡΘΡΟ ΕΙΝΑΙ ΗΔΗ ΣΤΑ ΑΓΑΠΗΜΕΝΑ !!")
        print("====================================================")
        print("\n\nΑν θέλετε να το αφιρέσετε απο τα αγαπημένα πατήστε 1")
        print("Αν όχι πατήστε κάτι για να συνεχίσετε.\n")
        a = input()
        if a=="1":
            fav = open("favourites.txt","r+")
            data = fav.read()
            data = data.replace(kod_arthrou,"")
            fav.close()
            fav = open("favourites.txt","w")
            fav.write(data)
            fav.close()
            print("\n\nΤΟ ΣΥΓΚΕΚΡΙΜΕΝΟ ΑΡΘΡΟ ΑΦΑΙΡΕΘΗΚΕ ΕΠΙΤΥΧΩΣ ΑΠΟ ΤΑ ΑΓΑΠΗΜΕΝΑ !!")  
    else:
        fav = open("favourites.txt","a")
        fav.write(kod_arthrou)
        fav.write("\n")
        fav.close()
        print("\n\nΤΟ ΣΥΓΚΕΚΡΙΜΕΝΟ ΑΡΘΡΟ ΠΡΟΣΤΕΘΗΚΕ ΕΠΙΤΥΧΩΣ ΣΤΑ ΑΓΑΠΗΜΕΝΑ!!")
        print("====================================================")

def open_favourites():
    fav = open("favourites.txt","r+")
    data = fav.read().splitlines()
    fav.close()
    c1=[]
    c2=[]
    if len(data)!=0:
        for i in data:
            if i != "":
                c1.append(i)
        for i in c1:
            sql ="""SELECT `ΤΙΤΛΟΣ`
                    FROM `ΕΠΙΣΤΗΜΟΝΙΚΟ ΑΡΘΡΟ`
                    WHERE `ΕΠΙΣΤΗΜΟΝΙΚΟ ΑΡΘΡΟ`.`ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ` = %s """%i
            mycursor.execute(sql)
            result=mycursor.fetchall()
            c2.append(result[0].get("ΤΙΤΛΟΣ"))
        what_to_do_with_article(c1,c2)
    else:print("\nΔΕΝ ΕΧΕΙ ΠΡΟΣΤΕΘΕΙ ΑΚΟΜΑ ΚΑΤΙ ΣΤΑ ΑΓΑΠΗΜΕΝΑ\n\n")
    
    

#### Συναρτήσεις που μέσω query βρίσκουν τα ζητούμενα επιστημονικά άρθρα
##==============================================================================##

##Συνάρτηση που επιστρέφει επιστημονικά άρθρα που αντιστοιχούν σε ένα επιστημονικό πεδίο
def sub_to_art(specific_subject):
    arts = """SELECT `ΤΙΤΛΟΣ`, `ΕΠΙΣΤΗΜΟΝΙΚΟ ΑΡΘΡΟ`.`ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ`
            FROM `αναφέρεται`
            JOIN `ΕΠΙΣΤΗΜΟΝΙΚΟ ΑΡΘΡΟ` ON  `αναφέρεται`.`ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ` =  `ΕΠΙΣΤΗΜΟΝΙΚΟ ΑΡΘΡΟ`.`ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ`
            JOIN `ΕΠΙΣΤΗΜΟΝΙΚΟ ΠΕΔΙΟ` ON `αναφέρεται`.`ΚΩΔΙΚΟΣ ΕΠΙΣΤΗΜΟΝΙΚΟΥ ΠΕΔΙΟΥ` =  `ΕΠΙΣΤΗΜΟΝΙΚΟ ΠΕΔΙΟ`.`ΚΩΔΙΚΟΣ ΕΠΙΣΤΗΜΟΝΙΚΟΥ ΠΕΔΙΟΥ`
            WHERE `ΕΠΙΣΤΗΜΟΝΙΚΟ ΠΕΔΙΟ`.`ΟΝΟΜΑ` LIKE %s"""
    mycursor.execute(arts,(specific_subject ,))    
    result1 = mycursor.fetchall()
    global kod_arthr
    kod_arthr=[]
    al=[]
    c2=[]
    if len(result1)!=0:
        for i in result1:
            al.append(list(i.values()))
            kod_arthr.append(i.get("ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ"))
        for i in range(len(al)) :
            c2.append(al[i][0])

        what_to_do_with_article(kod_arthr,c2)
    else:print("\nΛυπούμαστε αλλά δεν υπάρχουν άρθρα του συγκεκριμένου πεδίου!!\n\n")

##Συνάρτηση που επιστρέφει επιστημονικά άρθρα που αντιστοιχούν σε ένα συγγραφέα
def aut_to_art(specific_author):
    autlen=len(specific_author)
    ar = """SELECT DISTINCT `ΕΠΙΣΤΗΜΟΝΙΚΟ ΑΡΘΡΟ`.`ΤΙΤΛΟΣ`, `ΕΠΙΣΤΗΜΟΝΙΚΟ ΑΡΘΡΟ`.`ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ`
            FROM `συγγράφει`
            JOIN `ΕΠΙΣΤΗΜΟΝΙΚΟ ΑΡΘΡΟ` ON `συγγράφει`.`ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ` = `ΕΠΙΣΤΗΜΟΝΙΚΟ ΑΡΘΡΟ`.`ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ`
            JOIN `ΣΥΓΓΡΑΦΕΑΣ` ON `συγγράφει`.`ΚΩΔΙΚΟΣ ΣΥΓΓΡΑΦΕΑ` = `ΣΥΓΓΡΑΦΕΑΣ`.`ΚΩΔΙΚΟΣ ΣΥΓΓΡΑΦΕΑ`
            WHERE `ΣΥΓΓΡΑΦΕΑΣ`.`ΚΩΔΙΚΟΣ ΣΥΓΓΡΑΦΕΑ` = %s"""
    if autlen==1 and specific_author!="9":
        st = "20000"
    elif autlen == 2 or specific_author=="9": st = "2000"
    kod_sygg = st + str(int(specific_author)+1)
    mycursor.execute(ar,(kod_sygg))
    result2 = mycursor.fetchall()
    global kod_arthr
    kod_arthr=[]    
    al=[]
    c2=[]
    if len(result2)!=0:
        for i in result2:
            al.append(list(i.values()))
            kod_arthr.append(i.get("ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ"))
        for i in range(len(al)) :
            c2.append(al[i][0])
        what_to_do_with_article(kod_arthr,c2)
    else:print("\nΛυπούμαστε αλλά δεν υπάρχουν άρθρα του συγκεκριμένου συγγραφέα!!\n\n")
    
##Συνάρτηση που επιστρέφει επιστημονικά άρθρα που αντιστοιχούν σε έναν φορέα
def ins_to_art(specific_inst):
    instlen=len(specific_inst)
    ar1 = """ SELECT DISTINCT `ΕΠΙΣΤΗΜΟΝΙΚΟ ΑΡΘΡΟ`.`ΤΙΤΛΟΣ`, `ΕΠΙΣΤΗΜΟΝΙΚΟ ΑΡΘΡΟ`.`ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ`
                FROM `συγγράφει`
                JOIN `ΕΠΙΣΤΗΜΟΝΙΚΟ ΑΡΘΡΟ` ON `συγγράφει`.`ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ` = `ΕΠΙΣΤΗΜΟΝΙΚΟ ΑΡΘΡΟ`.`ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ`
                JOIN `ΦΟΡΕΑΣ` ON `συγγράφει`.`ΚΩΔΙΚΟΣ ΦΟΡΕΑ` = `ΦΟΡΕΑΣ`.`ΚΩΔΙΚΟΣ ΦΟΡΕΑ`
                WHERE `ΦΟΡΕΑΣ`.`ΚΩΔΙΚΟΣ ΦΟΡΕΑ` = %s """
    if instlen==1 and specific_inst!="9":
        f = "30000"
    elif instlen==2 or specific_inst=="9": f = "3000"
    kod_forea = f + str(int(specific_inst)+1)
    mycursor.execute(ar1,(kod_forea))
    result3 = mycursor.fetchall()
    global kod_arthr
    kod_arthr=[]    
    al=[]
    c2=[]
    if len(result3)!=0:
        for i in result3:
            al.append(list(i.values()))
            kod_arthr.append(i.get("ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ"))
        for i in range(len(al)) :
            c2.append(al[i][0])
        what_to_do_with_article(kod_arthr,c2)
    else:print("\nΛυπούμαστε αλλά δεν υπάρχουν άρθρα του συγκεκριμένου φορέα!!\n\n")

##Συνάρτηση που επιστρέφει επιστημονικά άρθρα που αντιστοιχούν σε ένα περιοδικό
def mag_to_art(specific_magazine):
    maglen=len(specific_magazine)
    ar2 = """SELECT `ΤΙΤΛΟΣ`, `ΕΠΙΣΤΗΜΟΝΙΚΟ ΑΡΘΡΟ`.`ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ`
                FROM `περιλαμβάνεται`
                JOIN `ΕΠΙΣΤΗΜΟΝΙΚΟ ΑΡΘΡΟ` ON  `περιλαμβάνεται`.`ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ` =  `ΕΠΙΣΤΗΜΟΝΙΚΟ ΑΡΘΡΟ`.`ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ`
                WHERE `περιλαμβάνεται`.`ΚΩΔΙΚΟΣ ΠΕΡΙΟΔΙΚΟΥ`=%s"""
    if maglen==1 and specific_magazine!="9":
        p = "10000"
    elif maglen==2 or specific_magazine=="9": p = "1000"
    kod_per = p + str(int(specific_magazine)+1)
    mycursor.execute(ar2,(kod_per))
    result4 = mycursor.fetchall()
    global kod_arthr
    kod_arthr=[]    
    al=[]
    c2=[]
    if len(result4)!=0:
        for i in result4:
            al.append(list(i.values()))
            kod_arthr.append(i.get("ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ"))
        for i in range(len(al)) :
            c2.append(al[i][0])
        what_to_do_with_article(kod_arthr,c2)
    else:print("\nΛυπούμαστε αλλά δεν υπάρχουν άρθρα του συγκεκριμένου περιοδικού!!\n\n")
##==============================================================================##

#### Συναρτήσεις που θα καλούνται στο βασικό μενού
##==============================================================================##
## Συνάρτηση που καλείται για αναζήτηση άρθρων με αφετηρία το επιστημονικό πεδίο
def from_subjects():
    subject = create_subject()
    print('\nΕΠΙΣΤΗΜΟΝΙΚΑ ΠΕΔΙΑ:')
    print('========================')  
    j=1
    for i in subject:
        print(j,i)
        j=j+1
    while True:
        sub = input('\nΚωδικός επιστημονικού πεδίου:')
        if sub.isdigit() and int(sub) > 0 and int(sub) <= len(subject):
            sub = int(sub)-1
            print('\n\nοκ, ... Αναζήτηση άρθρων για πεδίο:', subject[sub])
            sub_to_art(subject[sub])
            break
        else:print("Πληκτρολγήστε έναν σωστό αριθμό")
    
    
## Συνάρτηση που καλείται για αναζήτηση άρθρων με αφετηρία τον συγγραφέα
def from_authors():
    author = create_author()
    print("\nΣΥΓΓΡΑΦΕΙΣ:")
    print('========================')  
    j=1
    for i in author:
        print(j,i[0],i[1])
        j=j+1
    while True:
        aut = str(input('\nΚωδικός αρθρογράφου:'))
        if aut.isdigit() and int(aut) > 0 and int(aut) <= len(author):
            aut = int(aut)-1
            print("\nΤο προφίλ του συγγραφέα που αναζητήσατε είναι το εξής:")
            print("=======================================================")
            full_auth(str(aut))
            print("=======================================================")
            print('\nοκ, ... Αναζήτηση άρθρων του/της συγγραφέα:', author[aut][0], author[aut][1])
            aut_to_art(str(aut))
            break
        else:print("Πληκτρολγήστε έναν σωστό αριθμό")
        

## Συνάρτηση που καλείται για αναζήτηση άρθρων με αφετηρία τον φορέα
def from_institutions():
    institution = create_institutions()
    print('\nΦΟΡΕΙΣ:')
    print('========================')  
    j=1
    for i in institution:
        print(j,i[0])
        j=j+1
    while True:
        ins = input('\nΚωδικός φορέα:')
        if ins.isdigit() and int(ins) > 0 and int(ins) <= len(institution):
            ins = int(ins)-1
            print("\nΤο προφίλ του φορέα που αναζητήσατε είναι το εξής:")
            print("=======================================================")
            full_inst(str(ins))
            print("=======================================================")
            print('\nοκ, ... Αναζήτηση άρθρων του φορέα:', institution[ins][0])
            ins_to_art(str(ins))
            break
        else:print("Πληκτρολγήστε έναν σωστό αριθμό")


## Συνάρτηση που καλείται για αναζήτηση άρθρων με αφετηρία το περιοδικό
def from_magazines():
    magazine = create_magazines()
    print('\nΠΕΡΙΟΔΙΚΑ:')
    print('========================')  
    j=1
    for i in magazine:
        print(j,i[0])
        j=j+1
    while True:
        mag = input('\nΚωδικός περιοδικού:')
        if mag.isdigit() and int(mag) > 0 and int(mag) <= len(magazine):
            mag = int(mag)-1
            print("\nΤο προφίλ του περιοδικού που αναζητήσατε είναι το εξής:")
            print("=======================================================")
            full_magaz(str(mag))
            print("=======================================================")
            print('\nοκ, ... Αναζήτηση άρθρων του περιοδικού:', magazine[mag][0])
            mag_to_art(str(mag))
            break
        else:print("Πληκτρολγήστε έναν σωστό αριθμό")
        
def from_title():
    s1="select `ΤΙΤΛΟΣ`, `ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ` FROM `ΕΠΙΣΤΗΜΟΝΙΚΟ ΑΡΘΡΟ` "
    mycursor.execute(s1)
    a=mycursor.fetchall()
    c1=[]
    c2=[]
    for i in a:
        b=i.get('ΚΩΔΙΚΟΣ ΑΡΘΡΟΥ')
        c1.append(b)
        c2.append(i.get('ΤΙΤΛΟΣ'))
    what_to_do_with_article(c1,c2)


##==============================================================================##

def main_menu():
    while True:
        print("\n\nΑ Ρ Χ Ι Κ Ο   Μ Ε Ν Ο Υ\n")
        print("===========================")
        print("===========================\n")
        print("ΕΠΙΛΟΓΗ ΤΡΟΠΟΥ ΑΝΑΖΗΤΗΣΗΣ (enter για έξοδο)")
        print("==========================================")
        print("1: Αν θέλετε να αναζητείτε άμεσα δηλαδή να πληκτρολογείτε αυτό που ψάχνετε και όχι να επιλέγετε μέσω μιας λίστας\n")
        print("2: Αν θέλετε να αναζητείτε έμεσα δηλαδή να επιλέγετε μέσω μιας λίστας\n")
        print("3: Αν θέλετε να δείτε τα άρθρα που έχετε αποθηκεύσει στα αγαπημένα\n")
        print("4: Αν θέλετε να δείτε το ιστορικό τών άρθρων που έχετε επισκεφτεί (απο τα παλιά στα νεότερα)\n")
        ans = input("Πατήστε το αντίστοιχο νούμερο για να επιλέξετε τρόπο αναζήτησης: ")
        if ans == "1":
            print('\nΕΠΙΛΟΓΕΣ (enter για έξοδο)')
            print('1: Αναζήτηση άρθρου μέσω των επιστημονικών πεδίων')
            print('2: Αναζήτηση άρθρου μέσω των συγγραφέων')
            print('3: Αναζήτηση άρθρου μέσω των φορέων')
            print('4: Αναζήτηση άρθρου μέσω των περιοδικών')
            print('5: Αναζήτηση άρθρου μέσω λέξης κλειδιού')
            answer = input("Πατήστε το αντίστοιχο νούμερο για να επιλέξετε τρόπο αναζήτησης: ")
            if answer == "1":
                episthmoniko_pedio_search()
            elif answer == "2":
                author_search()
            elif answer == "3":
                foreas()
            elif answer == "4":
                magazine_search()
            elif answer == "5":
                key_words()
            elif answer == "":break
            else:print("Προσπαθήστε ξανά...\n")
        elif ans == "2":
            print('\nΕΠΙΛΟΓΕΣ (enter για έξοδο)')
            print('1: Αναζήτηση άρθρου μέσω των επιστημονικών πεδίων')
            print('2: Αναζήτηση άρθρου μέσω των συγγραφέων')
            print('3: Αναζήτηση άρθρου μέσω των φορέων')
            print('4: Αναζήτηση άρθρου μέσω των περιοδικών')
            print('5: Αναζήτηση χωρίς φίλτρο')
            answer = input("Πατήστε το αντίστοιχο νούμερο για να επιλέξετε τρόπο αναζήτησης: ")
            if answer == "1":
                from_subjects()
            elif answer == "2":
                from_authors()
            elif answer == "3":
                from_institutions()
            elif answer == "4":
                from_magazines()
            elif answer == "5":
                from_title()
            elif answer == "":break
            else:print("Προσπαθήστε ξανά...\n")
        elif ans == "3":
            open_favourites()
        elif ans == "4":
            open_history()
        elif ans == "":break
        else:print("Προσπαθήστε ξανά...\n")

main_menu()

# open_art("400001")




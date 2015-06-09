import smtplib 
from email.mime.text import MIMEText as MIME
# Credentials (if needed)
username = 'colinmcd94'  
password = 'mensetmanus'  

def setup_server():
    # The actual mail send  
    server = smtplib.SMTP('smtp.gmail.com:587')  
    server.starttls()  
    server.login(username,password)
    return server

def send(server,msg):
    m = MIME(msg)
    m['Subject'] = ""
    m['From'] = 'Colin McDonnell <colinmcd94@gmail.com>'
    m['To'] = "notes@fetchnotes.com"
    server.sendmail(m["From"], m["To"].split(","), m.as_string())
    ##send(server,"this is a test","jabberwocky","colinmcd@mit.edu")

databases = [["emerging",["emerging","technology","opportunity"]]]#["book","concept","field","genius","paper","skill"]

def get_data(database):
    fh = open("data/"+database+".txt", "r")
    data = fh.readlines()
    return data



server = setup_server()

for database in databases[2:]:
    data = get_data(database)
    for datum in data:
        try:
            print "#"+database+" "+ datum[2:]
            send(server,"#"+database+" "+ datum[2:])
        except:
            print "Server unexpectedly shut down"
            print "deleting server..."
            del server
            print "restarting server..."
            server = setup_server()
            print "server restarted.  commencing."
        
        
server.quit()
    

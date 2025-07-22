f=open("/etc/ssh/sshd_config")

find_password_option=False 


for line in f:
    if line[0]=="#":
        continue
    if "Password" in line:
        print(line)
    if line.strip() =="PasswordAuthentication no":
        find_password_option=True

if find_password_option ==True: 
    print("you are secure")  
else :
    print("you are not secure")

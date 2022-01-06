import logging

    
print("""
    1.install wordpress
    2.backup and send to ftp server
    3.reset wordpress
    4.restore last backup
    """)
ans= input("What would you like to do? ")
if ans=="1":
    print("\n Launch install")
elif ans=="2":
    print("\n Launch backup")
elif ans=="3":
    print("\n Launch reset")
elif ans=="4":
    print("\n Launch restore") 
else:
    print("\n Choose an option, try again!")
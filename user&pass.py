# THIS IS A LOGIN SCREEN, IT ASK FOR USER NAME AND PASSWORD
print(
    """\033[1;33m
    _____________________________________________________________
    |                           Welcome                          |
    | 123234r359095y90589086902869062525492684903689023869038903 |
    | 990238628858290802996996A456646489988489894904428048u13848 |
    | 9048q90835290890283iiguwru98wu89892757172567ythy387y5r6g54 |
    | gtr8tg489r489489r48845561321111111111111144grt84894gr98g49 |
    | gtejiojhioer8789988998789789789789789789789789789456564562 |
    | 88888897/79878984865484894tgr489gt89rg89t7g/t7486489748948 |
    | 9888*/8/8955288/*/*7/*589486848941605486048489489484989848 |
    |____________________________________________________________|
    |THiS is FOR kali.org |
    |_____________________|________________@
                          |BY = AHMAD H-K|
                          |--------------|

    """
)

# THIS IS A LOGIN SCREEN IT ASK FOR USERNAME AND PASSWORD, THERE IS MORE FROM ONE USER&PASS.


print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\twelcome ")
print("1. login using your username & password")
print("2. exit form this program\n\n")

Q1 = input("root@#kali: ")
if Q1 == "2":
    exit()

if Q1 == "1":
    security = 0
    # THIS IS ASK FOR THE USER
    username = ""
    while not username:
        username = input("\033[1;33mUsername: ")

    # THIS IS ASK FOR PASSWORD
    password = ""
    while not password:
        password = input("\033[32mPassword: ")

    # THIS IS IF THE USERNAME = "" AND THE PASSWORD = "" IT WILL WORK
    if username == "had90" and password == "909090":
        print("\t\t\t\t\t\t\t\tWelcome to login screen \n")
        How = input("how are you today: ")
        security = 5

    # THIS IS USER LOGIN IF THE USERNAME AND PASSWORD == TRUE  IT WILL ASK FOR 3 SECURITY Q
    elif username == "hajja1020" and password == "78451200":
        print("HAVE 3 SECURITY QUOTATIONS ")
        security = 10
        print("37 ** 7145/*")
        A = input("root@#kali: ")
        if A == "909090":
            print("password")
            B = input("root@#kali: ")
            if B == "898989":
                print("C")
                C = input("root@#klai: ")
                if C == "2":
                    print("|########################################|")
                    print("|1. SCAN A PEROT                         |")
                    print("|2. SCAN A WIFI                          |")
                    print("|3. MAC  A ADDERS                        |")
                    print("|########################################|")
                    perot = input("root@#kali: ")
                    if perot == "1":
                       import PS
                       print(PS)
                       if perot == "2":
                          exit()
                    if perot == "2":
                        print("WIFI")
                    if perot == "3":
                        print("MAC")

    # IF THE USERNAME = "NOT" OR PASSWORD = "NOT" IT WILL PRINT THE LINE AIDER ELSE

import socket
import threading
import time


localtime = time.asctime(time.localtime(time.time()))

IP = input("Enter the target IP ----> ")
target = IP
print("\033[1;33m----------------------------------------------")
print("\033[1;33mLocal current time :", localtime)
print("----------------------------------------------")
print("\033[32mThe scan has been start ")
print("----------------------------------------------")


# ip = socket.getmodulename(target)

def portscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)  #

    try:
        con = s.connect((target, port))
        print("|#######################|")
        print('|{+} :', port, "is open.     |")
        print("|#######################|")

        con.close()
    except:
        pass


r = 1
for x in range(1, 10000):
    t = threading.Thread(target=portscan, kwargs={'port': r})

    r += 1
    t.start()
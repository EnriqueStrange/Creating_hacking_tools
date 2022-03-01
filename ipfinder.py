import socket

hostname = socket.gethostname()

print("YOU ARE WORKING ON " + hostname)
print("YOUR IP IS " + socket.gethostbyname(hostname))

url = input("ENTER THE URL TO SCAN >> ")
print("THE IP FOR " + url + " IS ",socket.gethostbyname(url))
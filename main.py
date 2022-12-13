from Server_api import Server

#u open the file u want to decode (open("[FILENAME]", "rb") and one to write in (open("[FILENAME]", "a")
file_handler = open("ips", "rb")
save_response = open("server_scan.txt", "a")

count = 0 #start a counter to count the ips (not important)

while True: #make a loop
    percent = round(count / 304228 * 100, 3) #create an percent value for the counter (not important)

    #u read the first byte
    byteone = file_handler.read(1)
    b1 = int.from_bytes(byteone, "big", signed=False)
    #if the first byte is 0 it will stop the script: Because an IP-Adress can't be 0 in the first digit it will stop when the list reach the bottom
    if b1 == 0:
        break

    #u read the second byte
    bytetwo = file_handler.read(1)
    b2 = int.from_bytes(bytetwo, "big", signed=False)

    #u read the third byte
    bytethree = file_handler.read(1)
    b3 = int.from_bytes(bytethree, "big", signed=False)

    #u read the fourht byte
    bytefour = file_handler.read(1)
    b4 = int.from_bytes(bytefour, "big", signed=False)

    #u read the last to bytes to get the port
    bytefive = file_handler.read(2)
    b5 = int.from_bytes(bytefive, "big", signed=False)

    count = count + 1 #sets the ip counter 1 up

    ip = str(b1) + "." + str(b2) + "." + str(b3) + "." + str(b4)
    port = b5

    def search_str(file_path, word): #make a defenition to search in the script
        with open(file_path, 'r') as file:
            content = file.read()
            if word in content: #if it finds the ip in the text file it will skip it
                pass
            else:
                save_response.write(str(ip) + ":" + str(port))
                try:
                    pinger = Server(host=ip, port=port) #you ping the server
                    response = pinger.get_status() #and get the response
                    save_response.write(str(response) + "\n" + "\n")
                except:
                    save_response.write(" FAILED" + "\n" + "\n") #when the ip is not reachable, it will continue
                    pass

    search_str(r'F:\Projects\serverscanner\server_scan.txt', ip) #that is your file path where it search for the scanned ips

    print(str(count) + " " + "(" + str(percent) + "%" + ")", end='')
    print(str(ip) + ":" + str(port))

print("\n", end='')

#print how many ips you have scanned
print("You scanned " + str(count) + " " + "(" + str(percent) + "%" + ")" + " ips.")
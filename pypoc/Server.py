global sep
sep = "\u2063"

def packet(type: str, username: str, port: int, message: str):
    if type == "M":
        return(type+sep+username+sep+message+sep)
    if type == "J":
        return(type+sep+username+sep+str(port)+sep)

def parsePacket(packetContents: str):
    temptracker = 0
    temp = ""
    returnlist = ["","",""]
    for i in packetContents:
        if i != sep:
            temp = temp + i
        else:
            returnlist[temptracker] = temp
            temp = ""
            temptracker += 1
    return(returnlist)


pacdata = packet("J", "dimit", 3978, "hello world")
print(pacdata)
print(parsePacket(pacdata))


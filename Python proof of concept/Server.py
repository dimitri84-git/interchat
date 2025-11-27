global sep
sep = "\u2063"

def packet(type: str, username: str, port: int, message: str):
    if type == "M":
        return(type+sep+username+sep+message)
    if type == "J":
        return(type+sep+username+sep+port)

print(packet("M", "dimit", 3978, "hello world"))
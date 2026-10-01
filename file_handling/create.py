#file=open("team.txt","a")
#file.write("append mode added some new data to file .....\n new line")
#file.close()
#file=open("team.txt","r")
#data=file.read()
#print(data)
#file.close()

with open("team.txt","r") as file:
    lines=file.readlines()
    for line in lines:
        print(line,end="")
import checker
import json

with open("bincodes.txt") as file:
    lines = [line.rstrip() for line in file]

for bin in lines:
    check = checker.check(bin=bin)
    data1 = json.dumps(check)
    data = json.loads(data1)
    #data = json.loads(check)
    #print(data)
    print(data['Bin'])
    print(data['Type'])
    print(data['Brand'])
    print(data['Catergory'])
    print(data['Bank'])
    print(data['Bank_URL'])
    print(data['Country'])
    print(data['Country_Short'])



    f= open("checked_list.txt","a")
    f.write("\n")
    f.write("================================================================================"+"\n")
    f.write("BIN - "+ data['Bin']+"\n")
    f.write("Type - "+ data['Type']+"\n")
    f.write("Brand - "+ data['Brand']+"\n")
    f.write("Catergory - "+ data['Catergory']+"\n")
    f.write("Bank - "+ data['Bank']+"\n")
    f.write("Bank_URL - "+ data['Bank_URL']+"\n")
    f.write("Country - "+ data['Country']+"\n")
    f.write("                       Checked By Bin-X")
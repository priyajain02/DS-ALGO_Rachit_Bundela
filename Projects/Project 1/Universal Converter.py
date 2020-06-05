def binary_to_decimal(s):
    ans = 0
    val = 1
    for i in range(len(s) - 1,-1,-1):
        if(s[i] != "1" and s[i] != '0'):
            return("NOT A VALID STRING")
        ans = ans + (val * int(s[i]))
        val = val * 2

    return ans

def decimal_to_binary(s):
    ans = ""

    while(s>0):
        ans = str(s%2) + ans
        s = s//2

    return ans

def decimal_to_octal(s):
        ans = ""

        while(s>0):
            ans = str(s%8) + ans
            s = s//8


        return ans

def octal_to_decimal(s):

    ans = 0
    val = 1
    for i in range(len(s) - 1,-1,-1):
        if(int(s[i]) >= 8):
            return("NOT A VALID STRING")
        ans = ans + (val * int(s[i]))
        val = val * 8

    return ans

def hexadecimal_to_decimal(s):

    ans = 0
    val = 1
    for i in range(len(s) - 1,-1,-1):

        if(ord(s[i]) - ord('A') >= 0):
            num = ord(s[i]) - ord('A') + 10
            if(num > 15):
                return("NOT A VALID STRING")
        else:
            num = int(s[i])

        ans = ans + (val * num)
        val = val * 16

    return ans

def decimal_to_hexadecimal(s):
        ans = ""

        while(s>0):
            rem = s%16
            if(rem>=10):
                rem = chr(65 + rem - 10)
            ans = str(rem) + ans
            s = s//16

        return ans

def binary_to_octal(n):
    i=len(n)
    j=len(n)
    final=[]
    while(i>0):
        if(j>=3):
            res=n[j-3:j]
        elif(j==2):
            res=n[j-2:j]
        else:
            res=n[j-1:j]
        if(res=='000' or res=='00' or res=='0'):
                final.insert(0,'0')
                j=j-3
        elif(res=='001' or res=='01' or res=='1'):
                final.insert(0,'1')
                j=j-3
        elif(res=='010' or res=='10'):
                final.insert(0,'2')
                j=j-3
        elif(res=='011' or res=='11'):
                final.insert(0,'3')
                j=j-3
        elif(res=='100'):
                final.insert(0,'4')
                j=j-3
        elif(res=='101'):
                final.insert(0,'5')
                j=j-3
        elif(res=='110'):
                final.insert(0,'6')
                j=j-3
        elif(res=='111'):
                final.insert(0,'7')
                j=j-3
        else:
            print("Invalid Binary string")
            exit()
        i-=3
    s = "".join(final)
    return s

def octal_to_binary(n):
    ans = ""
    for i in range(len(n)):
        if(n[i]=='0'):
            ans += "000"
        elif(n[i]=='1'):
            ans += "001"
        elif(n[i]=='2'):
            ans += "010"
        elif(n[i]=='3'):
            ans += "011"
        elif(n[i]=='4'):
            ans += "100"
        elif(n[i]=='5'):
            ans += "101"
        elif(n[i]=='6'):
            ans += "110"
        elif(n[i]=='7'):
            ans += "111"
        else:
            return "NOT A VALID STRING"
    return ans

def binary_to_hexadecimal(s):
    dec = binary_to_decimal(s)
    if(dec == "NOT A VALID STRING"):
        return dec
    dec = int(dec)
    return decimal_to_hexadecimal(dec)

def hexadecimal_to_binary(hexdec):
    ans = ""
    for i in range(len(hexdec)):
        if(hexdec[i]=='0'):
            ans += "0000"
        elif (hexdec[i]=='1'):
            ans += "0001"
        elif (hexdec[i]=='2'):
            ans += "0010"
        elif (hexdec[i]=='3'):
            ans += "0011"
        elif (hexdec[i]=='4'):
            ans += "0100"
        elif (hexdec[i]=='5'):
            ans += "0101"
        elif (hexdec[i]=='6'):
            ans += "0110"
        elif (hexdec[i]=='7'):
            ans += "0111"
        elif (hexdec[i]=='8'):
            ans += "1000"
        elif (hexdec[i]=='9'):
            ans += "1001"
        elif (hexdec[i]=='A' or hexdec[i]=='a'):
            ans += "1010"
        elif (hexdec[i]=='B' or  hexdec[i]=='b'):
            ans += "1011"
        elif (hexdec[i]=='C' or hexdec[i]=='c'):
            ans += "1100"
        elif (hexdec[i]=='D' or hexdec[i]=='d'):
            ans += "1101"
        elif (hexdec[i]=='E' or hexdec[i]=='e'):
            ans += "1110"
        elif (hexdec[i]=='F' or hexdec[i]=='f'):
            ans += "1111"
        else:
            return("Invalid hexadecimal digit")
    return ans

def Octal_to_hexadecimal(s):
    dec = octal_to_decimal(s)
    if(dec == "NOT A VALID STRING"):
        return dec
    dec = int(dec)
    return decimal_to_hexadecimal(dec)

def Hexadecimal_to_octal(s):
    dec = hexadecimal_to_decimal(s)
    if(dec == "NOT A VALID STRING"):
        return dec
    dec = int(dec)
    return decimal_to_octal(dec)

print("\nWelcome to universal converter\n")
while(True):

    print("choose your conversion type:\n")
    print("Binary to decimal :             1")
    print("Decimal to binary :             2")
    print("Decimal to octal :              3")
    print("Octal to decimal :              4")
    print("Hexadecimal to decimal:         5")
    print("Decimal to hexadecimal:         6")
    print("Binary to octal:                7")
    print("Octal to binary:                8")
    print("Binary to hexadecimal:          9")
    print("Hexadecimal to binary:         10")
    print("Octal to hexadecimal:          11")
    print("Hexadecimal to octal:          12")

    print("Enter 0 to exit")

    type = int(input())

    if(type==0):
        print("Thank you")
        break

    print("Enter Input")
    s = input()
    print()

    if(type==1):
        print("Answer = ", binary_to_decimal(s))

    if(type==2):
        print("Answer = ", decimal_to_binary(int(s)))

    if(type==3):
        print("Answer = ", decimal_to_octal(int(s)))

    if(type==4):
        print("Answer = ", octal_to_decimal(s))

    if(type==5):
        print("Answer = ", hexadecimal_to_decimal(s))

    if(type==6):
        print("Answer = ", decimal_to_hexadecimal(int(s)))

    if(type==7):
        print("Answer = ", binary_to_octal(s))

    if(type==8):
        print("Answer = ", octal_to_binary(s))

    if(type==9):
        print("Answer = ", binary_to_hexadecimal(s))

    if(type==10):
        print("Answer = ", hexadecimal_to_binary(s))

    if(type==11):
        print("Answer = ", Octal_to_hexadecimal(s))

    if(type==12):
        print("Answer = ", Hexadecimal_to_octal(s))

    print()

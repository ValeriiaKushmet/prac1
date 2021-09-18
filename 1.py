def program():

    def getNumber(message):
        temp = 0
        try:
            temp = int(input(message))
            
        except ValueError:
            print("You entered not a num, try again")
            return getNumber(message)
        return temp
    def startProgram():
        answer = getNumber('Hochete prodovzhyty robotu z programoyu? \nNatysnit 1 - tak, 0 - ni: ')
        if answer == 0 or answer == 1:
            if answer == 1:
                program()
                
            else: 
                print('bye bye!')
        else:
            print("You entered not 0 or 1")
            startProgram()
    

    a = getNumber("input a:")
    b = getNumber("input b:")
    c = getNumber("input c:")
    
    print("a =", a, "b = ", b, "c = ", c)

    tempA = int(a)
    tempB = int(b)
    tempC = int(c)
    
    startProgram()
print('Lab1 \n "Programuvannya liniynych algorytmiv ta rozhhaludzhenych protsesiv" \n\t Kushmet Km-12, 12 variant')
print('Dano zminni a, b, c. \nZminyty yich znachennia tak, shchob:\n\ta zberigalosia znachennia a+b;\n\tv b stari znachennia c-a;\n\tv c suma starych znachen a+b+c')    
program();

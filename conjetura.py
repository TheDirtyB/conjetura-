
#################################################################################################################################


primos=(3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,
73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,
179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,
283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409,
419,421,431,433,439,443,449,457,461,463,467,479,487,491,499,503,509,521,523,541,
547,557,563,569,571,577,587,593,599,601,607,613,617,619,631,641,643,647,653,659,
661,673,677,683,691,701,709,719,727,733,739,743,751,757,761,769,773,787,797,809,
811,821,823,827,829,839,853,857,859,863,877,881,883,887,907,911,919,929,937,941,
947,953,967,971,977,983,991,997,1009,1013,1019,1021,1031,1033,1039,1049,1051,1061,1063,1069)


am = 1
rot = 1

GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
RESET = '\033[39m'


aum=2
lista = []
list2 = []
nn=32
n=1


for m in range(nn):
    list2.append('')

print(list2, end="")
list2 = []
nn = nn - 1

for i in range(32):

    n = n + aum
    lista.append(n)
        
    for m in range(rot):
        if lista.count(am) == 1:

            mas2 ,men2, men50 = 0, 0, 0

            valida = False

            if primos.count(am) == 1:
                #print(n , "Primo")
                print(YELLOW + "",am," " + RESET, end="")
                valida = True
            else:
                mas2 = am + 4

            if primos.count(mas2) == 1 and valida == False:
                #print(n , "(+ 4) =", mas2)
                print(GREEN + "",am," " + RESET, end="")
                valida = True
            else:
                men2 = am - 4

            if primos.count(men2) == 1 and valida == False:
                #print(n , "(- 4) =", men2)
                print(MAGENTA + "",am," " + RESET, end="")
                valida = True
            else: 
                men50 = am - 50

            if primos.count(men50) == 1 and valida == False:
                #print(n , "(- 50) =", men50)
                print(BLUE + "",am," " + RESET, end="")
                valida = True
 
        else:
            if len(str(am)) == 2:
                print("",am,"", end="")
            elif len(str(am)) == 1:
                print(" ",am,"", end="")
            else:
                print(am,"", end="")

        am = am + 1
        
    rot = rot + 2
    print("")

    for m in range(nn):
        list2.append('')

    print(list2, end="")
    list2 = []
    nn = nn - 1

    aum = aum + 2


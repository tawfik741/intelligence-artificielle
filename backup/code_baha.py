class Fait :
    def __init__(self,attribut,valeur,flag):
        self.attribut=attribut
        self.valeur=valeur
        self.flag=flag
        
    def __str__( self):
        return "fait : \n\tattribut:{}, \n\tvaleur:{}, \n\tflag:{}\n ".format(self.attribut, self.valeur, self.flag)
​
class Regle :
    def __init__(self,premisses,conclusions,rang):
        self.premisses=premisses
        self.conclusions=conclusions
        self.rang=rang
        self.executed=False
        
    def __str__( self):
        print('regle')
        print('\tpremisses')
        for premisse in self.premisses:
            print(premisse)
        print('\tconclusion')
        print ('\t\t'+self.conclusions)
        print('\texecuted '+str(self.executed))
        print()
        return ''
​
class Premisse :
    def __init__(self,attribut,valeur,operateur):
        self.attribut=attribut
        self.valeur=valeur
        self.operateur=operateur
        
    def __str__( self):
        return "\t\tattribut:{}, valeur:{}, operateur:{}".format(self.attribut, self.valeur, self.operateur)
​
​
def extractFait(line):
    
    if(not (line=='\n')):
        
        faitAttributes=line.split('\n')[0].split('=')
        
        faits.append(Fait(faitAttributes[0],faitAttributes[1],-1))
        
def extractRegle(line):
    regle=line.split('si ')[1].split('\n')[0]
    #print('regle')
    #print(regle)
    premisses=regle.split(' alors ')[0].split(' et ')
    conclusions=regle.split(' alors ')[1]
    print('premisses',premisses)
    #print(conclusions)
    
    newPremisses=[]
    
    for premisse in premisses:
        for operateur in operateurs :
            if operateur in premisse :
                premisseAttributes=premisse.split(operateur)
                newPremisses.append(Premisse(premisseAttributes[0],premisseAttributes[1],operateur))
                break
    
    regles.append(Regle(newPremisses,conclusions,len(regles)))
    
    #print()
    #print()
​
​
def checkRegleExecutable(regle,faits):
    i=0
    if regle.executed==True:
        print('regle executed')
        return False
    for premisse in regle.premisses:
    
        for fait in faits:
            if (premisse.operateur=='='):
                if(premisse.attribut==fait.attribut and premisse.valeur==fait.valeur):
                    i=i+1
                    break
            if (premisse.operateur=='<'):
                if(premisse.attribut==fait.attribut and premisse.valeur>fait.valeur):
                    i=i+1
                    break
            if (premisse.operateur=='>'):
                if(premisse.attribut==fait.attribut and premisse.valeur<fait.valeur):
                    i=i+1
                    break
            if (premisse.operateur=='<='):
                if(premisse.attribut==fait.attribut and premisse.valeur>=fait.valeur):
                    i=i+1
                    break
            if (premisse.operateur=='>='):
                if(premisse.attribut==fait.attribut and premisse.valeur<=fait.valeur):
                    i=i+1
                    break
​
    if(i==len(regle.premisses)):
        return True
    else :
        return False
​
​
def addToBf(fait,rang):
    fait=Fait(fait.split('=')[0],fait.split('=')[1],rang)
    if(checkFaitInBf(fait)):
        faits.append(fait)
        
def checkFaitInBf(fait):
    for f in faits:
        if (f.attribut==fait.attribut and f.valeur==fait.valeur):
            return False;
    return True
​
f=open('D:/9raya/GL 4\AI/tp/tp1/maladies.txt',"r")
​
faits=[]
regles=[]
​
​
line=f.readline()
​
operateurs=['<=','>=','=','<','>']
​
i=0
while(line):
    if(not line.startswith('si')):
        extractFait(line)    
        
    if(line.startswith('si')):
        extractRegle(line)
            
    # use realine() to read next line
    line = f.readline()
    
    i=i+1
    
f.close()
        
​
print()
print()
for fait in faits:
    print(fait)
for regle in regles:
    print(regle)
    
bre=[]
i=0
​
print('start')
​
while True:
    for regle in regles:
        if (checkRegleExecutable(regle,faits)):
            regle.executed=True
            print('regle added')
            bre.append(regle)
        
    if(len(bre)==0):
        break
    
    regleToExecute=bre[0]
    
    addToBf(regleToExecute.conclusions,regleToExecute.rang)
    
    for regle in bre:
        print (regle)
    
    bre.pop(0)
    
    
    
    
    
    for fait in faits:
        print(fait)
        
    i=i+1
    
    print()
    print()
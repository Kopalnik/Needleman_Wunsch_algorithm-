import numpy

def CPunktacja(nazwa):
    f=open(nazwa,'r')
    Odczyt=f.read()
    Odczyt=Odczyt.splitlines()
    n=len(Odczyt)-1
    MPunktacji=numpy.zeros((n,n),'i')    
    f.close()
    alfabet={}
    wiersz=Odczyt[0].split()
    for j in range(0,len(wiersz)):
        alfabet[wiersz[j]]=j
    for i in range(1,len(Odczyt)):
        wiersz=Odczyt[i].split()
        for j in range(1,len(wiersz)):
            if wiersz[j]!='':
                MPunktacji[i-1,j-1]=float(wiersz[j])
                MPunktacji[j-1,i-1]=MPunktacji[i-1,j-1]
    return MPunktacji, alfabet, n


def AlgorytmNeedelmannaWunscha(S1,S2,MPunktacji,Kara,alfabet):
    n1=len(S1)+1
    n2=len(S2)+1
    Ocena=numpy.zeros((n1,n2),'i')
    Strzalki=numpy.zeros((n1,n2),'i')
    for j in range(1,n2):
        Ocena[0,j]=-Kara*j
    for i in range(1,n1):        
        Ocena[i,0]=-Kara*i    
    for i in range(1,n1):
        for j in range(1,n2):
            OcenaN=Ocena[i-1,j]-Kara
            OcenaW=Ocena[i,j-1]-Kara
            p1=alfabet[S1[i-1]]
            p2=alfabet[S2[j-1]]            
            OcenaNW=Ocena[i-1,j-1]+MPunktacji[p1,p2]
            Ocena[i,j]=max(OcenaN,OcenaW,OcenaNW)
            if Ocena[i,j]==OcenaNW:
                Strzalki[i,j]=3
            elif Ocena[i,j]==OcenaW:
                Strzalki[i,j]=2
            else: #Ocena[i,j]==OcenaNW:
                Strzalki[i,j]=1
    SW1=list(S1)
    SW2=list(S2)
    i=n1-1
    j=n2-1
    while i!=0 and j!=0:
        if Strzalki[i,j]==3:
            i=i-1
            j=j-1
        elif Strzalki[i,j]==2:
            SW1.insert(i,'-')
            j=j-1
        else:
            SW2.insert(j,'-')
            i=i-1
    return SW1, SW2, Ocena[-1,-1]


MP, Alfa, n =CPunktacja('Blosum62.txt')
#MP, Alfa, n =CPunktacja('SP.txt')
print Alfa
print MP
print n
#S1='SHAKE'
#S2='SPEARE'
S1='MENEREKQVYLAKLSEQTERYDEMVEAMKKVAQLDVELTVEERNLVSVGYKNVIGARRASWRILSSIEQKEESKGNDENVKRLKNYRKRVEDELAKVCNDILSVIDKHLIPSSNAVESTVFFYKMKGDYYRYLAEFSSGAERKEAADQSLEAYKAAVAAAENGLAPTHPVRLGLALNFSVFYYEILNSPESACQLAKQAFDDAIAELDSLNEESYKDSTLIMQLLRDNLTLWTSDLNEEGDERTKGADEPQDEV'
#S2='MENERAKQVYLAKLNEQAERYDEMVEAMKKVAALDVELTIEERNLLSVGYKNVIGARRASWRILSSIEQKEESKGNEQNAKRIKDYRTKVEEELSKICYDILAVIDKHLVPFATSGESTVFYYKMKGDYFRYLAEFKSGADREEAADLSLKAYEAATSSASTELSTTHPIRLGLALNFSVFYYEILNSPERACHLAKRAFDEAIAELDSLNEDSYKDSTLIMQLLRDNLTLWTSDLEEGGK'
S2='MAATLGRDQYVYMAKLAEQAERYEEMVQFMEQLVTGATPAEELTVEERNLLSVAYKNVIGSLRAAWRIVSSIEQKEESRKNDEHVSLVKDYRSKVESELSSVCSGILKLLDSHLIPSAGASESKVFYLKMKGDYHRYMAEFKSGDERKTAAEDTMLAYKAAQDIAAADMAPTHPIRLGLALNFSVFYYEILNSSDKACNMAKQAFEEAIAELDTLGEESYKDSTLIMQLLRDNLTLWTSDMQTNQMHHIRDIKEHVKTEITAKPCVLSYYYSM'
SW1, SW2, Ocena=AlgorytmNeedelmannaWunscha(S1,S2,MP,6, Alfa)
print S1
print S2
sw1=''
sw2=''
for a in SW1:
    sw1=sw1+a
for a in SW2:
    sw2=sw2+a
print 'Ocena = ',Ocena
print sw1
print sw2


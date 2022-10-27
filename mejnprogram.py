import pygame 
import matplotlib.pyplot as plt
from klasabalon import balon


vreme = 0
brziniz=[]
visiniz=[]
xvisiniz=[]

terminalna_brzina = 0
termniz=[]

while vreme<30:
    #1. deo
    bv=balon.f_brzina(vreme)
    hv=balon.f_visina(vreme)

    #2. deo
    #bv=balon.f_brzina_sa_otporom(vreme)
    #hv=balon.f_visina_sa_otporom(vreme)

    #3. deo
    #bv=balon.f_brzina_s_vetrom(vreme)
    #hv=balon.f_polozaj_y_vetar(vreme)
    #xv=balon.f_polozaj_x_vetar(vreme)

    #4. deo
    #bv=balon.f_brzina_s_pomeranjem(vreme)
    #hv=balon.f_polozaj_y_vetar(vreme)
    #xv=balon.f_polozaj_x_vetar_pomeranje(vreme)

    #if(bv > terminalna_brzina):
    #    terminalna_brzina = bv
    
    #xvisiniz.append(xv)
    brziniz.append(bv)
    visiniz.append(hv)
    vreme+=1

"""
print(terminalna_brzina)
i=0
while i < 30:
    termniz.append(terminalna_brzina)
    i+=1
plt.plot([i for i in range(30)], termniz)
"""

plt.plot([i for i in range(30)], brziniz)
plt.ylabel('brzina [m/s]')
plt.xlabel('vreme [s]')
plt.show()

plt.plot([i for i in range(30)], visiniz)
plt.ylabel('visina [m]')
#plt.ylabel('položaj balona na x i y osi')
plt.xlabel('vreme [s]')
#plt.plot([i for i in range(30)], xvisiniz)
plt.show()

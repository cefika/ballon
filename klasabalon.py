import pygame
import math


class Balon:
    def __init__(self, masa, pocetna_brzina, pocetna_visina, B, ro=1.1455):
        self.masa = masa
        self.poluprecnik = 5
        self.brzina = pocetna_brzina
        self.visina = pocetna_visina
        self.xvisina = 10
        self.D = 1/2*0.0001 * ro * self.poluprecnik
        self.B = B  
        self.g=9.81
        # na početku ubrzanje se računa formulom a= B/m - g jer ne postoji otpor vazduha.
        self.ubrzanje = (self.B / self.masa) - self.g
        self.w = 10
        self.w_promenljiv = 10
    
    # 1 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    # brzinu računamo po formuli v(t)=v(prethodno)+a*t
    def f_brzina(self, t):
        self.brzina = self.brzina + self.ubrzanje * t
        return self.brzina

    # visinu računamo po formuli h(t)=h(prethodno)+v*t 
    def f_visina(self,t):
        self.visina = self.visina + self.f_brzina(t)*t
        return self.visina

    # 2 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    # UVODIMO OTPOR VAZDUHA => FD = −D*v*v
    def f_otpor_vazduha(self,t):
        if(t > 0):
            return -self.D*self.brzina*self.brzina
        else: return 0

    # ubrzanje sada nije konstantno, vec se menja u zavisnosti od vremena => a= (B+FD)/m - g
    def f_ubrzanje_sa_otporom(self, t):
        return ((self.B + self.f_otpor_vazduha(t))/ self.masa) - self.g

    def f_brzina_sa_otporom(self, t):
        self.brzina = self.brzina + self.f_ubrzanje_sa_otporom(t)*t
        return self.brzina
    
    def f_visina_sa_otporom(self, t):
        self.visina = self.visina + self.f_brzina_sa_otporom(t)*t
        return self.visina

    # 3 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    
    #UVODIMO VETAR 
    def f_brzina_s_vetrom (self, t):
        return math.sqrt(self.f_brzina_sa_otporom(t)*self.f_brzina_sa_otporom(t)+ self.w*self.w)

    def f_polozaj_y_vetar(self, t):
        return self.f_visina_sa_otporom(t)

    def f_polozaj_x_vetar(self, t):
        self.xvisina = self.xvisina + self.w*t
        return self.xvisina

    # 4 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    #UVODIMO POMERANJE VETRA w=w0 * (1- exp(-h/d))
    def f_brzina_s_pomeranjem(self, t):
        self.w_promenljiv = self.w*(1 - math.exp(-self.f_polozaj_y_vetar(t)/10))
        return  math.sqrt(self.f_brzina_sa_otporom(t)*self.f_brzina_sa_otporom(t)
                            + self.w_promenljiv*self.w_promenljiv)

    def f_polozaj_x_vetar_pomeranje(self, t):
        self.xvisina = self.xvisina + self.w_promenljiv*t
        return self.xvisina


"""
balon = Ballon (masa,pocetnabrzina,pocetnavisina,B)
"""
balon = Balon(1, 0, 0, 10)

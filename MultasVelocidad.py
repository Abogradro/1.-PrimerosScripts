
velocidad_max = 50
velocidad_registrada = float (input (""" Coloca la velocidad en la que estabas: """))
exceso = velocidad_registrada - velocidad_max

if exceso <= 0: 
    multa = 0 
    print (f""" Estás viajando a una velocidad de {velocidad_registrada} km/h. 
     Estás dentro del rango de velocidad, no tienes multa alguna, felicitaciones. """)
elif exceso <= 10: 
    multa = 927
    print (f""" Tienes un exceso de {exceso} km/h; por tanto tu multa es de {multa}  """)
else: 
    multa =2575
    print (f""" Tienes un exceso de {exceso} km/h; por tanto tu multa es de {multa}  """)
        

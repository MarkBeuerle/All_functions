studentencijfers = [ [95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0] ]

def gemiddelde_per_student(studentencijfers):
   s1=(studentencijfers[0][0]+studentencijfers[0][1]+studentencijfers[0][2])/3
   s2=(studentencijfers[1][0]+studentencijfers[1][1]+studentencijfers[1][2])/3
   s3=(studentencijfers[2][0]+studentencijfers[2][1]+studentencijfers[2][2])/3
   antw=[s1, s2, s3]
   return antw

def gemiddelde_van_alle_studenten(studentencijfers):
   x= (gemiddelde_per_student(studentencijfers))
   totaal=0
   for i in x:
       totaal= totaal+i
       antw=totaal/3
   return antw

print(gemiddelde_per_student(studentencijfers))

print(gemiddelde_van_alle_studenten(studentencijfers))
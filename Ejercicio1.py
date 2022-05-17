def escribe_media():
    print(f"================================================================")
    print("             Daremos a conocer las 5 Materia                     ")
    print(f"================================================================")
    a=float(input("Ingrese la nota de Calculo: "))
    b=float(input("Ingrese la nota de Algebra: "))
    c=float(input("Ingrese la nota de Programacion: "))
    d=float(input("Ingrese la nota de Realidad Nacional: "))
    e=float(input("Ingrese la nota de Metodos Numericos: "))
    print(f"================================================================")
    total = (a + b +c + d + e)
    promedio=(a*p1/100)+(b*p2/100)+(c*p3/100)+(d*p4/100)+(e*p5/100)
    print(f"El total es: {total}")
    print(f"================================================================")
    print(f"El Porcentaje de Calculo es: {p1} %")
    print(f"El Porcentaje de Algebra: es: {p2} %")
    print(f"El Porcentaje de Programacion es: {p3} %")
    print(f"El Porcentaje de Realidad Nacional es: {p4} %")
    print(f"El Porcentaje de Metodos numericos es: {p5} %")
    print(f"================================================================")
    print(f"El Porcentaje total de todas las materia es : {promedio}")
    print(f"================================================================")
    return
p1=30
p2=35
p3=20
p4=10
p5=5
escribe_media()
print("Programa terminado")
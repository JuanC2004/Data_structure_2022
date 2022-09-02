'''
Author: Juac
dates: 24/08/2022
Description: taller 1 python
'''

def signature_name ():
    signature = " Estructura de datos"
    print (f"La asignatura es: {signature}")

def signature_input():
    signature = input("Ingrese el nombre de la asignatura: ")
    print (f"La asignatura es: {signature}")

def signature_data_entry():
    signature_amount = int(input("ingrese el numero de asignaturas que va a cursar: "))
    i=0
    for i in range(signature_amount):
        signature_name = input(f"Ingrese el nombre de la asignatura {i+1}: ")
        signature_credits = int(input(f"Ingrese el numero de creditos de la asigantura {signature_name}: "))
         
def pair_numbes():
    while True:
        try:
            number =int (input("Ingrese un numero: ")) 
            break
        except:
            print("error")
    for i in range(number+1):
        if(i%2==0):
            print(i)

def unpair_negative_numbers():
    while True:
        try:
            number = int(input("Ingrese un numero: "))
            break
        except:
            print("error")
    if(number%2!=0 and number<0):
        print("El numero es impar negativo")
    else:
        print("El numero no cumple con las caracteristicas")

def password_mail():
    mail = input("Ingrese el correo electronico: ")
    aux = mail.endswith('@autonoma.edu.co')

    while (aux!= True):
        mail = input("Erro, vuelva a ingresar el correo: ")
        aux=mail.endswith('@autonoma.edu.co')

    print("Correo validado exitosamente")

    password = input("Ingrese la contraseña: ")
    while(password!='tad1-2022'):
        password = input("Error, contraseña invalida, vuelva a intentar: ")
    
    print("Contraseña validada correctamente")

signature_name()   
signature_input() 
signature_data_entry()
pair_numbes()
unpair_negative_numbers()
password_mail()
'''
    Author: Yaneth Mejía
    Verssion: 1.0
    Language: Python
'''
def say_hi():
    print('Hello world')
#Llamamos la función para que se ejecute
say_hi()

def input_data_user():
    user_name = input('Ingresa tu nombre: ')
    #Se debe de validar que el valor ingresado sea un nro
    while True:
        try:
            age = int(input('Edad:'))
            break
        except:
            print('Error, no es un valor numérico')
    print(f'{user_name}, tiene {age} años.')
#Llamamos la función para que se ejecute
input_data_user()

def input_frameworks_data():
    while True:
        try:
            languages_count = int(input('Cuántos fm conoces?'))
            counter = 1
            while counter <= languages_count:
                framework_name = input('        Framework: ')
                counter += 1
            break
        except:
            print('Error, no es un valor numérico')
#Llamamos la función para que se ejecute
input_frameworks_data()


def input_language_information():
    #Declaración de una lista vacía
    language_list = []
    while True:
        try:
            language_count = int(input('Cuantos lenguajes de prog conoces?'))
            for item_language in range(language_count):
                language_name = input(f'         {item_language}: ')
                #append() añade el lenguaje al final de la lista
                language_list.append(language_name)
            break
        except:
            print('Error, se esperaba un número')

#Llamamos la función para que se ejecute
input_language_information()

def insert_info_student():
    #solicitar nombre y documento del estudiante
    print('Ingresa la siguiente información')
    students_list = []
    while True:
        try:
            student_counter = int(input('Cuantos estudiantes ingresaras?: '))
            for item_student in range(1, student_counter+1):
                student_name = input('nombre: ')
                document = input('documento: ')
                #Lista a la cual se le agrego una tupla list(dupla())
                # La siguiente dupla tiene 3 posiciones (item_estudent, student_name, document)
                students_list.append((item_student, student_name, document))
            break
        except:  
            print('Se esperaba un dato numerico')
insert_info_student() 

def countries_information():
    countries_information = []
    while True:
        try:
            countrie_counter = int(input('cuantos paises conoces?: '))
            for item_country in range (1, country_counter+1):
                country_name = input('     pais: ')
                while True:
                    try:
                        population = int(input('     poblacion: '))
                    except:
                        print('Error, se esperaba un numero')
                countries_list.append((country_name,population)) 
                print(f'    Informacion paises\n     {countries_list}')       
        except:
            print('Se esperaba un dato numerico')
#llamado de funcion
countries_information()    

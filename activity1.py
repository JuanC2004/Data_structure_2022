class Activity1:
    #Crear metodo inicializador de la clase
    def init (self):
        #Declaración de variables
        self.editor_name = 'visual studio code'
        self.language = 'Python'
        self.version = 3.0
        self.user_name = ''

    def show_info(self):
        print(f'Estamos trabajando en {self.editor_name}, programando en {self.language}{self.version}')
        
    def input_data_user(self):
        self.user_name = input('Ingresa tu nombre: ')
        #Se debe de validar que el valor ingresado sea un nro
        while True:
            try:
                age = int(input('Edad:'))
                break
            except:
                print('Error, no es un valor numérico')
        print(f'{self.user_name}, tiene {age} años.')
    #Llamamos la función para que se ejecute
    

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
   
    def countries_information():
        countries_information = []
        while True:
            try:
                countries_counter = int(input('cuantos paises conoces?: '))
                for item_country in range (1, countries_counter+1):
                    country_name = input('     pais: ')
                    while True:
                        try:
                            population = int(input('     poblacion: '))
                            countries_information.append((country_name,population)) 
                            print(f'    Informacion paises\n     {countries_information}')  
                            break
                        except:
                            print('Error, se esperaba un numero')
  
                break                  
            except:
                print('Se esperaba un dato numerico')
    #llamado de funcion
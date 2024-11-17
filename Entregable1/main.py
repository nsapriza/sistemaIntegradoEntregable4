import csv
from random import randint
from itertools import chain
import random
from typing import Generator,Any,Callable
def imp_csv()->list:
    """
    ### Parameters
        None
    ### Returns
        - data:list
            - csv acotado a cuatro columnas
            - [Category,Value,Question,Answer]
    """
    with open('./Entregable1/JEOPARDY_CSV.csv', newline='\n',encoding="latin-1") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        j=0
        data = []
        i = 0
        for row in spamreader:
            i+=1
            if i >3000000:
                break
            data.append(row[3:7])
    return data


def hacelo_bonito(fun:Callable):
    
    """
        ### Parameters
            - fun:callable
                - funcion a decorar

    """
     
    def internal(entrada:int|list):
        if type(entrada) is int:
            max_index:int = entrada
            puntaje:int = 0
            i:int = 0
            preguntas:list[str] = []
            respuestas:list[str] = []
        else:
            max_index:int = entrada[0]
            puntaje:int = entrada[2]
            i:int = entrada[1]
            preguntas:list[str] = entrada[3]
            respuestas:list[str] = entrada[4]
        
        if i != max_index:
            print(f"\nPuntaje actual: {puntaje}\n")
        
        return fun([max_index,i,puntaje,preguntas,respuestas])
    return internal


def get_pregunta(data:list)->dict[str:int,str:str]:
    """
        Esta funcion busca una entrada en el dataset
        ### Parameters
            - data:list
                - entradas del csv recopiladas por imp_csv()
        ### Returns
            - dict
                - de la forma {
                                "index":indice de pregunta,
                                "question":pregunta,
                                "answer":respuesta,
                                "category":categoria
                                } 
    """
    index:int = randint(1,len(data)-1)
    question:str = data[index][2]
    answer:str = data[index][3]
    category:str = data[index][0]
    return {"index":index,"question":question,"answer":answer,"category":category}

def filter_by_category(data:list,category:str,question_index:int)->list[list]:
    """
        Esta funcion filtra el dataset por categoria y quita la pregunta original
        ### Parameters
            - data:list
                - entradas del csv recopiladas por imp_csv()
            - category:str
                - categoria de la pregunta original
            - question_index:int
                - indice de la pregunta original en el dataset original
        ### Returns
            - list
                - dataset filtrado por categoria o dataset original si el dataset filtrado tiene menos de dos elementos 
    """
    filtered:list = list(filter(lambda x:x[0]==category and x!=data[question_index],data))
    if len(filtered) < 2:
        return data
    return filtered

def get_possible_answers(filtered_data:list)->dict:
    """
        Esta funcion elije dos respuestas del dataset filtrado por categoria
        ### Parameters
            - filtered_data:list
                - dataset filtrado
        ### Returns
            - dict
                - de la forma {
                "answer_two":respuesta posible,
                "answer_three":respuesta posible,
                "raw_answer_two":entrada de la primer respuesta posible en dataset filtrado,
                "raw_answer_three":entrada de la segunda respuesta posible en dataset filtrado
                } 
    """
    answer_two_index:int = randint(1,len(filtered_data)-1)
    available_indicies:list = [i for i in range(1,len(filtered_data)-1) if i != answer_two_index ]
    
    if available_indicies != []:
        answer_three_index:int = random.choice(available_indicies)
    else:
        answer_three_index:int = answer_two_index

    raw_answer_two:list = filtered_data[answer_two_index]
    raw_answer_three:list = filtered_data[answer_three_index]
    answer_two:str = raw_answer_two[3]
    answer_three:str = raw_answer_three[3]
    
    return {"answer_two":answer_two,"answer_three":answer_three,"raw_answer_two":raw_answer_two,"raw_answer_three":raw_answer_three}
    
    
def preguntas(data:list)->list:
    """
    ### Parameters
        - data:list
            - entradas del csv recopiladas por imp_csv()
    ### Returns
        - list
            - lista de la forma [respuesta de usuario, respuesta correcta, pregunta] 
    """
    info_pregunta:dict = get_pregunta(data)
    pregunta:str = info_pregunta["question"]
    respuesta:str = info_pregunta["answer"]
    index:int = info_pregunta["index"]
    category:str = info_pregunta["category"]
    filtered_data:list[list] = filter_by_category(data,category,index)
    possible_answers:dict = get_possible_answers(filtered_data)
    answers:list = [respuesta,possible_answers["answer_two"],possible_answers["answer_three"]]
    random.shuffle(answers)
    print(f"Categoría: {category}")
    tmp:str = input(f"Pregunta: {pregunta} \nPosibles respuestas: {answers[0]}, {answers[1]}, {answers[2]} \nSu respuesta: ")
    return [tmp, respuesta,pregunta]  


def info() -> Generator[list,list,list]:
    """
    ### Parameters
        - None
    ### Returns
        - Generator[list, list, list, list, list]
            - un generador que al ser llamado con next realiza una llamada a preguntas()  
    """
    data:list[list] = imp_csv()
    yield preguntas(data)
    yield preguntas(data)
    yield preguntas(data)
    yield preguntas(data)
    yield preguntas(data)

    

def main()->int:
    """
    ### Parameters
        - None
    ### Returns
        - puntaje:int
    """
    print("\n==========================Nueva Partida===========================")
    generador:Generator[list,list,list] = info()

    @hacelo_bonito
    def looper(entrada:int|list)->int:
        """
        ### Parameters
            - entrada:int
            - numero de iteraciones
        ### Returns
            - puntaje:int
        """
        if type(entrada) is int:
            max_index:int = entrada
            puntaje:int = 0
            i:int = 0
            preguntas:list[str] = []
            respuestas:list[str] = []
        else:
            max_index:int = entrada[0]
            puntaje:int = entrada[2]
            i:int = entrada[1]
            preguntas:list[str] = entrada[3]
            respuestas:list[str] = entrada[4]

        if i == max_index:
            solucion:list[str] = ["Pregunta: "+valor + "\nRespuesta: " + list(chain(preguntas,respuestas))[len(preguntas) + indice] + "\n" for indice,valor in enumerate(preguntas)]
            print("\n=========Preguntas y respuestas correctas para la partida=========\n")
            print ("\n".join(map(str, solucion)))
            print("==================================================================\n")
            #print(solucion)
            return puntaje
        
        #print(f"index = {i}")

        [tmp,respuesta,pregunta] = next(generador)

        preguntas.append(pregunta)
        respuestas.append(respuesta)
        if tmp == respuesta:
            print("Correcto!!! ✅")
            puntaje+=10
        else:
            print("Incorrecto ❌")   

        return looper([max_index,i+1,puntaje,preguntas,respuestas])
    
    puntaje = looper(5)
    print(f"Puntaje Final: {puntaje}\n")
    print("==================================================================\n")

    return puntaje

if __name__ == "__main__":
    main()
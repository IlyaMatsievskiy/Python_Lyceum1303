#deps = [[7, 5], [5, 2], [5, 1], [6, 3], [6, 2], [7, 6], [3, 4], [3, 2], [3, 0], [1, 0], [2, 0], [4, 0]]
deps=[[0,1], [1,2], [2,3], [3, 1]]
#Задаем количество уроков
num_lessons = 4
#Структура данных графа(в какие вершины можно попасть из вершины
graph = dict()
#Количество входящих ребер в каждую вершину
incoming_edges = [0 for i in range(num_lessons)]
#Заполняем граф
for lesson in deps:
    counter=0
    #Пробуем вызвать ключ со значением lesson[0], если выдает ошибку, к counter прибавляем 1. Также можно использовать lesson[0] in graph, в ответ мы получим True либо False, но это я понял только когда написал с try except, так что оставлю так)
    try:
        graph[lesson[0]]
    except KeyError:
        counter+=1
    if counter==1:
        counter=0
        graph[lesson[0]]=[lesson[1]]
    else:
        graph[lesson[0]].append(lesson[1])
    # Подсчет кол-ва входящих ребер
    incoming_edges[lesson[1]] += 1
#Вершины кандидаты
cand = list()
#Проходимся по входным ребрам и ищем кандидатов, nodr - номер вершины
for node, number_of_edges in enumerate(incoming_edges):
    if number_of_edges == 0:
        cand.append(node)
answer = []
check=graph.copy()
while cand:
    # Берем одного любого кандидата
    current_element = cand.pop()
    if current_element in graph:
        for node in graph[current_element]:
            incoming_edges[node] -= 1
            if incoming_edges[node] == 0:
                cand.append(node)
    check[node].append("end")
    answer.append(current_element)
#if len(answer)==num_lessons:
    #print(answer)
#else:
    #print( "Нет решений")
z=0
for i in check:
    if check[i].count("end")!=1:
        z+=1
if z==0:
    print(answer)
else:
    print("Граф цикличен, решений нет.")


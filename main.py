from tkinter import *
from logic import floyd_warshall

# функция расчета алгоритма флойда-уоршела
def solve():
	
	nV = dimention_entry.get()
	graph = graph_entry.get()
	path = path_entry.get()
	INF = 999

	new_graph = [x.replace("[", "").replace("],", "").replace("]]", "") for x in graph.split (" [")]

	new_graph = [x.split(", ") for x in new_graph]

	new_graph = [ [y.replace("INF", "999") for y in x] for x in new_graph]

	new_graph = [ [int(y) for y in x ] for x in new_graph]

	print (new_graph)

	solution = floyd_warshall(new_graph)

	matrix_listbox.insert(0, f"Примечание: число 999 - обозначает бесконечность !!!")
	matrix_listbox.insert(0, f"Матрица расстояний: {solution}")
	matrix_listbox.insert(0, f"Исходный граф: {graph}")
	matrix_listbox.insert(0, f"-------------------------------------Решение-------------------------------------")

	path = path.split(" ")

	path = [int(x) for x in path]

	print (path[0] + path[1])

	print (path)

	fastest_path = solution [path[0] - 1] [path[1] - 1]

	print (fastest_path)

	path_listbox.insert(0, f"Примечание: число 999 - обозначает бесконечность !!!")
	path_listbox.insert(0, f"Самый короткий путь составит: {fastest_path}")
	path_listbox.insert(0, f"Мы хотим попасть из вершины {path[0]} в вершину {path[1]}")
	path_listbox.insert(0, f"-------------------------------------Решение-------------------------------------")
 
root = Tk ()
root.title("Алгоритм Флойд-Уоршелла")
root.geometry("435x660")
 
# Создаем поля для ввода и кнопку для совершения расчетов

dimention_text = "Введите размерность графа:"
dimention_label = Label(text=dimention_text, fg="#eee", bg="#333")
dimention_label.grid(column=0, row=0, padx=6, pady=6)

dimention_entry = Entry(width=32)
dimention_entry.grid(column=0, row=1, padx=6, pady=6)

graph_text = "Введите матрицу расстояний до вершин в графе:"
graph_label = Label(text=graph_text, fg="#eee", bg="#333")
graph_label.grid (column=0, row = 2, padx=6, pady=6)

solve_button = Button (text="Рассчитать",
	background="#555",
	foreground="#ccc",
	padx="20",
	pady="8",
	font="16",
	command=solve).grid(column=1, row=2, padx=6, pady=6)

graph_entry = Entry(width=32)
graph_entry.grid(column=0, row=3, padx=6, pady=6)

path_text = "Введите из какой в какую вершину\nвы хотите попасть через пробел:"
path_label = Label(text=path_text, fg="#eee", bg="#333")
path_label.grid (column=0, row = 4, padx=6, pady=6)

path_entry = Entry(width=32)
path_entry.grid(column=0, row=5, padx=6, pady=6)

# создаем списки для вывода данных

matrix_text = "Вывод матрицы расстояний до вершин:"
matrix_label = Label(text=matrix_text, fg="#eee", bg="#333")
matrix_label.grid (column=0, row = 6, padx=6, pady=6)

matrix_listbox = Listbox()
matrix_listbox.grid(row=7, column=0, columnspan=2, sticky=W+E, padx=5, pady=5)

path_matrix_text = "Вывод кратчайшего пути из\nодной вершины в другую:"
path_matrix_label = Label(text=path_matrix_text, fg="#eee", bg="#333")
path_matrix_label.grid (column=0, row = 8, padx=6, pady=6)

path_listbox = Listbox()
path_listbox.grid(row=9, column=0, columnspan=2, sticky=W+E, padx=5, pady=5)

 
root.mainloop()
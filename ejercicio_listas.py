
"""Instrucciones paso a paso
Crea una lista vacía llamada tareas.
Agrega al menos 3 tareas usando append().
(ejemplo: “hacer ejercicio”, “estudiar matemáticas”, “sacar la basura”)
Inserta una tarea urgente en la segunda posición usando insert().
Agrega varias tareas adicionales a la lista usando extend().
(ejemplo: una lista con 3 tareas más)
Elimina una tarea que ya hayas completado usando remove().
Quita la última tarea de la lista usando pop() y guarda el valor en una variable para mostrarlo después.
Ordena las tareas alfabéticamente usando sort().
Invierte el orden de la lista usando reverse().
Muestra la posición de una tarea específica en la lista usando index().
Limpia toda la lista de tareas usando clear()."""

listas_tareas = []
listas_tareas.append("Matemáticas")
listas_tareas.append("Estudiar")
listas_tareas.append("Leer capítulo")
print(listas_tareas)

listas_tareas.insert(1, "Sacar basura")
print("Lista despues de insert:", listas_tareas)

listas_tareas.extend (["Lavar trastes", "Alzar la cama", "Ir al gimnasio"])
print(listas_tareas)

listas_tareas.remove("Estudiar")
print("Lista después de remove:", listas_tareas)

ultimo = listas_tareas.pop()
print("El elemento eleminado de la lista es: ", ultimo)
print("Lista despues de pop", listas_tareas)

listas_tareas.sort()
print("Lista de tareas despues de sort: ", listas_tareas)

listas_tareas.reverse()
print("Lista de tareas despues de reverse: ", listas_tareas)

pos_basura = listas_tareas.index ("Sacar basura")
print ("La basura esta en la posición: ", pos_basura)

listas_tareas.clear()
print ("La lista despues de clear", listas_tareas)


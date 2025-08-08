def filtrar_estudiantes(estudiantes):
    """
    Recibe una tupla de estudiantes y devuelve una nueva tupla
    con los estudiantes cuyo promedio es mayor a 8.0.
    """

    estudiantes_aprobados = []

    for estudiante in estudiantes:
        
        promedio = estudiante[2]

        if promedio > 8.0:
            
            estudiantes_aprobados.append(estudiante)

    return tuple(estudiantes_aprobados)

estudiantes_clase = (
    ("Ana", 20, 9.5),
    ("Luis", 21, 7.8),
    ("Maria", 22, 8.5),
    ("Carlos", 19, 6.2),
    ("Sofia", 20, 9.0)
)

estudiantes_con_buen_promedio = filtrar_estudiantes(estudiantes_clase)

print(f"Estudiantes con promedio mayor a 8.0: {estudiantes_con_buen_promedio}")
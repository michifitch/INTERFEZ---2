import tkinter as tk
from tkinter import messagebox

class Curso:
    def __init__(self, nombre, profesor, horario):
        self.nombre = nombre
        self.profesor = profesor
        self.estudiantes = []
        self.horario = horario

    def mostrar_info(self):
        estudiantes_nombres = ", ".join([f"{est.nombre} {est.apellido}" for est in self.estudiantes])
        return (f"Curso: {self.nombre}\n"
                f"Profesor: {self.profesor.nombre} {self.profesor.apellido}\n"
                f"Horario: {self.horario.dia} de {self.horario.hora_inicio} a {self.horario.hora_fin}\n"
                f"Número de estudiantes: {len(self.estudiantes)}\n"
                f"Estudiantes: {estudiantes_nombres}")

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

class Profesor:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Estudiante:
    def __init__(self, nombre, apellido, id_estudiante):
        self.nombre = nombre
        self.apellido = apellido
        self.id_estudiante = id_estudiante

class Horario:
    def __init__(self, dia, hora_inicio, hora_fin):
        self.dia = dia
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin

class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Gestión de Cursos")
        self.geometry("600x400")

        self.create_widgets()

    def create_widgets(self):
        # Frame para registrar el curso
        self.frame_registrar_curso = tk.LabelFrame(self, text="Registrar Curso")
        self.frame_registrar_curso.pack(fill="both", expand="yes", padx=10, pady=10)

        tk.Label(self.frame_registrar_curso, text="Nombre del Curso:").grid(row=0, column=0, padx=5, pady=5)
        self.nombre_curso_entry = tk.Entry(self.frame_registrar_curso)
        self.nombre_curso_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.frame_registrar_curso, text="Nombre del Profesor:").grid(row=1, column=0, padx=5, pady=5)
        self.nombre_profesor_entry = tk.Entry(self.frame_registrar_curso)
        self.nombre_profesor_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.frame_registrar_curso, text="Apellido del Profesor:").grid(row=2, column=0, padx=5, pady=5)
        self.apellido_profesor_entry = tk.Entry(self.frame_registrar_curso)
        self.apellido_profesor_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self.frame_registrar_curso, text="Día del Horario:").grid(row=3, column=0, padx=5, pady=5)
        self.dia_horario_entry = tk.Entry(self.frame_registrar_curso)
        self.dia_horario_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(self.frame_registrar_curso, text="Hora de Inicio:").grid(row=4, column=0, padx=5, pady=5)
        self.hora_inicio_entry = tk.Entry(self.frame_registrar_curso)
        self.hora_inicio_entry.grid(row=4, column=1, padx=5, pady=5)

        tk.Label(self.frame_registrar_curso, text="Hora de Fin:").grid(row=5, column=0, padx=5, pady=5)
        self.hora_fin_entry = tk.Entry(self.frame_registrar_curso)
        self.hora_fin_entry.grid(row=5, column=1, padx=5, pady=5)

        tk.Label(self.frame_registrar_curso, text="Número de Estudiantes:").grid(row=6, column=0, padx=5, pady=5)
        self.num_estudiantes_entry = tk.Entry(self.frame_registrar_curso)
        self.num_estudiantes_entry.grid(row=6, column=1, padx=5, pady=5)

        tk.Button(self.frame_registrar_curso, text="Registrar", command=self.registrar_curso).grid(row=7, column=0, columnspan=2, pady=10)

        # Frame para la información del curso
        self.frame_curso_info = tk.LabelFrame(self, text="Información del Curso")
        self.frame_curso_info.pack(fill="both", expand="yes", padx=10, pady=10)

        self.curso_info_text = tk.Text(self.frame_curso_info, height=10)
        self.curso_info_text.pack(fill="both", expand="yes", padx=10, pady=10)

    def registrar_curso(self):
        nombre_curso = self.nombre_curso_entry.get()
        nombre_profesor = self.nombre_profesor_entry.get()
        apellido_profesor = self.apellido_profesor_entry.get()
        dia_horario = self.dia_horario_entry.get()
        hora_inicio_horario = self.hora_inicio_entry.get()
        hora_fin_horario = self.hora_fin_entry.get()
        num_estudiantes = self.num_estudiantes_entry.get()

        if nombre_curso and nombre_profesor and apellido_profesor and dia_horario and hora_inicio_horario and hora_fin_horario and num_estudiantes:
            profesor = Profesor(nombre_profesor, apellido_profesor)
            horario = Horario(dia_horario, hora_inicio_horario, hora_fin_horario)
            self.curso = Curso(nombre_curso, profesor, horario)

          
            for i in range(int(num_estudiantes)):
                nombre_estudiante = f"Estudiante {i + 1}"
                apellido_estudiante = f"Apellido {i + 1}"
                estudiante = Estudiante(nombre_estudiante, apellido_estudiante, i + 1)
                self.curso.agregar_estudiante(estudiante)

            # Mostrar información del curso
            self.curso_info_text.delete('1.0', tk.END) 
            self.curso_info_text.insert(tk.END, self.curso.mostrar_info() + "\n\n")
            messagebox.showinfo("Éxito", "Curso registrado exitosamente")
        else:
            messagebox.showerror("Error", "Todos los campos son obligatorios")

if __name__ == "__main__":
    app = Application()
    app.mainloop()

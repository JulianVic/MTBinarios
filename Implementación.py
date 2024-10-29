import tkinter as tk
from tkinter import messagebox

class TuringMachine:
    def __init__(self, tape: str):
        """Inicializa la máquina de Turing con la cinta, posición del cabezal, y estado inicial."""
        self.tape = list(tape)
        self.head_position = 0
        self.current_state = 'q0'
        self.binary_sequence = ''

    def process_step(self):
        """Realiza un paso en la máquina según el estado actual y el símbolo en la posición del cabezal."""
        symbol = self.tape[self.head_position]

        if self.current_state == 'q0':
            if symbol == '1':
                self.binary_sequence += symbol
                self.head_position += 1
                self.current_state = 'q1'

        elif self.current_state == 'q1':
            if symbol == '0':
                self.binary_sequence += symbol
                self.head_position += 1
                self.current_state = 'q2'

        elif self.current_state == 'q2':
            if symbol in '01':
                self.binary_sequence += symbol
                self.head_position += 1
            elif symbol == '=':
                self.current_state = 'q3'

    def run_machine(self) -> int:
        """Ejecuta la máquina hasta alcanzar el estado de aceptación o encontrar una cadena inválida."""
        while self.current_state != 'q3' and self.head_position < len(self.tape):
            self.process_step()
        return int(self.binary_sequence, 2) if self.current_state == 'q3' else None

def validate_tape(tape: str) -> bool:
    """Valida que la cadena comience con '10', termine con '=', y contenga solo '0', '1' o '='."""
    return tape.startswith("10") and tape.endswith("=") and all(char in '01=' for char in tape)

def execute_turing_machine():
    """Valida la entrada y ejecuta la máquina de Turing si la cadena es válida."""
    tape = input_entry.get()

    if not validate_tape(tape):
        messagebox.showerror("Error", "Cadena inválida. Asegúrese de que comience con '10', termine con '=', y contenga solo 0, 1 o =.")
        return

    machine = TuringMachine(tape)
    decimal_result = machine.run_machine()

    if decimal_result is not None:
        result_label.config(text=f"Resultado en decimal: {decimal_result}")
    else:
        messagebox.showerror("Error", "La cadena no fue aceptada por la máquina de Turing.")

# Configuración de la interfaz gráfica
window = tk.Tk()
window.title("Máquina de Turing para Decimales")
window.geometry("400x250")
window.config(bg="#2e3f4f")  # Fondo oscuro

# Título
title_label = tk.Label(window, text="Convertidor Binario a Decimal", font=("Arial", 16, "bold"), fg="#ffffff", bg="#2e3f4f")
title_label.pack(pady=(20, 10))

# Instrucciones y entrada de texto
input_frame = tk.Frame(window, bg="#2e3f4f")
input_frame.pack(pady=10)
input_label = tk.Label(input_frame, text="Ingrese una cadena (comience con 10 y termine con =):", font=("Arial", 10), fg="#a1b0c1", bg="#2e3f4f")
input_label.pack()
input_entry = tk.Entry(input_frame, font=("Arial", 12), width=30, justify="center", bg="#f0f0f0", relief="solid")
input_entry.pack(pady=5)

# Botón de ejecución
run_button = tk.Button(window, text="Ejecutar", command=execute_turing_machine, font=("Arial", 12, "bold"), bg="#4caf50", fg="#ffffff", activebackground="#388e3c", cursor="hand2", relief="flat")
run_button.pack(pady=(10, 10))

# Resultado
result_label = tk.Label(window, text="Resultado en decimal: ", font=("Arial", 12), fg="#ffffff", bg="#2e3f4f")
result_label.pack(pady=(10, 20))

# Iniciar la interfaz
window.mainloop()

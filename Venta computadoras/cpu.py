class CPU:
    contador_cpu = 0

    def __init__(self, motherboard, procesador, ram, gpu="integrada"):
        CPU.contador_cpu += 1
        self.id = CPU.contador_cpu
        self.motherboard = motherboard
        self.procesador = procesador
        self.gpu = gpu
        self.ram = ram

    def __str__(self):
        return f"ID: {self.id}\nMotherboard: {self.motherboard}\nProcesador: {self.procesador}\nGPU: {self.gpu}\nRAM(GB): {self.ram}"

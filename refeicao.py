
def main():
    time = input('Digite as horas de agora como ##:##: ')
    convert(time)

def convert(time):
   hora , minuto = time.split(":")
   hora = int(hora)
   minuto = float(int(minuto) / 60)
   resultado = hora + minuto

   if resultado >= 7 and resultado <= 8:
        print('Hora do café da manhã.')
   elif resultado >= 12 and resultado <= 13:
        print('Hora do almoço')
   elif resultado >= 18 and resultado <= 19:
        print('Hora do jantar')
   

if __name__ == "__main__":
 main() 


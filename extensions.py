nome_arquivo = input("Digite o nome de um arquivo (x.formato): ").lower()
formato = nome_arquivo.split('.', 1)
if formato[1] == ('jpg') or formato[1] == ('jpeg') or formato[1] == ('gif') or formato[1] == ('png') or formato[1] == ('pdf') or formato[1] == ('txt') or formato[1] == ('zip'):
    print(formato[1])
else: 
    print('application/octet-stream')

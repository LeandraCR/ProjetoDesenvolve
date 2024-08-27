notas = [7.5, 8.0, 6.5, 9.0, 8.5]
media = sum(notas) / len(notas)
print(f'A média das notas é:{media:.2f}')

nova_nota = 7.0
notas.append(nova_nota)

media = sum(notas) / len(notas)
print(f'A nova média, após adicionar {nova_nota}, é: {media:.2f}')

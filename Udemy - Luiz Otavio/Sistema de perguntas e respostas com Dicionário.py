perguntas = {
    'Pergunta 1': {
        'Pergunta': 'Quanto é 2 + 2 ?',
        'Opções': {'A': '23', 'B': '4', 'C': '44'},
        'Resposta_certa': 'B'
    },
    'Pergunta 2': {
        'Pergunta': 'Quanto é 6 * 2 ?',
        'Opções': {'A': '12', 'B': '44', 'C': 'x'},
        'Resposta_certa': 'A'
    },
}

for per_k, detalhes in perguntas.items():
    print(f'{per_k}:')
    print(detalhes['Pergunta'])
    for k, v in detalhes['Opções'].items():
        print(f'{k}: {v}')
    resp = input('Sua escolha: ').upper()
    if resp == detalhes['Resposta_certa']:
        print('Parabéns, viado\n')
    else:
        print(f'A resposta certa seria {detalhes["Resposta_certa"]}\n')



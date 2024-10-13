import pandas as pd
import math

df = pd.read_csv('Academy_Candidates.csv', sep=';')

vaga_porcentagem = (df['Vaga'].value_counts(normalize=True) * 100).round(1).to_dict()


def limpa_idade(idade):
    return int(idade.split()[0])

df['Idade'] = df['Idade'].apply(limpa_idade)

idade_media_por_vaga = df.groupby('Vaga')['Idade'].mean().round(2).to_dict()

idade_media_qa = idade_media_por_vaga.get('QA')


idade_mais_velho_por_vaga = df.groupby('Vaga')['Idade'].max().to_dict()


idade_mais_novo_por_vaga = df.groupby('Vaga')['Idade'].min().to_dict()


soma_idades_por_vaga = df.groupby('Vaga')['Idade'].sum().to_dict()


estados_distintos = df['Estado'].nunique()


def quadrado_perfeito(n):
    return math.isqrt(n) ** 2 == n

def palindromo(nome):
    return nome.lower() == nome[::-1].lower()


instrutor_qa = df[
    (df['Vaga'] == 'QA') & 
    (df['Estado'] == 'SC') &
    (df['Idade'].between(18, 30)) &
    (df['Idade'].apply(quadrado_perfeito)) &
    (df['Nome'].apply(lambda x: palindromo(x.split()[0])))
]

instrutor_qa_nome = instrutor_qa['Nome'].values[0]
    

instrutor_mobile = df[
    (df['Vaga'] == 'Mobile') &
    (df['Estado'] == 'PI') &
    (df['Idade'].between(30, 40)) &
    (df['Idade'] % 2 == 0) &
    (df['Nome'].apply(lambda x: x.split()[-1].startswith('C')))
]

instrutor_mobile_nome = instrutor_mobile['Nome'].values[0]



print("Proporção de candidatos por vaga (porcentagem):", vaga_porcentagem)

print("O número de estados distintos presentes entre os candidatos é de:", estados_distintos, "estados")

print("Idade média dos candidatos de QA:", idade_media_qa, "anos")

print("O candidato mais velho de Mobile tem:",idade_mais_velho_por_vaga.get('Mobile'), "anos")

print("O candidato mais novo de web tem:",idade_mais_novo_por_vaga.get('Web'), "anos")

print("A soma das idades dos candidatos de QA é de:",soma_idades_por_vaga.get('QA'))

print("O arquivo 'Sorted_Academy_Candidates.csv' foi criado.")

print("Nome completo do instrutor de QA:", instrutor_qa_nome)

print("Nome do instrutor de Mobile:", instrutor_mobile_nome)
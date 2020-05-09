def linha():
    print('-'*50)

dicionario_produtos = {}

while True:
    linha()
    print('ADICIONAR PRODUTOS')
    linha()
    produto = str(input('Qual o produto à cadastrar: '))
    custo_compra = float(input('Valor de compra do produto: R$'))
    linha()
    taxa_marketing = int(input('Digite a taxa de marketing: '))
    resultado = taxa_marketing / 100
    novo_custo_compra = custo_compra + (resultado * custo_compra)
    linha()
    custo_funcionario = int(input('Qual a % que quer colocar sobre o produto referente aos funcionarios? '))
    taxa_funcionario = custo_funcionario / 100
    funcioario_marketing = novo_custo_compra + (taxa_funcionario * novo_custo_compra)
    taxas_finais = funcioario_marketing
    linha()
    taxa_lucro = int(input('Quanto % de lucro quer sobre o produto? '))
    nova_taxa_lucro = taxa_lucro / 100
    valor_final_do_produto = taxas_finais + (nova_taxa_lucro * novo_custo_compra)
    dicionario_produtos[produto] = valor_final_do_produto
    print('Adicionado novo produto..')
    print(dicionario_produtos)
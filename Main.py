# Programa IT Academy – Processo Seletivo – Edição #18
# Nome: João Pedro de Moura Medeiros | Cientista de Dados e Inteligência Artificial

# Importando as principais bibliotecas

# Biblioteca pandas a qual será útil para a leitura, processamento e manipulação do dados
import pandas as pd
# Biblioteca time importada, pois durante o código ela foi necessária para as saídas aparecerem de forma correta
# Muitas não apareciam pois o célula executava de forma muito rápida, sendo assim necessária a importação
import time
# Biblioteca regex, servindo para apenas uma questão na funcionalidade 2, 
# o qual se deseja filtrar o números de strings
import re


class Programa():
    def __init__(self, df, df_transporte):
        self.df = df
        self.df_transporte = df_transporte

    def analise(self):
        # Visualizando as informações do df
        self.df.info()
        # Analisando de há dados faltantes
        self.df.isnull().sum()
        # Analisando métodos estatísticos do df
        self.df.describe()

    def menu():
        ''' FUNÇÃO CRIADA PARA A CRIAÇÃO DO MENU DO PROGRAMA '''
        print(" _ "*34)
        print("|                                                MENU                                                |")
        print("|                                                                                                    |")
        print("|                   DIGITE OS NÚMERO DAS FUNCIONALIDADES ABAIXO PARA ELAS EXECUTAREM                 |")
        print("|                                                                                                    |")
        print("| Funcionalidade 1.[Consultar trechos x modalidade]                                                  |")
        print("| Funcionalidade 2.[Cadastrar transporte]                                                            |")
        print("| Funcionalidade 3.[Dados estatísticos]                                                              |")
        print("| Funcionalidade 4.[Finalizar programa]                                                              |")
        print("|                                                                                                    |")
        print(" _ "*34)

    def functionality_1(self):
        ''' FUNÇÃO QUE APRESENTA O CÓDIGO DA FUNCIONALIDADE 1 '''
        # Inserido um try e um except, caso o usúario insira alguma entrada inválida
        try:
            # Aqui é feito a inserção das cidades de origem e destino
            print("\nINSIRA A CIDADE DE ORIGEM\nExemplo: 'PORTO ALEGRE'\n")
            time.sleep(1)
            # Aqui foi inserido a função input para o usuário inserir a cidade de origem
            city_1 = input('INSIRA A CIDADE DE ORIGEM:').upper()
            print('CIDADE DE ORIGEM INSERIDA')
            print(f'>>>>>{city_1}<<<<<\n')
            
            # As 5 linhas abaixo farão a mesma coisa, porém será inserida a cidade de destino
            print("INSIRA A CIDADE DE DESTINO\nExemplo: 'SAO PAULO'\n")
            time.sleep(1)
            city_2 = input('INSIRA A CIDADE DE DESTINO:').upper()
            print('CIDADE DE DESTINO INSERIDA!')
            print(f'>>>>>{city_2}<<<<<\n')
            
            # Aqui é feito a inserção da modalidade do caminhão
            print('-'*60,'\n\nDIGITE O NÚMERO DA MODALIDADE DO CAMINHÃO:\nExemplo: 1 - Caminhão de pequeno porte')
            print('         2 - Caminhão de médio porte \n         3 - Caminhão de grande porte\n')
            time.sleep(1)
            truck_modality = int(input('ESCOLHA A MODALIDADE DO CAMINHÃO:'))
            print('NÚMERO DA MODALIDADE DO CAMINHÃO INSERIDO!')
            print(f'>>>>>{truck_modality}<<<<<\n')

            # Será localizado no 'df_transport' a modalidade requisitadas pelo usurário
            list_truck_price = list(self.df_tranport.iloc[truck_modality-1])
            truck = list_truck_price[0] 
            price = list_truck_price[1]
            
            # Aqui se buscará no 'df' de distância das cidades, os dados das cidades requisitadas pelo usurário
            distance_between_cities = self.df.loc[city_1, city_2]
            # Após a pesquisa da distancia das cidades, se multiplicará ela pelo preço, dando assim o Preço por Km (R$/km) 
            # Foi usado a função 'round' para deixar 2 casas depois da vírgula
            price_per_km = round(distance_between_cities*price,2)

            # As linhas abaixo mostrarão o output com as cidades, modalidade e calculo conforme 
            # o exemplo dado na funcionalidade 1
            print('-'*60, '\n')
            print(f'De {city_1} para {city_2}, utilizando um {truck},')
            print(f'a distância é de {distance_between_cities} km e o custo será de R${price_per_km}.\n')
            print('-'*60)   

            time.sleep(1)

        except KeyError as c:
            print('-'*80)
            print(f'\nA cidade inserida {c} não está contida no nosso banco de dados\n')
            print('Por favor, insira as cidades sem: \n- Caracteres especiais \n- Acentos \n- Espaços no começo ou fim delas\n')
            print("Exemplo I: insira 'SAO PAULO' ao invés de 'SAO_PAULO'")
            print("Exemplo II: insira 'SAO PAULO' ao invés de 'SÃO PAULO'")
            print("Exemplo III: insira 'SAO PAULO' ao invés de '  SAO PAULO  '\n")
            print('Digite novamente 1.[Consultar trechos x modalidade] caso queira consultar a cidade de forma certa\n')
            print('-'*80)
            time.sleep(1)

        except (IndexError, UnboundLocalError):
            print('-'*90)
            print(f'\nO número inserido {truck_modality} da modalidade de caminhão não está contido no nosso banco de dados\n')
            print('Por favor, insira os números (1,2 ou 3), sendo eles sem: \n- Caracteres especiais \n- Acentos \n- Espaços no começo ou fim delas\n')
            print("Exemplo I: insira '2' ao invés de '_2_'")
            print("Exemplo II: insira '2' ao invés de '*2*'\n")
            print('Digite novamente 1.[Consultar trechos x modalidade] caso queira consultar a modalidade de forma certa\n')
            print('-'*90)
            time.sleep(1)

    def functionality_2(self): 
            ''' FUNÇÃO QUE APRESENTA O CÓDIGO DA FUNCIONALIDADE 2 '''
            # Inserido um try e um except, caso o usúario insira alguma entrada inválida
            try:
                print('\nFAÇA O CADASTRO DA SUA EMPRESA! INSIRA O NOME DE SUA EMPRESA\n')
                print('-'*80)
                # Input para o usuário cadastrar sua empresa
                company = str(input('\nFAÇA O CADASTRO DA SUA EMPRESA! INSIRA O NOME DE SUA EMPRESA'))
                print('\nNOME DA EMPRESA INSERIDO!')
                print(f'>>>>>{company}<<<<<\n')
                print('-'*80)
                time.sleep(2)
                
                # Usuário irá inserir as cidades desejadas, tendo ela sendo adicionadas em uma lista
                city_list = []
                print('\nINSIRA AS CIDADES DESEJADAS!\n')
                for i in range(1,4):
                    city_isf = ['INICIAL', 'DE PARADA', 'FINAL']
                    value_city = city_isf[i-1]
                    print(f'INSIRA A CIDADE {value_city}')
                    city_list.append(str(input(f'INSIRA A CIDADE {value_city}').upper()))
                    city_inserted = city_list[i-1]
                    print(f'CIDADE {value_city} INSERIDA FOI: {city_inserted}\n')
                print('-'*80,'\n')
                time.sleep(2)
                
                # Usuário irá inserir os itens desejadas com respectivamente seus pesos e quantidades
                # tendo cada um deles adicionados em uma lista 
                items_list = []
                weight_item_list = []
                quantity_item_list = []
                print('INSIRA OS NOMES DOS ITENS DESEJADOS COM SEUS PESOS E QUANTIDADES!\n')
                time.sleep(1)
                # Dentro desse for será requsitado colocar o nome do item, seu peso e quantidade
                for i in range(1,5):
                    print(f'\nINSIRA O NOME DO ITEM NÚMERO {i}')
                    items_list.append(str(input(f'INSIRA O NOME DO ITEM NÚMERO {i}')))
                    item_inserted = items_list[i-1]
                    time.sleep(1)
                    try:
                        print(f'INSIRA O PESO DO ITEM NÚMERO {i}')
                        weight_item_input = str(input(f'INSIRA O PESO DO ITEM NÚMERO {i}'))
                        weight_item_list.append(float(weight_item_input.replace(",", ".")))
                        weight_item_inserted = weight_item_list[i-1]
                        time.sleep(1)
                        print(f'INSIRA A QUANTIDADE DO ITEM NÚMERO {i}')
                        quantity_item_input = int(input(f'INSIRA A QUANTIDADE DO ITEM NÚMERO {i}'))
                        quantity_item_list.append(quantity_item_input)
                        quantity_item_inserted = quantity_item_list[i-1]
                        time.sleep(1)
                        print(f'\nO ITEM NÚMERO {i} INSERIDO FOI >>>{item_inserted}<<< E SEU PESO É DE >>>{weight_item_inserted}kg<<<')
                        print(f'COM >>>{quantity_item_inserted}<<< DE QUANTIDADE\n')
                    except (ValueError,KeyError):
                        print()
                        print('-'*90)
                        print('\nNUMERO INSERIDO DE FORMA ERRADA!\n')
                        print('PARA A INSERÇÃO DE PESO, É APENAS POSSÍVEL NÚMEROS!')
                        print('PARA A INSERÇÃO DE QUANTIDADE, É APENAS POSSÍVEL NÚMEROS INTEIROS(SEM PONTO OU VÍRGULA)!\n')
                        print('-'*90)
                        time.sleep(1)
                    time.sleep(1)
                print('-'*80,'\n')

                
                sum_distance = int(Programa.model_identify(city_list[0], city_list[1], city_list[2]))
                result = Programa.cost_transport(weight_item_list, quantity_item_list, items_list)

                # Interando sobre a lista retornada da função cost_transport, pegará as modalidade dos caminhões tais como 
                # ['Caminhão de porte GRANDE', 'Caminhão de porte MÉDIO', 'Caminhão de porte PEQUENO']
                list_total_prices_per_way = []
                for i in result[0]:
                    price_per_km = float(self.df_tranport.loc[self.df_tranport['Itens'] == i]['Preco por Km(R$/km)'])
                    total_price = round(price_per_km*sum_distance, 2)
                    list_total_prices_per_way.append(total_price)
                    
                # Aqui será feito o cálculo dos valores totais do transporte e os valores unitários
                var_total_price = round(sum(list_total_prices_per_way),2)
                sum_quantity_item_list= sum(quantity_item_list)
                var_unitary_price = round(var_total_price/sum_quantity_item_list,2)
                print(f'O valor total do transporte dos itens é R$ {var_total_price},')
                print(f'sendo R$ {var_unitary_price} é o custo unitário médio.\n')
                print('-'*80,'\n')

                # Aqui será feito o calculo do 'Custo médio por tipo de produto'
                set_items = list(set(items_list))
                mean_cust_per_product = round(var_total_price/len(set_items),2)

                # Aqui será feito o calculo do 'Custo total para cada modalidade de transporte (R$)'
                # Se retira valores duplicados 
                set_modality = list(set(result[0]))
                # Ordena em forma crescente os valores da list_total_prices_per_way
                list_total_prices_per_way.sort()
                set_sort_total_prices = list(set(list_total_prices_per_way))
                # Junta os valores pelo index de cada lista, isso retornará o 'Custo total para cada modalidade de transporte (R$)'
                cust_per_modality = tuple(zip(set_modality, set_sort_total_prices))
                
                # Aqui será feito o método para pegar o total de veículos deslocados
                list_nums = []
                for i in result[1]:
                    # É utilizado regex para filtrar o número da string
                    num = (re.findall('[0-9]+', i))
                    list_nums.append(num[-1])
                # Se faz a soma de todos o números, dando assim o 'Número total de veículos deslocados'
                total_trucks = 0
                for valor in list_nums:
                    total_trucks += int(valor)
                
                # Aqui será feito o armazenamento dos dados cadastrados em dicionário
                # Para que possa exibir um relatório dos transportes até então cadastrados na funcionalidade 3
                dict_transport = dict({'Empresa': company,
                                    'Custo total (R$)': var_total_price,
                                    # Custo médio por trecho ??? Não foi possível entender do enunciado, logo se fará a média por cada trecho
                                    'Custo por trecho (R$)': round(var_total_price/3,2), 
                                    'Custo médio por km (R$)': round(var_total_price/sum_distance,2),
                                    'Custo médio por tipo de produto (R$)': mean_cust_per_product,
                                    'Custo total por trecho (R$)': var_total_price,
                                    'Custo total para cada modalidade de transporte (R$)': cust_per_modality,
                                    'Número total de veículos deslocados': total_trucks, 
                                    'Total de itens Transportados': sum(quantity_item_list)})

                # Adicionará o dicionário em uma lista global, para guardar na memória, podendo utilizar na funcionalidade 3
                list_transport_register.append(dict_transport)
                time.sleep(2)
                
            except KeyError as c:
                print(f'A cidade inserida {c} não está contida no nosso banco de dados\n')
                print('Por favor, insira as cidades sem: \n- Caracteres especiais \n- Acentos \n- Espaços no começo ou fim delas\n')
                print("Exemplo I: insira 'SAO PAULO' ao invés de 'SAO_PAULO'")
                print("Exemplo II: insira 'SAO PAULO' ao invés de 'SÃO PAULO'")
                print("Exemplo III: insira 'SAO PAULO' ao invés de '  SAO PAULO  '\n")
                print('Digite novamente 2.[Cadastrar transporte] caso queira consultar a cidade de forma certa\n')
                print('-'*80)
                time.sleep(1)

    # Função que identifica a distância entre as cidades e retorna o valor total delas
    def model_identify(self, city_1, city_2, city_3):
        ''' FUNÇÃO QUE FAZ PARTE DA FUNCIONALIDADE 2 '''
        # df.loc[index, coluna] irá procurar no df o dados correspondente ao index e coluna
        distance_between_cities_1 = self.df.loc[city_1, city_2]
        distance_between_cities_2 = self.df.loc[city_2, city_3]
        sum_distance = distance_between_cities_1 + distance_between_cities_2

        print(f'de {city_1} para {city_2}, a distância a ser percorrida é de {distance_between_cities_1} km')
        print(f'e de {city_2} para {city_3}, a distância a ser percorrida é de {distance_between_cities_2} km')
        print(f'somando um total de {sum_distance} km, para transporte dos produtos')
        
        return sum_distance
        
    # Função para calcular o peso dos itens pelas suas quantidades e a partir disso escolhendo os caminhões para transporte
    def cost_transport(self, weight_item_list, quantity_item_list, items_list):
        ''' FUNÇÃO QUE FAZ PARTE DA FUNCIONALIDADE 2 '''
        list_total_weight_item = list(map(lambda x, y: (x*y), weight_item_list, quantity_item_list))
        total_weight = sum(list_total_weight_item)
        
        # Modalidades dos caminhões
        truck_modality_1 = self.df_tranport['Itens'][1]
        truck_modality_2 = self.df_tranport['Itens'][2]
        truck_modality_3 = self.df_tranport['Itens'][3]
        list_modality = [truck_modality_1, truck_modality_2, truck_modality_3]
        # Peso de transporte dos caminhões
        truck_weight_1 = self.df_tranport['Peso de transporte(kg)'][1]
        truck_weight_2 = self.df_tranport['Peso de transporte(kg)'][2]
        truck_weight_3 = self.df_tranport['Peso de transporte(kg)'][3]

        # Aqui será feito a contagem de quantos caminhões serão necessários para o transporte da carga se baseando no peso dela
        list_transport_truck = []
        while total_weight > 0:
            if total_weight >= truck_weight_3:    
                total_weight = total_weight - truck_weight_3
                list_transport_truck.append(truck_modality_3)
            elif total_weight >= truck_weight_2:
                total_weight = total_weight - truck_weight_2
                list_transport_truck.append(truck_modality_2)
            else:
                total_weight = total_weight - truck_weight_1
                list_transport_truck.append(truck_modality_1)

        truck_count_1 = list_transport_truck.count(truck_modality_1)
        truck_count_2 = list_transport_truck.count(truck_modality_2)
        truck_count_3 = list_transport_truck.count(truck_modality_3)
        
        # Criado um dicionário com a modalidade do caminhão como chave e o quantidade que necessitará para o transporte
        dict_truck_count = ({truck_modality_1: truck_count_1, truck_modality_2: truck_count_2, truck_modality_3: truck_count_3})
        values = list(dict_truck_count.values())
        
        list_truck_transport_count = list(map(lambda x, y: f'{x} {y}' if x != 0 else None , values, list_modality ))
        list_truck_transport_count = list(filter(lambda x: x is not None, list_truck_transport_count))

        ####print(list_truck_transport_count)
        str_truck_tranport_count = ', '.join(list_truck_transport_count)
        str_items_list = ', '.join(items_list)
        
        ####print(str_truck_tranport_count)
        ####print(list_transport_truck, '\n')
        print(f'{str_items_list} será necessário utilizar')
        print(f'{str_truck_tranport_count},\nde forma a resultar no menor custo de transporte por km rodado.')
        
        return (list_transport_truck, list_truck_transport_count)
        

    def functionality_3(): 
        ''' FUNÇÃO QUE APRESENTA O CÓDIGO DA FUNCIONALIDADE 3 '''
        # Pega a lista global e a transforma em um df para a visualização dos dados estatísticos
        df_register = pd.DataFrame(list_transport_register)
        # Caso o df esteja vazio printará a seguinte frase
        if df_register.empty:
            print()
            print('SEM DADOS ESTATISTÍCOS DOS TRANSPORTES CADASTRADOS! CADASTRE ALGUM TRANSPORTE\n')
        # Senão mostra na tela para o usuário os dados estatisticos
        else:
            print()
            print(df_register.to_string(),'\n') 
        print('-'*80) 
    

# Leitura do arquivo .csv
df = pd.read_csv('DNIT-Distancias.csv', delimiter=';') 

# Pegando todos os nomes das cidades e tranformando em uma série de dados
# Foi feito isso pois ela será inserida no index do df, facilitando a consulta das distâncias das cidades
column_city = pd.Series(df.columns) 
# Vizualizando a nova coluna
#display(column_city)

# Insiro a coluna recém criada no index do df, para ser feita com mais eficiência a orientação a dados
df = df.set_index(column_city)

''' CRIADO UM DF DAS MODALIDADES DE CAMINHÕES IGUAL AO QUE SE APRESENTA NO ENUNCIADO, PARA FACILITAR A CONSULTA '''
# Lista de modalidades de caminhões
list_truck = ['Caminhão de porte PEQUENO', 'Caminhão de porte MÉDIO', 'Caminhão de porte GRANDE']
# Lista de preço por Km (R$/km)
list_price = [4.87, 11.92, 27.44]
# Lista de peso de transporte (kg)
transport_weight = [1000, 4000, 10000]
# Criando um df da modalidade e preço por Km, conforme aparece no enunciado
df_tranport = pd.DataFrame({'Itens': list_truck, 'Preco por Km(R$/km)': list_price, 'Peso de transporte(kg)': transport_weight}, index=[1,2,3])
# Visualizando o df
# display(df_tranport)
list_transport_register = []


if __name__ == '__main__':

    Programa(df, df_tranport)
    # Chamando a função menu
    Programa.menu()
    list_functionality = ['1.[Consultar trechos x modalidade]',
                        '2.[Cadastrar transporte]',
                        '3.[Dados estatísticos]',
                        '4.[Finalizar o programa]']
    i = int
    # Criado um while para ficar rodando o programa
    while i != 4: 
        # Inserido um try e um except, caso o usúario insira alguma entrada inválida
        try: 
            print("\nDIGITE O NÚMERO DA FUNCIONALIDADE\n")
            # Usuário deve digitar o número de alguma funcionalidade
            i = int(input("DIGITE O NÚMERO DA FUNCIONALIDADE:"))
            number_functionality = list_functionality[i-1]
            print(f"O NÚMERO DA FUNCIONALIDADE ESCOLHIDO FOI\n>>> {number_functionality}\n")
            time.sleep(2)
            print('-'*60)
            if (i == 1):
                # Executará o código da funcionalidade 
                Programa.functionality_1()
            elif (i == 2):
                # Executará o código da funcionalidade 
                Programa.functionality_2()
            elif (i == 3):
                # Executará o código da funcionalidade 
                Programa.functionality_3()
            elif (i == 4):
                print("\nO PROGRAMA FOI FINALIZADO! ATÉ LOGO!")
                break
            else:
                print("\nERRO DE NUMERAÇÃO, DIGITE APENAS OS NÚMEROS DAS FUNCIONALIDADES (1, 2, 3, 4)\n")
                print('-'*60)
                time.sleep(1)
        except (ValueError, IndexError):
            print('-'*60)
            print("\nDIGITE APENAS NÚMEROS (1, 2, 3 OU 4)\n")
            print('-'*60)
            time.sleep(1)



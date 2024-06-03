import csv
import re
import pandas as pd
from datetime import datetime, date, timedelta
from unidecode import unidecode
from fpdf import FPDF
from docx import Document
from colorama import Fore, init, Style

init(autoreset=True)

def main():
    try:
        with open("dados.csv", "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read()
            print("Arquivo dados.csv aberto com sucesso!")
    except FileNotFoundError:
        with open("dados.csv", "a", encoding="utf-8", newline='') as arquivo:
            arquivo.write('')
            print("Arquivo dados.csv criado com sucesso!")
    
    print("OLÁ. SEJA BEM VINDO A SUA AGENDA DE TAREFAS!")

    menu()

def prox_reg():
    try:
        with open('dados.csv', 'r', encoding='utf-8') as arquivo:
            reader = csv.reader(arquivo)
            registros = [int(row[0]) for row in reader if row]
            if registros:
                return max(registros) + 1
            else:
                return 1
            
    except FileNotFoundError:
            return 1

def verifica_tarefas():
    nome_colunas = ["Núm. Registro", "Tarefa", "Descrição", "Vencimento", "Estado"]
    data = pd.read_csv('dados.csv', header=None, names=nome_colunas)
    
    hoje = datetime.now()
    tres_dias = hoje + timedelta(days=3)
    
    # Convertendo a coluna 'Vencimento' para datetime
    data['Vencimento'] = pd.to_datetime(data['Vencimento'], format='%d/%m/%Y', errors='coerce')
    
    # Verificando tarefas que vencem nos próximos 3 dias
    proximas_tarefas = data[(data['Vencimento'] >= hoje) & (data['Vencimento'] <= tres_dias)]
    numero_tarefas = len(proximas_tarefas)
    
    if numero_tarefas == 0:
        print(Fore.GREEN + "Não há tarefas vencendo nos próximos 3 dias." + Fore.RESET)
    else:
        print(Fore.YELLOW + f"Existem {numero_tarefas} tarefas a vencer nos próximos 3 dias." + Fore.RESET)
    
    # Verificando tarefas vencidas
    tarefas_vencidas = data[data['Vencimento'] < hoje]
    numero_vencidas = len(tarefas_vencidas)
    
    if numero_vencidas == 0:
        print(Fore.GREEN + "Não há tarefas vencidas." + Fore.RESET)
    else:
        print(Fore.RED + f"Existem {numero_vencidas} tarefas vencidas." + Fore.RESET)
        vencidas = input("Deseja ver as tarefas vencidas (1-SIM/2-NÃO)? ")
        uni_vencidas = unidecode(vencidas.lower())
        
        if uni_vencidas == "sim" or uni_vencidas == "1" or uni_vencidas == "1-sim":
            # Formatar e exibir a tabela de tarefas vencidas
            tarefas_vencidas['Vencimento'] = tarefas_vencidas['Vencimento'].dt.strftime('%d/%m/%Y')
            df_str = tarefas_vencidas.astype(str)
            col_widths = {col: max(df_str[col].str.len().max(), len(col)) + 2 for col in df_str.columns}
            format_dict = {col: "{{:<{}}}".format(width).format for col, width in col_widths.items()}

            formatted_rows = []
            for index, row in df_str.iterrows():
                formatted_row = " | ".join([format_dict[col](row[col]) for col in df_str.columns])
                formatted_rows.append(formatted_row)

            header = " | ".join([format_dict[col](col) for col in df_str.columns])
            separator = "-" * len(header)

            print(Fore.BLUE + separator)
            print(Fore.BLUE + header)
            print(Fore.BLUE + separator)

            for row in formatted_rows:
                print(Fore.BLUE + row)

            print(Fore.BLUE + separator + Style.RESET_ALL)
        elif uni_vencidas == "nao" or uni_vencidas == "2" or uni_vencidas == "2-nao":
            print("Você optou por não ver as tarefas vencidas.")
        else:
            print("Opção inválida!")
    return

def menu():
    tarefas = 0
    for linhas in open('dados.csv'):
        tarefas += 1

    if tarefas == 1:
        print("VOCÊ POSSUI", tarefas, "TAREFA.")
    else:
        print("VOCÊ POSSUI", tarefas, "TAREFAS.")

    verifica_tarefas()
    
    print("ESCOLHA UMA OPÇÃO:")
    print("1 - Busca")
    print("2 - Nova tarefa")
    print("3 - Visualizar tarefas")
    print("4 - Tarefas a vencer")
    print("5 - Marcar tarefa concluída")
    print("6 - Editar tarefa")
    print("7 - Excluir tarefa")
    print("8 - Sair")

    try: 
        escolha = int(input("Digite o número da opção desejada:"))

        if escolha == 1:
            print("Busca")
            busca_tarefa()
        if escolha == 2:
            print("Nova tarefa")
            nova_tarefa()
        elif escolha == 3:
            print("Visualizar tarefas")
            ver_tarefas()
        elif escolha == 4:
            tarefas_proximas()
        elif escolha == 5:
            print("Marcar tarefa")
            marcar_tarefa()
        elif escolha == 6:
            print("Editar tarefa")
            edit_tarefa()
        elif escolha == 7:
            print("Excluir tarefa")
            excluir_tarefa()
        elif escolha == 8:
            print("Sair")
            return
        else:
            print("Escolha uma opção válida!")
            menu()
    except ValueError:
        print(Fore.YELLOW + "Digite apenas o número da opção." + Fore.RESET)
        menu()
        return


def busca_tarefa():
    print("Escolha o tipo de busca:")
    print("1 - Por nome da tarefa")
    print("2 - Por vencimento (no formato DD/MM/AAAA)")
    print("3 - Por estado")
    tipo_busca = input("Digite o número correspondente à opção desejada: ")

    nome_colunas = ["# Reg", "Tarefa", "Descrição", "Vencimento", "Estado"]
    data = pd.read_csv('dados.csv', header=None, names=nome_colunas)

    # Convertendo a coluna 'Vencimento' para datetime
    data['Vencimento'] = pd.to_datetime(data['Vencimento'], format='%d/%m/%Y', errors='coerce')

    if tipo_busca == "1":
        nome_tarefa = input("Digite o nome da tarefa: ")
        resultado = data[data["Tarefa"].str.contains(nome_tarefa, case=False)].copy()
    elif tipo_busca == "2":
        while True:
            vencimento = input("Digite a data de vencimento (no formato DD/MM/AAAA): ")
            try:
                data_vencimento = datetime.strptime(vencimento, "%d/%m/%Y")
                break
            except ValueError:
                print(Fore.RED + "Formato inválido! Digite a data no formato correto." + Fore.RESET)
        resultado = data[data["Vencimento"] == data_vencimento].copy()
    elif tipo_busca == "3":
        print("Escolha o estado da tarefa:")
        print("1 - Finalizada")
        print("2 - Não finalizada")
        estado_opcao = input("Digite o número correspondente à opção desejada: ")
        estado = "Finalizada" if estado_opcao == "1" else "Não finalizada"
        resultado = data[data["Estado"] == estado].copy()
    else:
        print(Fore.RED + "Opção inválida!" + Fore.RESET)
        return

    if resultado.empty:
        print(Fore.GREEN + "Nenhuma tarefa encontrada." + Fore.RESET)
    else:
        print(Fore.YELLOW + "Tarefas encontradas:" + Fore.RESET)

        # Formatando a tabela
        resultado['Vencimento'] = resultado['Vencimento'].dt.strftime('%d/%m/%Y')  # Formatar datas

        col_widths = {"# Reg": 5, "Tarefa": 16, "Descrição": 46, "Vencimento": 12, "Estado": 15}
        
        def quebra_linha(texto, largura):
            return [texto[i:i+largura] for i in range(0, len(texto), largura)]

        format_dict = {col: "{{:<{}}}".format(width).format for col, width in col_widths.items()}

        def formatar_linha(row):
            linhas = {col: quebra_linha(str(row[col]), col_widths[col]) for col in resultado.columns}
            max_linhas = max(len(linhas[col]) for col in linhas)
            linha_formatada = []
            for i in range(max_linhas):
                linha = " | ".join([format_dict[col](linhas[col][i] if i < len(linhas[col]) else "") for col in resultado.columns])
                linha_formatada.append(linha)
            return linha_formatada

        print(Fore.BLUE + "-" * (sum(col_widths.values()) + 4))
        header = " | ".join([format_dict[col](col) for col in resultado.columns])
        print(Fore.BLUE + header)
        print(Fore.BLUE + "-" * (sum(col_widths.values()) + 4))

        linhas_resultado = []
        for _, row in resultado.iterrows():
            linhas_resultado.extend(formatar_linha(row))
            linhas_resultado.append("-" * (sum(col_widths.values()) + 4))

        for linha in linhas_resultado:
            print(Fore.BLUE + linha)

    salvar_arquivo = input("Deseja salvar o resultado em um arquivo (txt, pdf, docx)? (S/N): ").upper()
    if salvar_arquivo == "S":
        formato = input("Digite o formato desejado (txt, pdf, docx): ").lower()
        nome_arquivo = input("Digite o nome do arquivo (padrão: tarefas_dia_data_atual.extensão): ")
        if not nome_arquivo:
            data_atual = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            nome_arquivo = f"tarefas_dia_{data_atual}.{formato}"
        
        conteudo_tabela = formatar_tabela(resultado)
        
        if formato == 'txt':
            with open(nome_arquivo, 'w', encoding='utf-8') as file:
                file.write(conteudo_tabela)
        elif formato == 'pdf':
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            for line in conteudo_tabela.split("\n"):
                pdf.cell(180, 10, txt=line, ln=True)
            pdf.output(nome_arquivo)
        elif formato == 'docx':
            doc = Document()
            for line in conteudo_tabela.split("\n"):
                doc.add_paragraph(line)
            doc.save(nome_arquivo)
        else:
            print(Fore.RED + "Formato inválido!" + Fore.RESET)
            return
        print(Fore.GREEN + f"Resultado salvo com sucesso em '{nome_arquivo}'." + Fore.RESET)

def formatar_tabela(df):
    col_widths = {"# Reg": 5, "Tarefa": 16, "Descrição": 46, "Vencimento": 12, "Estado": 15}

    def quebra_linha(texto, largura):
        return [texto[i:i+largura] for i in range(0, len(texto), largura)]

    format_dict = {col: "{{:<{}}}".format(width).format for col, width in col_widths.items()}

    def formatar_linha(row):
        linhas = {col: quebra_linha(str(row[col]), col_widths[col]) for col in df.columns}
        max_linhas = max(len(linhas[col]) for col in linhas)
        linha_formatada = []
        for i in range(max_linhas):
            linha = " | ".join([format_dict[col](linhas[col][i] if i < len(linhas[col]) else "") for col in df.columns])
            linha_formatada.append(linha)
        return linha_formatada

    output = []
    output.append("-" * (sum(col_widths.values()) + 4))
    header = " | ".join([format_dict[col](col) for col in df.columns])
    output.append(header)
    output.append("-" * (sum(col_widths.values()) + 4))

    for _, row in df.iterrows():
        linhas = formatar_linha(row)
        for linha in linhas:
            output.append(linha)
        output.append("-" * (sum(col_widths.values()) + 4))
    
    return "\n".join(output)
    
def nova_tarefa():
    print("Você deseja criar uma nova tarefa? (1-SIM/2-NÃO)")
    respNova = int(input())
    while True:
        nova_tarefa = {}
        if respNova == 1:
            nova_tarefa['registro'] = prox_reg()
            editar_tarefa = True
            while editar_tarefa:
                nova_tarefa['titulo'] = input("Digite o título da tarefa: ")
                nova_tarefa['descricao'] = input("Digite uma breve descrição da tarefa: ")

                while True:
                    nova_tarefa['vencimento'] = input("Qual a data limite para essa tarefa (DD/MM/AAAA): ")
                    if re.match(r'\d{2}/\d{2}/\d{4}', nova_tarefa['vencimento']):
                        data_atual = datetime.now().strftime("%d/%m/%Y")
                        if datetime.strptime(nova_tarefa['vencimento'], "%d/%m/%Y") >= datetime.strptime(data_atual, "%d/%m/%Y"):
                            break
                        else:
                            print('A data inserida é anterior à data atual. Por favor, insira uma data futura.')
                    else:
                        print('Formato inválido! Entre com uma data válida no formato DD/MM/AAAA.')
            
                nova_tarefa['estado'] = int(input("A tarefa está concluída? (1-SIM/2-NÃO): "))

                print(Fore.BLUE + "-" * 60)
                print("Resumo da tarefa:")
                print("Título:", nova_tarefa['titulo'])
                print("Descrição:", nova_tarefa['descricao'])
                print("Vencimento:", nova_tarefa['vencimento'])
                print("Estado:", "Finalizada" if nova_tarefa['estado'] == 1 else "Não finalizada")
                print("-" * 60 + Style.RESET_ALL)

                print("Deseja corrigir algum campo? (1-SIM/2-NÃO)")
                corrigir = int(input())
                if corrigir == 1:
                    print("Qual campo você deseja corrigir?")
                    print("1 - Título")
                    print("2 - Descrição")
                    print("3 - Vencimento")
                    print("4 - Estado")
                    campo_corrigir = int(input())
                    if campo_corrigir == 1:
                        continue
                    elif campo_corrigir == 2:
                        continue
                    elif campo_corrigir == 3:
                        continue
                    elif campo_corrigir == 4:
                        continue
                    else:
                        print("Opção inválida!")
                else:
                    editar_tarefa = False

            if nova_tarefa['titulo'] == '' or nova_tarefa['descricao'] == '' or nova_tarefa['vencimento'] == '' or nova_tarefa['estado'] == '':
                print("Por favor, preencha todos os campos.")
            elif nova_tarefa['estado'] == 1:
                nova_tarefa['estado'] = "Finalizada"
                salvar_tarefa(nova_tarefa)
                menu()
                return
            elif nova_tarefa['estado'] == 2:
                nova_tarefa['estado'] = "Não finalizada"
                salvar_tarefa(nova_tarefa)
                menu()
                return
            else:
                print("Opção inválida! Escolha apenas 1 ou 2")

        elif respNova == 2:
            menu()
            return
        else:
            print("Opção inválida, digite 1 para sim ou 2 para não.")
            respNova = int(input())


def salvar_tarefa(nova_tarefa):
    with open("dados.csv", "a", encoding="utf-8", newline='') as arquivo:
        novodado = csv.writer(arquivo)
        novodado.writerow([nova_tarefa['registro'], nova_tarefa['titulo'], nova_tarefa['descricao'], nova_tarefa['vencimento'], nova_tarefa['estado']])
        print("Tarefa salva com sucesso:", nova_tarefa)


def ver_tarefas():
    nome_colunas = ["Núm. Registro", "Tarefa", "Descrição", "Vencimento", "Estado"]
    data = pd.read_csv('dados.csv', header=None, names=nome_colunas)

    if data.empty:
        print(Fore.YELLOW + "Não há tarefas para exibir.")
        print(Fore.RESET)
        menu()
        return
    
    data = data.astype(str)
    col_widths = {col: max(data[col].str.len().max(), len(col)) + 2 for col in data.columns}
    format_dict = {col: "{{:<{}}}".format(width).format for col, width in col_widths.items()}
    header = " | ".join([format_dict[col](col) for col in data.columns])
    divider = "-" * len(header)  # Linha divisória
    
    data_atual = date.today()
    data_forma = data_atual.strftime('%d/%m/%Y')
    print()
    print(Fore.BLUE + "######################################################################################################################╗")
    print("A data de hoje é", Fore.MAGENTA + data_forma)
    print(Fore.BLUE + header)
    print(divider)
    
    for index, row in data.iterrows():
        formatted_row = " | ".join([format_dict[col](val) for col, val in row.items()]) + "║"
        print(formatted_row)
        
    print()
    print("######################################################################################################################╝")
    print(Fore.RESET)
    menu()
    return

def quebra_linha(text, n=30):
    """Insere quebras de linha em um texto a cada n caracteres."""
    return '\n'.join([text[i:i+n] for i in range(0, len(text), n)])

def tarefas_proximas():
    nome_colunas = ["Núm. Registro", "Tarefa", "Descrição", "Vencimento", "Estado"]
    data = pd.read_csv('dados.csv', header=None, names=nome_colunas)
    
    hoje = datetime.now()
    tres_dias = hoje + timedelta(days=3)
    
    data['Vencimento'] = pd.to_datetime(data['Vencimento'], format='%d/%m/%Y', errors='coerce')
    data['Vencimento'] = data['Vencimento'].dt.strftime('%d/%m/%Y')

    proximas_tarefas = data[(pd.to_datetime(data['Vencimento'], format='%d/%m/%Y') >= hoje) & (pd.to_datetime(data['Vencimento'], format='%d/%m/%Y') <= tres_dias)]
    
    numero_tarefas = len(proximas_tarefas)
    
    if proximas_tarefas.empty:
        print(Fore.GREEN + "Não há tarefas vencendo nos próximos 3 dias." + Fore.RESET)
    else:
        print(Fore.YELLOW + f"Existem {numero_tarefas} tarefas a vencer nos próximos 3 dias:" + Fore.RESET)
        
        results = proximas_tarefas[['Núm. Registro', 'Tarefa', 'Vencimento']]
        results = results.applymap(str)
        
        # Limita o texto
        results['Tarefa'] = results['Tarefa'].apply(quebra_linha)
        
        # Formatação da tabela
        results_str = results.astype(str)
        col_widths = {col: max(results_str[col].str.len().max(), len(col)) + 2 for col in results_str.columns}
        format_dict = {col: "{{:<{}}}".format(width).format for col, width in col_widths.items()}
        
        print()
        header = " | ".join([format_dict[col](col) for col in results_str.columns])
        print(Fore.BLUE + "-" * len(header))
        print(Fore.BLUE + header)
        print(Fore.BLUE + "-" * len(header))
        
        for index, row in results_str.iterrows():
            formatted_row = " | ".join([format_dict[col](val) for col, val in row.items()])
            print(Fore.BLUE + formatted_row)
        
        print(Fore.BLUE + "-" * len(header) + Style.RESET_ALL)
        print(Fore.RESET)
    menu()
    return()
    
def resumo_tarefas():
    
    nome_colunas = ["Núm. Registro", "Tarefa", "Descrição", "Vencimento", "Estado"]
    results = pd.read_csv('dados.csv', header=None, names=nome_colunas)
    results.columns = nome_colunas

    if results.empty:
        print(Fore.YELLOW + "Não há tarefas para exibir.")
        return

    results = results[["Núm. Registro", "Tarefa"]]
    results = results.astype(str)
    col_widths = {col: max(results[col].str.len().max(), len(col)) + 2 for col in results.columns}
    format_dict = {col: "{{:<{}}}".format(width).format for col, width in col_widths.items()}
    print()
    print(Fore.BLUE + "########################################## ╗")
    header = " | ".join([format_dict[col](col) for col in results.columns])
    print(Fore.BLUE + header)
    print(Fore.BLUE + "-" * len(header))
    
    for index, row in results.iterrows():
        formatted_row = " | ".join([format_dict[col](val) for col, val in row.items()]) + " ║"
        print(Fore.BLUE + formatted_row)

    print()
    print(Fore.BLUE + "########################################## ╝")
    print(Fore.RESET)

def encontrar_tarefa(data, numero_ou_nome):
    
    data['Núm. Registro'] = data['Núm. Registro'].astype(str)

    if numero_ou_nome.isdigit():
        numero_registro = numero_ou_nome
        linha_tarefa = data.loc[data['Núm. Registro'] == numero_registro]
    else:
        linha_tarefa = data.loc[data['Tarefa'].str.contains(numero_ou_nome, case=False, na=False)]

    if not linha_tarefa.empty:
        return linha_tarefa
    else:
        return None
        
def marcar_tarefa():
    nome_colunas = ["Núm. Registro", "Tarefa", "Descrição", "Vencimento", "Estado"]
    data = pd.read_csv('dados.csv', header=None, names=nome_colunas)
    
    resumo_tarefas()
    
    numero_tarefa = input("Digite o número da tarefa que deseja marcar como finalizada ou 0(zero) para cancelar: ")    
    linha_tarefa = encontrar_tarefa(data, numero_tarefa)

    if linha_tarefa is not None:
        print(Fore.YELLOW + "Tarefa encontrada!" + Fore.RESET)
        
        linha_tarefa_str = linha_tarefa.astype(str)
        col_widths = {col: max(linha_tarefa_str[col].str.len().max(), len(col)) + 2 for col in linha_tarefa_str.columns}
        format_dict = {col: "{{:<{}}}".format(width).format for col, width in col_widths.items()}
        
        formatted_row = " | ".join([format_dict[col](linha_tarefa_str.iloc[0][col]) for col in linha_tarefa_str.columns])
        
        print(Fore.BLUE + "-" * len(formatted_row))
        print(Fore.BLUE + formatted_row)
        print(Fore.BLUE + "-" * len(formatted_row) + Style.RESET_ALL)

        while True:
            print(Fore.BLUE + "Realmente deseja marcar esta tarefa como finalizada (1-Sim/2-Não)? ")
            resp = input()
            print(Fore.RESET)
            resp_uni = unidecode(resp.lower())
            if resp_uni == "sim" or resp == "1" or resp == "1-sim":
                data.loc[linha_tarefa.index, 'Estado'] = "Finalizada"
                data.to_csv('dados.csv', index=False, header=False)
                print(Fore.YELLOW + "Tarefa finalizada com sucesso!" + Fore.RESET)
            elif resp_uni == "nao" or resp == "2" or "2-nao":
                print(Fore.BLUE + "Tarefa " + Fore.YELLOW + "NÃO" + Fore.BLUE + " finalizada!" + Fore.RESET)
            else:
                print(Fore.YELLOW + "Opção inválida!" + Fore.RESET)
                continue

            menu()
            return
    else:
        print(Fore.YELLOW + "Tarefa não encontrada." + Fore.RESET)
        menu()
        return


def edit_tarefa():
    nome_colunas = ["Núm. Registro", "Tarefa", "Descrição", "Vencimento", "Estado"]
    data = pd.read_csv('dados.csv', header=None, names=nome_colunas)
    
    resumo_tarefas()
    
    numero_tarefa = input("Digite o número da tarefa que deseja editar ou 0(zero) para cancelar: ")
    if numero_tarefa == "0":
        print(Fore.YELLOW + "Operação cancelada pelo usuário." + Fore.RESET)
        menu()
        return
    else:    
        linha_tarefa = encontrar_tarefa(data, numero_tarefa)

        if linha_tarefa is not None:
            print(Fore.YELLOW + "Tarefa encontrada!" + Fore.RESET)
            
            linha_tarefa_str = linha_tarefa.astype(str)
            col_widths = {col: max(linha_tarefa_str[col].str.len().max(), len(col)) + 2 for col in linha_tarefa_str.columns}
            format_dict = {col: "{{:<{}}}".format(width).format for col, width in col_widths.items()}
            
            formatted_row = " | ".join([format_dict[col](linha_tarefa_str.iloc[0][col]) for col in linha_tarefa_str.columns])
            
            print(Fore.BLUE + "-" * len(formatted_row))
            print(Fore.BLUE + formatted_row)
            print(Fore.BLUE + "-" * len(formatted_row) + Style.RESET_ALL)

            print("Escolha qual informação deseja alterar:")
            print("1 - Título")
            print("2 - Descrição")
            print("3 - Vencimento")
            print("4 - Estado")
            print("5 - Todos")
            print("6 - Cancelar")
            escolha = input("Digite o número da opção que deseja alterar: ")

            if escolha == "1":
                novo_titulo = input("Digite o novo título da tarefa: ")
                data.loc[linha_tarefa.index, 'Tarefa'] = novo_titulo
                print(Fore.GREEN + "Título da tarefa atualizado com sucesso!" + Fore.RESET)
            
            elif escolha == "2":
                nova_descricao = input("Digite a nova descrição da tarefa: ")
                data.loc[linha_tarefa.index, 'Descrição'] = nova_descricao
                print(Fore.GREEN + "Descrição da tarefa atualizada com sucesso!" + Fore.RESET)
            
            elif escolha == "3":
                while True:
                    nova_data = input("Qual a data limite para essa tarefa (DD/MM/AAAA): ")
                    if re.match(r'\d{2}/\d{2}/\d{4}', nova_data):
                        data_atual = datetime.now().strftime("%d/%m/%Y")
                        nova_data_obj = datetime.strptime(nova_data, "%d/%m/%Y")
                        if nova_data_obj >= datetime.strptime(data_atual, "%d/%m/%Y"):
                            data.loc[linha_tarefa.index, 'Vencimento'] = nova_data
                            print(Fore.GREEN + "Data de vencimento da tarefa atualizada com sucesso!" + Fore.RESET)
                            break
                        else:
                            print(Fore.RED + 'A data inserida é anterior à data atual. Insira uma data futura.' + Fore.RESET)
                    else:
                        print(Fore.RED + 'Formato inválido! Entre com uma data válida no formato DD/MM/AAAA.' + Fore.RESET)
                    
            elif escolha == "4":
                while True:
                    novo_estado = input("A tarefa está concluída (1-Sim/2-Não)? ")
                    estado_uni = unidecode(novo_estado.lower())
                    if estado_uni in ["sim", "1", "1-sim"]:
                        data.loc[linha_tarefa.index, 'Estado'] = "Finalizada"
                        print(Fore.GREEN + "Estado da tarefa atualizado com sucesso!" + Fore.RESET)
                        break
                    elif estado_uni in ["nao", "2", "2-nao"]:
                        data.loc[linha_tarefa.index, 'Estado'] = "Não finalizada"
                        print(Fore.GREEN + "Estado da tarefa atualizado com sucesso!" + Fore.RESET)
                        break
                    else:
                        print(Fore.RED + "Opção inválida! Digite 'Sim', 'Não', '1', '2', '1-Sim' ou '2-Não'." + Fore.RESET)

            elif escolha == "5":
                novo_titulo = input("Digite o novo título da tarefa: ")
                nova_descricao = input("Digite a nova descrição da tarefa: ")
                nova_data = input("Qual a data limite para essa tarefa (DD/MM/AAAA): ")

                while True:
                    novo_estado = input("A tarefa está concluída (1-Sim/2-Não)? ").strip().lower()
                    estado_uni = unidecode(novo_estado)
                    if estado_uni in ["sim", "1", "1-sim"]:
                        estado = "Finalizada"
                        data.loc[linha_tarefa.index, 'Estado'] = estado
                        print(Fore.GREEN + f"Estado da tarefa atualizado para '{estado}' com sucesso!" + Fore.RESET)
                        break
                    elif estado_uni in ["nao", "2", "2-nao"]:
                        estado = "Não finalizada"
                        data.loc[linha_tarefa.index, 'Estado'] = estado
                        print(Fore.GREEN + f"Estado da tarefa atualizado para '{estado}' com sucesso!" + Fore.RESET)
                        break
                    else:
                        print(Fore.RED + "Opção inválida! Digite 'Sim', 'Não', '1', '2', '1-Sim' ou '2-Não'." + Fore.RESET)

                if re.match(r'\d{2}/\d{2}/\d{4}', nova_data):
                    data_atual = datetime.now().strftime("%d/%m/%Y")
                    nova_data_obj = datetime.strptime(nova_data, "%d/%m/%Y")
                    if nova_data_obj >= datetime.strptime(data_atual, "%d/%m/%Y"):
                        data.loc[linha_tarefa.index, 'Tarefa'] = novo_titulo
                        data.loc[linha_tarefa.index, 'Descrição'] = nova_descricao
                        data.loc[linha_tarefa.index, 'Vencimento'] = nova_data
                        print(Fore.GREEN + "Tarefa atualizada com sucesso!" + Fore.RESET)
                    else:
                        print(Fore.RED + 'A data inserida é anterior à data atual. Insira uma data futura.' + Fore.RESET)
                else:
                    print(Fore.RED + 'Formato inválido! Entre com uma data válida no formato DD/MM/AAAA.' + Fore.RESET)

                    
            elif escolha == "6":
                print(Fore.YELLOW + "Edição cancelada pelo usuário." + Fore.RESET)
            else:
                print(Fore.RED + "Opção inválida! Escolha um número de 1 a 6." + Fore.RESET)

            data.to_csv('dados.csv', index=False, header=False)
            
        else:
            print(Fore.YELLOW + "Tarefa não encontrada." + Fore.RESET)
    
    menu()
    return


def excluir_tarefa():
    nome_colunas = ["Núm. Registro", "Tarefa", "Descrição", "Vencimento", "Estado"]
    data = pd.read_csv('dados.csv', header=None, names=nome_colunas)
    
    resumo_tarefas()

    num_nome = input("Digite o número ou nome da tarefa que deseja excluir: ")

    linha_tarefa = encontrar_tarefa(data, num_nome)

    if linha_tarefa is not None:
        print(Fore.YELLOW + "Tarefa encontrada!")
        
        linha_tarefa_str = linha_tarefa.astype(str)
        col_widths = {col: max(linha_tarefa_str[col].str.len().max(), len(col)) + 2 for col in linha_tarefa_str.columns}
        format_dict = {col: "{{:<{}}}".format(width).format for col, width in col_widths.items()}
        
        formatted_row = " | ".join([format_dict[col](linha_tarefa_str.iloc[0][col]) for col in linha_tarefa_str.columns])
        
        print(Fore.BLUE + "-" * len(formatted_row))
        print(Fore.BLUE + formatted_row)
        print(Fore.BLUE + "-" * len(formatted_row) + Style.RESET_ALL)

        while True:
            confirmacao = input("Tem certeza que deseja excluir esta tarefa? (Sim/Não): ")
            uni_confirma = unidecode(confirmacao.lower())
            if uni_confirma == "sim" or uni_confirma == "1" or uni_confirma == "1-sim":
                data = data.drop(linha_tarefa.index)
                data.to_csv('dados.csv', index=False, header=False)
                print(Fore.YELLOW + "Tarefa excluída com sucesso!" + Style.RESET_ALL)
                break
            elif uni_confirma == "nao" or uni_confirma == "2" or uni_confirma == "2-nao":
                print(Fore.YELLOW + "Operação de exclusão cancelada." + Style.RESET_ALL)
                break
            else:
                print("Opção inválida! Tente novamente!")
                continue
        else:
            print(Fore.YELLOW + "Tarefa não encontrada." + Style.RESET_ALL)
    menu()
    return

    
if __name__ == "__main__":
    main()


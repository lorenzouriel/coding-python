import xlsxwriter

def create_server_specifications_excel(file_name):
    # Cria um arquivo Excel
    workbook = xlsxwriter.Workbook(file_name)

    # Aba para especificações dos servidores
    worksheet_servers = workbook.add_worksheet("Servidores")
    headers_servers = [
        "Nome do Servidor",
        "IP",
        "MAC Address",
        "Modelo do Servidor",
        "Fabricante",
        "Tipo da Placa-Mãe",
        "Quantidade de CPUs",
        "Memória RAM (GB)",
        "Capacidade de Armazenamento (GB)",
        "Localização Física",
        "Status",
        "Data de Aquisição",
        "Responsável pelo Servidor",
        "VLAN",
        "Configuração RAID",
        "Sistema Operacional Instalado"
    ]
    for col_num, header in enumerate(headers_servers):
        worksheet_servers.write(0, col_num, header)
    for col_num, header in enumerate(headers_servers):
        worksheet_servers.set_column(col_num, col_num, max(len(header) + 2, 15))

    # Aba para HDs
    worksheet_hds = workbook.add_worksheet("HDs")
    headers_hds = [
        "ID do HD",
        "Modelo",
        "Capacidade (GB)",
        "Tipo (HDD/SSD)",
        "Servidor Associado"
    ]
    for col_num, header in enumerate(headers_hds):
        worksheet_hds.write(0, col_num, header)
    for col_num, header in enumerate(headers_hds):
        worksheet_hds.set_column(col_num, col_num, max(len(header) + 2, 15))

    # Aba para Memórias RAM
    worksheet_ram = workbook.add_worksheet("Memórias RAM")
    headers_ram = [
        "ID da Memória",
        "Modelo",
        "Capacidade (GB)",
        "Frequência (MHz)",
        "Servidor Associado"
    ]
    for col_num, header in enumerate(headers_ram):
        worksheet_ram.write(0, col_num, header)
    for col_num, header in enumerate(headers_ram):
        worksheet_ram.set_column(col_num, col_num, max(len(header) + 2, 15))

    # Fecha o arquivo Excel
    workbook.close()
    print(f"Arquivo Excel '{file_name}' criado com sucesso!")

# Nome do arquivo Excel
file_name = "especificacoes_servidores.xlsx"

# Chama a função para criar o arquivo Excel
create_server_specifications_excel(file_name)
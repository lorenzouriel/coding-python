# The while loop is a fundamental flow control structure in Python, allowing you to execute a block of code repeatedly while a specified condition evaluates to True. 
# In data engineering, the use of while can be extremely useful for several tasks, such as continuous monitoring of data sources, executing ETL (Extract, Transform, Load) 
# processes until there is no more data to process, or even implementing automatic reconnection attempts to services or databases when the first attempt fails.

dados = []
entrada = ""
while entrada.lower() != "sair":
    entrada = input("Digite um valor (ou 'sair' para terminar): ")
from typing import List

def calculate_median(valores: List[float]) -> float:
    return sum(valores)  / len(valores)

values = [1, 2, 3, 4, 5]
calculate = calculate_median(values) 
print(calculate)
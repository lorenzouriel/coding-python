transaction = {'value': 12000, 'hour': 20}

if transaction['value'] > 10000 or transaction['hour'] < 9 or transaction['hour'] > 18:
    print("Suspicious transaction")
else:
    print("Normal transaction")
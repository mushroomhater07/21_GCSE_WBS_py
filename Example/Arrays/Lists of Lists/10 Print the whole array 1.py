temps = [["Month","January","February","March","April"],["London","5.9°C","6.0°C","8.0°C","9.9°C"],["Cardiff","4.8°C","4.7°C","6.5°C","8.2°C"],["Edinburgh","3.6°C","3.9°C","5.5°C","7.3°C"]]

for indexA in range(5):
  for indexB in range(len(temps)):
    print(temps[indexB][indexA])

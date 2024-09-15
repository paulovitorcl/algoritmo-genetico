import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('analysis_results.csv')

plt.figure(figsize=(10, 6))
for method in df['selection_method'].unique():
    subset = df[df['selection_method'] == method]
    plt.plot(subset['crossover_method'] + ' - ' + subset['mutation_method'] + ' - ' + subset['reinsertion_method'],
             subset['average_time'],
             label=method)

plt.xlabel('Configuração')
plt.ylabel('Tempo Médio de Execução')
plt.title('Tempo Médio de Execução por Configuração')
plt.xticks(rotation=90)
plt.legend()
plt.tight_layout()
plt.savefig('execution_time_comparison.png')
plt.show()

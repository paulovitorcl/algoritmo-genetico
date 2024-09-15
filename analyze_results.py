import pandas as pd

def analyze_results(filename):
    df = pd.read_csv(filename)
    
    # Calcule o percentual de convergência e tempo médio de execução
    analysis = df.groupby(['selection_method', 'crossover_method', 'mutation_method', 'reinsertion_method']).agg(
        convergence_rate=('converged', lambda x: (x.sum() / len(x)) * 100),
        average_time=('execution_time', 'mean')
    ).reset_index()
    
    # Salve a análise em um novo arquivo CSV
    analysis.to_csv('analysis_results.csv', index=False)
    print("Análise concluída e salva em 'analysis_results.csv'")

if __name__ == "__main__":
    analyze_results('experiments_results.csv')

import pandas as pd
import sys

def analyze_results(input_filenames, output_filename):
    all_data = []

    for filename in input_filenames:
        df = pd.read_csv(filename)
        df['source_file'] = filename  # Adiciona a coluna com o nome do arquivo
        all_data.append(df)

    combined_df = pd.concat(all_data, ignore_index=True)

    # Calcule o percentual de convergência e tempo médio de execução por problema e arquivo
    analysis = combined_df.groupby(['source_file', 'problem']).agg(
        convergence_rate=('converged', lambda x: (x.sum() / len(x)) * 100),
        average_time=('execution_time', 'mean')
    ).reset_index()

    # Salve a análise em um novo arquivo CSV
    analysis.to_csv(output_filename, index=False)
    print(f"Análise concluída e salva em '{output_filename}'")

if __name__ == "__main__":
    input_filenames = ['resultados_2/results.csv', 'resultados_2/results_2.csv', 'resultados_2/results_3.csv', 'resultados_2/results_4.csv', 'resultados_2/results_5.csv']
    output_filename = 'resultados_2/analysis_output_2.csv'
    analyze_results(input_filenames, output_filename)

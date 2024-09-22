import pandas as pd
import sys

def analyze_results(input_filename, output_filename):
    df = pd.read_csv(input_filename)

    # Calcule o percentual de convergência e tempo médio de execução por problema
    analysis = df.groupby('problem').agg(
        convergence_rate=('converged', lambda x: (x.sum() / len(x)) * 100),
        average_time=('execution_time', 'mean')
    ).reset_index()

    # Salve a análise em um novo arquivo CSV
    analysis.to_csv(output_filename, index=False)
    print(f"Análise concluída e salva em '{output_filename}'")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script_name.py <input_filename> <output_filename>")
        sys.exit(1)
    input_filename = sys.argv[1]
    output_filename = sys.argv[2]
    analyze_results(input_filename, output_filename)

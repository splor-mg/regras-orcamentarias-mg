from tests.demo.helper import load_json, evaluate_df
import zen
import pandas as pd

def main():
    
    # OBS: carregar o motor apenas uma vez [ver seção boas práticas - https://docs.gorules.io/developers/sdks/python#best-practices]
    engine = zen.ZenEngine({"loader": load_json})


    # ------------------------------------------------------------
    # BATCH EVALUATION
    # engine.evaluate = testar apenas um caso
    # evaluate_batch = testar uma lista de casos

    results = engine.evaluate_batch([
    {"key": "pasep_demo", "context": {"ano": 2026, "acao_cod": 7663}},
    {"key": "pasep_demo", "context": {"ano": 2026, "acao_cod": 7663, "elemento_item_cod": 4706}}
    ])
    
    print("------------------------------------------------------------")
    print("EXEMPLO 1 --> BATCH EVALUATION")
    count = 0
    for result in results:
        if result["success"]:
            print(f"case {count}: {result["data"]["result"]["pasep"]}")
        else:
            print(f"case {count}: Evaluation failed -", result["error"])
        count += 1


    # ------------------------------------------------------------
    # A ORDEM IMPORTA

    print("------------------------------------------------------------")    
    print("\nEXEMPLO 2 --> A ORDEM IMPORTA")

    result = engine.evaluate("asps_demo", {
    "ano": 2026,
    "funcao_cod": 10,
    "uo_cod": 1451,
    "fonte_cod": 10,
    "modalidade_cod": 90,
    "elemento_item_cod": 3501,
    "elemento_cod": 35
    })
    print(f"case {count}: asps_demo.json - asps {result["result"]["asps"]}")
    count += 1

    result = engine.evaluate("asps_demo_wrong", {
    "ano": 2026,
    "funcao_cod": 10,
    "uo_cod": 1451,
    "fonte_cod": 10,
    "modalidade_cod": 90,
    "elemento_item_cod": 3501,
    "elemento_cod": 35
    })
    print(f"case {count}: asps_demo_wrong.json - asps {result["result"]["asps"]}")

    # ------------------------------------------------------------
    # AVALIAR PLANILHAS
    
    print("------------------------------------------------------------")
    print("\nEXEMPLO 3 --> AVALIAR PLANILHAS")

    print("\nPerformance CSV x EXCEL")
    results = evaluate_df('tests/demo/exec_desp_EI.csv', engine, key='asps_demo')
    print(f"CSV: {results[1]}")
    results = evaluate_df('tests/demo/exec_desp_EI.xlsx', engine, key='asps_demo')
    print(f"EXCEL: {results[1]}")


    print("\nASPS COM EI")
    results = evaluate_df('tests/demo/exec_desp_EI.csv', engine, key='asps_demo')
    expected = pd.read_csv('tests/demo/asps_relatorios_EI.csv')

    #results vs expected - coluna ASPS
    results_s = results[0]['asps']
    expected_s = expected['ASPS']
    df_comp = pd.DataFrame({
        'Resultados (results)': results_s,
        'Esperado (expected)': expected_s
    })
    divergencias = df_comp[df_comp['Resultados (results)'] != df_comp['Esperado (expected)']]
    print(f"Total de linhas divergentes: {len(divergencias)}")
    print("\nAbaixo estão as divergências (mostrando as primeiras 20):")
    print(divergencias.head(20))




if __name__ == '__main__':
    main()

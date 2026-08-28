import time
from pathlib import Path

import pandas as pd
import zen

DEMO_DIR = Path(__file__).resolve().parent
_COMPILED = {}


def load_json(key: str):
    # Pré-compilar evita reparsear o JDM a cada linha do batch.
    if key not in _COMPILED:
        path = DEMO_DIR / f'{key}.json'
        _COMPILED[key] = zen.ZenDecisionContent(path.read_text(encoding='utf-8'))
    return _COMPILED[key]


def evaluate_df(path, engine, key):
    t0 = time.perf_counter()

    if path.endswith('.csv'):
        df = pd.read_csv(path)
    elif path.endswith('csv.gz'):
        df = pd.read_csv(path, compression='gzip')
    elif path.endswith(('.xlsx', '.xls')):
        df = pd.read_excel(path)
    else:
        raise ValueError(f'Formato de arquivo não suportado: {path}')
    t_read = time.perf_counter()

    # adaptação temporária - uso base DCAF
    df.columns = [str(c).lower() for c in df.columns]

    rows = df.to_dict(orient='records')
    requests = [{'key': key, 'context': row} for row in rows]
    t_prep = time.perf_counter()

    results = engine.evaluate_batch(requests)
    t_eval = time.perf_counter()

    results_dicts = [result['data']['result'] for result in results]
    results_df = pd.DataFrame(results_dicts)
    t_end = time.perf_counter()

    n = len(rows)
    performance = (
        f'evaluate_df ({n} linhas): '
        f'leitura {t_read - t0:.2f}s | '
        f'preparo {t_prep - t_read:.2f}s | '
        f'regras {t_eval - t_prep:.2f}s | '
        f'dataframe {t_end - t_eval:.2f}s | '
        f'total {t_end - t0:.2f}s'
    )

    return [results_df, performance]

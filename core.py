import pandas as pd
import consts

def preprocess_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """Limpia nombres de columnas y asegura tipos de datos."""
    df.columns = [c.strip() for c in df.columns]
    # Asegurar que el ID es el índice
    if consts.COL_ID in df.columns:
        df[consts.COL_ID] = df[consts.COL_ID].astype(int)
        df = df.set_index(consts.COL_ID)
    return df

def get_binary_matrix(df: pd.DataFrame) -> pd.DataFrame:
    """Genera la matriz binaria basada en las columnas de días definidas en consts."""
    matrix = {}
    # Solo procesamos las columnas que figuran como días en nuestras constantes
    valid_days = [c for c in df.columns if c in consts.DAYS_COLUMNS]
    
    for day in valid_days:
        day_data = df[day].fillna("").astype(str)
        # Extraemos slots únicos presentes en los datos
        found_slots = {s.strip() for line in day_data for s in line.split(';') if s.strip()}
        
        for slot in sorted(found_slots):
            matrix[f"{day}_{slot}"] = day_data.apply(lambda x: 1 if slot in x else 0)
            
    return pd.DataFrame(matrix)

def get_stats(df_bin: pd.DataFrame):
    """Métricas de depuración."""
    density = df_bin.sum(axis=1).sort_values().astype(int)
    # Pandas 3.0 grouping por prefijo de columna
    day_freq = df_bin.T.groupby(lambda x: x.split('_')[0]).sum().T.sum().sort_values(ascending=False)
    slot_freq = df_bin.sum().sort_values(ascending=False)
    return density, day_freq, slot_freq

def find_groups_greedy(df_bin: pd.DataFrame, n: int) -> tuple[list[dict], list[int]]:
    """Selección iterativa de grupos basada en máxima coincidencia."""
    remaining_ids = list(df_bin.index)
    groups = []

    for i in range(n):
        if not remaining_ids or df_bin.loc[remaining_ids].sum().max() == 0:
            break
        
        current_view = df_bin.loc[remaining_ids]
        best_slot = current_view.sum().idxmax()
        matched_ids = current_view[current_view[best_slot] == 1].index.tolist()
        
        day_info = best_slot.split('_', 1)
        groups.append({
            "Grupo": i + 1,
            "Día": day_info[0],
            "Slot": day_info[1] if len(day_info) > 1 else "",
            "Nº": len(matched_ids),
            "IDs": ";".join(map(str, sorted(matched_ids)))
        })
        
        remaining_ids = [idx for idx in remaining_ids if idx not in matched_ids]
        
    return groups, remaining_ids

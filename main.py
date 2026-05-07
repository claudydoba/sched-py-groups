import sys
import consts
import core
import utils
import pandas as pd

def run_analysis(file_path: str):
    log = utils.setup_logger()
    
    # 1. Ingesta
    log.info(f"Cargando datos desde: {file_path}")
    raw_df = utils.load_csv(file_path)
    df_clean = core.preprocess_dataframe(raw_df)
    
    # 2. Transformación
    df_bin = core.get_binary_matrix(df_clean)
    
    # 3. Depuración y Calidad
    density, day_f, slot_f = core.get_stats(df_bin)
    
    utils.log_section(log, "Ranking de disponibilidad por ID", density)
    
    restrictive = density[density < consts.MIN_DENSITY_THRESHOLD].index.tolist()
    if restrictive:
        log.warning(f"IDs con disponibilidad crítica ( < {consts.MIN_DENSITY_THRESHOLD} slots): {restrictive}")
    
    utils.log_section(log, "Frecuencia de Slots", slot_f.head(10))

    # 4. Cálculo
    groups, leftovers = core.find_groups_greedy(df_bin, n=consts.DEFAULT_N_GROUPS)
    
    # 5. Salida
    utils.log_section(log, "Propuesta de Grupos", pd.DataFrame(groups))
    
    if leftovers:
        log.warning(f"Personas sin asignar: {leftovers}")

if __name__ == "__main__":
    # Puedes pasar el path como argumento: python main.py datos.csv
    input_file = sys.argv[1] if len(sys.argv) > 1 else "disponibilidad.csv"
    run_analysis(input_file)



import io
import pandas as pd

def main():
    print("Hello from sched-py-groups!")

    # 1. Entrada de datos
    data = """Id | Monday | Tuesday | Wednesday | Thursday | Friday
    8 | Midday: 11:10-13:10 | Midday: 11:10-13:10 | Midday: 11:10-13:10 | Midday: 11:10-13:10 | Morning: 9:00-11:00
    9 | Morning: 9:00-11:00 | Afternoon: 14:00-16:00 | Afternoon: 14:00-16:00 | Afternoon: 14:00-16:00 | Midday: 11:10-13:10
    10 | Morning: 9:00-11:00;Midday: 11:10-13:10;Afternoon: 14:00-16:00 | Morning: 9:00-11:00;Afternoon: 14:00-16:00 | Morning: 9:00-11:00;Midday: 11:10-13:10;Afternoon: 14:00-16:00 | Morning: 9:00-11:00;Midday: 11:10-13:10;Afternoon: 14:00-16:00 | Morning: 9:00-11:00;Midday: 11:10-13:10
    11 | Morning: 9:00-11:00;Midday: 11:10-13:10;Afternoon: 14:00-16:00;Late Afternoon: 16:10-18:10 | Morning: 9:00-11:00;Midday: 11:10-13:10;Afternoon: 14:00-16:00;Late Afternoon: 16:10-18:10 | Morning: 9:00-11:00;Midday: 11:10-13:10;Afternoon: 14:00-16:00;Late Afternoon: 16:10-18:10 | Morning: 9:00-11:00;Midday: 11:10-13:10;Afternoon: 14:00-16:00;Late Afternoon: 16:10-18:10 | Morning: 9:00-11:00;Midday: 11:10-13:10
    12 | Morning: 9:00-11:00;Midday: 11:10-13:10;Afternoon: 14:00-16:00;Late Afternoon: 16:10-18:10 | Morning: 9:00-11:00;Midday: 11:10-13:10;Afternoon: 14:00-16:00;Late Afternoon: 16:10-18:10 | Morning: 9:00-11:00;Midday: 11:10-13:10;Afternoon: 14:00-16:00;Late Afternoon: 16:10-18:10 | Morning: 9:00-11:00;Midday: 11:10-13:10;Afternoon: 14:00-16:00;Late Afternoon: 16:10-18:10 | Morning: 9:00-11:00;Midday: 11:10-13:10
    13 | Morning: 9:00-11:00;Midday: 11:10-13:10;Afternoon: 14:00-16:00 | Midday: 11:10-13:10;Afternoon: 14:00-16:00 | Morning: 9:00-11:00;Midday: 11:10-13:10 | Afternoon: 14:00-16:00 | Morning: 9:00-11:00;Midday: 11:10-13:10
    14 | Morning: 9:00-11:00;Midday: 11:10-13:10 | Morning: 9:00-11:00;Midday: 11:10-13:10 | Morning: 9:00-11:00;Midday: 11:10-13:10 | Morning: 9:00-11:00;Midday: 11:10-13:10 | Morning: 9:00-11:00;Midday: 11:10-13:10
    15 | Morning: 9:00-11:00 | | Morning: 9:00-11:00 | | 
    16 | Morning: 9:00-11:00;Midday: 11:10-13:10;Afternoon: 14:00-16:00 | | | Morning: 9:00-11:00;Midday: 11:10-13:10;Afternoon: 14:00-16:00;Late Afternoon: 16:10-18:10 | Morning: 9:00-11:00;Midday: 11:10-13:10
    17 | Midday: 11:10-13:10;Morning: 9:00-11:00 | Midday: 11:10-13:10;Morning: 9:00-11:00 | Midday: 11:10-13:10;Morning: 9:00-11:00 | Midday: 11:10-13:10;Morning: 9:00-11:00 | Midday: 11:10-13:10;Morning: 9:00-11:00
    18 | Midday: 11:10-13:10 | Midday: 11:10-13:10 | Midday: 11:10-13:10 | Midday: 11:10-13:10 | Midday: 11:10-13:10
    19 | Morning: 9:00-11:00;Midday: 11:10-13:10 | Morning: 9:00-11:00;Midday: 11:10-13:10 | Midday: 11:10-13:10;Morning: 9:00-11:00 | Morning: 9:00-11:00;Midday: 11:10-13:10 | Morning: 9:00-11:00;Midday: 11:10-13:10
    20 | Late Afternoon: 16:10-18:10 | Late Afternoon: 16:10-18:10 | Late Afternoon: 16:10-18:10 | Late Afternoon: 16:10-18:10 | Midday: 11:10-13:10
    21 | Morning: 9:00-11:00;Midday: 11:10-13:10 | | Morning: 9:00-11:00;Midday: 11:10-13:10 | Morning: 9:00-11:00;Midday: 11:10-13:10 | Morning: 9:00-11:00;Midday: 11:10-13:10
    22 | | Midday: 11:10-13:10 | Midday: 11:10-13:10 | Midday: 11:10-13:10 | 
    23 | Late Afternoon: 16:10-18:10;Morning: 9:00-11:00;Midday: 11:10-13:10;Afternoon: 14:00-16:00 | Morning: 9:00-11:00;Midday: 11:10-13:10;Afternoon: 14:00-16:00;Late Afternoon: 16:10-18:10 | Morning: 9:00-11:00;Midday: 11:10-13:10;Afternoon: 14:00-16:00;Late Afternoon: 16:10-18:10 | Afternoon: 14:00-16:00;Late Afternoon: 16:10-18:10;Morning: 9:00-11:00;Midday: 11:10-13:10 | Morning: 9:00-11:00;Midday: 11:10-13:10
    24 | Morning: 9:00-11:00;Midday: 11:10-13:10;Late Afternoon: 16:10-18:10 | Morning: 9:00-11:00;Midday: 11:10-13:10;Afternoon: 14:00-16:00;Late Afternoon: 16:10-18:10 | Morning: 9:00-11:00;Midday: 11:10-13:10 | Afternoon: 14:00-16:00;Late Afternoon: 16:10-18:10 | 
    25 | Midday: 11:10-13:10;Morning: 9:00-11:00;Afternoon: 14:00-16:00 | Morning: 9:00-11:00;Midday: 11:10-13:10;Afternoon: 14:00-16:00 | Morning: 9:00-11:00;Midday: 11:10-13:10;Afternoon: 14:00-16:00 | Morning: 9:00-11:00;Midday: 11:10-13:10;Afternoon: 14:00-16:00 | Morning: 9:00-11:00;Midday: 11:10-13:10
    26 | Afternoon: 14:00-16:00 | Afternoon: 14:00-16:00 | Afternoon: 14:00-16:00 | Afternoon: 14:00-16:00 | Midday: 11:10-13:10
    27 | Morning: 9:00-11:00;Afternoon: 14:00-16:00 | Morning: 9:00-11:00;Afternoon: 14:00-16:00 | Afternoon: 14:00-16:00 | Morning: 9:00-11:00;Afternoon: 14:00-16:00 | 
    28 | Morning: 9:00-11:00;Late Afternoon: 16:10-18:10 | Morning: 9:00-11:00;Late Afternoon: 16:10-18:10 | Morning: 9:00-11:00;Late Afternoon: 16:10-18:10 | Late Afternoon: 16:10-18:10 | 
    29 | Late Afternoon: 16:10-18:10 | | | | Midday: 11:10-13:10
    30 | Midday: 11:10-13:10;Late Afternoon: 16:10-18:10 | Midday: 11:10-13:10;Late Afternoon: 16:10-18:10 | Midday: 11:10-13:10;Late Afternoon: 16:10-18:10 | Midday: 11:10-13:10;Late Afternoon: 16:10-18:10 | Midday: 11:10-13:10
    32 | Midday: 11:10-13:10;Afternoon: 14:00-16:00 | Midday: 11:10-13:10;Afternoon: 14:00-16:00 | Midday: 11:10-13:10;Afternoon: 14:00-16:00 | Midday: 11:10-13:10;Afternoon: 14:00-16:00 | Midday: 11:10-13:10
    33 | Midday: 11:10-13:10 | Morning: 9:00-11:00;Midday: 11:10-13:10 | Morning: 9:00-11:00;Midday: 11:10-13:10;Late Afternoon: 16:10-18:10 | Morning: 9:00-11:00;Midday: 11:10-13:10 | 
    34 | Afternoon: 14:00-16:00;Late Afternoon: 16:10-18:10 | Late Afternoon: 16:10-18:10 | Afternoon: 14:00-16:00;Late Afternoon: 16:10-18:10 | Late Afternoon: 16:10-18:10 | 
    35 | | Late Afternoon: 16:10-18:10 | | Late Afternoon: 16:10-18:10 | 
    36 | Midday: 11:10-13:10 | Midday: 11:10-13:10;Morning: 9:00-11:00 | Midday: 11:10-13:10 | Morning: 9:00-11:00;Midday: 11:10-13:10 | Midday: 11:10-13:10
    37 | Late Afternoon: 16:10-18:10 | Late Afternoon: 16:10-18:10 | Late Afternoon: 16:10-18:10 | Late Afternoon: 16:10-18:10 | Morning: 9:00-11:00;Midday: 11:10-13:10
    38 | Midday: 11:10-13:10 | Afternoon: 14:00-16:00 | Midday: 11:10-13:10 | Late Afternoon: 16:10-18:10 | Midday: 11:10-13:10
    39 | Afternoon: 14:00-16:00;Midday: 11:10-13:10 | Midday: 11:10-13:10;Afternoon: 14:00-16:00 | Midday: 11:10-13:10;Afternoon: 14:00-16:00 | Midday: 11:10-13:10;Afternoon: 14:00-16:00 | Midday: 11:10-13:10
    """

    # Limpiar y cargar
    df_input = pd.read_csv(io.StringIO(data), sep="|", skipinitialspace=True).dropna(axis=1, how='all')
    df_input.columns = [c.strip() for c in df_input.columns]
    df_input.set_index('Id', inplace=True)

    # --- 1. Identificación de Restricciones por Persona ---
    print("--- DEBUG: Disponibilidad Total por Persona (nº de slots) ---")
    # Contamos cuántas veces aparece un separador ';' o una franja en cada celda
    def count_slots(row):
        total = 0
        for cell in row:
            if pd.isna(cell) or cell.strip() == "": continue
            total += len([s for s in cell.split(';') if s.strip()])
        return total

    person_density = df_input.apply(count_slots, axis=1).sort_values()
    print(person_density)
    print(f"\nAlerta: IDs con menos de 3 slots totales: {person_density[person_density < 3].index.tolist()}\n")


    # --- 2. Transformación a Matriz Binaria ---
    binary_data = {}
    for day in df_input.columns:
        all_slots = set()
        df_input[day].fillna("").apply(lambda x: [all_slots.add(s.strip()) for s in x.split(';') if s.strip()])
        for slot in sorted(all_slots):
            col_name = f"{day}_{slot}"
            binary_data[col_name] = df_input[day].fillna("").apply(lambda x: 1 if slot in x else 0)

    df_binary = pd.DataFrame(binary_data)

    # --- 3. Frecuencias ---
    print("--- DEBUG: Frecuencias por Binomio (Día_Franja) ---")
    print(df_binary.sum().sort_values(ascending=False))
    print("\n--- DEBUG: Frecuencias por Día ---")
    print(df_binary.groupby(lambda x: x.split('_')[0], axis=1).sum().sum().sort_values(ascending=False))
    print("\n")


    # --- 4. Algoritmo de Búsqueda ---
    def find_best_groups(df, n_groups=3):
        remaining_people = set(df.index)
        results = []
        
        for i in range(1, n_groups + 1):
            if not remaining_people: break
            
            current_df = df.loc[list(remaining_people)]
            best_slot = current_df.sum().idxmax()
            people_in_group = current_df[current_df[best_slot] == 1].index.tolist()
            
            day, time = best_slot.split('_', 1)
            results.append({
                "Grupo": f"Grupo {i}",
                "Día y horario": f"{day} {time}",
                "Nº participantes": len(people_in_group),
                "IDs": ";".join(map(str, sorted(people_in_group)))
            })
            remaining_people -= set(people_in_group)
            
        return pd.DataFrame(results), remaining_people

    final_groups, leftovers = find_best_groups(df_binary)

    # 5. Salida Final
    print("--- RESULTADO FINAL ---")
    print(final_groups.to_string(index=False))

    if leftovers:
        print(f"\nIDs sin grupo asignado: {';'.join(map(str, leftovers))}")

if __name__ == "__main__":
    main()

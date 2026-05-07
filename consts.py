"""
Constantes de dominio para el procesamiento de disponibilidad.
"""

# Cabeceras esperadas en el CSV de entrada
COL_ID = "Id"
COL_MON = "Monday"
COL_TUE = "Tuesday"
COL_WED = "Wednesday"
COL_THU = "Thursday"
COL_FRI = "Friday"

DAYS_COLUMNS = [COL_MON, COL_TUE, COL_WED, COL_THU, COL_FRI]

# Identificadores de franjas horarias (para normalización o filtrado)
SLOT_MORNING = "Morning: 9:00-11:00"
SLOT_MIDDAY = "Midday: 11:10-13:10"
SLOT_AFTERNOON = "Afternoon: 14:00-16:00"
SLOT_LATE_AFTERNOON = "Late Afternoon: 16:10-18:10"

ALL_VALID_SLOTS = [
    SLOT_MORNING,
    SLOT_MIDDAY,
    SLOT_AFTERNOON,
    SLOT_LATE_AFTERNOON
]

# Configuración del algoritmo
DEFAULT_N_GROUPS = 3
MIN_DENSITY_THRESHOLD = 3

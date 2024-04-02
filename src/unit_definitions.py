import libsbml as ls

# Unit definitions, translating a unit string to the elementary unit
# compositions following the SBML structure.
# Unit IDs should match up with vocabulary of QUDT (https://qudt.org/2.1/vocab/unit) 
# except that the '-' character is replaced by '_' due to restrictions of SBML.
UnitDefinitions = [
    {
        "id" : "UNITLESS",
        "qudt" : "UNITLESS",
        "synonyms" : [
            "unitless",
            "dimensionless"
        ],
        "units": [
            { "kind": ls.UNIT_KIND_DIMENSIONLESS, "exponent": 1, "multiplier": 1, "scale": 0 }
        ]
    },
    # Amount/volume units
    {
        "id" : "MOL",
        "qudt" : "MOL",
        "synonyms" : [
            "mol"
        ],
        "units": [
            { "kind": ls.UNIT_KIND_MOLE, "exponent": 1, "multiplier": 1, "scale": 0 }
        ]
    },
    {
        "id" : "MilliMOL",
        "qudt" : "MilliMOL",
        "synonyms" : [
            "mmol"
        ],
        "units": [
            { "kind": ls.UNIT_KIND_MOLE, "exponent": 1, "multiplier": 1, "scale": -3 }
        ]
    },
    {
        "id" : "KiloGM",
        "qudt" : "KiloGM",
        "synonyms" : [
            "kg"
        ],
        "units": [
            { "kind": ls.UNIT_KIND_GRAM, "exponent": 1, "multiplier": 1, "scale": 3 }
        ]
    },
    {
        "id" : "GM",
        "qudt" : "GM",
        "synonyms" : [
            "g"
        ],
        "units": [
            { "kind": ls.UNIT_KIND_GRAM, "exponent": 1, "multiplier": 1, "scale": 0 }
        ]
    },
    {
        "id" : "MilliGM",
        "qudt" : "MilliGM",
        "synonyms" : [
            "mg"
        ],
        "units": [
            { "kind": ls.UNIT_KIND_GRAM, "exponent": 1, "multiplier": 1, "scale": -3 }
        ]
    },
    {
        "id" : "MicroGM",
        "qudt" : "MicroGM",
        "synonyms" : [
            "ug"
        ],
        "units": [
            { "kind": ls.UNIT_KIND_GRAM, "exponent": 1, "multiplier": 1, "scale": -6 }
        ]
    },
    {
        "id" : "L",
        "qudt" : "L",
        "synonyms" : [
            "L"
        ],
        "units": [
            { "kind": ls.UNIT_KIND_LITRE, "exponent": 1, "multiplier": 1, "scale": 0 }
        ]
    },
    {
        "id" : "MilliL",
        "qudt" : "MilliL",
        "synonyms" : [
            "mL"
        ],
        "units": [
            { "kind": ls.UNIT_KIND_LITRE, "exponent": 1, "multiplier": 1, "scale": -3 }
        ]
    },
    # Concentration units
    {
        "id" : "MicroGM_PER_KiloGM",
        "qudt" : "MicroGM-PER-KiloGM",
        "synonyms" : [
            "ug/kg",
            "ug_per_kg"
        ],
        "units": [
            { "kind": ls.UNIT_KIND_GRAM, "exponent": 1, "multiplier": 1, "scale": -6 },
            { "kind": ls.UNIT_KIND_GRAM, "exponent": -1, "multiplier": 1, "scale": 3 }
        ]
    },
    {
        "id" : "MilliGM_PER_KiloGM",
        "qudt" : "MilliGM-PER-KiloGM",
        "synonyms" : [
            "mg/kg",
            "mg_per_kg"
        ],
        "units": [
            { "kind": ls.UNIT_KIND_GRAM, "exponent": 1, "multiplier": 1, "scale": -3 },
            { "kind": ls.UNIT_KIND_GRAM, "exponent": -1, "multiplier": 1, "scale": 3 }
        ]
    },
    {
        "id" : "GM_PER_KiloGM",
        "qudt" : "GM-PER-KiloGM",
        "synonyms" : [
            "g/kg",
            "g_per_kg"
        ],
        "units": [
            { "kind": ls.UNIT_KIND_GRAM, "exponent": 1, "multiplier": 1, "scale": 0 },
            { "kind": ls.UNIT_KIND_GRAM, "exponent": -1, "multiplier": 1, "scale": 3 }
        ]
    },
    {
        "id" : "MicroGM_PER_GM",
        "qudt" : "MicroGM-PER-GM",
        "synonyms" : [
            "ug/g",
            "ug_per_g"
        ],
        "units": [
            { "kind": ls.UNIT_KIND_GRAM, "exponent": 1, "multiplier": 1, "scale": -6 },
            { "kind": ls.UNIT_KIND_GRAM, "exponent": -1, "multiplier": 1, "scale": 0 }
        ]
    },
    {
        "id" : "MilliGM_PER_GM",
        "qudt" : "MilliGM-PER-GM",
        "synonyms" : [
            "mg/g",
            "mg_per_g"
        ],
        "units": [
            { "kind": ls.UNIT_KIND_GRAM, "exponent": 1, "multiplier": 1, "scale": -3 },
            { "kind": ls.UNIT_KIND_GRAM, "exponent": -1, "multiplier": 1, "scale": 0 }
        ]
    },
    {
        "id" : "GM_PER_GM",
        "qudt" : "GM-PER-GM",
        "synonyms" : [
            "g/g",
            "g_per_g"
        ],
        "units": [
            { "kind": ls.UNIT_KIND_GRAM, "exponent": 1, "multiplier": 1, "scale": 0 },
            { "kind": ls.UNIT_KIND_GRAM, "exponent": -1, "multiplier": 1, "scale": 0 }
        ]
    },
    {
        "id" : "MicroGM_PER_L",
        "qudt" : "MicroGM-PER-L",
        "synonyms" : [
            "ug_per_L",
            "ug/L"
        ],
        "units": [
            { "kind": ls.UNIT_KIND_GRAM, "exponent": 1, "multiplier": 1, "scale": -6 },
            { "kind": ls.UNIT_KIND_LITRE, "exponent": -1, "multiplier": 1, "scale": 0 }
        ]
    },
    {
        "id" : "MilliGM_PER_L",
        "qudt" : "MilliGM-PER-L",
        "synonyms" : [
            "mg_per_L",
            "mg/L"
        ],
        "units": [
            { "kind": ls.UNIT_KIND_GRAM, "exponent": 1, "multiplier": 1, "scale": -3 },
            { "kind": ls.UNIT_KIND_LITRE, "exponent": -1, "multiplier": 1, "scale": 0 }
        ]
    },
    {
        "id" : "GM_PER_L",
        "qudt" : "GM-PER-L",
        "synonyms" : [
            "g_per_L",
            "g/L"
        ],
        "units": [
            { "kind": ls.UNIT_KIND_GRAM, "exponent": 1, "multiplier": 1, "scale": 0 },
            { "kind": ls.UNIT_KIND_LITRE, "exponent": -1, "multiplier": 1, "scale": 0 }
        ]
    },
    {
        "id" : "MOL_PER_L",
        "qudt" : "MOL-PER-L",
        "synonyms" : [
            "mol_per_L",
            "mol/L"
        ],
        "units": [
            { "kind": ls.UNIT_KIND_MOLE, "exponent": 1, "multiplier": 1, "scale": 0 },
            { "kind": ls.UNIT_KIND_LITRE, "exponent": -1, "multiplier": 1, "scale": 0 }
        ]
    },
    {
        "id" : "MilliMOL_PER_L",
        "qudt" : "MilliMOL-PER-L",
        "synonyms" : [
            "mmol_per_L",
            "mmol/L"
        ],
        "units": [
            { "kind": ls.UNIT_KIND_MOLE, "exponent": 1, "multiplier": 1, "scale": -3 },
            { "kind": ls.UNIT_KIND_LITRE, "exponent": -1, "multiplier": 1, "scale": 0 }
        ]
    },
    # Time units
    {
        "id" : "SEC",
        "qudt" : "SEC",
        "synonyms" : [
            "seconds",
            "s"
        ],
        "units": [
            { "kind": ls.UNIT_KIND_SECOND, "exponent": 1, "multiplier": 1, "scale": 0 }
        ]
    },
    {
        "id" : "HR",
        "qudt" : "HR",
        "synonyms" : [
            "hours",
            "h"
        ],
        "units": [
            { "kind": ls.UNIT_KIND_SECOND, "exponent": 1, "multiplier": 3600, "scale": 0 }
        ]
    },
    {
        "id" : "DAY",
        "qudt" : "DAY",
        "synonyms" : [
            "days",
            "d"
        ],
        "units": [
            { "kind": ls.UNIT_KIND_SECOND, "exponent": 1, "multiplier": 24 * 3600, "scale": 0 }
        ]
    },
    # Rate units
    {
        "id" : "PER_SEC",
        "qudt" : "PER-SEC",
        "synonyms" : [
            "per_second",
            "1/sec",
            "1/s",
            "s-1"
        ],
        "units": [
            { "kind": ls.UNIT_KIND_SECOND, "exponent": -1, "multiplier": 1, "scale": 1 }
        ]
    },
    {
        "id" : "PER_H",
        "qudt" : "PER-H",
        "synonyms" : [
            "per_hour",
            "1/h",
            "h-1"
        ],
        "units": [
            { "kind": ls.UNIT_KIND_SECOND, "exponent": -1, "multiplier": 3600, "scale": 1 }
        ]
    },
    {
        "id" : "PER_DAY",
        "qudt" : "PER-DAY",
        "synonyms" : [
            "per_day",
            "1/day",
            "1/d",
            "d-1"
        ],
        "units": [
            { "kind": ls.UNIT_KIND_SECOND, "exponent": -1, "multiplier": 24 * 3600, "scale": 1 }
        ]
    },
    {
        "id" : "MilliMOL_PER_HR",
        "qudt" : "MilliMOL-PER-HR",
        "synonyms" : [
            "mmol_per_hour",
            "mmol/h"
        ],
        "units": [
            { "kind": ls.UNIT_KIND_MOLE, "exponent": 1, "multiplier": 1, "scale": -3 },
            { "kind": ls.UNIT_KIND_SECOND, "exponent": -1, "multiplier": 3600, "scale": 1 }
        ]
    },
    {
        "id" : "MOL_PER_HR",
        "qudt" : "MOL-PER-HR",
        "synonyms" : [
            "mol/h",
            "mol_per_hour"
        ],
        "units": [
            { "kind": ls.UNIT_KIND_MOLE, "exponent": 1, "multiplier": 1, "scale": 0 },
            { "kind": ls.UNIT_KIND_SECOND, "exponent": -1, "multiplier": 3600, "scale": 1 }
        ]
    },
    {
        "id" : "L_PER_HR",
        "qudt" : "L-PER-HR",
        "synonyms" : [
            "L_per_h",
            "L/h",
            "L.h-1"
        ],
        "units": [
            { "kind": ls.UNIT_KIND_LITRE, "exponent": 1, "multiplier": 1, "scale": 0 },
            { "kind": ls.UNIT_KIND_SECOND, "exponent": -1, "multiplier": 3600, "scale": 1 }
        ]
    },
    {
        "id" : "DeciM_PER_HR",
        "qudt" : "DeciM-PER-HR",
        "synonyms" : [
            "dm_per_hour",
            "dm/h",
            "dm.h-1"
        ],
        "units": [
            { "kind": ls.UNIT_KIND_METRE, "exponent": 1, "multiplier": 1, "scale": -1 },
            { "kind": ls.UNIT_KIND_SECOND, "exponent": -1, "multiplier": 3600, "scale": 1 }
        ]
    },
    # Rate per mass units
    {
        "id" : "L_PER_KiloGM_HR",
        "qudt" : "L-PER-KiloGM-HR",
        "synonyms" : [
            "L_per_kg_h",
            "L.kg-1.h-1"
        ],
        "units": [
            { "kind": ls.UNIT_KIND_LITRE, "exponent": 1, "multiplier": 1, "scale": 0 },
            { "kind": ls.UNIT_KIND_SECOND, "exponent": -1, "multiplier": 3600, "scale": 1 },
            { "kind": ls.UNIT_KIND_GRAM, "exponent": -1, "multiplier": 1, "scale": 3 },
        ]
    },
    {
        "id" : "MilliMOL_PER_L_HR",
        "qudt" : "MilliMOL-PER-L-HR",
        "synonyms" : [
            "mM_per_L_h",
            "mM.L-1.h-1"
        ],
        "units": [
            { "kind": ls.UNIT_KIND_MOLE, "exponent": 1, "multiplier": 1, "scale": -3 },
            { "kind": ls.UNIT_KIND_SECOND, "exponent": -1, "multiplier": 3600, "scale": 1 },
            { "kind": ls.UNIT_KIND_LITRE, "exponent": -1, "multiplier": 1, "scale": 3 },
        ]
    },
    # Area units
    {
        "id" : "DeciM2",
        "qudt" : "DeciM2",
        "synonyms" : [
            "dm_square",
            "dm^2",
            "dm2"
        ],
        "units": [
            { "kind": ls.UNIT_KIND_METRE, "exponent": 2, "multiplier": 1, "scale": -1 },
        ]
    },
    # Length units
    {
        "id" : "DeciM",
        "qudt" : "DeciM",
        "synonyms" : [
            "dm"
        ],
        "units": [
            { "kind": ls.UNIT_KIND_METRE, "exponent": 1, "multiplier": 1, "scale": -1 },
        ]
    }
]

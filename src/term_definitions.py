import libsbml as ls

TermDefinitions = [
    # Model terms: species
    {
        "name": "mammals",
        "element_type": "model",
        "description": "Model for mammals (mammalia).",
        "synonyms": [
            "mammalia",
            "mammals"
        ],
        "resources": [
            {
                "qualifier": "bqbiol:hasTaxon",
                "URI": "taxonomy/40674"
            }
        ]
    },
    {
        "name": "human",
        "element_type": "model",
        "description": "Model for human (homo sapiens).",
        "synonyms": [
            "homo sapiens",
            "human"
        ],
        "resources": [
            {
                "qualifier": "bqbiol:hasTaxon",
                "URI": "taxonomy/9606"
            }
        ]
    },
    # Compartment terms
    {
        "name": "adipose tissue",
        "element_type": "compartment",
        "description": "Adipose tissue (fat) compartment.",
        "recommended_id": "Fat",
        "synonyms": [
            "fat",
            "adipose tissue"
        ],
        "resources": [
            {
                "qualifier": "bqbiol:is",
                "URI": "uberon/UBERON:0001013"
            }
        ]
    },
    {
        "name": "arterial blood",
        "element_type": "compartment",
        "recommended_id": "Art",
        "description": "Arterial blood compartment.",
        "synonyms": [
            "arterial blood",
            "art"
        ],
        "resources": [
            {
                "qualifier": "bqbiol:is",
                "URI": "uberon/UBERON:0013755"
            }
        ]
    },
    {
        "name": "arterial blood plasma",
        "element_type": "compartment",
        "recommended_id": "Art_Plasma",
        "description": "Arterial blood plasma compartment.",
        "synonyms": [
            "Art_Plas"
            "arterial blood plasma"
        ]
    },
    {
        "name": "blood",
        "element_type": "compartment",
        "recommended_id": "Blood",
        "description": "Blood compartment.",
        "synonyms": [
            "plasma"
        ],
        "resources": [
            {
                "qualifier": "bqbiol:is",
                "URI": "uberon/UBERON:0000178"
            }
        ]
    },
    {
        "name": "blood plasma",
        "element_type": "compartment",
        "recommended_id": "Plasma",
        "description": "Blood plasma compartment.",
        "synonyms": [
            "blood plasma"
        ],
        "resources": [
            {
                "qualifier": "bqbiol:is",
                "URI": "uberon/UBERON:0001969"
            }
        ]
    },
    {
        "name": "epidermis",
        "element_type": "compartment",
        "recommended_id": "Epidermis",
        "description": "Epidermis compartment.",
        "synonyms": [
            "epidermis",
            "skin epidermis"
        ]
    },
    {
        "name": "filtrate",
        "element_type": "compartment",
        "recommended_id": "Filtrate",
        "description": "Filtrate compartment.",
        "synonyms": [
            "filtrate",
            "fil"
        ]
    },
    {
        "name": "gut",
        "element_type": "compartment",
        "recommended_id": "Gut",
        "description": "Gut (digestive tract) compartment.",
        "synonyms": [
            "gut",
            "digestive tract"
        ],
        "resources": [
            {
                "qualifier": "bqbiol:is",
                "URI": "uberon/UBERON:0001555"
            }
        ]
    },
    {
        "name": "kidney",
        "element_type": "compartment",
        "recommended_id": "Kidney",
        "description": "Kidney compartment.",
        "synonyms": [
            "kidney",
            "kid"
        ]
    },
    {
        "name": "liver",
        "element_type": "compartment",
        "recommended_id": "Liver",
        "description": "Liver compartment.",
        "synonyms": [
            "liver",
            "liv"
        ],
        "resources": [
            {
                "qualifier": "bqbiol:is",
                "URI": "uberon/UBERON:0002107"
            }
        ]
    },
    {
        "name": "lung",
        "element_type": "compartment",
        "recommended_id": "Lung",
        "description": "Lung compartment.",
        "synonyms": [
            "lung",
            "lungs"
        ]
    },
    {
        "name": "poorly perfused tissue",
        "element_type": "compartment",
        "recommended_id": "Poor",
        "description": "Poorly perfused tissue compartment.",
        "synonyms": [
            "poorly perfused tissue"
        ]
    },
    {
        "name": "rest-of-body",
        "element_type": "compartment",
        "description": "Rest-of-body compartment.",
        "recommended_id": "Rest",
        "synonyms": [
            "rest-of-body",
            "rest",
            "periphery"
        ]
    },
    {
        "name": "richly perfused tissue",
        "element_type": "compartment",
        "description": "Richly perfused tissue compartment.",
        "recommended_id": "Rich",
        "synonyms": [
            "richly perfused tissue"
        ]
    },
    {
        "name": "skin",
        "element_type": "compartment",
        "recommended_id": "Skin",
        "description": "Skin compartment.",
        "synonyms": [
            "skin"
        ],
        "resources": [
            {
                "qualifier": "bqbiol:is",
                "URI": "uberon/UBERON:0002097"
            }
        ]
    },
    {
        "name": "stratum corneum",
        "element_type": "compartment",
        "recommended_id": "SC",
        "description": "Stratum corneum compartment.",
        "synonyms": [
            "stratum corneum"
        ]
    },
    {
        "name": "urine",
        "element_type": "compartment",
        "recommended_id": "Urine",
        "description": "Urine compartment.",
        "synonyms": [
            "urine"
        ]
    },
    {
        "name": "venous blood",
        "element_type": "compartment",
        "recommended_id": "Ven",
        "description": "Venous blood compartment.",
        "synonyms": [
            "venous blood"
        ],
        "resources": [
            {
                "qualifier": "bqbiol:is",
                "URI": "uberon/UBERON:0013756"
            }
        ]
    },
    {
        "name": "venous blood plasma",
        "element_type": "compartment",
        "recommended_id": "Ven_Plasma",
        "description": "Venous blood plasma compartment.",
        "synonyms": [
            "Ven_Plas",
            "venous blood plasma"
        ],
        "resources": [
            {
                "qualifier": "bqbiol:is",
                "URI": "obo/NCIT_C132462"
            }
        ]
    },
    {
        "name": "viable epidermis",
        "element_type": "compartment",
        "recommended_id": "VE",
        "description": "Viable epidermis compartment.",
        "synonyms": [
            "viable epidermis"
        ]
    },
    # Species terms
    {
        "name": "metabolite",
        "element_type": "species",
        "description": "Species is a metabolite.",
        "synonyms": [
            "metabolite"
        ],
        "resources": [
            {
                "qualifier": "bqbiol:is",
                "URI": "http://identifiers.org/CHEBI:25212"
            }
        ]
    },
    {
        "name": "simple chemical",
        "element_type": "species",
        "description": "Species is a simple chemical.",
        "synonyms": [
            "simple chemical"
        ],
        "resources": [
            {
                "qualifier": "bqbiol:is",
                "URI": "sbo/SBO:0000247"
            }
        ]
    },
    # Parameters
    {
        "name": "body mass",
        "element_type": "parameter",
        "recommended_id": "BW",
        "description": "Body mass (or body weight) parameter.",
        "synonyms": [
            "BM",
            "BW",
            "body mass",
            "body weight"
        ],
        "resources": [
            {
                "qualifier": "bqbiol:is",
                "URI": "http://purl.obolibrary.org/obo/NCIT_C81328"
            },
            {
                "qualifier": "bqbiol:is",
                "URI": "http://purl.obolibrary.org/obo/CMO_0000012"
            }
        ]
    },
    {
        "name": "body surface area",
        "element_type": "parameter",
        "recommended_id": "BSA",
        "description": "Body surface area (BSA) parameter.",
        "synonyms": [
            "BSA",
            "body surface area"
        ],
        "resources": [
            {
                "qualifier": "bqbiol:is",
                "URI": "http://purl.obolibrary.org/obo/NCIT_C25157"
            }
        ]
    },
    {
        "name": "cardiac blood output",
        "recommended_id": "QCC",
        "element_type": "parameter",
        "description": "Cardiac blood output.",
        "synonyms": [
            "QCC"
        ]
    },
    {
        "name": "molar weight",
        "recommended_id": "MW",
        "element_type": "parameter",
        "description": "Molecular weight.",
        "synonyms": [
            "MW"
        ]
    }
]

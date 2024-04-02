import libsbml as ls

TermDefinitions = [
    # Model terms
    {
        "name": "mammals",
        "element_type": "model",
        "description": "Model for mammals (mammalia).",
        "synonyms": [
            "mammalia",
            "mammals"
        ],
        "bqbiol": "hasTaxon",
        "resources": [
            "taxonomy/40674"
        ]
    },
    {
        "name": "mammals",
        "element_type": "model",
        "description": "Model for human (homo sapiens).",
        "synonyms": [
            "homo sapiens",
            "human"
        ],
        "bqbiol": "hasTaxon",
        "resources": [
            "taxonomy/40674"
        ]
    },
    # Compartment terms
    {
        "name": "adipose tissue",
        "element_type": "compartment",
        "description": "Adipose tissue (fat) compartment.",
        "bqbiol": "is",
        "synonyms": [
            "fat",
            "adipose tissue"
        ],
        "resources": [
            "uberon/UBERON:0001013"
        ]
    },
    {
        "name": "liver",
        "element_type": "compartment",
        "description": "Liver compartment.",
        "bqbiol": "is",
        "synonyms": [
            "liver"
        ],
        "resources": [
            "uberon/UBERON:0002107"
        ]
    },
    {
        "name": "gut",
        "element_type": "compartment",
        "description": "Gut (digestive tract) compartment.",
        "bqbiol": "is",
        "synonyms": [
            "gut",
            "digestive tract"
        ],
        "resources": [
            "uberon/UBERON:0001555"
        ]
    },
    # Species terms
    {
        "name": "metabolite",
        "element_type": "species",
        "description": "Species is a metabolite.",
        "bqbiol": "is",
        "synonyms": [
            "metabolite"
        ],
        "resources": [
            "http://identifiers.org/CHEBI:25212"
        ]
    },
    {
        "name": "simple chemical",
        "element_type": "species",
        "description": "Species is a simple chemical.",
        "bqbiol": "is",
        "synonyms": [
            "simple chemical"
        ],
        "resources": [
            "sbo/SBO:0000247"
        ]
    },
    # Parameters
    {
        "name": "body mass",
        "element_type": "parameter",
        "description": "Body mass (or body weight) parameter.",
        "bqbiol": "is",
        "synonyms": [
            "BM",
            "BW",
            "body mass",
            "body weight"
        ],
        "resources": [
            "http://purl.obolibrary.org/obo/NCIT_C81328",
            "http://purl.obolibrary.org/obo/CMO_0000012"
        ]
    },
    {
        "name": "body surface area",
        "element_type": "parameter",
        "description": "Body surface area (BSA) parameter.",
        "bqbiol": "is",
        "synonyms": [
            "BSA",
            "body surface area"
        ],
        "resources": [
            "http://purl.obolibrary.org/obo/NCIT_C25157"
        ]
    }
]

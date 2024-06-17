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
        "recommended_id": "Art_Plas",
        "description": "Arterial blood plasma compartment.",
        "synonyms": [
            "Art_Plas",
            "Art_Plasma",
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
        "recommended_id": "Ven_Plas",
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
    # Parameters: physiological
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
        "description": "Cardiac blood output as a function of body weight.",
        "synonyms": [
            "QCC"
        ]
    },
    # Parameters: physiological - compartment volumes
    {
        "name": "alveolar volume",
        "element_type": "parameter",
        "recommended_id": "VAlv",
        "description": "Alveolar volume.",
        "synonyms": [
            "VAlv"
        ]
    },
    {
        "name": "arterial blood plasma volume",
        "element_type": "parameter",
        "recommended_id": "VArt_Plas",
        "description": "Volume of arterial blood plasma.",
        "synonyms": [
            "VArt_Plas",
            "VArt_Plasma"
        ]
    },
    {
        "name": "fat volume",
        "element_type": "parameter",
        "recommended_id": "VFat",
        "description": "Volume of adipose tissue or fat compartment.",
        "synonyms": [
            "VFat",
            "VF"
        ]
    },
    {
        "name": "gut volume",
        "element_type": "parameter",
        "recommended_id": "VGut",
        "description": "Volume of the gut.",
        "synonyms": [
            "VGut",
            "VG"
        ]
    },
    {
        "name": "kidney volume",
        "element_type": "parameter",
        "recommended_id": "VKidney",
        "description": "Volume of kidney compartment.",
        "synonyms": [
            "VKidney",
            "VK"
        ]
    },
    {
        "name": "liver volume",
        "element_type": "parameter",
        "recommended_id": "VLiver",
        "description": "Volume of liver compartment.",
        "synonyms": [
            "VLiver",
            "VL"
        ]
    },
    {
        "name": "lung volume",
        "element_type": "parameter",
        "recommended_id": "VLung",
        "description": "Volume of the lung compartment.",
        "synonyms": [
            "VLung",
            "VLun"
        ]
    },
    {
        "name": "plasma volume",
        "element_type": "parameter",
        "recommended_id": "VPlasma",
        "description": "Volume of blood plasma.",
        "synonyms": [
            "VPlasma",
            "VPlas"
        ]
    },
    {
        "name": "rest-of-body volume",
        "element_type": "parameter",
        "recommended_id": "VRest",
        "description": "Volume of rest-of-body compartment.",
        "synonyms": [
            "VRest",
            "VR"
        ]
    },
    {
        "name": "skin volume",
        "element_type": "parameter",
        "recommended_id": "VSkin",
        "description": "Volume of skin.",
        "synonyms": [
            "VSkin",
            "VSk"
        ]
    },
    {
        "name": "stratum corneum volume",
        "element_type": "parameter",
        "recommended_id": "VSC",
        "description": "Volume of stratum corneum.",
        "synonyms": [
            "VSC"
        ]
    },
    {
        "name": "venous blood plasma volume",
        "element_type": "parameter",
        "recommended_id": "VVen_Plas",
        "description": "Volume of blood plasma.",
        "synonyms": [
            "VVen_Plas",
            "VVen_Plasma"
        ]
    },
    {
        "name": "viable epidermis corneum volume",
        "element_type": "parameter",
        "recommended_id": "VVE",
        "description": "Volume of viable epidermis.",
        "synonyms": [
            "VVE"
        ]
    },
    # Parameters: chemical
    {
        "name": "molar weight",
        "recommended_id": "MW",
        "element_type": "parameter",
        "description": "Molecular weight.",
        "synonyms": [
            "MW"
        ]
    },
    {
        "name": "logP",
        "element_type": "parameter",
        "recommended_id": "logP",
        "description": "logP descriptor.",
        "synonyms": [
            "logP"
        ],
        "resources": [
            {
                "qualifier": "bqbiol:is",
                "URI": "http://semanticscience.org/resource/CHEMINF_000251"
            }
        ]
    },
    # Parameters: chemical - partition coefficients
    {
        "name": "partition coefficient fat/plasma",
        "element_type": "parameter",
        "recommended_id": "PC_Fat_Plas",
        "description": "Partition coefficient fat/plasma.",
        "synonyms": [
            "PF",
            "PC_Fat_Plas",
            "PC_Fat_Plasma"
        ]
    },
    {
        "name": "partition coefficient gut/plasma",
        "element_type": "parameter",
        "recommended_id": "PC_Gut_Plas",
        "description": "Partition coefficient gut/plasma.",
        "synonyms": [
            "PG",
            "PC_Git_Plas",
            "PC_Gut_Plasma"
        ]
    },
    {
        "name": "partition coefficient kidney/plasma",
        "element_type": "parameter",
        "recommended_id": "PC_Kid_Plas",
        "description": "Partition coefficient kidney/plasma.",
        "synonyms": [
            "PK",
            "PC_Kid_Plas",
            "PC_Kidney_Plasma"
        ]
    },
    {
        "name": "partition coefficient liver/plasma",
        "element_type": "parameter",
        "recommended_id": "PC_Liv_Plas",
        "description": "Partition coefficient liver/plasma.",
        "synonyms": [
            "PL",
            "PC_Liv_Plas",
            "PC_Liver_Plasma"
        ]
    },
    {
        "name": "partition coefficient lung/plasma",
        "element_type": "parameter",
        "recommended_id": "PC_Lun_Plas",
        "description": "Partition coefficient lung/plasma.",
        "synonyms": [
            "PLun",
            "PC_Lun_Plas",
            "PC_Lun_Plasma"
        ]
    },
    {
        "name": "partition coefficient rest-of-body/plasma",
        "element_type": "parameter",
        "recommended_id": "PC_Rest_Plas",
        "description": "Partition coefficient rest-of-body/plasma.",
        "synonyms": [
            "PR",
            "PC_Rest_Plas",
            "PC_Rest_Plasma"
        ]
    },
    {
        "name": "partition coefficient skin/plasma",
        "element_type": "parameter",
        "recommended_id": "PC_Skin_Plas",
        "description": "Partition coefficient skin/plasma.",
        "synonyms": [
            "PSk",
            "PC_Skin_Plas",
            "PC_Skin_Plasma"
        ]
    }
]

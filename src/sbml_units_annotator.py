import libsbml as ls
import numpy as np
from sbmlutils.metadata.annotator import ModelAnnotator, ExternalAnnotation, annotate_sbml_doc
from sbmlutils.log import get_logger
from unit_definitions import UnitDefinitions
from typing import List

logger = get_logger(__name__)

class sbmlUnitsAnnotator:

    def annotateUnits(
        self,
        sbml_file,
        annotations_file,
        out_file
    ):
        """Annotate the units of the SBML file using the annotations
        file and write results to the specified out file."""

        # Open SBML document using libSBML
        document = ls.readSBML(sbml_file)
        model = document.getModel()

        # Read annotations file
        df = ModelAnnotator.read_annotations_df(annotations_file)
        df = df.replace(np.nan, None)

        # Read model units
        unitsDictionary = dict()
        for unitDef in model.getListOfUnitDefinitions():
            unitsDictionary[unitDef.getId()] = unitDef

        # Iterate over annotation records
        for index, row in df.iterrows():
            elementId = str(row["element_id"])
            if (elementId):
                if (row["unit"] is not None):
                    self.setElementUnit(
                        document,
                        row["element_id"],
                        row["sbml_type"],
                        row["unit"],
                        unitsDictionary
                    )
                
                if ("element_description" in row \
                    and row["element_description"] is not None):
                    self.setElementName(
                        document,
                        row["element_id"],
                        row["sbml_type"],
                        row["element_description"],
                        True
                    )

        # Annotate model terms if URI field is set
        if ('URI' in df.columns):
            df = df[df['URI'].notnull()]
            if (not 'pattern' in df.columns):
                df['pattern'] = df['element_id'] 
            if (not 'annotation_type' in df.columns):
                df['annotation_type'] = 'rdf'
            if (not 'qualifier' in df.columns):
                df['qualifier'] = 'BQB_IS'
            if (not 'resource' in df.columns):
                df['resource'] = df['URI']

            entries = df.to_dict("records")
            annotations = []
            for entry in entries:
                annotations.append(ExternalAnnotation(entry))
            annotate_sbml_doc(document, annotations)

        # Write SBML file
        logger.info(f"Writing SBML to file [{out_file}].")
        ls.writeSBML(document, out_file)

    def findUnitDefinition(self, str):
        """Find unit definition matching the provided string."""
        res = None
        for index, value in enumerate(UnitDefinitions):
            if any(val.lower() == str.lower() for val in value['synonyms']):
                res = value
                break
        return res

    def setElementUnit(
        self,
        doc,
        elementId,
        elementType,
        unitId,
        unitsDictionary
    ):
        """Set element unit of element with specified id and type to the specfied unit."""
        if (elementType == "document"):
            model = doc.getModel()
            uDef = self.getOrAddUnitDefinition(doc, unitId, unitsDictionary)
            if (elementId == "timeUnits" and not model.isSetTimeUnits()):
                model.setTimeUnits(uDef.getId())
            elif (elementId == "substanceUnits" and not model.isSetSubstanceUnits()):
                model.setSubstanceUnits(uDef.getId())
            elif (elementId == "volumeUnits" and not model.isSetVolumeUnits()):
                model.setVolumeUnits(uDef.getId())
        elif (elementId):
            el = doc.getElementBySId(elementId)
            if (el is None):
                logger.error(f"Cannot set unit [{unitId}] for {elementType} [{elementId}]: element not found!")
                return
            if (not el.isSetUnits()):
                uDef = self.getOrAddUnitDefinition(doc, unitId, unitsDictionary)
                if (uDef):
                    logger.info(f"Setting unit [{unitId}] for {elementType} [{elementId}].")
                    el.setUnits(uDef.getId())

    def setElementName(
        self,
        doc,
        elementId,
        elementType,
        name,
        overwrite
    ):
        """Set element unit of element with specified id and type to the specfied unit."""
        el = doc.getElementBySId(elementId)
        if (el is None):
            logger.error(f"Cannot set name for {elementType} [{elementId}]: element not found!")
            return
        if not el.isSetName() or overwrite:
            el.setName(name)

    def getOrAddUnitDefinition(self, doc, unitId, unitsDictionary):
        if (unitId not in unitsDictionary):
            unitDef = self.findUnitDefinition(unitId)
            if (unitDef is None):
                logger.error(f"Cannot set unit [{unitId}]: unknown unit definition!")
                return
            model = doc.getModel()
            uDef = model.getUnitDefinition(unitDef["id"])
            if (not uDef):
                unitDefId = unitDef["id"]
                logger.info(f"Adding unit definition [{unitDefId}] for [{unitId}]")
                uDef = model.createUnitDefinition()
                uDef.setId(unitDefId)
                for unitPart in unitDef["units"]:
                    u = uDef.createUnit()
                    u.setKind(unitPart["kind"])
                    u.setExponent(unitPart["exponent"])
                    u.setMultiplier(unitPart["multiplier"])
                    u.setScale(unitPart["scale"])
            unitsDictionary[unitId] = uDef
        return unitsDictionary[unitId]

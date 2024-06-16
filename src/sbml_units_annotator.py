import libsbml as ls
import numpy as np
from sbmlutils.metadata.annotator import ModelAnnotator
from sbmlutils.log import get_logger
from unit_definitions import UnitDefinitions
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
            if (elementId and row["unit"] is not None):
                self.setElementUnit(
                    document,
                    row["element_id"],
                    row["sbml_type"],
                    row["unit"],
                    unitsDictionary
                )


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

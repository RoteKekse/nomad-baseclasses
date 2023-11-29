#
# Copyright The NOMAD Authors.
#
# This file is part of NOMAD. See https://nomad-lab.eu for further info.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import numpy as np

from nomad.metainfo import (Quantity, SubSection)
from nomad.datamodel.data import ArchiveSection

from . import WetChemicalDeposition


class DropCastingProperties(ArchiveSection):
    suspension_concentration = Quantity(
        type=np.dtype(
            np.float64),
        a_eln=dict(
            component='NumberEditQuantity'))

    dropcast_amount = Quantity(
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        #Link to ontology class 'volume', Link to ontology class 'volume setting datum'
        links = ['http://purl.obolibrary.org/obo/PATO_0000918', 'http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002158'],
=======
        #Link to class 'volume'
        links = ['http://purl.obolibrary.org/obo/PATO_0000918'],
        #Link to class 'volume setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002158'],
>>>>>>> 93909fc (Added links in files dip coating, vaporization and dropcasting, dropcasting)
=======
        #Link to class 'volume', Link to class 'volume setting datum'
=======
        #Link to ontology class 'volume', Link to ontology class 'volume setting datum'
>>>>>>> 8794d04 (Updated 'Link to class' to 'Link to ontology class')
        links = ['http://purl.obolibrary.org/obo/PATO_0000918', 'http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002158'],
>>>>>>> 1916ad1 (Fixed double links)
=======
        #Link to ontology class 'volume', Link to ontology class 'volume setting datum'
        links = ['http://purl.obolibrary.org/obo/PATO_0000918', 'http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002158'],
>>>>>>> 273b34793553e64e4e271202f9f7bbff0e56ed58
        type=np.dtype(
            np.float64),
        unit=('ml'),
        a_eln=dict(
            component='NumberEditQuantity',
            defaultDisplayUnit='ml'))

    temperature = Quantity(
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        #Link to ontology class 'temperature', Link to ontology class 'temperature setting datum'
        links = ['http://purl.obolibrary.org/obo/PATO_0000146', 'http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002111'],
=======
        #Link to class 'temperature'
        links = ['http://purl.obolibrary.org/obo/PATO_0000146'],
        #Link to class 'temperature setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002111'],
>>>>>>> 93909fc (Added links in files dip coating, vaporization and dropcasting, dropcasting)
=======
        #Link to class 'temperature', Link to class 'temperature setting datum'
=======
        #Link to ontology class 'temperature', Link to ontology class 'temperature setting datum'
>>>>>>> 8794d04 (Updated 'Link to class' to 'Link to ontology class')
        links = ['http://purl.obolibrary.org/obo/PATO_0000146', 'http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002111'],
>>>>>>> 1916ad1 (Fixed double links)
=======
        #Link to ontology class 'temperature', Link to ontology class 'temperature setting datum'
        links = ['http://purl.obolibrary.org/obo/PATO_0000146', 'http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002111'],
>>>>>>> 273b34793553e64e4e271202f9f7bbff0e56ed58
        type=np.dtype(
            np.float64),
        unit=('°C'),
        a_eln=dict(
            component='NumberEditQuantity',
            defaultDisplayUnit='°C'))

    atmosphere = Quantity(
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        #Link to ontology class 'atmosphere'
=======
        #Link to class 'atmosphere'
>>>>>>> 93909fc (Added links in files dip coating, vaporization and dropcasting, dropcasting)
=======
        #Link to ontology class 'atmosphere'
>>>>>>> 8794d04 (Updated 'Link to class' to 'Link to ontology class')
=======
        #Link to ontology class 'atmosphere'
>>>>>>> 273b34793553e64e4e271202f9f7bbff0e56ed58
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00001012'],
        type=str,
        a_eln=dict(
            component='EnumEditQuantity',
            props=dict(suggestions=["N2O flow", "ambient"])
        ))


class DropCasting(WetChemicalDeposition):
    m_def = Section(
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        #Link to ontology class 'Drop casting'
=======
        #Link to class 'Drop casting'
>>>>>>> 93909fc (Added links in files dip coating, vaporization and dropcasting, dropcasting)
=======
        #Link to ontology class 'Drop casting'
>>>>>>> 8794d04 (Updated 'Link to class' to 'Link to ontology class')
=======
        #Link to ontology class 'Drop casting'
>>>>>>> 273b34793553e64e4e271202f9f7bbff0e56ed58
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002059'],
    )

    properties = SubSection(
        section_def=DropCastingProperties)

    def normalize(self, archive, logger):
        super(DropCasting,
              self).normalize(archive, logger)

        self.method = "Drop Casting"

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

from nomad.metainfo import (
    Quantity,
    SubSection,
    Datetime)
from nomad.datamodel.data import ArchiveSection

from .wet_chemical_deposition import WetChemicalDeposition


class VaporizationProperties(ArchiveSection):

    temperature = Quantity(
<<<<<<< HEAD
        #Link to ontology class 'temperature', Link to ontology class 'temperature setting datum'
        links = ['http://purl.obolibrary.org/obo/PATO_0000146', 'http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002111'],
=======
        #Link to class 'temperature'
        links = ['http://purl.obolibrary.org/obo/PATO_0000146'],
        #Link to class 'temperature setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002111'],
>>>>>>> 93909fc (Added links in files dip coating, vaporization and dropcasting, dropcasting)
        type=np.dtype(np.float64),
        unit=('°C'),
        a_eln=dict(component='NumberEditQuantity', defaultDisplayUnit='°C'))

    initial_time = Quantity(
<<<<<<< HEAD
        #Link to ontology class 'time', Link to ontology class 'time setting datum'
        links = ['http://purl.obolibrary.org/obo/PATO_0000165', 'http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005085'],
=======
        #Link to class 'time'
        links = ['http://purl.obolibrary.org/obo/PATO_0000165'],
>>>>>>> 93909fc (Added links in files dip coating, vaporization and dropcasting, dropcasting)
        type=Datetime,
        a_eln=dict(component='DateTimeEditQuantity'))


class VaporizationAndDropCasting(WetChemicalDeposition):
    '''Base class for spin coating of a sample'''
    m_def = Section(
<<<<<<< HEAD
        #Link to ontology class 'Drop casting'
=======
        #Link to class 'Drop casting'
>>>>>>> 30bb487 (Added link to drop casting in vaporization and dropcasting file)
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002059'],

    )

    properties = SubSection(
        section_def=VaporizationProperties, repeats=True)

    def normalize(self, archive, logger):
        super(VaporizationAndDropCasting, self).normalize(archive, logger)
        self.method = "Vaporization and Drop Casting"

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
    Reference,
    SubSection)

from nomad.datamodel.data import ArchiveSection

from .wet_chemical_deposition import WetChemicalDeposition
from ..material_processes_misc import Annealing


class SprayPyrolysisProperties(ArchiveSection):

    temperature = Quantity(
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
>>>>>>> 2bfcffa (First Commit, added links in files annealing, quenching, sintering, wet chemical depo, dip coating, spin coating, spray pyrolysis, slot die coating)
=======
        #Link to class 'temperature', Link to class 'temperature setting datum'
=======
        #Link to ontology class 'temperature', Link to ontology class 'temperature setting datum'
>>>>>>> 8794d04 (Updated 'Link to class' to 'Link to ontology class')
        links = ['http://purl.obolibrary.org/obo/PATO_0000146', 'http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002111'],
>>>>>>> 1916ad1 (Fixed double links)
        type=np.dtype(np.float64),
        unit=('°C'),
        a_eln=dict(component='NumberEditQuantity', defaultDisplayUnit='°C'))

    time = Quantity(
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        #Link to ontology class 'time', Link to ontology class 'time setting datum'
        links = ['http://purl.obolibrary.org/obo/PATO_0000165', 'http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005085'],
=======
        #Link to class 'process time'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00001063'],
        #Link to class 'process time setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002072'],
>>>>>>> 2bfcffa (First Commit, added links in files annealing, quenching, sintering, wet chemical depo, dip coating, spin coating, spray pyrolysis, slot die coating)
=======
        #Link to class 'process time', Link to class 'process time setting datum'
=======
        #Link to ontology class 'process time', Link to ontology class 'process time setting datum'
>>>>>>> 8794d04 (Updated 'Link to class' to 'Link to ontology class')
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00001063', 'http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002072'],
>>>>>>> 1916ad1 (Fixed double links)
        type=np.dtype(np.float64),
        unit=('minute'),
        a_eln=dict(component='NumberEditQuantity', defaultDisplayUnit='minute'))


class SprayPyrolysis(WetChemicalDeposition):
    '''Base class for spray pyrolysis of a sample'''
    m_def = Section(
<<<<<<< HEAD
<<<<<<< HEAD
        #Link to ontology class 'Spray pyrolysis'
=======
        #Link to Class 'Spray pyrolysis'
>>>>>>> 2bfcffa (First Commit, added links in files annealing, quenching, sintering, wet chemical depo, dip coating, spin coating, spray pyrolysis, slot die coating)
=======
        #Link to ontology class 'Spray pyrolysis'
>>>>>>> 8794d04 (Updated 'Link to class' to 'Link to ontology class')
        links = ['http://purl.obolibrary.org/obo/CHMO_0001516'],
    )

    properties = SubSection(section_def=SprayPyrolysisProperties)

    def normalize(self, archive, logger):
        super(SprayPyrolysis, self).normalize(archive, logger)

        self.method = "Spray Pyrolysis"

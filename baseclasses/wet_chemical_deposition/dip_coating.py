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
    Section,
    SubSection,
    Reference)
from nomad.datamodel.data import ArchiveSection


from .wet_chemical_deposition import WetChemicalDeposition


class DipCoatingProperties(ArchiveSection):

    time = Quantity(
<<<<<<< HEAD
<<<<<<< HEAD
        #Link to ontology class 'time', Link to ontology class 'time setting datum'
        links = ['http://purl.obolibrary.org/obo/PATO_0000165', 'http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005085'],
=======
        #Link zur Klasse 'process time'
=======
        #Link to class 'process time'
>>>>>>> ff6f4e2 (Corrected files from previous commit)
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00001063'],
        #Link to class 'process time setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002072'],
>>>>>>> 2bfcffa (First Commit, added links in files annealing, quenching, sintering, wet chemical depo, dip coating, spin coating, spray pyrolysis, slot die coating)
        type=np.dtype(
            np.float64),
        unit=('minute'),
        a_eln=dict(
            component='NumberEditQuantity',
            defaultDisplayUnit='minute',
            props=dict(
                minValue=0)))


class DipCoating(WetChemicalDeposition):
    '''Base class for spin coating of a sample'''
    m_def = Section(
<<<<<<< HEAD
        #Link to ontology class 'dip coating'
=======
        #Link to class 'dip coating'
>>>>>>> 2bfcffa (First Commit, added links in files annealing, quenching, sintering, wet chemical depo, dip coating, spin coating, spray pyrolysis, slot die coating)
        links = ['http://purl.obolibrary.org/obo/CHMO_0001471'],
        )

    properties = SubSection(
        section_def=DipCoatingProperties)

    def normalize(self, archive, logger):
        super(DipCoating, self).normalize(archive, logger)
        self.method = "Dip Coating"

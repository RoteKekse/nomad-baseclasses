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

from nomad.metainfo import (Quantity, Reference, SubSection)
from nomad.datamodel.data import ArchiveSection

from ..chemical import Chemical
from nomad.datamodel.metainfo.basesections import PubChemPureSubstanceSection
from .. import LayerDeposition


class PVDProcess(ArchiveSection):

    target = Quantity(
        #Link to ontology class 'pvd source'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002035'],
        type=Reference(Chemical.m_def),
        shape=['*'],
        a_eln=dict(component='ReferenceEditQuantity'))

    target_2 = SubSection(
        #Link to ontology class 'pvd source'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002035'],
        section_def=PubChemPureSubstanceSection, repeats=True)

    power = Quantity(
<<<<<<< HEAD
        #Link to ontology class 'power', Link to ontology class 'power setting datum'
=======
        #Link to class 'power', Link to class 'power setting datum'
>>>>>>> 46c0756 (Started adding links to vapour based deposition)
        links = ['http://purl.obolibrary.org/obo/PATO_0001024','http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002104'],
        type=np.dtype(
            np.float64),
        unit=('W'),
        a_eln=dict(
            component='NumberEditQuantity',
            defaultDisplayUnit='W',
            props=dict(
                minValue=0)))

    pressure = Quantity(
<<<<<<< HEAD
        #Link to ontology class 'pressure'
        links = ['http://purl.obolibrary.org/obo/PATO_0001025'],
=======
        #Link to class 'total pressure'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00001094'],
>>>>>>> 1a08f68 (Added further links to vapour based deposition (evaporation; pvd))
        type=np.dtype(
            np.float64),
        unit=('ubar'),
        a_eln=dict(
            component='NumberEditQuantity',
            defaultDisplayUnit='ubar',
            props=dict(
                minValue=0)))

    time = Quantity(
<<<<<<< HEAD
        #Link to ontology class 'time', Link to ontology class 'time setting datum'
        links = ['http://purl.obolibrary.org/obo/PATO_0000165', 'http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005085'],
=======
        #Link to class 'process time', Link to class 'process time setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00001063','http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002072'],
>>>>>>> 46c0756 (Started adding links to vapour based deposition)
        type=np.dtype(
            np.float64),
        unit=('s'),
        a_eln=dict(
            component='NumberEditQuantity',
            defaultDisplayUnit='s',
            props=dict(
                minValue=0)))

    rotation_speed = Quantity(
<<<<<<< HEAD
        #Link to ontology class 'Rotation speed', Link to ontology class 'rotation speed setting datum'
=======
        #Link to class 'Rotation speed', Link to class 'rotation speed setting datum'
>>>>>>> 1a08f68 (Added further links to vapour based deposition (evaporation; pvd))
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002026','http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002005'],
        type=np.dtype(np.float64),
        unit=('1/s'),
        a_eln=dict(component='NumberEditQuantity', defaultDisplayUnit='1/s'))

    temperature = Quantity(
<<<<<<< HEAD
        #Link to ontology class 'temperature', Link to ontology class 'temperature setting datum'
        links = ['http://purl.obolibrary.org/obo/PATO_0000146','http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002111'],
=======
        #Link to class 'substrate temperature', Link to class 'substrate temperature setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00009996','http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00009995'],
>>>>>>> 46c0756 (Started adding links to vapour based deposition)
        type=np.dtype(np.float64),
        unit=('°C'),
        a_eln=dict(component='NumberEditQuantity', defaultDisplayUnit='°C'))

    voltage = Quantity(
        type=np.dtype(
            np.float64),
        unit=('V'),
        a_eln=dict(
            component='NumberEditQuantity',
            defaultDisplayUnit='V'))


class PVDeposition(LayerDeposition):
    '''Base class for evaporation of a sample'''
    m_def = Section(
<<<<<<< HEAD
        #Link to ontology class 'physical vapour deposition'
=======
        #Link to class 'physical vapour deposition'
>>>>>>> 46c0756 (Started adding links to vapour based deposition)
        links = ['http://purl.obolibrary.org/obo/CHMO_0001356'],
    )

    process = SubSection(
        section_def=PVDProcess)

    def normalize(self, archive, logger):
        super(PVDeposition, self).normalize(archive, logger)

        self.method = "Physical Vapour Deposition"

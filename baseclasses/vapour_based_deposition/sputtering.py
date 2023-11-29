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

from nomad.datamodel.data import ArchiveSection
from nomad.metainfo import (Quantity, Reference, SubSection)

from ..chemical import Chemical
from .. import LayerDeposition
from nomad.datamodel.metainfo.basesections import PubChemPureSubstanceSection


class SputteringProcess(ArchiveSection):

    target = Quantity(
        #Link to ontology class 'pvd source'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002035'],
        type=Reference(Chemical.m_def),
        a_eln=dict(component='ReferenceEditQuantity'))

    target_2 = SubSection(
        #Link to ontology class 'pvd source'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002035'],
        section_def=PubChemPureSubstanceSection)

    thickness = Quantity(
        type=np.dtype(
            np.float64),
        unit=('nm'),
        a_eln=dict(
            component='NumberEditQuantity',
            defaultDisplayUnit='nm',
            props=dict(
                minValue=0)))

    gas = Quantity(
        #Link to ontology class 'chemical substance'
        links = ['http://purl.obolibrary.org/obo/CHEBI_59999'],
        type=Reference(Chemical.m_def),
        a_eln=dict(component='ReferenceEditQuantity'))

    source = Quantity(
        #Link to ontology class 'pvd source'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002035'],
        type=str,
        a_eln=dict(
            component='EnumEditQuantity',
            props=dict(
                suggestions=[
                    '1',
                    '2',
                    '3',
                    '4',
                ])))

    thickness = Quantity(
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        #Link to ontology class 'thickness'
=======
        #Link to class 'thickness'
>>>>>>> 26fa046 (added links to vapour based -> sputtering)
=======
        #Link to ontology class 'thickness'
>>>>>>> 8794d04 (Updated 'Link to class' to 'Link to ontology class')
=======
        #Link to ontology class 'thickness'
>>>>>>> 273b34793553e64e4e271202f9f7bbff0e56ed58
        links = ['http://purl.obolibrary.org/obo/PATO_0000915'],
        type=np.dtype(
            np.float64),
        unit=('nm'),
        a_eln=dict(
            component='NumberEditQuantity',
            defaultDisplayUnit='nm',
            props=dict(
                minValue=0)))

    pressure = Quantity(
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        #Link to ontology class 'pressure', Link to ontology class 'pressure setting datum'
=======
        #Link to class 'pressure', Link to class 'pressure setting datum'
>>>>>>> 26fa046 (added links to vapour based -> sputtering)
=======
        #Link to ontology class 'pressure', Link to ontology class 'pressure setting datum'
>>>>>>> 8794d04 (Updated 'Link to class' to 'Link to ontology class')
=======
        #Link to ontology class 'pressure', Link to ontology class 'pressure setting datum'
>>>>>>> 273b34793553e64e4e271202f9f7bbff0e56ed58
        links = ['http://purl.obolibrary.org/obo/PATO_0001025','http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005040'],
        type=np.dtype(
            np.float64),
        unit=('mbar'),
        a_eln=dict(
            component='NumberEditQuantity',
            defaultDisplayUnit='mbar',
            props=dict(
                minValue=0)))

    capman_pressure = Quantity(
        #Link to ontology class 'pressure', Link to ontology class 'pressure setting datum'
        links = ['http://purl.obolibrary.org/obo/PATO_0001025','http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005040'],
        type=np.dtype(
            np.float64),
        unit=('mmmHg'),
        a_eln=dict(
            component='NumberEditQuantity',
            defaultDisplayUnit='mmmHg',
            props=dict(
                minValue=0)))

    temperature = Quantity(
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        #Link to ontology class 'temperature', Link to ontology class 'temperature setting datum'
        links = ['http://purl.obolibrary.org/obo/PATO_0000146','http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002071'],
=======
        #Link to class 'process temperature', Link to class 'process temperature setting datum'
=======
        #Link to ontology class 'process temperature', Link to ontology class 'process temperature setting datum'
>>>>>>> 8794d04 (Updated 'Link to class' to 'Link to ontology class')
        links = ['','http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002071'],
>>>>>>> 26fa046 (added links to vapour based -> sputtering)
=======
        #Link to ontology class 'temperature', Link to ontology class 'temperature setting datum'
        links = ['http://purl.obolibrary.org/obo/PATO_0000146','http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002071'],
>>>>>>> dfae14f (Changed 'process time' & sd links into 'time' & sd links)
=======
        #Link to ontology class 'temperature', Link to ontology class 'temperature setting datum'
        links = ['http://purl.obolibrary.org/obo/PATO_0000146','http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002071'],
>>>>>>> 273b34793553e64e4e271202f9f7bbff0e56ed58
        type=np.dtype(np.float64),
        unit=('°C'),
        a_eln=dict(component='NumberEditQuantity', defaultDisplayUnit='°C'))

    burn_in_time = Quantity(
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        #Link to ontology class 'time', Link to ontology class 'time setting datum' (missing class)
        links = ['http://purl.obolibrary.org/obo/PATO_0000165','http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005085'],
=======
        #Link to class 'process time', Link to class 'process time setting datum'
=======
        #Link to ontology class 'process time', Link to ontology class 'process time setting datum'
>>>>>>> 8794d04 (Updated 'Link to class' to 'Link to ontology class')
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00001063','http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002072'],
>>>>>>> 26fa046 (added links to vapour based -> sputtering)
=======
        #Link to ontology class 'time', Link to ontology class 'time setting datum' (missing class)
        links = ['http://purl.obolibrary.org/obo/PATO_0000165','http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005085'],
>>>>>>> dfae14f (Changed 'process time' & sd links into 'time' & sd links)
=======
        #Link to ontology class 'time', Link to ontology class 'time setting datum' (missing class)
        links = ['http://purl.obolibrary.org/obo/PATO_0000165','http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005085'],
>>>>>>> 273b34793553e64e4e271202f9f7bbff0e56ed58
        type=np.dtype(
            np.float64),
        unit=('s'),
        a_eln=dict(
            component='NumberEditQuantity',
            defaultDisplayUnit='s',
            props=dict(
                minValue=0)))

    deposition_time = Quantity(
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        #Link to ontology class 'time', Link to ontology class 'time setting datum'
        links = ['http://purl.obolibrary.org/obo/PATO_0000165','http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005085'],
=======
        #Link to class 'process time', Link to class 'process time setting datum'
=======
        #Link to ontology class 'process time', Link to ontology class 'process time setting datum'
>>>>>>> 8794d04 (Updated 'Link to class' to 'Link to ontology class')
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00001063','http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002072'],
>>>>>>> 26fa046 (added links to vapour based -> sputtering)
=======
        #Link to ontology class 'time', Link to ontology class 'time setting datum'
        links = ['http://purl.obolibrary.org/obo/PATO_0000165','http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005085'],
>>>>>>> dfae14f (Changed 'process time' & sd links into 'time' & sd links)
=======
        #Link to ontology class 'time', Link to ontology class 'time setting datum'
        links = ['http://purl.obolibrary.org/obo/PATO_0000165','http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005085'],
>>>>>>> 273b34793553e64e4e271202f9f7bbff0e56ed58
        type=np.dtype(
            np.float64),
        unit=('s'),
        a_eln=dict(
            component='NumberEditQuantity',
            defaultDisplayUnit='s',
            props=dict(
                minValue=0)))

    power = Quantity(
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        #Link to ontology class 'power', Link to ontology class 'power setting datum'
=======
        #Link to class 'power', Link to class 'power setting datum'
>>>>>>> 26fa046 (added links to vapour based -> sputtering)
=======
        #Link to ontology class 'power', Link to ontology class 'power setting datum'
>>>>>>> 8794d04 (Updated 'Link to class' to 'Link to ontology class')
=======
        #Link to ontology class 'power', Link to ontology class 'power setting datum'
>>>>>>> 273b34793553e64e4e271202f9f7bbff0e56ed58
        links = ['http://purl.obolibrary.org/obo/PATO_0001024','http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002104'],
        type=np.dtype(
            np.float64),
        unit=('W'),
        a_eln=dict(
            component='NumberEditQuantity',
            defaultDisplayUnit='W', props=dict(minValue=0)))

    voltage = Quantity(
        type=np.dtype(
            np.float64),
        unit=('V'),
        a_eln=dict(
            component='NumberEditQuantity',
            defaultDisplayUnit='V'))

    gas_flow_rate = Quantity(
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        #Link to ontology class 'gas flow rate', Link to ontology class 'gas flow rate setting datum'
=======
        #Link to class 'gas flow rate', Link to class 'gas flow rate setting datum'
>>>>>>> 26fa046 (added links to vapour based -> sputtering)
=======
        #Link to ontology class 'gas flow rate', Link to ontology class 'gas flow rate setting datum'
>>>>>>> 8794d04 (Updated 'Link to class' to 'Link to ontology class')
=======
        #Link to ontology class 'gas flow rate', Link to ontology class 'gas flow rate setting datum'
>>>>>>> 273b34793553e64e4e271202f9f7bbff0e56ed58
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002114','http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002108'],
        type=np.dtype(
            np.float64),
        unit=('cm**3/minute'),
        a_eln=dict(
            component='NumberEditQuantity',
            defaultDisplayUnit='cm**3/minute', props=dict(minValue=0)))


class Sputtering(LayerDeposition):
    '''Base class for evaporation of a sample'''

    m_def = Section(
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        #Link to ontology class 'sputter deposition'
=======
        #Link to class 'sputter deposition'
>>>>>>> 26fa046 (added links to vapour based -> sputtering)
=======
        #Link to ontology class 'sputter deposition'
>>>>>>> 8794d04 (Updated 'Link to class' to 'Link to ontology class')
=======
        #Link to ontology class 'sputter deposition'
>>>>>>> 273b34793553e64e4e271202f9f7bbff0e56ed58
        links = ['http://purl.obolibrary.org/obo/CHMO_0001364'],
    )

    processes = SubSection(
        section_def=SputteringProcess, repeats=True)

    def normalize(self, archive, logger):
        super(Sputtering, self).normalize(archive, logger)

        self.method = "Sputtering"

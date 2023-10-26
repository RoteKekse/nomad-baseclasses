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

from nomad.metainfo import (Quantity, Reference, SubSection, Section)
from nomad.datamodel.data import ArchiveSection

from nomad.datamodel.metainfo.basesections import PubChemPureSubstanceSection
from .. import LayerDeposition
from ..chemical import Chemical


class EvaporationSources(ArchiveSection):
    chemical = Quantity(
<<<<<<< HEAD
        #Link to ontology class 'chemical substance'
=======
        #Link to class 'chemical substance'
>>>>>>> 1a08f68 (Added further links to vapour based deposition (evaporation; pvd))
        links = ['http://purl.obolibrary.org/obo/CHEBI_59999'],
        type=Reference(Chemical.m_def),
        a_eln=dict(component='ReferenceEditQuantity'))

    chemical_2 = SubSection(
<<<<<<< HEAD
        #Link to ontology class 'chemical substance'
=======
        #Link to class 'chemical substance'
>>>>>>> 1a08f68 (Added further links to vapour based deposition (evaporation; pvd))
        links = ['http://purl.obolibrary.org/obo/CHEBI_59999'],
        section_def=PubChemPureSubstanceSection)

    sources = Quantity(
        type=str,
        a_eln=dict(component='StringEditQuantity',
                   props=dict(
                       suggestions=[
                           'TE1',
                           'TE2',
                           'UE1',
                           'UE2'])))

    tooling_factor = Quantity(
        type=np.dtype(np.float64),
        a_eln=dict(component='NumberEditQuantity'))

    mass_before_weighing = Quantity(
<<<<<<< HEAD
        #Link to ontology class 'mass'
=======
        #Link to class 'mass'
>>>>>>> 1a08f68 (Added further links to vapour based deposition (evaporation; pvd))
        links = ['http://purl.obolibrary.org/obo/PATO_0000125'],
        type=np.dtype(
            np.float64),
        unit=('g'),
        a_eln=dict(
            component='NumberEditQuantity',
            defaultDisplayUnit='g',
            props=dict(
                minValue=0)))

    mass_after_weighing = Quantity(
<<<<<<< HEAD
        #Link to ontology class 'mass'
=======
        #Link to class 'mass'
>>>>>>> 1a08f68 (Added further links to vapour based deposition (evaporation; pvd))
        links = ['http://purl.obolibrary.org/obo/PATO_0000125'],
        type=np.dtype(
            np.float64),
        unit=('g'),
        a_eln=dict(
            component='NumberEditQuantity',
            defaultDisplayUnit='g',
            props=dict(
                minValue=0)))

    mass_after_processing = Quantity(
<<<<<<< HEAD
        #Link to ontology class 'mass'
=======
        #Link to class 'mass'
>>>>>>> 1a08f68 (Added further links to vapour based deposition (evaporation; pvd))
        links = ['http://purl.obolibrary.org/obo/PATO_0000125'],
        type=np.dtype(
            np.float64), unit=('g'), a_eln=dict(
            component='NumberEditQuantity', defaultDisplayUnit='g', props=dict(
                minValue=0)))

    comment = Quantity(
        type=str,
        a_eln=dict(component='RichTextEditQuantity'))

    # def normalize(self, archive, logger):
    # TODO add check if mass increased
    # if self.mass_before_weighing and self.mass_after_weighing:
    #     diff = self.mass_after_weighing - self.mass_before_weighing


class PerovsciteEvaporation(ArchiveSection):
    evaporation_sources = SubSection(
        section_def=EvaporationSources, repeats=True)


class Evaporation(ArchiveSection):
    m_def = Section(label_quantity='name'
<<<<<<< HEAD
<<<<<<< HEAD
                    #Link to ontology class 'evporation'
                    #links = [class doesnt exist],
=======
                    #Link to class 'evaporation'
                    links
>>>>>>> 46c0756 (Started adding links to vapour based deposition)
=======
                    #Link to class 'evporation'
                    #links = [class doesnt exist],
>>>>>>> 1a08f68 (Added further links to vapour based deposition (evaporation; pvd))
                    )
    name = Quantity(
        type=str
    )

    chemical = Quantity(
<<<<<<< HEAD
        #Link to ontology class 'chemical substance'
=======
        #Link to class 'chemical substance'
>>>>>>> 1a08f68 (Added further links to vapour based deposition (evaporation; pvd))
        links = ['http://purl.obolibrary.org/obo/CHEBI_59999'],
        type=Reference(Chemical.m_def),
        a_eln=dict(component='ReferenceEditQuantity'))

    chemical_2 = SubSection(
<<<<<<< HEAD
        #Link to ontology class 'chemical substance'
=======
        #Link to class 'chemical substance'
>>>>>>> 1a08f68 (Added further links to vapour based deposition (evaporation; pvd))
        links = ['http://purl.obolibrary.org/obo/CHEBI_59999'],
        section_def=PubChemPureSubstanceSection)

    source = Quantity(
        type=str,
        a_eln=dict(
            component='EnumEditQuantity',
            props=dict(
                suggestions=[
                    'LTE1',
                    'LTE2',
                    'LTE3',
                    'LTE4',
                    'ULTE1',
                    'ULTE2'])))

    thickness = Quantity(
<<<<<<< HEAD
        #Link to ontology class 'thickness'
=======
        #Link to class 'thickness'
>>>>>>> 1a08f68 (Added further links to vapour based deposition (evaporation; pvd))
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
        #Link to ontology class 'pressure', Link to ontology class 'pressure setting datum'
        links = ['http://purl.obolibrary.org/obo/PATO_0001025','http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005040'],
=======
        #Link to class 'total pressure'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00001094'],
>>>>>>> 1a08f68 (Added further links to vapour based deposition (evaporation; pvd))
=======
        #Link to class 'pressure'
        links = ['http://purl.obolibrary.org/obo/PATO_0001025','http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005040'],
>>>>>>> cd7fa1c (Added links to pevcd, fixed spelling error perovscite)
        type=np.dtype(
            np.float64),
        unit=('mbar'),
        a_eln=dict(
            component='NumberEditQuantity',
            defaultDisplayUnit='mbar',
            props=dict(
                minValue=0)))

    start_rate = Quantity(
<<<<<<< HEAD
        #Link to ontology class 'rate'
=======
        #Link to class 'rate'
>>>>>>> cd7fa1c (Added links to pevcd, fixed spelling error perovscite)
        links = ['http://purl.obolibrary.org/obo/PATO_0000161'],
        type=np.dtype(
            np.float64),
        unit=('angstrom/s'),
        a_eln=dict(
            component='NumberEditQuantity',
            defaultDisplayUnit='angstrom/s', props=dict(minValue=0)))

    target_rate = Quantity(
<<<<<<< HEAD
        #Link to ontology class 'rate'
=======
        #Link to class 'rate'
>>>>>>> cd7fa1c (Added links to pevcd, fixed spelling error perovscite)
        links = ['http://purl.obolibrary.org/obo/PATO_0000161'],
        type=np.dtype(
            np.float64),
        unit=('angstrom/s'),
        a_eln=dict(
            component='NumberEditQuantity',
            defaultDisplayUnit='angstrom/s', props=dict(minValue=0)))

    time = Quantity(
<<<<<<< HEAD
        #Link to ontology class 'time', Link to ontology class 'time setting datum'
        links = ['http://purl.obolibrary.org/obo/PATO_0000165', 'http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005085'],
=======
        #Link to class 'process time', Link to class 'process time setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00001063','http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002072'],
>>>>>>> 1a08f68 (Added further links to vapour based deposition (evaporation; pvd))
        type=np.dtype(
            np.float64),
        unit=('s'),
        a_eln=dict(
            component='NumberEditQuantity',
            defaultDisplayUnit='s',
            props=dict(
                minValue=0)))

    def normalize(self, archive, logger):

        if self.chemical:
            if self.chemical.name:
                self.name = self.chemical.name

        if self.chemical_2:
            if self.chemical_2.name:
                self.name = self.chemical_2.name

        if self.thickness:
            if self.name:
                self.name += ' ' + str(self.thickness)
            else:
                self.name = str(self.thickness)


class OrganicEvaporation(Evaporation):
    temparature = Quantity(
<<<<<<< HEAD
        #Link to ontology class 'temperature', Link to ontology class 'process temperature setting datum'
        links = ['http://purl.obolibrary.org/obo/PATO_0000146','http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002111'],
=======
        #Link to class 'process temperature', Link to class 'process temperature setting datum'
        links = ['','http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002071'],
>>>>>>> 1a08f68 (Added further links to vapour based deposition (evaporation; pvd))
        type=np.dtype(
            np.float64),
        unit=('°C'),
        shape=[2],
        a_eln=dict(
            component='NumberEditQuantity',
            defaultDisplayUnit='°C',
            label="Temperature"))


class InorganicEvaporation(Evaporation):
    power = Quantity(
<<<<<<< HEAD
        #Link to ontology class 'power', Link to ontology class 'power setting datum'
=======
        #Link to class 'power', Link to class 'power setting datum'
>>>>>>> 1a08f68 (Added further links to vapour based deposition (evaporation; pvd))
        links = ['http://purl.obolibrary.org/obo/PATO_0001024','http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002104'],
        type=np.dtype(
            np.float64),
        unit=('W'),
        shape=[2],
        a_eln=dict(
            component='NumberEditQuantity',
            defaultDisplayUnit='W',
            props=dict(
                minValue=0)))


class Evaporations(LayerDeposition):
    '''Base class for evaporation of a sample'''

    organic_evaporation = SubSection(
        section_def=OrganicEvaporation, repeats=True)

    inorganic_evaporation = SubSection(
        section_def=InorganicEvaporation, repeats=True)

    perovscite_evaporation = SubSection(
        section_def=InorganicEvaporation, repeats=True)

    def normalize(self, archive, logger):
        super(Evaporations, self).normalize(archive, logger)

        self.method = "Evaporation"

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
    Reference, SubSection)
from nomad.datamodel.data import ArchiveSection

from ..chemical import Chemical
from nomad.datamodel.metainfo.basesections import PubChemPureSubstanceSection


class Quenching(ArchiveSection):
    pass


class AntiSolventQuenching(Quenching):

    m_def = Section(
<<<<<<< HEAD
<<<<<<< HEAD
        #Link to ontology class 'anti solvent quenching'
=======
        #Link to class 'anti solvent quenching'
>>>>>>> 2bfcffa (First Commit, added links in files annealing, quenching, sintering, wet chemical depo, dip coating, spin coating, spray pyrolysis, slot die coating)
=======
        #Link to ontology class 'anti solvent quenching'
>>>>>>> da2afee (Added links to 'material_processes_misc and fixed structure of older links)
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00001052'],
        label_quantity='name'
        )
    name = Quantity(type=str)

    anti_solvent = Quantity(
<<<<<<< HEAD
<<<<<<< HEAD
        #Link to ontology class 'solvent'
=======
        #Link to class 'solvent'
>>>>>>> 2bfcffa (First Commit, added links in files annealing, quenching, sintering, wet chemical depo, dip coating, spin coating, spray pyrolysis, slot die coating)
=======
        #Link to ontology class 'solvent'
>>>>>>> da2afee (Added links to 'material_processes_misc and fixed structure of older links)
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00000026'],
        type=Reference(Chemical.m_def),
        a_eln=dict(component='ReferenceEditQuantity'))

    anti_solvent_2 = SubSection(
<<<<<<< HEAD
<<<<<<< HEAD
        #Link to ontology class 'solvent'
=======
        #Link to class 'solvent'
>>>>>>> 2bfcffa (First Commit, added links in files annealing, quenching, sintering, wet chemical depo, dip coating, spin coating, spray pyrolysis, slot die coating)
=======
        #Link to ontology class 'solvent'
>>>>>>> da2afee (Added links to 'material_processes_misc and fixed structure of older links)
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00000026'],
        section_def=PubChemPureSubstanceSection)

    anti_solvent_volume = Quantity(
<<<<<<< HEAD
<<<<<<< HEAD
        #Link to ontology class 'volume', Link to ontology class 'volume setting datum'
        links = ['http://purl.obolibrary.org/obo/PATO_0000918','http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002158'],
=======
        #Link to class 'volume setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002158'],
        #Link zur Klasse 'volume'
        links = ['http://purl.obolibrary.org/obo/PATO_0000918'],
>>>>>>> 2bfcffa (First Commit, added links in files annealing, quenching, sintering, wet chemical depo, dip coating, spin coating, spray pyrolysis, slot die coating)
=======
        #Link to ontology class 'volume', Link to ontology class 'volume setting datum'
        links = ['http://purl.obolibrary.org/obo/PATO_0000918','http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002158'],
>>>>>>> da2afee (Added links to 'material_processes_misc and fixed structure of older links)
        type=np.dtype(
            np.float64),
        unit=('ml'),
        a_eln=dict(
            component='NumberEditQuantity',
            defaultDisplayUnit='ml',
            props=dict(
                minValue=0)))

    anti_solvent_dropping_time = Quantity(
<<<<<<< HEAD
<<<<<<< HEAD
        #Link to ontology class 'anti solvent dropping time', Link to ontology class 'anti solvent dropping time setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002150','http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002151'],
=======
        #Link to class 'anti solvent dropping time setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002151'],
        #Link to class 'anti solvent dropping time'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002150'],
>>>>>>> 2bfcffa (First Commit, added links in files annealing, quenching, sintering, wet chemical depo, dip coating, spin coating, spray pyrolysis, slot die coating)
=======
        #Link to ontology class 'anti solvent dropping time', Link to ontology class 'anti solvent dropping time setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002150','http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002151'],
>>>>>>> da2afee (Added links to 'material_processes_misc and fixed structure of older links)
        type=np.dtype(
            np.float64), unit=('s'), a_eln=dict(
            component='NumberEditQuantity', defaultDisplayUnit='s', props=dict(
                minValue=0)))

    anti_solvent_dropping_flow_rate = Quantity(
<<<<<<< HEAD
<<<<<<< HEAD
        #Link to ontology class 'anti solvent dropping flow rate', Link to ontology class 'anti solvent dropping flow rate setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005091','http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005094'],
=======
        #Link to class 'anti solvent dropping flow rate'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005091'],
        #Link to class 'anti solvent dropping flow rate setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005094'],
>>>>>>> 2bfcffa (First Commit, added links in files annealing, quenching, sintering, wet chemical depo, dip coating, spin coating, spray pyrolysis, slot die coating)
=======
        #Link to ontology class 'anti solvent dropping flow rate', Link to ontology class 'anti solvent dropping flow rate setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005091','http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005094'],
>>>>>>> da2afee (Added links to 'material_processes_misc and fixed structure of older links)
        type=np.dtype(
            np.float64), unit=('ul/s'), a_eln=dict(
            component='NumberEditQuantity', defaultDisplayUnit='ul/s', props=dict(
                minValue=0)))

    anti_solvent_dropping_height = Quantity(
<<<<<<< HEAD
<<<<<<< HEAD
        #Link to ontology class 'anti solvent dropping height', Link to ontology class 'anti solvent dropping height setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005092','http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005093'],
=======
        #Link to class 'anti solvent dropping height'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005092'],
        #Link to class 'anti solvent dropping height setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005093'],
>>>>>>> 2bfcffa (First Commit, added links in files annealing, quenching, sintering, wet chemical depo, dip coating, spin coating, spray pyrolysis, slot die coating)
=======
        #Link to ontology class 'anti solvent dropping height', Link to ontology class 'anti solvent dropping height setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005092','http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005093'],
>>>>>>> da2afee (Added links to 'material_processes_misc and fixed structure of older links)
        type=np.dtype(
            np.float64), unit=('mm'), a_eln=dict(
            component='NumberEditQuantity', defaultDisplayUnit='mm', props=dict(
                minValue=0)))

    def normalize(self, archive, logger):

        if self.anti_solvent and self.anti_solvent.name:
            if self.anti_solvent_volume:
                self.name = self.anti_solvent.name + \
                    ' ' + str(self.anti_solvent_volume)
            else:
                self.name = self.anti_solvent.name


class SpinCoatingAntiSolvent(AntiSolventQuenching):
    pass


class GasQuenching(Quenching):
    m_def = Section(
<<<<<<< HEAD
<<<<<<< HEAD
        #Link to ontology class 'gas quenching'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00001077']
=======
        #Link to class 'gas quenching'
<<<<<<< HEAD
        link = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00001077']
>>>>>>> 2bfcffa (First Commit, added links in files annealing, quenching, sintering, wet chemical depo, dip coating, spin coating, spray pyrolysis, slot die coating)
    )
    gas = Quantity(
        #Link to ontology class 'chemical substance'
        links = ['http://purl.obolibrary.org/obo/CHEBI_59999'],
=======
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00001077']
    )
    gas = Quantity(
        #Link to class 'gas mixture'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002107'],
>>>>>>> ff6f4e2 (Corrected files from previous commit)
=======
        #Link to ontology class 'gas quenching'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00001077']
    )
    gas = Quantity(
        #Link to ontology class 'chemical substance'
        links = ['http://purl.obolibrary.org/obo/CHEBI_59999'],
>>>>>>> da2afee (Added links to 'material_processes_misc and fixed structure of older links)
        type=str,
        a_eln=dict(component='StringEditQuantity'))


class AirKnifeGasQuenching(GasQuenching):
    m_def = Section(
<<<<<<< HEAD
<<<<<<< HEAD
        #Link to ontology class 'air knife gas quenching'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005032'],
    )
    air_knife_pressure = Quantity(
        #Link to ontology class 'air knife pressure', Link to ontology class 'air knife pressure setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005021','http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005027'],
=======
        #Link to class 'air knife gas quenching'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005032'],
    )
    air_knife_pressure = Quantity(
        #Link to class 'air knife pressure'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005021'],
        #Link to class 'air knife pressure setting datum'
<<<<<<< HEAD
        link = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005027'],
>>>>>>> 2bfcffa (First Commit, added links in files annealing, quenching, sintering, wet chemical depo, dip coating, spin coating, spray pyrolysis, slot die coating)
=======
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005027'],
>>>>>>> ff6f4e2 (Corrected files from previous commit)
=======
        #Link to ontology class 'air knife gas quenching'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005032'],
    )
    air_knife_pressure = Quantity(
        #Link to ontology class 'air knife pressure', Link to ontology class 'air knife pressure setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005021','http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005027'],
>>>>>>> da2afee (Added links to 'material_processes_misc and fixed structure of older links)
        type=np.dtype(
            np.float64),
        unit=('mbar'),
        description=('The pressure of the air knife gas.'),
        a_eln=dict(
            component='NumberEditQuantity',
            defaultDisplayUnit='mbar',
            props=dict(
                minValue=0)))

    air_knife_speed = Quantity(
<<<<<<< HEAD
<<<<<<< HEAD
        #Link to ontology class 'air knife speed', Link to ontology class 'air knife speed setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005025','http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005026'],
=======
        #Link to class 'air knife speed'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005025'],
        #Link to class 'air knife speed setting datum'
<<<<<<< HEAD
        link = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005026'],
>>>>>>> 2bfcffa (First Commit, added links in files annealing, quenching, sintering, wet chemical depo, dip coating, spin coating, spray pyrolysis, slot die coating)
=======
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005026'],
>>>>>>> ff6f4e2 (Corrected files from previous commit)
=======
        #Link to ontology class 'air knife speed', Link to ontology class 'air knife speed setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005025','http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005026'],
>>>>>>> da2afee (Added links to 'material_processes_misc and fixed structure of older links)
        type=np.dtype(
            np.float64),
        unit=('mm/s'),
        description=('The speed of the air knife moving over the sample.'),
        a_eln=dict(
            component='NumberEditQuantity',
            defaultDisplayUnit='mm/s',
            props=dict(
                minValue=0)))

    air_knife_angle = Quantity(
<<<<<<< HEAD
<<<<<<< HEAD
        #Link to ontology class 'air knife angle', Link to ontology class 'air knife angle setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005024','http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005029'],
=======
        #Link to class 'air knife angle'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005024'],
        #Link to class 'air knife angle setting datum'
<<<<<<< HEAD
        link = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005029'],
>>>>>>> 2bfcffa (First Commit, added links in files annealing, quenching, sintering, wet chemical depo, dip coating, spin coating, spray pyrolysis, slot die coating)
=======
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005029'],
>>>>>>> ff6f4e2 (Corrected files from previous commit)
=======
        #Link to ontology class 'air knife angle', Link to ontology class 'air knife angle setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005024','http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005029'],
>>>>>>> da2afee (Added links to 'material_processes_misc and fixed structure of older links)
        type=np.dtype(
            np.float64),
        unit=('degree'),
        description=('The angle of the air knife with respect to the sample, ie. 90° is straight above the sample.'),
        a_eln=dict(
            component='NumberEditQuantity',
            defaultDisplayUnit='degree',
            props=dict(
                minValue=0)))

    air_knife_distance_to_thin_film = Quantity(
<<<<<<< HEAD
<<<<<<< HEAD
        #Link to ontology class 'air knife distance to thinfilm', Link to ontology class 'air knife distance to thinfilm setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005023','http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005028'],
=======
        #Link to class 'air knife distance to thinfilm'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005023'],
        #Link to class 'air knife distance to thinfilm setting datum'
<<<<<<< HEAD
        link = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005028'],
>>>>>>> 2bfcffa (First Commit, added links in files annealing, quenching, sintering, wet chemical depo, dip coating, spin coating, spray pyrolysis, slot die coating)
=======
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005028'],
>>>>>>> ff6f4e2 (Corrected files from previous commit)
=======
        #Link to ontology class 'air knife distance to thinfilm', Link to ontology class 'air knife distance to thinfilm setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005023','http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005028'],
>>>>>>> da2afee (Added links to 'material_processes_misc and fixed structure of older links)
        type=np.dtype(
            np.float64),
        description=('The distance of the air knife to the thin film.'),
        unit=('um'),
        a_eln=dict(
            component='NumberEditQuantity',
            defaultDisplayUnit='um',
            props=dict(
                minValue=0)))

    air_knife_time = Quantity(
        type=np.dtype(
            np.float64),
        description=('The time the air knife is on.'),
        unit=('s'),
        a_eln=dict(
            component='NumberEditQuantity',
            defaultDisplayUnit='s',
            props=dict(
                minValue=0)))


class SpinCoatingGasQuenching(GasQuenching):
    pass

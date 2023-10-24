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

from ..solution import Solution
from .wet_chemical_deposition import WetChemicalDeposition
from ..material_processes_misc import Annealing, AirKnifeGasQuenching


class SlotDieCoatingProperties(ArchiveSection):

    flow_rate = Quantity(
<<<<<<< HEAD
        #Link to ontology class 'flow rate', Link to ontology class 'flow rate setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005039', 'http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005048'],
=======
        #Der Link zur Quality
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005039'],
        #Der Link zum Setting Datum
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005048'],
>>>>>>> 2bfcffa (First Commit, added links in files annealing, quenching, sintering, wet chemical depo, dip coating, spin coating, spray pyrolysis, slot die coating)
        type=np.dtype(
            np.float64),
        unit=('ml/minute'),
        a_eln=dict(
            component='NumberEditQuantity',
            defaultDisplayUnit='ml/minute', props=dict(minValue=0)))

    slot_die_head_width = Quantity(
<<<<<<< HEAD
        #Link to ontology class 'slot die head width', Link to ontology class 'slot die head width setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005038', 'http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005047'],
=======
        #Der Link zur Quality
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005038'],
        #Der Link zum Setting Datum
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005047'],
>>>>>>> 2bfcffa (First Commit, added links in files annealing, quenching, sintering, wet chemical depo, dip coating, spin coating, spray pyrolysis, slot die coating)
        type=np.dtype(
            np.float64),
        unit=('mm'),
        a_eln=dict(
            component='NumberEditQuantity',
            defaultDisplayUnit='mm',
            props=dict(
                minValue=0)))

    slot_die_shim_width = Quantity(
<<<<<<< HEAD
        #Link to ontology class 'slot die shim width', Link to ontology class 'slot die chim width setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005035', 'http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005045'],
=======
        #Der Link zur Quality
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005035'],
        #Der Link zum Setting Datum
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005045'],
>>>>>>> 2bfcffa (First Commit, added links in files annealing, quenching, sintering, wet chemical depo, dip coating, spin coating, spray pyrolysis, slot die coating)
        type=np.dtype(
            np.float64),
        unit=('mm'),
        a_eln=dict(
            component='NumberEditQuantity',
            defaultDisplayUnit='mm',
            props=dict(
                minValue=0)))

    slot_die_shim_thickness = Quantity(
<<<<<<< HEAD
        #Link to ontology class 'slot die shim thickness', Link to ontology class 'slot die shim thickness setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005036', 'http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005046'],
=======
        #Der Link zur Quality
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005036'],
        #Der Link zum Setting Datum
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005046'],
>>>>>>> 2bfcffa (First Commit, added links in files annealing, quenching, sintering, wet chemical depo, dip coating, spin coating, spray pyrolysis, slot die coating)
        type=np.dtype(
            np.float64),
        unit=('mm'),
        a_eln=dict(
            component='NumberEditQuantity',
            defaultDisplayUnit='mm',
            props=dict(
                minValue=0)))

    slot_die_head_distance_to_thinfilm = Quantity(
<<<<<<< HEAD
        #Link to ontology class 'slot die head distance to thinfilm', Link to ontology class 'slot die head distane to thinfilm setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005034', 'http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005044'],
=======
        #Der Link zur Quality
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005034'],
        #Der Link zum Setting Datum
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005044'],
>>>>>>> 2bfcffa (First Commit, added links in files annealing, quenching, sintering, wet chemical depo, dip coating, spin coating, spray pyrolysis, slot die coating)
        type=np.dtype(
            np.float64),
        unit=('mm'),
        a_eln=dict(
            component='NumberEditQuantity',
            defaultDisplayUnit='mm',
            props=dict(
                minValue=0)))
    
    slot_die_head_speed = Quantity(
<<<<<<< HEAD
        #Link to ontology class 'slot die head speed', Link to ontology class 'slot die head speed setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005033', 'http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005033'],
=======
        #Der Link zur Quality
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005033'],
        #Der Link zum Setting Datum
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005033'],
>>>>>>> 2bfcffa (First Commit, added links in files annealing, quenching, sintering, wet chemical depo, dip coating, spin coating, spray pyrolysis, slot die coating)
        type=np.dtype(
            np.float64),
        unit=('mm/s'),
        a_eln=dict(
            component='NumberEditQuantity',
            defaultDisplayUnit='mm/s',
            props=dict(
                minValue=0)))

    temperature = Quantity(
<<<<<<< HEAD
        #Link to ontology class 'temperature', Link to ontology class 'temperature setting datum'
        links = ['http://purl.obolibrary.org/obo/PATO_0000146', 'http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002111'],
=======
        #Der Link zur Quality
        links = ['http://purl.obolibrary.org/obo/PATO_0000146'],
        #Der Link zum Setting Datum
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#print_head_temperature_setting_datum'],
>>>>>>> 2bfcffa (First Commit, added links in files annealing, quenching, sintering, wet chemical depo, dip coating, spin coating, spray pyrolysis, slot die coating)
        type=np.dtype(
            np.float64),
        unit=('°C'),
        a_eln=dict(
            component='NumberEditQuantity',
            defaultDisplayUnit='°C',
            props=dict(
                minValue=0)))


class SlotDieCoating(WetChemicalDeposition):
    '''Spin Coating'''
    m_def = Section(
<<<<<<< HEAD
        #Link to ontology class 'slot die coating'
=======
>>>>>>> 2bfcffa (First Commit, added links in files annealing, quenching, sintering, wet chemical depo, dip coating, spin coating, spray pyrolysis, slot die coating)
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00000075']
    )
    properties = SubSection(section_def=SlotDieCoatingProperties)
    

    def normalize(self, archive, logger):
        super(SlotDieCoating, self).normalize(archive, logger)

        self.method = "Slot Die Coating"

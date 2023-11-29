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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        #Link to ontology class 'flow rate', Link to ontology class 'flow rate setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005039', 'http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005048'],
=======
        #Der Link zur Quality
=======
        #Link to class 'flow rate'
>>>>>>> ff6f4e2 (Corrected files from previous commit)
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005039'],
        #Link to class 'flow rate setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005048'],
>>>>>>> 2bfcffa (First Commit, added links in files annealing, quenching, sintering, wet chemical depo, dip coating, spin coating, spray pyrolysis, slot die coating)
=======
        #Link to class 'flow rate', Link to class 'flow rate setting datum'
=======
        #Link to ontology class 'flow rate', Link to ontology class 'flow rate setting datum'
>>>>>>> 8794d04 (Updated 'Link to class' to 'Link to ontology class')
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005039', 'http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005048'],
>>>>>>> 1916ad1 (Fixed double links)
=======
        #Link to ontology class 'flow rate', Link to ontology class 'flow rate setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005039', 'http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005048'],
>>>>>>> 273b34793553e64e4e271202f9f7bbff0e56ed58
        type=np.dtype(
            np.float64),
        unit=('ml/minute'),
        a_eln=dict(
            component='NumberEditQuantity',
            defaultDisplayUnit='ml/minute', props=dict(minValue=0)))

    slot_die_head_width = Quantity(
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        #Link to ontology class 'slot die head width', Link to ontology class 'slot die head width setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005038', 'http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005047'],
=======
        #Der Link zur Quality
=======
        #Link to class 'slot die head width'
>>>>>>> ff6f4e2 (Corrected files from previous commit)
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005038'],
        #Link to class 'slot die head width setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005047'],
>>>>>>> 2bfcffa (First Commit, added links in files annealing, quenching, sintering, wet chemical depo, dip coating, spin coating, spray pyrolysis, slot die coating)
=======
        #Link to class 'slot die head width', Link to class 'slot die head width setting datum'
=======
        #Link to ontology class 'slot die head width', Link to ontology class 'slot die head width setting datum'
>>>>>>> 8794d04 (Updated 'Link to class' to 'Link to ontology class')
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005038', 'http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005047'],
>>>>>>> 1916ad1 (Fixed double links)
=======
        #Link to ontology class 'slot die head width', Link to ontology class 'slot die head width setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005038', 'http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005047'],
>>>>>>> 273b34793553e64e4e271202f9f7bbff0e56ed58
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        #Link to ontology class 'slot die shim width', Link to ontology class 'slot die chim width setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005035', 'http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005045'],
=======
        #Der Link zur Quality
=======
        #Link to class 'slot die shim width'
>>>>>>> ff6f4e2 (Corrected files from previous commit)
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005035'],
        #Link to class 'slot die chim width setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005045'],
>>>>>>> 2bfcffa (First Commit, added links in files annealing, quenching, sintering, wet chemical depo, dip coating, spin coating, spray pyrolysis, slot die coating)
=======
        #Link to class 'slot die shim width', Link to class 'slot die chim width setting datum'
=======
        #Link to ontology class 'slot die shim width', Link to ontology class 'slot die chim width setting datum'
>>>>>>> 8794d04 (Updated 'Link to class' to 'Link to ontology class')
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005035', 'http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005045'],
>>>>>>> 1916ad1 (Fixed double links)
=======
        #Link to ontology class 'slot die shim width', Link to ontology class 'slot die chim width setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005035', 'http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005045'],
>>>>>>> 273b34793553e64e4e271202f9f7bbff0e56ed58
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        #Link to ontology class 'slot die shim thickness', Link to ontology class 'slot die shim thickness setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005036', 'http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005046'],
=======
        #Der Link zur Quality
=======
        #Link to class 'slot die shim thickness''
>>>>>>> ff6f4e2 (Corrected files from previous commit)
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005036'],
        #Link to class 'slot die shim thickness setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005046'],
>>>>>>> 2bfcffa (First Commit, added links in files annealing, quenching, sintering, wet chemical depo, dip coating, spin coating, spray pyrolysis, slot die coating)
=======
        #Link to class 'slot die shim thickness', Link to class 'slot die shim thickness setting datum'
=======
        #Link to ontology class 'slot die shim thickness', Link to ontology class 'slot die shim thickness setting datum'
>>>>>>> 8794d04 (Updated 'Link to class' to 'Link to ontology class')
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005036', 'http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005046'],
>>>>>>> 1916ad1 (Fixed double links)
=======
        #Link to ontology class 'slot die shim thickness', Link to ontology class 'slot die shim thickness setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005036', 'http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005046'],
>>>>>>> 273b34793553e64e4e271202f9f7bbff0e56ed58
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        #Link to ontology class 'slot die head distance to thinfilm', Link to ontology class 'slot die head distane to thinfilm setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005034', 'http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005044'],
=======
        #Der Link zur Quality
=======
        #Link to class 'slot die head distance to thinfilm'
>>>>>>> ff6f4e2 (Corrected files from previous commit)
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005034'],
        #Link to class 'slot die head distane to thinfilm setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005044'],
>>>>>>> 2bfcffa (First Commit, added links in files annealing, quenching, sintering, wet chemical depo, dip coating, spin coating, spray pyrolysis, slot die coating)
=======
        #Link to class 'slot die head distance to thinfilm', Link to class 'slot die head distane to thinfilm setting datum'
=======
        #Link to ontology class 'slot die head distance to thinfilm', Link to ontology class 'slot die head distane to thinfilm setting datum'
>>>>>>> 8794d04 (Updated 'Link to class' to 'Link to ontology class')
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005034', 'http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005044'],
>>>>>>> 1916ad1 (Fixed double links)
=======
        #Link to ontology class 'slot die head distance to thinfilm', Link to ontology class 'slot die head distane to thinfilm setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005034', 'http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005044'],
>>>>>>> 273b34793553e64e4e271202f9f7bbff0e56ed58
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        #Link to ontology class 'slot die head speed', Link to ontology class 'slot die head speed setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005033', 'http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005033'],
=======
        #Der Link zur Quality
=======
        #Link to class 'slot die head speed'
>>>>>>> ff6f4e2 (Corrected files from previous commit)
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005033'],
        #Link to class 'slot die head speed setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005033'],
>>>>>>> 2bfcffa (First Commit, added links in files annealing, quenching, sintering, wet chemical depo, dip coating, spin coating, spray pyrolysis, slot die coating)
=======
        #Link to class 'slot die head speed', Link to class 'slot die head speed setting datum'
=======
        #Link to ontology class 'slot die head speed', Link to ontology class 'slot die head speed setting datum'
>>>>>>> 8794d04 (Updated 'Link to class' to 'Link to ontology class')
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005033', 'http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005033'],
>>>>>>> 1916ad1 (Fixed double links)
=======
        #Link to ontology class 'slot die head speed', Link to ontology class 'slot die head speed setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005033', 'http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005033'],
>>>>>>> 273b34793553e64e4e271202f9f7bbff0e56ed58
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        #Link to ontology class 'temperature', Link to ontology class 'temperature setting datum'
        links = ['http://purl.obolibrary.org/obo/PATO_0000146', 'http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002111'],
=======
        #Der Link zur Quality
        links = ['http://purl.obolibrary.org/obo/PATO_0000146'],
        #Der Link zum Setting Datum
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#print_head_temperature_setting_datum'],
>>>>>>> 2bfcffa (First Commit, added links in files annealing, quenching, sintering, wet chemical depo, dip coating, spin coating, spray pyrolysis, slot die coating)
=======
        #Link to class 'temperature'
        links = ['http://purl.obolibrary.org/obo/PATO_0000146'],
        #Link to class 'temperature setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002111'],
>>>>>>> ff6f4e2 (Corrected files from previous commit)
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
            defaultDisplayUnit='°C',
            props=dict(
                minValue=0)))


class SlotDieCoating(WetChemicalDeposition):
    '''Spin Coating'''
    m_def = Section(
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        #Link to ontology class 'slot die coating'
=======
>>>>>>> 2bfcffa (First Commit, added links in files annealing, quenching, sintering, wet chemical depo, dip coating, spin coating, spray pyrolysis, slot die coating)
=======
        #Link to class 'slot die coating'
>>>>>>> ff6f4e2 (Corrected files from previous commit)
=======
        #Link to ontology class 'slot die coating'
>>>>>>> 8794d04 (Updated 'Link to class' to 'Link to ontology class')
=======
        #Link to ontology class 'slot die coating'
>>>>>>> 273b34793553e64e4e271202f9f7bbff0e56ed58
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00000075']
    )
    properties = SubSection(section_def=SlotDieCoatingProperties)
    

    def normalize(self, archive, logger):
        super(SlotDieCoating, self).normalize(archive, logger)

        self.method = "Slot Die Coating"

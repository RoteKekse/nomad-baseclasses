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
    Reference,
    MEnum)
from nomad.datamodel.data import ArchiveSection

from ..solution import Solution
from .wet_chemical_deposition import WetChemicalDeposition


class NozzleVoltageProfile(ArchiveSection):
    pass


class PrintHeadPath(ArchiveSection):
    pass


class LP50NozzleVoltageProfile(NozzleVoltageProfile):
    m_def = Section(
        #Link to ontology class 'print nozzle voltage profile'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005083'],
    )
    voltage_a = Quantity(
        type=np.dtype(
            np.float64), unit=('V'), a_eln=dict(
            component='NumberEditQuantity', defaultDisplayUnit='V', props=dict(
                minValue=0, maxValue=130)))

    rise_edge_a = Quantity(
        type=np.dtype(
            np.float64),
        unit=('us'),
        a_eln=dict(
            component='NumberEditQuantity',
            defaultDisplayUnit='us',
            props=dict(
                minValue=1,
                maxValue=25)))

    peak_time_a = Quantity(
        #Link to ontology class 'time', Link to ontology class 'time setting datum'
        links = ['http://purl.obolibrary.org/obo/PATO_0000165','http://purl.obolibrary.org/obo/PATO_0000165'],
        type=np.dtype(
            np.float64),
        unit=('us'),
        a_eln=dict(
            component='NumberEditQuantity',
            defaultDisplayUnit='us',
            props=dict(
                minValue=0,
                maxValue=25)))

    fall_edge_a = Quantity(
        type=np.dtype(
            np.float64),
        unit=('us'),
        a_eln=dict(
            component='NumberEditQuantity',
            defaultDisplayUnit='us',
            props=dict(
                minValue=1,
                maxValue=25)))

    voltage_b = Quantity(
        type=np.dtype(
            np.float64), unit=('V'), a_eln=dict(
            component='NumberEditQuantity', defaultDisplayUnit='V', props=dict(
                minValue=0, maxValue=130)))

    rise_edge_b = Quantity(
        type=np.dtype(
            np.float64),
        unit=('us'),
        a_eln=dict(
            component='NumberEditQuantity',
            defaultDisplayUnit='us',
            props=dict(
                minValue=1,
                maxValue=25)))

    peak_time_b = Quantity(
        #Link to ontology class 'time', Link to ontology class 'time setting datum'
        links = ['http://purl.obolibrary.org/obo/PATO_0000165','http://purl.obolibrary.org/obo/PATO_0000165'],
        type=np.dtype(
            np.float64),
        unit=('us'),
        a_eln=dict(
            component='NumberEditQuantity',
            defaultDisplayUnit='us',
            props=dict(
                minValue=0,
                maxValue=25)))

    fall_edge_b = Quantity(
        type=np.dtype(
            np.float64),
        unit=('us'),
        a_eln=dict(
            component='NumberEditQuantity',
            defaultDisplayUnit='us',
            props=dict(
                minValue=1,
                maxValue=25)))


class LP50PrintHeadPath(PrintHeadPath):
    quality_factor = Quantity(
<<<<<<< HEAD
<<<<<<< HEAD
        #Link to ontology class 'print head path', Link to ontology class 'print head position setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005084', 'http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005090'],
=======
        #Link to class 'print head path'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005084'],
        #Link to class 'print head position setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005090'],
>>>>>>> 2f6c86c (Added links to inkjet printing file)
=======
        #Link to class 'print head path', Link to class 'print head position setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005084', 'http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005090'],
>>>>>>> 1916ad1 (Fixed double links)
        type=MEnum(
            'QF1',
            'QF2',
            'QF3',
            'QF4',
            'QF5',
            'QF6',
            'QF7',
            'QF8',
            'QF9',
            'QF10',
            'QF11',
            'QF12',
            'QF13',
            'QF14',
            'QF15',
            'QF16'),
        shape=[],
        a_eln=dict(
            component='EnumEditQuantity',
        ))

    directional = Quantity(
<<<<<<< HEAD
<<<<<<< HEAD
        #Link to ontology class 'printing direction'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005077'],
=======
        #Link to class 'printing direction' (to be added)
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005077'],
        #Link to class 'printing direction setting datum'
>>>>>>> 2f6c86c (Added links to inkjet printing file)
=======
        #Link to class 'printing direction'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005077'],
>>>>>>> da93fa5 (Started adding links to subsections)
        type=MEnum('uni-directional', 'bi-directional',
                   'uni-directional reverse'),
        shape=[],
        a_eln=dict(
            component='EnumEditQuantity',
        ))

    swaths = Quantity(
        type=np.dtype(
            np.float64), a_eln=dict(
            component='NumberEditQuantity'))

    wait_run_time = Quantity(
        #Link to ontology class 'time', Link to ontology class 'time setting datum'
        links = ['http://purl.obolibrary.org/obo/PATO_0000165','http://purl.obolibrary.org/obo/PATO_0000165'],
        type=np.dtype(
            np.float64), unit=('s'), a_eln=dict(
            component='NumberEditQuantity', defaultDisplayUnit='s', props=dict(
                minValue=0)))

    total_run_time = Quantity(
        #Link to ontology class 'time', Link to ontology class 'time setting datum'
        links = ['http://purl.obolibrary.org/obo/PATO_0000165','http://purl.obolibrary.org/obo/PATO_0000165'],
        type=np.dtype(
            np.float64), unit=('s'), a_eln=dict(
            component='NumberEditQuantity', defaultDisplayUnit='s', props=dict(
                minValue=0)))


class PrintHeadProperties(ArchiveSection):
    print_speed = Quantity(
<<<<<<< HEAD
<<<<<<< HEAD
        #Link to ontology class 'print speed', Link to ontology class 'print speed setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005074', 'http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#print_speed_setting_datum'],
=======
        #Link to class 'print speed'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005074'],
        #Link to class 'print speed setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#print_speed_setting_datum'],
>>>>>>> 2f6c86c (Added links to inkjet printing file)
=======
        #Link to class 'print speed', Link to class 'print speed setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005074', 'http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#print_speed_setting_datum'],
>>>>>>> 1916ad1 (Fixed double links)
        type=np.dtype(
            np.float64),
        unit=('mm/s'),
        a_eln=dict(
            component='NumberEditQuantity',
            defaultDisplayUnit='mm/s',
            props=dict(
                minValue=1, maxValue=400)))

    print_head_angle = Quantity(
<<<<<<< HEAD
<<<<<<< HEAD
        #Link to ontology class 'print head angle', Link to ontology class 'printing head angle setting datum'    
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005079', 'http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#print_head_angle_setting_datum'],
=======
        #Link to class 'print head angle'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005079'],
        #Link to class 'printing head angle setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#print_head_angle_setting_datum'],
>>>>>>> 2f6c86c (Added links to inkjet printing file)
=======
        #Link to class 'print head angle', Link to class 'printing head angle setting datum'    
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005079', 'http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#print_head_angle_setting_datum'],
>>>>>>> 1916ad1 (Fixed double links)
        type=np.dtype(
            np.float64),
        unit=('deg'),
        a_eln=dict(
            component='NumberEditQuantity',
            defaultDisplayUnit='deg',
            props=dict(
                minValue=0)))

    print_head_temperature = Quantity(
<<<<<<< HEAD
<<<<<<< HEAD
        #Link to ontology class 'print head temperature', Link to ontology class 'print head temperature setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005070', 'http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#print_head_temperature_setting_datum'],
=======
        #Link to class 'print head temperature'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005070'],
        #Link to class 'print head temperature setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#print_head_temperature_setting_datum'],
>>>>>>> 2f6c86c (Added links to inkjet printing file)
=======
        #Link to class 'print head temperature', Link to class 'print head temperature setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005070', 'http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#print_head_temperature_setting_datum'],
>>>>>>> 1916ad1 (Fixed double links)
        type=np.dtype(
            np.float64), unit=('°C'), a_eln=dict(
            component='NumberEditQuantity', defaultDisplayUnit='°C', props=dict(
                minValue=20, maxValue=120)))

    print_head_distance_to_substrate = Quantity(
<<<<<<< HEAD
<<<<<<< HEAD
        #Link to ontology class 'print head distance to substrate', Link to ontology class 'print head distance to substrate setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005078', 'http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#print_head_distance_to_substrate_setting_datum'],
=======
        #Link to class 'print head distance to substrate'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005078'],
        #Link to class 'print head distance to substrate setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#print_head_distance_to_substrate_setting_datum'],
>>>>>>> 2f6c86c (Added links to inkjet printing file)
=======
        #Link to class 'print head distance to substrate', Link to class 'print head distance to substrate setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005078', 'http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#print_head_distance_to_substrate_setting_datum'],
>>>>>>> 1916ad1 (Fixed double links)
        type=np.dtype(
            np.float64), unit=('mm'), a_eln=dict(
            component='NumberEditQuantity', defaultDisplayUnit='mm', props=dict(
                minValue=-27, maxValue=35)))

    print_head_width = Quantity(
<<<<<<< HEAD
<<<<<<< HEAD
        #Link to ontology class 'print head width', Link to ontology class 'print head width setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005066', 'http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#print_head_width_setting_datum'],
=======
        #Link to class 'print head width'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005066'],
        #Link to class 'print head width setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#print_head_width_setting_datum'],
>>>>>>> 2f6c86c (Added links to inkjet printing file)
=======
        #Link to class 'print head width', Link to class 'print head width setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005066', 'http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#print_head_width_setting_datum'],
>>>>>>> 1916ad1 (Fixed double links)
        type=np.dtype(
            np.float64), unit=('mm'), a_eln=dict(
            component='NumberEditQuantity', defaultDisplayUnit='mm'))

    print_nozzle_distance = Quantity(
<<<<<<< HEAD
<<<<<<< HEAD
        #Link to ontology class 'print nozzle distance', Link to ontology class 'print nozzle distance setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005072', 'http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#print_nozzle_distance_setting_datum'],
=======
        #Link to class 'print nozzle distance'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005072'],
        #Link to class 'print nozzle distance setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#print_nozzle_distance_setting_datum'],
>>>>>>> 2f6c86c (Added links to inkjet printing file)
=======
        #Link to class 'print nozzle distance', Link to class 'print nozzle distance setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005072', 'http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#print_nozzle_distance_setting_datum'],
>>>>>>> 1916ad1 (Fixed double links)
        type=np.dtype(
            np.float64), unit=('mm'), a_eln=dict(
            component='NumberEditQuantity', defaultDisplayUnit='mm'))

    print_nozzle_width = Quantity(
<<<<<<< HEAD
<<<<<<< HEAD
        #Link to ontology class 'print nozzle width', Link to ontology class 'print nozzle width setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005067', 'http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005095'],
=======
        #Link to class 'print nozzle width'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005067'],
        #Link to class 'print nozzle width setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005095'],
>>>>>>> 2f6c86c (Added links to inkjet printing file)
=======
        #Link to class 'print nozzle width', Link to class 'print nozzle width setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005067', 'http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005095'],
>>>>>>> 1916ad1 (Fixed double links)
        type=np.dtype(
            np.float64), unit=('um'), a_eln=dict(
            component='NumberEditQuantity', defaultDisplayUnit='um'))

    print_nozzle_drop_volume = Quantity(
<<<<<<< HEAD
<<<<<<< HEAD
        #Link to ontology class 'print nozzle drop volume', Link to ontology class 'print nozzle drop volume setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005080', 'http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005096'],
=======
        #Link to class 'print nozzle drop volume'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005080'],
        #Link to class 'print nozzle drop volume setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005096'],
>>>>>>> 2f6c86c (Added links to inkjet printing file)
=======
        #Link to class 'print nozzle drop volume', Link to class 'print nozzle drop volume setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005080', 'http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005096'],
>>>>>>> 1916ad1 (Fixed double links)
        type=np.dtype(
            np.float64), unit=('pl'), a_eln=dict(
            component='NumberEditQuantity', defaultDisplayUnit='pl'))


class InkjetPrintingProperties(ArchiveSection):

    # m_def = Section(label_quantity='name')

    resolution_x = Quantity(
<<<<<<< HEAD
        #Link to ontology class 'printing resolution x'
=======
        #Link to class 'printing resolution x'
>>>>>>> 2f6c86c (Added links to inkjet printing file)
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005076'],
        type=np.dtype(
            np.float64),
        # unit=('ml'),
        a_eln=dict(
            component='NumberEditQuantity',
            # defaultDisplayUnit='ml',
            props=dict(
                minValue=0)))

    resolution_y = Quantity(
<<<<<<< HEAD
        #Link to ontology class 'printing resolution y'
=======
        #Link to class 'printing resolution y'
>>>>>>> 2f6c86c (Added links to inkjet printing file)
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005081'],
        type=np.dtype(
            np.float64),
        # unit=('ml'),
        a_eln=dict(
            component='NumberEditQuantity',
            # defaultDisplayUnit='ml',
            props=dict(
                minValue=0)))

    substrate_height = Quantity(
<<<<<<< HEAD
        #Link to ontology class 'substrate height'
=======
        #Link to class 'substrate height'
>>>>>>> 2f6c86c (Added links to inkjet printing file)
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005073'],
        type=np.dtype(
            np.float64), unit=('mm'), a_eln=dict(
            component='NumberEditQuantity', defaultDisplayUnit='mm', props=dict(
                minValue=0, maxValue=35)))

    substrate_temperature = Quantity(
<<<<<<< HEAD
<<<<<<< HEAD
        #Link to ontology class 'substrate temperature', Link to ontology class 'substrate temperature setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00009996', 'http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00009995'],
=======
        #Link to class 'substrate temperature'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00009996'],
        #Link to class 'substrate temperature setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00009995'],
>>>>>>> 2f6c86c (Added links to inkjet printing file)
=======
        #Link to class 'substrate temperature', Link to class 'substrate temperature setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00009996', 'http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00009995'],
>>>>>>> 1916ad1 (Fixed double links)
        type=np.dtype(
            np.float64), unit=('°C'), a_eln=dict(
            component='NumberEditQuantity', defaultDisplayUnit='°C', props=dict(
                minValue=20, maxValue=60)))

    cartridge_pressure = Quantity(
<<<<<<< HEAD
<<<<<<< HEAD
        #Link to ontology class 'cartridge pressure', Link to ontology class 'cartridge pressure setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005069', 'http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#cartridge_pressure_setting_datum'],
=======
        #Link to class 'cartridge pressure'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005069'],
        #Link to class 'cartridge pressure setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#cartridge_pressure_setting_datum'],
>>>>>>> 2f6c86c (Added links to inkjet printing file)
=======
        #Link to class 'cartridge pressure', Link to class 'cartridge pressure setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005069', 'http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#cartridge_pressure_setting_datum'],
>>>>>>> 1916ad1 (Fixed double links)
        type=np.dtype(
            np.float64), unit=('mbar'), a_eln=dict(
            component='NumberEditQuantity', defaultDisplayUnit='mbar', props=dict(
                minValue=0, maxValue=38)))

    cartridge_temperature = Quantity(
<<<<<<< HEAD
<<<<<<< HEAD
        #Link to ontology class 'cartridge temperature', Link to ontology class 'cartridge temperature setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005071', 'http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#cartridge_temperature_setting_datum'],
=======
        #Link to class 'cartridge temperature'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005071'],
        #Link to class 'cartridge temperature setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#cartridge_temperature_setting_datum'],
>>>>>>> 2f6c86c (Added links to inkjet printing file)
=======
        #Link to class 'cartridge temperature', Link to class 'cartridge temperature setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005071', 'http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#cartridge_temperature_setting_datum'],
>>>>>>> 1916ad1 (Fixed double links)
        type=np.dtype(
            np.float64), unit=('°C'), a_eln=dict(
            component='NumberEditQuantity', defaultDisplayUnit='°C'))

    print_head_properties = SubSection(
        section_def=PrintHeadProperties)


class LP50InkjetPrintingProperties(InkjetPrintingProperties):
    not_using_lp50_computer = Quantity(
        type=bool,
        shape=[],
        a_eln=dict(
            component='BoolEditQuantity',
        ))

    active_nozzles = Quantity(
        type=MEnum('all', 'Spectra', 'DMC', 'Konika Minolta'),
        shape=[],
        a_eln=dict(
            component='RadioEnumEditQuantity',
        ))

    printer_software = Quantity(
        type=str, a_eln=dict(
            component='StringEditQuantity'))


class LP50InkjetPrinting(WetChemicalDeposition):
    '''Base class for inkjet printing of a layer on a sample'''
    m_def = Section(
<<<<<<< HEAD
        #Link to ontology class 'ink jet printing'
=======
        #Link to class 'ink jet printing'
>>>>>>> 2f6c86c (Added links to inkjet printing file)
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002053'],
    )

    recipe_used = Quantity(
        type=str,
        a_eln=dict(component='FileEditQuantity'),
        a_browser=dict(adaptor='RawFileAdaptor'))

    print_head_used = Quantity(
<<<<<<< HEAD
        #Link to ontology class 'print head', Link to relation 'has participant'
=======
        #Link to class 'print head', Link to relation 'has participant'
>>>>>>> da93fa5 (Started adding links to subsections)
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005064','http://purl.obolibrary.org/obo/RO_0000057'],
        type=str,
        a_eln=dict(component='FileEditQuantity'),
        a_browser=dict(adaptor='RawFileAdaptor'))

    properties = SubSection(
        section_def=LP50InkjetPrintingProperties)

    print_head_path = SubSection(
<<<<<<< HEAD
        #Link to ontology class 'print head path', Link to relation 'has_specified_input'
=======
        #Link to class 'print head path', Link to relation 'has_specified_input'
>>>>>>> da93fa5 (Started adding links to subsections)
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005084','http://purl.obolibrary.org/obo/OBI_0000293'],
        section_def=LP50PrintHeadPath)

    nozzle_voltage_profile = SubSection(
<<<<<<< HEAD
        #Link to ontology class 'print nozzle voltage profile', Link to relation 'has_specified_input'
=======
        #Link to class 'print nozzle voltage profile', Link to relation 'has_specified_input'
>>>>>>> da93fa5 (Started adding links to subsections)
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005083','http://purl.obolibrary.org/obo/OBI_0000293'],
        section_def=LP50NozzleVoltageProfile)

    def normalize(self, archive, logger):
        super(LP50InkjetPrinting, self).normalize(archive, logger)
        self.method = "Inkjet printing"

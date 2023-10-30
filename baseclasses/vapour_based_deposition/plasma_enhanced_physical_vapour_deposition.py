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
import os

from nomad.metainfo import (Quantity, SubSection, Section)
from nomad.datamodel.data import ArchiveSection

from .. import LayerDeposition


class LogData(ArchiveSection):
    m_def = Section(label_quantity='name',
                    a_plot=[
                        {
                            'x': 'time',
                            'y': ['power', 'pressure'],
                            'layout': {
                                "showlegend": True,
                                'yaxis': {
                                    "fixedrange": False},
                                'xaxis': {
                                    "fixedrange": False}},
                        }])
    name = Quantity(type=str)

    power_mean = Quantity(
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        #Link to ontology class 'power'
=======
        #Link to class 'power',
>>>>>>> cd7fa1c (Added links to pevcd, fixed spelling error perovscite)
=======
        #Link to ontology class 'power',
>>>>>>> 8794d04 (Updated 'Link to class' to 'Link to ontology class')
=======
        #Link to ontology class 'power'
>>>>>>> dfae14f (Changed 'process time' & sd links into 'time' & sd links)
        links = ['http://purl.obolibrary.org/obo/PATO_0001024'],
        type=np.dtype(
            np.float64),
        unit=('W'),
        a_eln=dict(
            component='NumberEditQuantity',
            defaultDisplayUnit='W',
            props=dict(
                minValue=0)))

    power_var = Quantity(
        #Link to ontology class 'power'
        links = ['http://purl.obolibrary.org/obo/PATO_0001024'],
        type=np.dtype(
            np.float64),
        unit=('W'),
        a_eln=dict(
            component='NumberEditQuantity',
            defaultDisplayUnit='W',
            props=dict(
                minValue=0)))

    pressure_mean = Quantity(
<<<<<<< HEAD
<<<<<<< HEAD
        #Link to ontology class 'pressure'
=======
        #Link to class 'pressure'
>>>>>>> cd7fa1c (Added links to pevcd, fixed spelling error perovscite)
=======
        #Link to ontology class 'pressure'
>>>>>>> 8794d04 (Updated 'Link to class' to 'Link to ontology class')
        links = ['http://purl.obolibrary.org/obo/PATO_0001025'],
        type=np.dtype(
            np.float64),
        unit=('mbar'),
        a_eln=dict(
            component='NumberEditQuantity',
            defaultDisplayUnit='mbar',
            props=dict(
                minValue=0)))

    pressure_var = Quantity(
        #Link to ontology class 'pressure'
        links = ['http://purl.obolibrary.org/obo/PATO_0001025'],
        type=np.dtype(
            np.float64),
        unit=('mbar'),
        a_eln=dict(
            component='NumberEditQuantity',
            defaultDisplayUnit='mbar',
            props=dict(
                minValue=0)))

    temperature_mean = Quantity(
<<<<<<< HEAD
<<<<<<< HEAD
        #Link to ontology class 'temperature'
=======
        #Link to class 'temperature'
>>>>>>> cd7fa1c (Added links to pevcd, fixed spelling error perovscite)
=======
        #Link to ontology class 'temperature'
>>>>>>> 8794d04 (Updated 'Link to class' to 'Link to ontology class')
        links = ['http://purl.obolibrary.org/obo/PATO_0000146'],
        type=np.dtype(np.float64),
        unit=('°C'),
        a_eln=dict(component='NumberEditQuantity', defaultDisplayUnit='°C'))

    temperature_var = Quantity(
        #Link to ontology class 'temperature'
        links = ['http://purl.obolibrary.org/obo/PATO_0000146'],
        type=np.dtype(np.float64),
        unit=('°C'),
        a_eln=dict(component='NumberEditQuantity', defaultDisplayUnit='°C'))

    power = Quantity(
<<<<<<< HEAD
<<<<<<< HEAD
        #Link to ontology class 'power', Link to ontology class 'power setting datum'
=======
        #Link to class 'power', Link to class 'power setting datum'
>>>>>>> cd7fa1c (Added links to pevcd, fixed spelling error perovscite)
=======
        #Link to ontology class 'power', Link to ontology class 'power setting datum'
>>>>>>> 8794d04 (Updated 'Link to class' to 'Link to ontology class')
        links = ['http://purl.obolibrary.org/obo/PATO_0001024','http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002104'],
        type=np.dtype(
            np.float64),
        shape=['*'],
        unit=('W'),
        a_plot=[
            {
                'x': 'time',
                'y': 'power',
                'layout': {
                    'yaxis': {
                        "fixedrange": False},
                    'xaxis': {
                        "fixedrange": False}},
            }])

    pressure = Quantity(
<<<<<<< HEAD
<<<<<<< HEAD
        #Link to ontology class 'pressure', Link to ontology class 'pressure setting datum'
=======
        #Link to class 'pressure', Link to class 'pressure setting datum'
>>>>>>> cd7fa1c (Added links to pevcd, fixed spelling error perovscite)
=======
        #Link to ontology class 'pressure', Link to ontology class 'pressure setting datum'
>>>>>>> 8794d04 (Updated 'Link to class' to 'Link to ontology class')
        links = ['http://purl.obolibrary.org/obo/PATO_0001025','http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005040'],
        type=np.dtype(
            np.float64),
        shape=['*'],
        unit=('mbar'),
        a_plot=[
            {
                'x': 'time',
                'y': 'pressure',
                'layout': {
                    'yaxis': {
                        "fixedrange": False},
                    'xaxis': {
                        "fixedrange": False}},
            }])

    time = Quantity(
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
>>>>>>> cd7fa1c (Added links to pevcd, fixed spelling error perovscite)
=======
        #Link to ontology class 'time', Link to ontology class 'time setting datum'
        links = ['http://purl.obolibrary.org/obo/PATO_0000165','http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005085'],
>>>>>>> dfae14f (Changed 'process time' & sd links into 'time' & sd links)
        type=np.dtype(
            np.float64),
        shape=['*'],
        unit=('s'))

    temperature = Quantity(
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
>>>>>>> cd7fa1c (Added links to pevcd, fixed spelling error perovscite)
=======
        #Link to ontology class 'temperature', Link to ontology class 'temperature setting datum'
        links = ['http://purl.obolibrary.org/obo/PATO_0000146','http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002071'],
>>>>>>> dfae14f (Changed 'process time' & sd links into 'time' & sd links)
        type=np.dtype(np.float64),
        shape=['*'],
        unit=('°C'),
        a_plot=[
            {
                'x': 'time',
                'y': 'temperature',
                'layout': {
                    'yaxis': {
                        "fixedrange": False},
                    'xaxis': {
                        "fixedrange": False}},
            }])


class GasFlow(ArchiveSection):

    m_def = Section(label_quantity='name')
    name = Quantity(type=str)

    # gas_ref = Quantity(
    #     type=Reference(Gas.m_def),
    #     a_eln=dict(component='ReferenceEditQuantity'))

    gas_str = Quantity(
        type=str,
        a_eln=dict(component='StringEditQuantity'))

    gas_flow_rate = Quantity(
<<<<<<< HEAD
<<<<<<< HEAD
        #Link to ontology class 'gas flow rate', Link to ontology class 'gas flow rate setting datum'
=======
        #Link to class 'gas flow rate', Link to class 'gas flow rate setting datum'
>>>>>>> cd7fa1c (Added links to pevcd, fixed spelling error perovscite)
=======
        #Link to ontology class 'gas flow rate', Link to ontology class 'gas flow rate setting datum'
>>>>>>> 8794d04 (Updated 'Link to class' to 'Link to ontology class')
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002114','http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002108'],
        type=np.dtype(
            np.float64),
        unit=('cm**3/minute'),
        a_eln=dict(
            component='NumberEditQuantity',
            defaultDisplayUnit='cm**3/minute', props=dict(minValue=0)))

    def normalize(self, archive, logger):
        if self.gas_str:
            if self.gas_flow_rate:
                self.name = f"{self.gas_str} {str(self.gas_flow_rate)}"
            else:
                self.name = self.gas_str

        print(self.name)


class PECVDProcess(ArchiveSection):

    power = Quantity(
<<<<<<< HEAD
<<<<<<< HEAD
        #Link to ontology class 'power', Link to ontology class 'power setting datum'
=======
        #Link to class 'power', Link to class 'power setting datum'
>>>>>>> cd7fa1c (Added links to pevcd, fixed spelling error perovscite)
=======
        #Link to ontology class 'power', Link to ontology class 'power setting datum'
>>>>>>> 8794d04 (Updated 'Link to class' to 'Link to ontology class')
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
<<<<<<< HEAD
        #Link to ontology class 'pressure', Link to ontology class 'pressure setting datum'
=======
        #Link to class 'pressure', Link to class 'pressure setting datum'
>>>>>>> cd7fa1c (Added links to pevcd, fixed spelling error perovscite)
=======
        #Link to ontology class 'pressure', Link to ontology class 'pressure setting datum'
>>>>>>> 8794d04 (Updated 'Link to class' to 'Link to ontology class')
        links = ['http://purl.obolibrary.org/obo/PATO_0001025','http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005040'],
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
>>>>>>> cd7fa1c (Added links to pevcd, fixed spelling error perovscite)
=======
        #Link to ontology class 'time', Link to ontology class 'time setting datum'
        links = ['http://purl.obolibrary.org/obo/PATO_0000165','http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005085'],
>>>>>>> dfae14f (Changed 'process time' & sd links into 'time' & sd links)
        type=np.dtype(
            np.float64),
        unit=('s'),
        a_eln=dict(
            component='NumberEditQuantity',
            defaultDisplayUnit='s',
            props=dict(
                minValue=0)))

    temperature = Quantity(
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
>>>>>>> cd7fa1c (Added links to pevcd, fixed spelling error perovscite)
=======
        #Link to ontology class 'temperature', Link to ontology class 'temperature setting datum'
        links = ['http://purl.obolibrary.org/obo/PATO_0000146','http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002071'],
>>>>>>> dfae14f (Changed 'process time' & sd links into 'time' & sd links)
        type=np.dtype(np.float64),
        unit=('°C'),
        a_eln=dict(component='NumberEditQuantity', defaultDisplayUnit='°C'))

    plate_spacing = Quantity(
<<<<<<< HEAD
<<<<<<< HEAD
        #Link to ontology class 'plate spacing'
=======
        #Link to class 'plate spacing'
>>>>>>> cd7fa1c (Added links to pevcd, fixed spelling error perovscite)
=======
        #Link to ontology class 'plate spacing'
>>>>>>> 8794d04 (Updated 'Link to class' to 'Link to ontology class')
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002004'],
        type=np.dtype(
            np.float64), unit=('mm'), a_eln=dict(
            component='NumberEditQuantity', defaultDisplayUnit='mm'), props=dict(
            minValue=0))

    gases = SubSection(
        section_def=GasFlow, repeats=True)

    log_data = SubSection(
        section_def=LogData, repeats=True)


class PECVDeposition(LayerDeposition):
    '''Base class for evaporation of a sample'''

    recipe = Quantity(
        type=str,
        a_eln=dict(component='FileEditQuantity'),
        a_browser=dict(adaptor='RawFileAdaptor'))

    logs = Quantity(
        type=str,
        shape=['*'],
        a_eln=dict(component='FileEditQuantity'),
        a_browser=dict(adaptor='RawFileAdaptor'))

    process = SubSection(
        section_def=PECVDProcess)

    def normalize(self, archive, logger):

        process = PECVDProcess()
        if self.process is not None:
            process = self.process
        if self.recipe is not None and os.path.splitext(self.recipe)[
                1] == ".set":
            from ..helper.parse_files_pecvd_pvcomb import parse_recipe
            with archive.m_context.raw_file(self.recipe) as f:
                parse_recipe(f, process)

        if self.logs is not None:
            logs = []
            for log in self.logs:
                if os.path.splitext(log)[1] == ".log":
                    from ..helper.parse_files_pecvd_pvcomb import parse_log
                    with archive.m_context.raw_file(log) as f:
                        if process.time:
                            data = parse_log(
                                f,
                                process,
                                np.int64(0.9 * process.time),
                                np.int64(0.05 * process.time))
                        else:
                            data = parse_log(f, process)
                        data.name = log
                        logs.append(data)
            process.log_data = logs
        self.process = process

        if self.process is not None and self.process.gases and self.layer_material_name is None:
            formulas = [gas.gas_str.strip() for gas in self.process.gases]
            self.layer_material_name = ",".join(formulas)

        super(PECVDeposition, self).normalize(archive, logger)

        self.method = "Plasma Enhanced Chemical Vapour Deposition"

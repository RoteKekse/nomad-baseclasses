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

from nomad.metainfo import (Quantity)

from nomad.datamodel.data import ArchiveSection


class Annealing(ArchiveSection):
    '''Base class for annealing of a sample'''
    m_def = Section(
        #Link to class 'annealing'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00001033']
    )
    temperature = Quantity(
        #Link to class 'temperature'
        links = ['http://purl.obolibrary.org/obo/PATO_0000146'],
        #Link to class 'annealing temperature'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002001'],
        #Link to class 'annealing temperature setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002073'],
        type=np.dtype(
            np.float64),
        unit=('°C'),
        shape=[],
        a_eln=dict(
            component='NumberEditQuantity',
            defaultDisplayUnit='°C'))

    time = Quantity(
        #Link to class 'time'
        links = ['http://purl.obolibrary.org/obo/PATO_0000165'],
        #Link to class 'process time'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00001063'],
        #Link to class 'process time setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002072'],
        type=np.dtype(
            np.float64),
        unit=('s'),
        shape=[],
        a_eln=dict(
            component='NumberEditQuantity',
            defaultDisplayUnit='minute',
            props=dict(
                minValue=0)))

    # humidity = Quantity(
    #     type=np.dtype(np.float64),
    #     a_eln=dict(component='NumberEditQuantity'))

    # function = Quantity(
    #     type=str,
    #     a_eln=dict(component='StringEditQuantity',
    #                props=dict(
    #                    suggestions=[
    #                        'Top Annealing',
    #                        'Annealing after deposition',
    #                    ])))


# class AnnealingStandAlone(Annealing,ProcessOnSample):
#     def normalize(self, archive, logger):
#         super(Annealing, self).normalize(archive, logger)

#         self.method = "Annealing"

# class ThermalAnnealing(AnnealingStandAlone):
#     pass


# class SolventAnnealing(AnnealingStandAlone):
#     solvent = Quantity(
#         type=Reference(Chemical.m_def),
#         a_eln=dict(component='ReferenceEditQuantity'))

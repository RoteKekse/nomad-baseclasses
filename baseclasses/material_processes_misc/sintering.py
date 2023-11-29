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


class Sintering(ArchiveSection):
    '''Base class for sintering of a sample'''
    temperature = Quantity(
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        #Link to ontology class 'temperature', Link to ontology class 'temperature setting datum'
        links = ['http://purl.obolibrary.org/obo/PATO_0000146','http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002111'],
=======
        #Link to class 'temperature'
<<<<<<< HEAD
        link = ['http://purl.obolibrary.org/obo/PATO_0000146'],
>>>>>>> 2bfcffa (First Commit, added links in files annealing, quenching, sintering, wet chemical depo, dip coating, spin coating, spray pyrolysis, slot die coating)
=======
        links = ['http://purl.obolibrary.org/obo/PATO_0000146'],
        #Link to class 'temperature setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002111'],
>>>>>>> ff6f4e2 (Corrected files from previous commit)
=======
        #Link to ontology class 'temperature', Link to ontology class 'temperature setting datum'
        links = ['http://purl.obolibrary.org/obo/PATO_0000146','http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002111'],
>>>>>>> da2afee (Added links to 'material_processes_misc and fixed structure of older links)
=======
        #Link to ontology class 'temperature', Link to ontology class 'temperature setting datum'
        links = ['http://purl.obolibrary.org/obo/PATO_0000146','http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002111'],
>>>>>>> 273b34793553e64e4e271202f9f7bbff0e56ed58
        type=np.dtype(
            np.float64),
        unit=('°C'),
        shape=[],
        a_eln=dict(
            component='NumberEditQuantity',
            defaultDisplayUnit='°C'))

    time = Quantity(
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        #Link to ontology class 'process time', Link to ontology class 'process time setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00001063','http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002072'],
=======
        #Link to class 'process time'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00001063'],
        #Link to class 'process time setting datum'
<<<<<<< HEAD
        link = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002072'],
>>>>>>> 2bfcffa (First Commit, added links in files annealing, quenching, sintering, wet chemical depo, dip coating, spin coating, spray pyrolysis, slot die coating)
=======
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002072'],
>>>>>>> ff6f4e2 (Corrected files from previous commit)
=======
        #Link to ontology class 'process time', Link to ontology class 'process time setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00001063','http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002072'],
>>>>>>> da2afee (Added links to 'material_processes_misc and fixed structure of older links)
=======
        #Link to ontology class 'process time', Link to ontology class 'process time setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00001063','http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002072'],
>>>>>>> 273b34793553e64e4e271202f9f7bbff0e56ed58
        type=np.dtype(
            np.float64),
        unit=('s'),
        shape=[],
        a_eln=dict(
            component='NumberEditQuantity',
            defaultDisplayUnit='minute',
            props=dict(
                minValue=0)))

    ramp = Quantity(
        type=np.dtype(
            np.float64),
        unit=('s'),
        shape=[],
        a_eln=dict(
            component='NumberEditQuantity',
            defaultDisplayUnit='minute',
            props=dict(
                minValue=0)))


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

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
    SubSection,
    Reference)
from nomad.datamodel.data import ArchiveSection

from nomad.datamodel.metainfo.eln import Entity

from .wet_chemical_deposition import WetChemicalDeposition


class SpinCoatingRecipeSteps(ArchiveSection):
    m_def = Section(label_quantity='name')

    name = Quantity(type=str,
                    a_eln=dict(component='StringEditQuantity'))

    time = Quantity(
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        #Link to ontology class 'process time', Link to ontology class 'process time setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00001063', 'http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002072'],
=======
        #Link to class 'process time'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00001063'],
        #Link to class 'process time setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002072'],
>>>>>>> 2bfcffa (First Commit, added links in files annealing, quenching, sintering, wet chemical depo, dip coating, spin coating, spray pyrolysis, slot die coating)
=======
        #Link to class 'process time', Link to class 'process time setting datum'
=======
        #Link to ontology class 'process time', Link to ontology class 'process time setting datum'
>>>>>>> 8794d04 (Updated 'Link to class' to 'Link to ontology class')
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00001063', 'http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002072'],
>>>>>>> 1916ad1 (Fixed double links)
=======
        #Link to ontology class 'time', Link to ontology class 'time setting datum'
        links = ['http://purl.obolibrary.org/obo/PATO_0000165', 'http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005085'],
>>>>>>> 273b347 (Modified spin coating)
=======
        #Link to ontology class 'time', Link to ontology class 'time setting datum'
        links = ['http://purl.obolibrary.org/obo/PATO_0000165', 'http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00005085'],
>>>>>>> 273b34793553e64e4e271202f9f7bbff0e56ed58
        type=np.dtype(
            np.float64),
        unit=('s'),
        a_eln=dict(
            component='NumberEditQuantity',
            defaultDisplayUnit='s',
            props=dict(
                minValue=0)))

    speed = Quantity(
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        #Link to ontology class 'rotation speed', Link to ontology class 'rotation speed setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002026', 'http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002005'],
=======
        #Link to class 'rotation speed'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002026'],
        #Link to class 'rotation speed setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002005'],
>>>>>>> 2bfcffa (First Commit, added links in files annealing, quenching, sintering, wet chemical depo, dip coating, spin coating, spray pyrolysis, slot die coating)
=======
        #Link to class 'rotation speed', Link to class 'rotation speed setting datum'
=======
        #Link to ontology class 'rotation speed', Link to ontology class 'rotation speed setting datum'
>>>>>>> 8794d04 (Updated 'Link to class' to 'Link to ontology class')
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002026', 'http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002005'],
>>>>>>> 1916ad1 (Fixed double links)
=======
        #Link to ontology class 'rotation speed', Link to ontology class 'rotation speed setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002026', 'http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002005'],
>>>>>>> 273b34793553e64e4e271202f9f7bbff0e56ed58
        type=np.dtype(
            np.float64),
        unit=('rpm'),
        a_eln=dict(
            component='NumberEditQuantity',
            defaultDisplayUnit='rpm',
            props=dict(
                minValue=0)))

    acceleration = Quantity(
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        #Link to ontology class 'rotation acceleration', Link to ontology class 'rotation acceleration setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002049', 'http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002002'],
=======
        #Link to class 'rotation acceleration'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002049'],
        #Link to class 'rotation acceleration setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002002'],
>>>>>>> 2bfcffa (First Commit, added links in files annealing, quenching, sintering, wet chemical depo, dip coating, spin coating, spray pyrolysis, slot die coating)
=======
        #Link to class 'rotation acceleration', Link to class 'rotation acceleration setting datum'
=======
        #Link to ontology class 'rotation acceleration', Link to ontology class 'rotation acceleration setting datum'
>>>>>>> 8794d04 (Updated 'Link to class' to 'Link to ontology class')
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002049', 'http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002002'],
>>>>>>> 1916ad1 (Fixed double links)
=======
        #Link to ontology class 'rotation acceleration', Link to ontology class 'rotation acceleration setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002049', 'http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002002'],
>>>>>>> 273b34793553e64e4e271202f9f7bbff0e56ed58
        type=np.dtype(
            np.float64),
        unit=('rpm/s'),
        a_eln=dict(
            component='NumberEditQuantity',
            defaultDisplayUnit='rpm/s'))


class SpinCoatingRecipe(Entity):

    steps = SubSection(
        section_def=SpinCoatingRecipeSteps, repeats=True)


class SpinCoating(WetChemicalDeposition):
    '''Base class for spin coating of a sample'''
    m_def = Section(
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        #Link to ontology class 'spin coating'
=======
        #Link to class 'spin coating'
>>>>>>> 2bfcffa (First Commit, added links in files annealing, quenching, sintering, wet chemical depo, dip coating, spin coating, spray pyrolysis, slot die coating)
=======
        #Link to ontology class 'spin coating'
>>>>>>> 8794d04 (Updated 'Link to class' to 'Link to ontology class')
=======
        #Link to ontology class 'spin coating'
>>>>>>> 273b34793553e64e4e271202f9f7bbff0e56ed58
        links = ['http://purl.obolibrary.org/obo/CHMO_0001472'],
    )

    recipe = Quantity(
        type=Reference(SpinCoatingRecipe.m_def),
        a_eln=dict(component='ReferenceEditQuantity'))

    recipe_steps = SubSection(
        section_def=SpinCoatingRecipeSteps, repeats=True)

    def normalize(self, archive, logger):
        super(SpinCoating, self).normalize(archive, logger)
        self.method = "Spin Coating"

        if self.recipe_steps is None and self.recipe and self.recipe.steps is not None:
            steps = [step for step in self.recipe.steps]
            self.recipe_steps = steps

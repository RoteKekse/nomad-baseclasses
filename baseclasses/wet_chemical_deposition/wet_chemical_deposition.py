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
    SubSection, Section
)

from nomad.datamodel.data import ArchiveSection
from ..solution import Solution
from .. import LayerDeposition
from ..material_processes_misc import Annealing, Quenching, Sintering
from baseclasses.helper.utilities import rewrite_json_recursively


class PrecursorSolution(ArchiveSection):

    m_def = Section(label_quantity='name',
<<<<<<< HEAD
                    #Link to ontology class 'precursor solution'
                    links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00001081'],
=======
                    #Link to class 'precursor solution'
<<<<<<< HEAD
                    links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00001081']
>>>>>>> 2bfcffa (First Commit, added links in files annealing, quenching, sintering, wet chemical depo, dip coating, spin coating, spray pyrolysis, slot die coating)
=======
                    links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00001081'],
>>>>>>> ff6f4e2 (Corrected files from previous commit)
                    )
    name = Quantity(type=str)

    reload_referenced_solution = Quantity(
        type=bool,
        default=False,
        a_eln=dict(component='ButtonEditQuantity')
    )

    solution = Quantity(
<<<<<<< HEAD
        #Link to ontology class 'Solution'
=======
        #Link to class 'Solution'
>>>>>>> 2bfcffa (First Commit, added links in files annealing, quenching, sintering, wet chemical depo, dip coating, spin coating, spray pyrolysis, slot die coating)
        links = ['http://purl.obolibrary.org/obo/CHEBI_75958'],
        type=Reference(Solution.m_def),
        a_eln=dict(component='ReferenceEditQuantity', label="Solution Reference"))

    solution_volume = Quantity(
<<<<<<< HEAD
        #Link to ontology class 'volume setting datum', Link to ontology class 'volume'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002158', 'http://purl.obolibrary.org/obo/PATO_0000918'],
=======
        #Link to class 'volume setting datum'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002158'],
        #Link to class 'volume'
        links = ['http://purl.obolibrary.org/obo/PATO_0000918'],
>>>>>>> 2bfcffa (First Commit, added links in files annealing, quenching, sintering, wet chemical depo, dip coating, spin coating, spray pyrolysis, slot die coating)
        type=np.dtype(
            np.float64),
        unit=('ml'),
        a_eln=dict(
            component='NumberEditQuantity',
            defaultDisplayUnit='ml',
            props=dict(
                minValue=0)))

    solution_details = SubSection(
        section_def=Solution)

    def normalize(self, archive, logger):

        if self.reload_referenced_solution and self.solution:
            self.reload_referenced_solution = False
            rewrite_json_recursively(archive, "reload_referenced_solution", False)
            self.solution_details = self.solution.m_copy()

        if self.solution and self.solution.name:
            if self.solution_volume:
                self.name = self.solution.name + \
                    ' ' + str(self.solution_volume)
            else:
                self.name = self.solution.name

        if self.solution_details and self.solution_details.name:
            if self.solution_volume:
                self.name = self.solution_details.name + \
                    ' ' + str(self.solution_volume)
            else:
                self.name = self.solution_details.name


def copy_solutions(sol):
    if not sol.solution:
        return
    if sol.solution_details:
        return

    sol.solution_details = sol.solution.m_copy(deep=True)
    sol.solution = None

    if not sol.solution_details.other_solution:
        return
    for sol_other in sol.solution_details.other_solution:
        copy_solutions(sol_other)


class WetChemicalDeposition(LayerDeposition):
    '''Wet Chemical Deposition'''
    m_def = Section(
<<<<<<< HEAD
<<<<<<< HEAD
        #Link to ontology class 'wet chemical deposition'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002051'],
    )
    
=======
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002051']
    )
    #Die folgenden Qualitäten wurden nicht verlinkt/in den Mutterklassen verlinkt, da importiert.
>>>>>>> 2bfcffa (First Commit, added links in files annealing, quenching, sintering, wet chemical depo, dip coating, spin coating, spray pyrolysis, slot die coating)
=======
        #Link to class 'wet chemical deposition'
        links = ['http://www.semanticweb.org/ot2661/ontologies/2022/8/TFSCO#TFSCO_00002051'],
    )
    
>>>>>>> ff6f4e2 (Corrected files from previous commit)
    solution = SubSection(
        #Link to relation 'has specified input'
        section_def=PrecursorSolution, repeats=True, links = ['http://purl.obolibrary.org/obo/OBI_0000293'])
    #Link to relation 'has part'
    annealing = SubSection(section_def=Annealing, links = ['http://purl.obolibrary.org/obo/RO_0001019'])
    #Link to relation 'has part'
    quenching = SubSection(section_def=Quenching, links = ['http://purl.obolibrary.org/obo/RO_0001019'])
    #Link to relation 'has part'
    sintering = SubSection(section_def=Sintering, repeats=True, links = ['http://purl.obolibrary.org/obo/RO_0001019'])

    def normalize(self, archive, logger):
<<<<<<< HEAD
<<<<<<< HEAD
        super(WetChemicalDeposition, self).normalize(archive, logger)

        if self.samples and self.solution:
            for wc_sol in self.solution:
                copy_solutions(wc_sol)
=======
        super(WetChemicalDeposition, self).normalize(archive, logger)
>>>>>>> fad3d17 (First Commit, added links in files annealing, quenching, sintering, wet chemical depo, dip coating, spin coating, spray pyrolysis, slot die coating)
=======
        super(WetChemicalDeposition, self).normalize(archive, logger)
>>>>>>> 2bfcffa (First Commit, added links in files annealing, quenching, sintering, wet chemical depo, dip coating, spin coating, spray pyrolysis, slot die coating)

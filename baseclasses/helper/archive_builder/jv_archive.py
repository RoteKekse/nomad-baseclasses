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

import os

from nomad.units import ureg

from baseclasses.solar_energy.jvmeasurement import SolarCellJVCurveCustom


def get_jv_archive(jv_dict, mainfile, jvm):

    jvm.file_name = os.path.basename(mainfile)
    jvm.active_area = jv_dict['active_area'] if 'active_area' in jv_dict else None
    jvm.intensity = jv_dict['intensity'] if 'intensity' in jv_dict else None
    jvm.integration_time = jv_dict['integration_time'] if 'integration_time' in jv_dict else None
    jvm.settling_time = jv_dict['settling_time'] if 'settling_time' in jv_dict else None
    jvm.averaging = jv_dict['averaging'] if 'averaging' in jv_dict else None
    jvm.compliance = jv_dict['compliance'] if 'compliance' in jv_dict else None
    jvm.jv_curve = []

    for curve_idx, curve in enumerate(jv_dict['jv_curve']):
        jv_set = SolarCellJVCurveCustom(
            cell_name=curve['name'],
            voltage=curve['voltage'],
            current_density=curve['current_density'],
            light_intensity=jv_dict['intensity'] if 'intensity' in jv_dict else None,
            open_circuit_voltage=round(
                jv_dict['V_oc'][curve_idx],
                2) * ureg('V'),
            short_circuit_current_density=round(
                jv_dict['J_sc'][curve_idx],
                2) * ureg('mA/cm^2'),
            fill_factor=round(
                jv_dict['Fill_factor'][curve_idx],
                2) * 0.01,
            efficiency=round(
                jv_dict['Efficiency'][curve_idx],
                2),
            potential_at_maximum_power_point=round(
                jv_dict['U_MPP'][curve_idx],
                2) * ureg('V'),
            current_density_at_maximun_power_point=round(
                jv_dict['J_MPP'][curve_idx],
                2) * ureg('mA/cm^2'),
            series_resistance=round(
                    jv_dict['R_ser'][curve_idx],
                    2) * ureg('ohm*cm^2'),
            shunt_resistance=round(
                        jv_dict['R_par'][curve_idx],
                        2) * ureg('ohm*cm^2'),
        )
        jvm.jv_curve.append(jv_set)
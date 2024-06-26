#  Copyright (c) 2020 KTH Royal Institute of Technology
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

# Example config file for an inverted pendulum inverted_pendulum
import os

from cleave.api.plant import SimpleConstantActuator, \
    SimpleSensor
from cleave.impl.inverted_pendulum import InvPendulumStateWithViz

host = 'localhost'
port = 5000

tick_rate = 100
emu_duration = '10s'

state = InvPendulumStateWithViz(
    fail_angle_rad=int(os.getenv('FAIL_ANGLE_RAD', -1)),
    pend_mass=float(os.getenv('PEND_MASS', 0.2)),
    pend_length=float(os.getenv('PEND_LEN', 1.2))
)

sample_rate = int(os.getenv('SAMPLE_RATE', 100))
sensors = [
    SimpleSensor('position', sample_rate),
    SimpleSensor('speed', sample_rate),
    SimpleSensor('angle', sample_rate),
    SimpleSensor('ang_vel', sample_rate),
]

actuators = [
    SimpleConstantActuator(0, prop_name='force')
]

output_dir = 'plant_metrics'

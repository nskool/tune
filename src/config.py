#  Copyright 2021 Hugging Face Inc.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from dataclasses import dataclass
from logging import getLogger

from omegaconf import MISSING
from transformers import __version__ as transformers_version

from backends import BackendConfig


LOGGER = getLogger("benchmark")


@dataclass()
class BenchmarkConfig:
    # Store the transformers version used during the benchmark
    transformers_version: str = transformers_version

    # Number of forward pass to run before recording any performance counters.
    warmup_runs: int = 5

    # Duration in seconds the benchmark will collect performance counters
    benchmark_duration: int = 5

    # The backend to use for recording timing (pytorch, torchscript, tensorflow, xla, onnxruntime)
    backend: BackendConfig = MISSING

    # Name of the model used for the benchmark
    model: str = MISSING

    # CPU or CUDA device to run inference on
    device: str = MISSING

    # The dtype of the model to run inference with (float32, float16, int8, bfloat16)
    precision: str = MISSING

    # Use Transparent Huge Page mechanis to increase CPU cache hit probability
    use_huge_page: bool = False

    # Number of sample given to the model at each forward
    batch_size: int = 1

    # The length of the sequence (in tokens) given to the model
    sequence_length: int = MISSING

    # Number of // model to allocate
    num_instances: int = 1

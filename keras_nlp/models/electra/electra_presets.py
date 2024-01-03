# Copyright 2023 The KerasNLP Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Electra model presets and configurations."""

backbone_presets = {
    "google/electra-base-generator": {
        "metadata": {
            "description": (
                "Base Electra generator model from Google."
                "ELECTRA models are trained to distinguish 'real' input tokens vs 'fake' input "
                "tokens generated by another neural network, similar to the discriminator of a GAN.",
            ),
            "params": "33576960 ",
            "official_name": "Electra",
            "path": "electra",
            "model_card": "https://huggingface.co/google/electra-base-generator",
        },
        "config": {
            "vocab_size": 30522,
            "embedding_dim": 768,
            "num_layers": 12,
            "num_heads": 4,
            "hidden_dim": 256,
            "intermediate_dim": 1024,
            "dropout": 0.1,
            "max_sequence_length": 512,
        },
        "preprocessor_config": {
            "lowercase": False,
        },
        # TODO: Upload weights on GCS.
        "weights_url": "https://storage.googleapis.com/pranav-keras/electra-base-generator/model.weights.h5",
        "weights_hash": "e712b170dd9077cf60b52431698c9b0b",
        "vocabulary_url": "https://storage.googleapis.com/pranav-keras/electra-base-generator/vocab.txt",
        "vocabulary_hash": "64800d5d8528ce344256daf115d4965e",
    },
    "google/electra-small-generator": {
        "metadata": {
            "description": (
                "Small Electra generator model from Google."
                "ELECTRA models are trained to distinguish 'real' input tokens vs 'fake' input "
                "tokens generated by another neural network, similar to the discriminator of a GAN.",
            ),
            "params": "13548800",
            "official_name": "Electra",
            "path": "electra",
            "model_card": "https://huggingface.co/google/electra-small-generator",
        },
        "config": {
            "vocab_size": 30522,
            "embedding_dim": 128,
            "num_layers": 12,
            "num_heads": 4,
            "hidden_dim": 256,
            "intermediate_dim": 1024,
            "dropout": 0.1,
            "max_sequence_length": 512,
        },
        "preprocessor_config": {
            "lowercase": True,
        },
        # TODO: Upload weights on GCS.
        "weights_url": "https://storage.googleapis.com/pranav-keras/electra-small-generator/model.weights.h5",
        "weights_hash": "fbb12bccdf9316898b74e32daee493a5",
        "vocabulary_url": "https://storage.googleapis.com/pranav-keras/electra-small-generator/vocab.txt",
        "vocabulary_hash": "64800d5d8528ce344256daf115d4965e",
    },
    "google/electra-small-discriminator": {
        "metadata": {
            "description": (
                "Small Electra discriminator model from Google."
                "ELECTRA models are trained to distinguish 'real' input tokens vs 'fake' input "
                "tokens generated by another neural network, similar to the discriminator of a GAN.",
            ),
            "params": "13548800",
            "official_name": "Electra",
            "path": "electra",
            "model_card": "https://huggingface.co/google/electra-small-discriminator",
        },
        "config": {
            "vocab_size": 30522,
            "embedding_dim": 128,
            "num_layers": 12,
            "num_heads": 4,
            "hidden_dim": 256,
            "intermediate_dim": 1024,
            "dropout": 0.1,
            "max_sequence_length": 512,
        },
        "preprocessor_config": {
            "lowercase": True,
        },
        # TODO: Upload weights on GCS.
        "weights_url": "https://storage.googleapis.com/pranav-keras/electra-small-discriminator/model.weights.h5",
        "weights_hash": "07737662bb3623e3476d2d58d3d5894b",
        "vocabulary_url": "https://storage.googleapis.com/pranav-keras/electra-small-discriminator/vocab.txt",
        "vocabulary_hash": "64800d5d8528ce344256daf115d4965e",
    },
    "google/electra-base-discriminator": {
        "metadata": {
            "description": (
                "Base Electra discriminator model from Google."
                "ELECTRA models are trained to distinguish 'real' input tokens vs 'fake' input "
                "tokens generated by another neural network, similar to the discriminator of a GAN.",
            ),
            "params": "109482240",
            "official_name": "Electra",
            "path": "electra",
            "model_card": "https://huggingface.co/google/electra-base-discriminator",
        },
        "config": {
            "vocab_size": 30522,
            "embedding_dim": 768,
            "num_layers": 12,
            "num_heads": 12,
            "hidden_dim": 768,
            "intermediate_dim": 3072,
            "dropout": 0.1,
            "max_sequence_length": 512,
        },
        "preprocessor_config": {
            "lowercase": False,
        },
        # TODO: Upload weights on GCS.
        "weights_url": "https://storage.googleapis.com/pranav-keras/electra-base-discriminator/model.weights.h5",
        "weights_hash": "312a5be02eba68cab29527f6a9090526",
        "vocabulary_url": "https://storage.googleapis.com/pranav-keras/electra-base-discriminator/vocab.txt",
        "vocabulary_hash": "64800d5d8528ce344256daf115d4965e",
    },
}
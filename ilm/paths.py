import os
import pathlib

_LIB_DIR = os.path.dirname(os.path.join(pathlib.Path(__file__).absolute()))
_REPO_DIR = os.path.dirname(_LIB_DIR)

OFFICIAL_GPT2_ENCODER_DIR = os.path.join(_LIB_DIR, 'official_gpt2_encoder')

RUS_GPT2_ENCODER_DIR = os.path.join(_LIB_DIR, '..', 'rus_gpt2')

RUS_SBERT_ENCODER_DIR = os.path.join(_LIB_DIR, '..', 'rus_sbert')

RAW_DATA_DIR = os.path.join(_REPO_DIR, 'data', 'raw_data')

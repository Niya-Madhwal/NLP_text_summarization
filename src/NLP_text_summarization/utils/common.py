import os
import sys
from box.exceptions import BoxValueError
import yaml
from box import ConfigBox
from src.NLP_text_summarization.logging import logger
from ensure import ensure_annotations
from pathlib import Path
from typing  import Any


@ensure_annotations
def read_yaml(file_path: Path) -> ConfigBox:
    try:
        with open(file_path) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {file_path} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
@ensure_annotations    
def creating_directories(path_to_directory: list, verbose=True):
    for path in path_to_directory:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")

    

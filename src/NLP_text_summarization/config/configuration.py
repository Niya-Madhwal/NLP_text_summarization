from src.NLP_text_summarization.constants import *
from src.NLP_text_summarization.utils.common import read_yaml, creating_directories
from src.NLP_text_summarization.entity import DataIngestionConfig, DataTransformationConfig

class ConfigurationManager:
    def __init__(self,
                config_path=CONFIG_FILE_PATH,
                params_file_path=PARAMS_FILE_PATH):
        self.config = read_yaml(config_path)
        self.params = read_yaml(params_file_path)

        creating_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self)-> DataIngestionConfig: ##reading  asll configs in data_ingestion config
        config= self.config.data_ingestion
        creating_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir= config.root_dir,
            source_URL= config.source_URL,
            local_data_file= config.local_data_file,
            unzip_dir = config.unzip_dir

        )

        return data_ingestion_config
    
    def get_data_transformation_config(self)-> DataTransformationConfig:
        config = self.config.data_transformation

        creating_directories([config.root_dir])

        data_transformation_config =DataTransformationConfig(
                    root_dir= config.root_dir,
                    data_path= config.data_path,
                    tokenizer_name= config.tokenizer_name
            
        )
        return  data_transformation_config
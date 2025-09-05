from src.NLP_text_summarization.logging import logger
from src.NLP_text_summarization.config.configuration import ConfigurationManager
from src.NLP_text_summarization.components.data_ingestion import DataIngestionConfig
from src.NLP_text_summarization.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"

try :
    logger.info(f"{STAGE_NAME} started")
    data_ingestion_pipeline = DataIngestionTrainingPipeline()
    data_ingestion_pipeline.initiate_data_ingestion()
    logger.info(f"{STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e
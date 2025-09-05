from src.NLP_text_summarization.logging import logger
from src.NLP_text_summarization.config.configuration import ConfigurationManager
from src.NLP_text_summarization.components.data_tranformation import DataTransformationConfig
from src.NLP_text_summarization.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.NLP_text_summarization.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline
from src.NLP_text_summarization.pipeline.model_evalaution_pipeline import ModelEvaluationTrainingPipeline
from src.NLP_text_summarization.pipeline.model_trainer_pipeline import ModelTrainerPipeline
from src.NLP_text_summarization.components.model_trainer import ModelTrainer
STAGE_NAME = "Data Ingestion Stage"

try :
    logger.info(f"{STAGE_NAME} started")
    data_ingestion_pipeline = DataIngestionTrainingPipeline()
    data_ingestion_pipeline.initiate_data_ingestion()
    logger.info(f"{STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation Stage"

try :
    logger.info(f"{STAGE_NAME} started")
    data_ingestion_pipeline = DataTransformationTrainingPipeline()
    data_ingestion_pipeline.initiate_data_transformation()
    logger.info(f"{STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME="Model Trainer stage"

try:
    logger.info(f"stage {STAGE_NAME} initiated")
    model_trainer_pipeline=ModelTrainerPipeline()
    model_trainer_pipeline.initiate_model_trainer()
    logger.info(f"Stage {STAGE_NAME} Completed")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Evaluation stage"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_evaluation = ModelEvaluationTrainingPipeline()
   model_evaluation.initiate_model_evaluation()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e




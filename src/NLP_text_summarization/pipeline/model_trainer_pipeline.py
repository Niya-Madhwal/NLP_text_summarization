from src.NLP_text_summarization.config.configuration import ModelTrainerConfig, ConfigurationManager
from src.NLP_text_summarization.components.model_trainer import ModelTrainer


class ModelTrainerPipeline:
    def __init__(self):
        pass
    def initiate_model_trainer(self):
            config = ConfigurationManager()
            model_trainer_config = config.get_model_trainer_config()
            model_trainer = ModelTrainer(config=model_trainer_config)
            model_trainer.train()
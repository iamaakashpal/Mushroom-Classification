import os,sys
from mushroom.logger import logging
from mushroom.exception import CustomException
from mushroom.config.configuration import Configuration
from mushroom.entity.artifact_entity import DataIngestionArtifact

class DataIngestion:
    def __init__(self) -> None:
        try:
            pass
        except Exception as e:
            raise CustomException(e,sys) from e

    def initiated_data_ingestion() -> DataIngestionArtifact:
        try:
            pass
        except Exception as e:
            raise CustomException(e,sys) from e
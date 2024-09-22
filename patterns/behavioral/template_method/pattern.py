import logging
from abc import ABC, abstractmethod

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Document(ABC):
    def create_document(self):
        self.open()
        self.write_content()
        self.add_metadata()
        self.save()
        self.close()

    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def write_content(self):
        pass

    @abstractmethod
    def add_metadata(self):
        pass

    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def close(self):
        pass


class PDFDocument(Document):
    def open(self):
        logger.info("Opening PDF document.")

    def write_content(self):
        logger.info("Writing PDF content.")

    def add_metadata(self):
        logger.info("Adding metadata to PDF.")

    def save(self):
        logger.info("Saving PDF document.")

    def close(self):
        logger.info("Closing PDF document.")


class WordDocument(Document):
    def open(self):
        logger.info("Opening Word document.")

    def write_content(self):
        logger.info("Writing Word content.")

    def add_metadata(self):
        logger.info("Adding metadata to Word document.")

    def save(self):
        logger.info("Saving Word document.")

    def close(self):
        logger.info("Closing Word document.")

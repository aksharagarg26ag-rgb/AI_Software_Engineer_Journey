from pathlib import Path
#path = "data/resumes/resume1.txt" - instead of writing this, pathlib automatically creates path
import config
import logging

logger= logging.getLogger(__name__)

#UTF-8 can correctly read almost every language and symbol.
#Without it,some systems may show ���� or throw encoding errors.

class Upload:

    # Supported file formats
    SUPPORTED_EXTENSIONS = {".txt", ".pdf", ".docx"}

    def __init__(self):
        self.resume_folder = Path(config.RESUME_FOLDER)
        self.job_folder = Path(config.JOB_FOLDER)

    def _validate_file(self, file_path: Path):

        if not file_path.exists():
            logger.error(f"File not found: {file_path}")
            raise FileNotFoundError(f"File not found: {file_path}")

        if file_path.suffix.lower() not in self.SUPPORTED_EXTENSIONS:
            logger.error(f"Unsupported file type: {file_path.suffix}")
            raise ValueError(
                f"Unsupported file type '{file_path.suffix}'. "
                f"Supported types are: {self.SUPPORTED_EXTENSIONS}"
            )
        
    def load_document(self, folder: Path, filename: str):
        file_path = folder / filename
        #Path("data") / "resume.txt" -> data/resume.txt
        logger.info(f"Loading document: {file_path}")
        self._validate_file(file_path)
        return file_path
    
    def load_resume(self, filename: str):
        
        return self._load_document(self.resume_folder, filename)

    def load_job(self, filename: str):
     
        return self._load_document(self.job_folder, filename)
       
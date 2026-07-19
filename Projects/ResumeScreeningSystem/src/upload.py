from pathlib import Path #path = "data/resumes/resume1.txt" - instead of writing this, pathlib automatically creates path
import config

#UTF-8 can correctly read almost every language and symbol.
#Without it,some systems may show ���� or throw encoding errors.

class Upload:

    def __init__(self):
        self.resume_folder = Path(config.RESUME_FOLDER)
        self.job_folder = Path(config.JOB_FOLDER)

    def load_resume(self, filename):

        file_path = self.resume_folder / filename

        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()

    def load_job(self, filename):

        file_path = self.job_folder / filename

        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
        

from src.upload import Upload
from src.extractor import TextExtractor
from utils.preprocessing import clean_text
from src.chunking import ResumeChunker
from src.embedding import SentenceEmbedding
from src.vector_database import VectorDatabase
from src.retriever import Retriever
from src.skill_analysis import SkillAnalyzer
from src.report import ReportGenerator
from src.prompt_builder import PromptBuilder
from src.llm_feedback import LLMFeedback

    

# Create Objects
uploader = Upload()

extractor = TextExtractor()

chunker = ResumeChunker()

embedding_model = SentenceEmbedding()

analyzer = SkillAnalyzer()

report_generator = ReportGenerator()
prompt_builder = PromptBuilder()
llm = LLMFeedback()


    

#Upload files
resume = uploader.load_resume("resume2.txt")
job_description = uploader.load_job("job_description.txt")

# Clean Text
resume_text = extractor.extract_text(resume)
job_text = extractor.extract_text(job_description)

clean_resume = clean_text(resume_text)
clean_job = clean_text(job_text)

# Chunk Resume
resume_chunks = chunker.chunk_text(clean_resume)

# Generate Embeddings
resume_embeddings = embedding_model.generate_embeddings(resume_chunks)
job_embedding = embedding_model.generate_embeddings([clean_job])

 # Build Vector Database
dimension = resume_embeddings.shape[1]
vector_db = VectorDatabase(dimension)
vector_db.add_embeddings(resume_embeddings)

# Retrieve Relevant Chunks
retriever = Retriever(vector_db)

retrieved_chunks = retriever.retrieve(
    job_embedding)

analysis = analyzer.analyze(
    resume_text,
    job_text
)

prompt = prompt_builder.build_prompt( retrieved_chunks,  job_text)

feedback = llm.generate(prompt)

report = report_generator.generate_report(analysis,  feedback)

#Print Report
print("\n========== ATS REPORT ==========\n")

# for key, value in report.items():

#         print(f"{key} : {value}")


for key, value in report.items():

    print()

    print("=" * 50)

    print(key)

    print("=" * 50)

    print(value)
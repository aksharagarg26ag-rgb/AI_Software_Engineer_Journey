def build_prompt(resume_sections, job_description):

    context = "\n\n".join(resume_sections)

    prompt = f"""
    You are an experienced technical recruiter.

    Job Description

    {job_description}

    Candidate Resume Sections

    {context}

    Tasks

    1. Summarize the candidate.
    2. Identify strengths.
    3. Identify missing skills.
    4. Suggest improvements.
    5. Estimate ATS score out of 100.
    6. Recommend whether to shortlist the candidate.

    Return the answer in clear bullet points.
    """

    return prompt
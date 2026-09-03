import json
import time
from pydantic import BaseModel, Field
from typing import List
from google import genai
from google.genai import types

# ==========================================
# 1. PYDANTIC MODELS
# ==========================================


class Role(BaseModel):
    title: str
    company: str
    dates: str
    tailored_bullets: List[str] = Field(
        description="Exactly 3 bullet points tailored to the target job description.")


class TailoredCVData(BaseModel):
    summary: str = Field(
        description="A 3-4 sentence professional summary tailored to the job description.")
    roles: List[Role]


class ChatResponse(BaseModel):
    intent: str = Field(
        description="Must be 'chat' or 'cv'. Use 'cv' if the user pastes a job description or asks for a tailored resume. Otherwise use 'chat'.")
    reply: str = Field(
        description="If 'chat', answer the question in the first-person as Alfred. If 'cv', acknowledge the job description and say you are generating the CV.")

# ==========================================
# 2. CV GENERATOR FUNCTION
# ==========================================


def generate_tailored_content(master_data: dict, job_desc: str, api_key: str) -> TailoredCVData:
    client = genai.Client(api_key=api_key)
    experience_payload = {
        "master_experience": master_data.get("master_experience", [])}

    prompt = f"""
    You are an expert technical recruiter tailoring a resume. Your task is to select and refine 
    my existing experience to match the target job description.
    
    CRITICAL RULES:
    1. FILTER IRRELEVANT ROLES: Evaluate each job role in the master data. If a role has no relevance to the target job description, OMIT IT entirely.
    2. STRICT FACTUAL ACCURACY: You must ONLY use the facts, tools, and experiences explicitly listed in the Master Resume Data.
    3. NO HALLUCINATION: Do NOT invent, fabricate, or make up any jobs, metrics, responsibilities, or skills.
    4. REPHRASING ALLOWED: Select the most relevant bullet points and rephrase them to highlight their relevance to the target job, but the core achievement must remain 100% true.
    
    Target Job Description:
    {job_desc}
    
    Master Resume Data:
    {json.dumps(experience_payload)}
    """

    max_retries = 3
    for attempt in range(max_retries):
        try:
            response = client.models.generate_content(
                model='gemini-3.6-flash',
                contents=prompt,
                config=types.GenerateContentConfig(
                    response_mime_type="application/json",
                    response_schema=TailoredCVData,
                    temperature=0.1
                )
            )
            return response.parsed

        except Exception as e:
            if "503" in str(e) and attempt < (max_retries - 1):
                time.sleep(5)
                continue
            else:
                raise e

# ==========================================
# 3. CHAT INTENT ROUTER FUNCTION
# ==========================================


def process_chat_message(master_data: dict, user_input: str, api_key: str) -> ChatResponse:
    client = genai.Client(api_key=api_key)

    prompt = f"""
    You are an AI chatbot acting as Alfred Malinga. 
    
    CRITICAL RULES:
    1. STRICT FACTUAL ACCURACY: You must ONLY use the facts and experiences listed in the Master Data below.
    2. NO HALLUCINATION: Do NOT invent skills, hobbies, or past jobs. If you don't know the answer based on the data, say so politely.
    3. BEHAVIOR: Answer in the first-person ("I am...", "I worked..."). Be professional, concise, and friendly.
    4. INTENT DETECTION: If the user pastes a job description or asks for a CV/resume, set intent to 'cv' and reply with a brief acknowledgment (e.g., "I see you provided a job description! I am generating a tailored CV for you now.").
    
    Master Data:
    {json.dumps(master_data)}
    
    User Message:
    {user_input}
    """

    max_retries = 3
    for attempt in range(max_retries):
        try:
            response = client.models.generate_content(
                model='gemini-3.6-flash',
                contents=prompt,
                config=types.GenerateContentConfig(
                    response_mime_type="application/json",
                    response_schema=ChatResponse,
                    temperature=0.3
                )
            )
            return response.parsed

        except Exception as e:
            if "503" in str(e) and attempt < (max_retries - 1):
                time.sleep(5)
                continue
            else:
                raise e

# This module analyzes Jenkins logs using OpenAI's GPT model to identify issues, errors, or warnings.
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY is not set in the environment variables.")

client = OpenAI(api_key=api_key)

def analyze_log(log_content: str) -> str:

    prompt = f"""
    You are an expert in analyzing Jenkins logs. 
    Please analyze the following Jenkins log and provide a detailed summary of any issues, errors, or warnings found in the log. 
    If there are no issues, please state that the log appears to be clean.

    Log Content:
    {log_content}
    """

    response = client.responses.create(
        model="gpt-4o-mini",
        instructions=prompt,
        input= f"""Analyze the provided Jenkins log content and summarize any issues, errors, or warnings found. If there are no issues, state that the log appears to be clean.
        <jenkins_log>
        {log_content}
        </jenkins_log>
        """,
    )

    return response.output_text


    
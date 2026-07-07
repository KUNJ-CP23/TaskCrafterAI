import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def extract_tasks(meeting_notes):

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"""
You are an AI Project Manager.

Extract every task from the meeting notes.

Return ONLY a valid JSON array.

Requirements:
- One task per JSON object.
- Do not merge tasks.
- If owner is missing, use "Unassigned".
- If due date is missing, use "".
- If priority is not mentioned, infer High, Medium or Low.

Return exactly in this format:

[
    {{
        "task": "",
        "owner": "",
        "due_date": "",
        "priority": ""
    }}
]

Meeting Notes:

{meeting_notes}
"""
    )

    return response.text
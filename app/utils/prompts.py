def doctor_prompt(symptoms: str, language: str) -> str:
    """
    Generates a prompt for diagnosing symptoms.
    """
    return f"""
You are a highly experienced doctor. Please perform the following tasks:
1. Analyze the given symptoms provided by the patient and determine the most likely diagnosis.
2. Provide a detailed explanation of the possible conditions associated with these symptoms.
3. Suggest a course of action for the patient, such as visiting a specialist or performing specific tests.
4. Respond strictly in the language specified by the user.

Patient's Input:
Symptoms: {symptoms}
Language: {language}

Format your response in clear markdown.
"""

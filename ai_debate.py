# ai_debate.py
from config import API_KEYS, MODELS, claude_client, openai_client, genai, deepseek_client

def query_all_models(prompt: str) -> dict:
    """Get responses from all AI models in parallel"""
    responses = {}
    
    # Query Claude
    try:
        claude_response = claude_client.messages.create(
            model=MODELS["CLAUDE"],
            max_tokens=2000,
            messages=[{"role": "user", "content": prompt}]
        )
        responses["claude"] = claude_response.content[0].text
    except Exception as e:
        print(f"⚠️ Claude Error: {str(e)[:100]}...")
        responses["claude"] = None

    # Query ChatGPT
    try:
        chatgpt_response = openai_client.chat.completions.create(
            model=MODELS["CHATGPT"],
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        responses["chatgpt"] = chatgpt_response.choices[0].message.content
    except Exception as e:
        print(f"⚠️ ChatGPT Error: {str(e)[:100]}...")
        responses["chatgpt"] = None

    # Query Gemini Flash
    try:
        gemini_model = genai.GenerativeModel(MODELS["GEMINI_FLASH"])
        gemini_response = gemini_model.generate_content(prompt)
        responses["gemini"] = gemini_response.text
    except Exception as e:
        print(f"⚠️ Gemini Error: {str(e)[:100]}...")
        responses["gemini"] = None

    return responses

def deepseek_analysis(responses: dict, original_prompt: str) -> str:
    """Use DeepSeek to analyze and debate the responses"""
    debate_prompt = f"""
    [ROLE]
    You are the Supreme AI Arbiter. Analyze these responses to:
    "{original_prompt}"
    
    [RESPONSES]
    {chr(10).join([f"{model.upper()}: {response}" for model, response in responses.items() if response])}
    
    [TASK]
    1. Identify common ground
    2. Highlight contradictions
    3. Provide final verdict with reasoning
    4. Format as Markdown with headings
    """
    
    try:
        response = deepseek_client.chat.completions.create(
            model=MODELS["DEEPSEEK_REASONER"],
            messages=[{"role": "user", "content": debate_prompt}],
            temperature=0.3,
            max_tokens=3000
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"🚨 DeepSeek Analysis Failed: {str(e)[:200]}"

if __name__ == "__main__":
    # Example usage
    user_prompt = "Should humans pursue AGI development given current alignment challenges?"
    
    print("🔄 Collecting model responses...")
    responses = query_all_models(user_prompt)
    
    print("\n🔍 Analyzing with DeepSeek...")
    analysis = deepseek_analysis(responses, user_prompt)
    
    print("\n=== FINAL ANALYSIS ===")
    print(analysis)

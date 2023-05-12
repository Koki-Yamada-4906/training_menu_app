import openai

        
def call_openai_gpt():
    openai.api_key = "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"
    prompt = "今、一番人気の旅行先を教えて"
    response = openai.Completion.create(
        engine="text-curie-001",
        prompt=prompt,
        max_tokens=1048,
        n=1,
        stop=None,
        temperature=1,
    )
    print(response["choices"][0]["text"])
call_openai_gpt()
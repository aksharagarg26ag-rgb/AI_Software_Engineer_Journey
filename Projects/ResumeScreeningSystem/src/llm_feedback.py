import google.generativeai as genai
import config

genai.configure(api_key=config.GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


class LLMFeedback:

    def generate(self, prompt):

        response = model.generate_content(prompt)

        return response.text
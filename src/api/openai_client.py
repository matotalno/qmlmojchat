import os
import logging
from openai import AsyncOpenAI
from dotenv import load_dotenv

logger = logging.getLogger(__name__)

class OpenAIClient:
    def __init__(self):
        load_dotenv()
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            raise ValueError("OPENAI_API_KEY nije pronađen u environment varijablama")
        
        self.client = AsyncOpenAI(api_key=api_key)
        self.model = os.getenv('OPENAI_MODEL', 'gpt-4-turbo-preview')
        self.temperature = float(os.getenv('TEMPERATURE', '0.7'))
        self.max_tokens = int(os.getenv('MAX_TOKENS', '2000'))
        
        logger.info(f"OpenAI Client inicijalizovan sa modelom: {self.model}")
        
    async def get_streaming_response(self, message):
        try:
            if not message.strip():
                raise ValueError("Prazna poruka")

            logger.debug("Započinjem streaming odgovor")
            response = await self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": message}],
                stream=True,
                max_tokens=self.max_tokens,
                temperature=self.temperature
            )
            
            async for chunk in response:
                if chunk.choices[0].delta.content:
                    yield chunk.choices[0].delta.content
                    
        except Exception as e:
            logger.error(f"Greška u API pozivu: {e}", exc_info=True)
            yield f"Došlo je do greške: {str(e)}"

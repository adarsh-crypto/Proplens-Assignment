from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import aiohttp
import logging

app = FastAPI()

logger = logging.getLogger(__name__)

class RequestItem(BaseModel):
    messages: list
    stream: bool
    use_context: bool

STREAM = False
USE_CONTEXT = True

async def fetch_response(request_item: RequestItem) -> str:
    async with aiohttp.ClientSession() as session:
        try:
            async with session.post('http://0.0.0.0:8069/v1/chat/completions', json=request_item.dict()) as response:
                response.raise_for_status()
                data = await response.json()
                content = data['choices'][0]['message']['content']
                return content
        except (aiohttp.ClientError, KeyError, IndexError) as e:
            logger.error(f"Error fetching response: {e}")
            raise HTTPException(status_code=500, detail="Failed to fetch model response")
    
@app.post("/api/")
async def get_response(user_message_data: dict):
    try:
        user_message_content = user_message_data.get("content", "")
        
        system_message_content = """

        You are an expert AI model specialized in natural language processing and real estate data analysis. Your task is to serve as the core of a Question and Answer (QnA) system designed to fetch accurate information from a dataset of real estate projects. 
        Your primary goals are:

            Accurate Information Retrieval: Extract precise and relevant answers from the dataset based on the questions asked, ensuring the responses are directly aligned with the data provided.

            Scalability: Handle queries efficiently, even as the dataset scales to include up to 100 projects. Ensure that your responses remain accurate and timely, with minimal latency.

            Hallucination Prevention: Validate the information in your responses to avoid any "hallucinations" (i.e., generating information that is not present in the dataset). If uncertain, prioritize providing a response that reflects this uncertainty rather than generating potentially false data.

            Context Awareness: Maintain awareness of the context within each query and the dataset. Understand and utilize the relationships between different data points to provide comprehensive answers.

            API Integration: Operate within an API environment, responding to multiple concurrent requests while maintaining accuracy and low latency.

            Documentation and Testing: Assist in documenting any bugs, suggesting fixes, and improving the system's overall performance. Ensure that your responses are consistent with testing results.
            
        """
                
        request_item = RequestItem(
            messages=[
                {"role": "system", "content": system_message_content},
                {"role": "user", "content": user_message_content}
            ],
            stream=STREAM,
            use_context=USE_CONTEXT
        )
        
        content = await fetch_response(request_item)
        return {"content": content}
    except HTTPException as e:
        raise e
    except Exception as e:
        logger.error(f"Internal server error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
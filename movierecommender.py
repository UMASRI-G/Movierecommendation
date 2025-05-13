
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

# Load the OpenAI API key from .env
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def recommend_movies(favorite_movie, genre=None, language=None):
    llm = ChatOpenAI(model="gpt-4o", temperature=0.7)

    system_message = SystemMessage(
        content=(
            "You are a movie expert who recommends good movies. "
            "Consider user's favorite movie, genre, language, and suggest similar movies with a short reason."
        )
    )

    user_input = f"My favorite movie is '{favorite_movie}'."
    if genre:
        user_input += f" I like the genre '{genre}'."
    if language:
        user_input += f" I prefer movies in '{language}'."

    messages = [
        system_message,
        HumanMessage(content=user_input)
    ]

    response = llm.invoke(messages)
    return response.content

# For command-line testing
if __name__ == "__main__":
    fav = input("Your favorite movie: ")
    genre = input("Preferred genre (optional): ")
    lang = input("Preferred language (optional): ")
    
    recommendations = recommend_movies(fav, genre, lang)
    print("\n🎥 Movie Recommendations:\n")
    print(recommendations)
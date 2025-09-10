from crewai import Agent
from langchain_openai import ChatOpenAI
import os
from tools.vision_tools import BlipImageCaptioner
from langchain.tools import Tool


llm =llm = ChatOpenAI(
    model="gpt-4",
    api_key=os.environ["OPENAI_API_KEY"]
)


caption_interpreter = Agent(
    role="Image Analyst",
    goal="Generate detailed and accurate captions from images using BLIP model",
    backstory="""You are an expert computer vision analyst with years of experience 
            in image interpretation. Your specialty is extracting detailed visual information 
            from images and converting them into comprehensive, descriptive captions that 
            capture not just objects, but mood, atmosphere, and visual storytelling elements.""",
    
    tools=[BlipImageCaptioner.caption_image],
    llm=llm,
    verbose=True,
    allow_delegation=False
)


lore_agent = Agent(
    role="World Building Architect",
    goal="Craft engaging storylines that weave together characters and setting",
    backstory="""You are a seasoned storyteller and narrative architect with deep 
            understanding of story structure, pacing, and dramatic tension. You excel at 
            creating plots that are both surprising and inevitable, with compelling conflicts 
            and satisfying resolutions.""",
    llm=llm,
    verbose=True,
    allow_delegation=False
)

character_agent = Agent(
    role="Character Development Specialist",
    goal="Create compelling characters based on visual elements from the image caption",
    backstory="""You are a master character developer with expertise in psychology, 
            literature, and human behavior. You excel at taking visual cues and transforming 
            them into rich, multi-dimensional characters with compelling backstories, motivations, 
            and personality traits. Your characters feel real and relatable. short descriptions.""",
    llm=llm,
    verbose=True,
    allow_delegation=False
)


story_agent = Agent(
    role="Story Synthesis Master",
    goal="Combine all elements into a cohesive, engaging final story with a plot and genre(comedy or suspense or drama).Plot driven not character driven",
    backstory="""You are a master storyteller and editor with exceptional ability to 
            synthesize diverse narrative elements into polished, engaging stories. Your 
            expertise lies in maintaining consistency, ensuring proper pacing, and creating 
            prose that captivates readers from beginning to end. Make a story with defined start and end plots preferably a moral. it should have a comedy or drama or suspense element to it. story should be plot driven not character driven.""",
    llm=llm,
    verbose=True,
    allow_delegation=False
)




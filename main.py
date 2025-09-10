from dotenv import load_dotenv
load_dotenv()

from crewai import Agent ,Crew
from agents import caption_interpreter, lore_agent, character_agent, story_agent
from tasks import StoryTasks

if __name__ == "__main__":
    image_path = input("Enter the image filename : ")

 
    task_builder = StoryTasks(image_path)
    tasks = task_builder.all_tasks()

    crew = Crew(
        agents=[caption_interpreter, lore_agent, character_agent, story_agent],
        tasks=tasks,
        verbose=True
    )

    result = crew.kickoff()
    print("\n\n FINAL STORY OUTPUT \n")
    print(result)

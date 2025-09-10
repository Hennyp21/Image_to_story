from crewai import Task
from agents import caption_interpreter, lore_agent, character_agent, story_agent

class StoryTasks:
    def __init__(self, image_path: str):
     
        self.caption_task = Task(
            agent=caption_interpreter,
            description=f"Generate a description for the given image: {image_path}.",
            expected_output="A concise caption describing the image content.Be thorough and descriptive to provide rich material for story creation."
        )


        self.character_task = Task(
            agent=character_agent,
            description="""Based on the image caption provided, create 2-3 compelling characters for a  {{context}}For each character, develop:
            -
            - Motivations and goals
            - Relationships to other characters
            - How they connect to the visual elements from the image
            
            Make characters feel authentic and multi-dimensional.
            """,
            expected_output="Facts or context related to the image.",
            context=[self.caption_task]
        )

     
        self.lore_task = Task(
    description="Using this image caption, craft a fantasy world's setting and historical background: {{context}}",
    expected_output="A vivid and creative backstory for the fantasy world and set a plot where the characters can interact and the stoy  unfolds",
    agent=lore_agent,
    context=[self.caption_task]
)

        
        self.story_task = Task(
    description="Write a final approximate 200-word short story based on the caption, characters: {{context}}",
    expected_output="A captivating fantasy story with a clear structure and imaginative flow. With a defined start and end points preferably a moral. i should have comedy or horror or suspense elemnts and should have a plot",
    agent=story_agent,
    context=[self.caption_task, self.lore_task, self.character_task]
)

    def all_tasks(self):
        return [
            self.caption_task,
            self.character_task,
            self.lore_task,
            self.story_task
        ]

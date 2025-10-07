SYSTEM_PROMPT = """
Based on the provided topics (TaskTopic) and task rarity (TaskRarity), generate a task (Task) with the following fields:
    title (task name),
    description (task description, no more than two short sentences),
    experience (amount of experience, a multiple of 10, from 10 to 100),
    currencyReward (in-game currency reward, calculated as experience divided by 2 (Must be only integer number)),
    agility (agility, from 0 to 10),
    strength (strength, from 0 to 10),
    intelligence (intelligence, from 0 to 10).

Conditions:
    1. The task name and description must correspond to the provided topics (TaskTopic).
    2. Task rarity (TaskRarity) determines:
        - Experience: COMMON (10-20), UNCOMMON (30-40), RARE (50-60), EPIC (70-80), LEGENDARY (90-100).
        - Completion time: COMMON (5-30 minutes), UNCOMMON (30-60 minutes), RARE (1-2 hours), EPIC (2-4 hours), LEGENDARY (several hours, up to the end of the day).
        - Maximum attribute points: COMMON (2), UNCOMMON (4), RARE (6), EPIC (8), LEGENDARY (10).
    3. Attribute values (agility, strength, intelligence) must strictly depend on the task type:
        - If the task does not imply improvement of a specific attribute, its value must be 0.
        - The sum of all attributes must not exceed the maximum for the task's rarity.
    4. Tasks must be achievable by any person, regardless of their current conditions.
    5. Tasks must be creative and diverse, but should not cause the user to feel shame, discomfort, or awkwardness.
    6. If the task relates to physical activity (PHYSICAL_ACTIVITY),
       it must be genuinely beneficial and aimed at improving the user's physical characteristics.
       Use well-known exercise routines such as push-ups, squats, running, planks, and others.
       The difficulty level and number of repetitions must correspond to the task's rarity.
    7. Tasks must not resemble children's games or fantastical activities (e.g., "walking on an imaginary rope").
       They must be realistic and useful for improving physical, mental, or social skills.
    8. Return fields STRICTLY only in the name and format that I indicated to you
    
    Output the result as a valid JSON object
"""


def generate_task_user_prompt(topics: list[str], rarity: str) -> str:
    return f"TaskTopics: [{', '.join(topics)}], TaskRarity: {rarity}"

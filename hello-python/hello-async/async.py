import asyncio
import random
import time

story = [
    "A shepherd boy tended his master’s sheep near a dark forest.",
    "He found it rather dull and decided to have some fun.",
    "He ran toward the village shouting, 'Wolf! Wolf! The Wolf is chasing the sheep!'",
    "The villagers rushed to his aid, only to find there was no wolf.",
    "The boy laughed, enjoying the trick.",
    "He repeated the prank another day, and the villagers fell for it again.",
    "Then one evening, a real wolf attacked his flock.",
    "The boy ran toward the village crying louder than before, 'Wolf! Wolf!'",
    "But this time, no one came. They thought he was lying again.",
    "The wolf destroyed the flock, and the boy learned a hard lesson.",
]

async def random_sleep():
    min_time = 2
    max_time = 3
    delay = random.randint(min_time, max_time)
    print(f"\nRunning task in the background that will take from {min_time} to {max_time} seconds. \n")
    await asyncio.sleep(delay)
    print(f"\nBackground task is now complete. \n")

async def print_story():
    for line in story:
        print(line)
        await asyncio.sleep(0.5)

async def gather_tasks(*tasks):
    await asyncio.gather(*tasks)

if __name__=="__main__":
    # The five steps to async code:
    # 1. Use a library that has async functions. Here we use asyncio.sleep(), but it could be something like openAI's async version of their API call.
    # 2. Put `await` in front of the async function call. 
    #    This is special in two ways: First, it is blocking within it's function, so nothing runs after `await` in that function until that line completes.
    #    Second, it is non-blocking for any other async function outside the definition. `await` is the point in the code where it gives back control to the event loop.
    # 3. Put `async` in front of any function that has an `await` in it.
    # 4. `asyncio.run()` is required to call any function with `async` in front of it.
    # 5. `asyncio.gather()` is required to get any benefit from async. It allows you to run multiple async functions at once. Wrap it in an async helper function to use it.
    asyncio.run(gather_tasks(random_sleep(), print_story())) 

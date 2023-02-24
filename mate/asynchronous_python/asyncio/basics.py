import asyncio
import random

# A co-routine
async def add(x: int, y: int):
    # function can do work between 1 second to 5 seconds
    await asyncio.sleep(random.randrange(1, 5))
    return x + y

# Create a function to schedule co-routines on the event loop
# then print results
async def get_results():
    result = None
    try:
        # Wait for 3 seconds for co-routine to execute
        result = await asyncio.wait_for(add(3, 4), timeout=3)
    except asyncio.exceptions.TimeoutError:
        result = "fallback payload"

    print(result)

asyncio.run(get_results())
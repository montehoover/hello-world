# Hello Async

Run with:
```
python async.py
```

There are five steps to writing async code:
1. You must use a prebuilt library that has async functions. Examples:
   ```python
   asyncio.sleep(0.5)
   ```
   or
   ```python
   httpx.AsyncClient().get("www.google.com")
   ```
2. Put `await` in front of the async function call.
   ```python
   await asyncio.sleep(0.5)
   ```
   or
   ```python
   await httpx.AsyncClient().get("www.google.com")
   ``` 
   This is special in two ways: First, it is blocking within it's function, so nothing runs after `await` in that function until that line completes.
   Second, it is non-blocking for any other async function outside the definition. `await` is the point in the code where it gives back control to the event loop.
3. Put `async` in front of any function that has an `await` in it.
   ```python
   async def random_sleep():
       await asyncio.sleep(random.randint(5, 10))
   ```
4. `asyncio.run()` is required to call any function with `async` in front of it.
   ```python
   asyncio.run(random_sleep())
   ```
5. `asyncio.gather()` is required to get any benefit from async. It allows you to run multiple async functions at once. Wrap it in an async helper function to use it.
   ```python
   async def gather_tasks(*tasks):
       await asyncio.gather(*tasks)
   
   asyncio.run(gather_tasks(random_sleep(), print_story()))
   ```
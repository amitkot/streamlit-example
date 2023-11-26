import streamlit as st
import asyncio
from datetime import datetime


# Define the asynchronous function
async def async_function():
    # Example async operation
    await asyncio.sleep(5)  # Simulating a delay
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# Function to run the async function and return the result
def run_async_function():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    result = loop.run_until_complete(async_function())
    loop.close()
    return result


# Define an asynchronous generator
async def async_generator():
    for i in range(5):
        await asyncio.sleep(1)
        yield f"Data piece {i}"


# Function to run the async generator and update the output container
async def run_async_code(output_container):
    async for data in async_generator():
        output_container.write(data)


# Streamlit app layout
st.title("Streamlit Async Example")

# Create a container to display results
output_container = st.container()

# Button to start the async generator
if st.button("Run Async Generator"):
    # Clear the previous output in the container
    output_container.empty()

    # Run the async generator and update the container
    asyncio.run(run_async_code(output_container))

# When the button is clicked
if st.button("Run Async Function"):
    with st.spinner("Running async function..."):
        result = run_async_function()
        st.success(f"Async function completed! Result: {result}")

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


# Streamlit app layout
st.title("Asyncio in Streamlit")

# When the button is clicked
if st.button("Run Async Function"):
    with st.spinner("Running async function..."):
        result = run_async_function()
        st.success(f"Async function completed! Result: {result}")

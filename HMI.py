import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="M2R Platform",
    page_icon=":recycle:",  # You can replace this with an actual icon
    layout="wide",  # For a wider layout
)

# Custom CSS for Styling (inline for simplicity)
st.markdown(
    """
    <style>
    body {
        font-family: sans-serif;
    }
    .container {
        max-width: 1200px;
        margin: 0 auto;
        padding: 20px;
    }
    .hero {
        background-color: #f0f0f0; /* Light gray background */
        padding: 50px 0;
        text-align: center;
    }
    .hero h1 {
        font-size: 3em;
        margin-bottom: 20px;
    }
    .hero p {
        font-size: 1.2em;
        margin-bottom: 30px;
    }
    .hero button {
        background-color: #007bff; /* Blue button */
        color: white;
        padding: 15px 30px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 1em;
    }
    .hero button:hover {
        background-color: #0056b3; /* Darker blue on hover */
    }
    /* Add more styles for other sections as needed */
    </style>
    """,
    unsafe_allow_html=True,
)

# Header
st.markdown(
    """
    <header>
        <div class="container">
            <nav>
                <div class="logo">
                    <img src="https://placehold.co/150x50?text=M2R+Logo" alt="M2R Logo"> 
                </div>
                <ul>
                    <li><a href="#">Home</a></li>
                    <li><a href="#">About Us</a></li>
                    <li><a href="#">Services</a></li>
                    <li><a href="#">Transaction</a></li>
                    <li><a href="#">Contact Us</a></li>
                </ul>
            </nav>
        </div>
    </header>
    """,
    unsafe_allow_html=True,
)

# Hero Section
st.markdown(
    """
    <section class="hero">
        <div class="container">
            <h1>Hello! World Changer</h1>
            <p>Cluttered with castoffs??? Don't chuck it, chuck it into cash instead!</p>
            <div class="buttons">
                <button onclick="window.location.href = 'login_page.html';">Login</button> 
                <button onclick="window.location.href = 'signup_page.html';">Sign Up</button> 
            </div>
        </div>
    </section>
    """,
    unsafe_allow_html=True,
)

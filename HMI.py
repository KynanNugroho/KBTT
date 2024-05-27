import streamlit as st

st.set_page_config(page_title="M2R Platform", page_icon="logo.png")

# Header
st.markdown(
    """
    <header>
        <div class="container">
            <nav>
                <div class="logo">
                    <img src="logo.png" alt="M2R Logo">
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
                <button class="login-btn">Login</button>
                <button class="signup-btn">Sign Up</button>
            </div>
        </div>
    </section>
    """,
    unsafe_allow_html=True,
)

# About Section
st.markdown(
    """
    <section class="about">
        <div class="container">
            <h2>Welcome to M2R Platform</h2>
            <p>M2R "Market of Recycle Rubbish" is a digital platform that allows users to sell recyclable waste, buy recyclable waste, and find waste banks (collection bosses) in the East Java region.</p>
        </div>
    </section>
    """,
    unsafe_allow_html=True,
)

# Services Section
st.markdown(
    """
    <section class="services">
        <div class="container">
            <h2>Our Services</h2>
            <div class="service-items">
                <div class="service-item">
                    <img src="sell-icon.png" alt="Sell Waste">
                    <h3>Sell Waste</h3>
                    <p>Turn your recyclable waste into cash.</p>
                </div>
                <div class="service-item">
                    <img src="buy-icon.png" alt="Buy Waste">
                    <h3>Buy Waste</h3>
                    <p>Find recyclable materials for your needs.</p>
                </div>
                <div class="service-item">
                    <img src="trash-bank-icon.png" alt="Trash Bank">
                    <h3>Trash Bank</h3>
                    <p>Locate waste banks in East Java.</p>
                </div>
            </div>
        </div>
    </section>
    """,
    unsafe_allow_html=True,
)

# Footer
st.markdown(
    """
    <footer>
        <div class="container">
            <p>&copy; 2023 M2R Platform</p>
        </div>
    </footer>
    """,
    unsafe_allow_html=True,
)

        

# app.py
import streamlit as st
import streamlit.components.v1 as components
import matplotlib.pyplot as plt
import numpy as np
import io
from PIL import Image

# Page config
st.set_page_config(
    page_title="Advanced Conic Sections",
    layout="wide",
    initial_sidebar_state="collapsed"
)

@st.cache_data
def generate_conic_images():
    """Generate matplotlib plots for each conic section"""
    images = {}

    plt.style.use('default')

    # Circle
    fig, ax = plt.subplots(figsize=(3, 3), facecolor='white')
    theta = np.linspace(0, 2*np.pi, 100)
    x = 2 * np.cos(theta)
    y = 2 * np.sin(theta)
    ax.plot(x, y, 'red', linewidth=4)
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    ax.set_title('Circle', fontsize=14, fontweight='bold')
    ax.set_facecolor('white')
    buf = io.BytesIO()
    plt.savefig(buf, format='png', facecolor='white', bbox_inches='tight', dpi=100)
    buf.seek(0)
    images['Circle'] = buf
    plt.close()

    # Ellipse
    fig, ax = plt.subplots(figsize=(3, 3), facecolor='white')
    x = 2.5 * np.cos(theta)
    y = 1.5 * np.sin(theta)
    ax.plot(x, y, 'blue', linewidth=4)
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    ax.set_title('Ellipse', fontsize=14, fontweight='bold')
    ax.set_facecolor('white')
    buf = io.BytesIO()
    plt.savefig(buf, format='png', facecolor='white', bbox_inches='tight', dpi=100)
    buf.seek(0)
    images['Ellipse'] = buf
    plt.close()

    # Parabola
    fig, ax = plt.subplots(figsize=(3, 3), facecolor='white')
    x = np.linspace(-2, 2, 100)
    y = x**2
    ax.plot(x, y, 'gold', linewidth=4)
    ax.set_xlim(-3, 3)
    ax.set_ylim(-0.5, 4)
    ax.grid(True, alpha=0.3)
    ax.set_title('Parabola', fontsize=14, fontweight='bold')
    ax.set_facecolor('white')
    buf = io.BytesIO()
    plt.savefig(buf, format='png', facecolor='white', bbox_inches='tight', dpi=100)
    buf.seek(0)
    images['Parabola'] = buf
    plt.close()

    # Hyperbola
    fig, ax = plt.subplots(figsize=(3, 3), facecolor='white')
    x1 = np.linspace(1.5, 3, 50)
    x2 = np.linspace(-3, -1.5, 50)
    y1 = np.sqrt(x1**2 - 1)
    y2 = -np.sqrt(x1**2 - 1)
    y3 = np.sqrt(x2**2 - 1)
    y4 = -np.sqrt(x2**2 - 1)
    ax.plot(x1, y1, 'green', linewidth=4)
    ax.plot(x1, y2, 'green', linewidth=4)
    ax.plot(x2, y3, 'green', linewidth=4)
    ax.plot(x2, y4, 'green', linewidth=4)
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.grid(True, alpha=0.3)
    ax.set_title('Hyperbola', fontsize=14, fontweight='bold')
    ax.set_facecolor('white')
    buf = io.BytesIO()
    plt.savefig(buf, format='png', facecolor='white', bbox_inches='tight', dpi=100)
    buf.seek(0)
    images['Hyperbola'] = buf
    plt.close()

    return images

# Header
st.markdown("""
    <div style="background: linear-gradient(to right, #1f4037, #99f2c8); padding: 30px; text-align: center;">
        <h1 style="color: black; margin-bottom: 5px;">
            🌐 Advanced Conic Sections
        </h1>
        <div style="color: #333; font-style: italic; font-size: 1.1rem;">
            From 2D Mathematical Theory to 3D Real-World Applications
        </div>
    </div>
""", unsafe_allow_html=True)

# Description
st.markdown("""
<div style="background-color: #111; color: white; padding: 20px; font-size: 1rem;">
This interactive visualization demonstrates how conic sections (circle, ellipse, parabola, hyperbola) emerge from the intersection of a plane with a double-napped cone. Use the controls to change the angle and position of the slicing plane. This mimics real-world applications such as satellite dish design (parabola), planetary orbits (ellipse), and navigation systems (hyperbola).
</div>
""", unsafe_allow_html=True)

# New 3D/2D Explanation Section
st.markdown("""
### 🧠 Visualizing 3D to 2D: How Conic Sections Are Formed
This diagram shows how a slicing plane intersects a cone to produce the familiar 2D graphs:
- Circles and ellipses from horizontal and angled slices
- Parabolas from parallel slices
- Hyperbolas from intersecting both nappes

These visuals bridge algebra with spatial reasoning — a powerful tool for geometry learners.
""")

try:
    image = Image.open("a4d3bf3f-4eb8-42de-ad44-51fbee1326ba.png")
    st.image(image, caption="Combined 3D Cone Slices and 2D Graphs", use_column_width=True)
except Exception as e:
    st.error(f"Could not load the updated 3D/2D image: {e}")

# Remaining app content omitted for brevity...
# You can copy the rest of the code from your working app here

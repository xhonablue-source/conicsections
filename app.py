# app.py
import streamlit as st
import streamlit.components.v1 as components
import matplotlib.pyplot as plt
import numpy as np
import io

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

# Learning Objectives + h,k definitions
st.markdown("""
### 🔍 Learning Objectives
- Understand the geometric construction of conic sections
- Explore the relationship between slicing angles and conic shapes
- Connect mathematical theory to real-world applications

**Standards Alignment:**
- HSG.GPE.A.2 – Derive the equation of a parabola given a focus and directrix  
- HSG.GPE.A.1 – Derive the equation of a circle given its center and radius

---

### 📍 Understanding h and k
In all conic section equations, **`h` and `k`** represent the coordinates of the **center** (or **vertex**, for parabolas):  
- `h` shifts the graph **left or right**  
- `k` shifts the graph **up or down**  
So the point **(h, k)** tells you where the conic section is positioned on the graph.
""")

# Visual Aid Chart with Generated Images
st.markdown("""
### 🔹 Visual Aid: Match Shapes, Equations, and Descriptions
""")

try:
    conic_images = generate_conic_images()
    cols = st.columns(4)
    conic_data = {
        "Circle": ("(x - h)² + (y - k)² = r²", "Red circle centered at (h,k)"),
        "Ellipse": ("(x - h)² / a² + (y - k)² / b² = 1", "Blue stretched oval across axes"),
        "Parabola": ("(y - k)² = 4p(x - h)", "Yellow curved V shape"),
        "Hyperbola": ("(y - k)² / a² - (x - h)² / b² = 1", "Green mirrored arcs (open sideways)")
    }
    for i, (shape, (eq, desc)) in enumerate(conic_data.items()):
        with cols[i]:
            st.image(conic_images[shape], caption=shape, use_container_width=True)
            st.markdown(f"**Equation**: `{eq}`\n\n**Visual**: {desc}")
except Exception as e:
    st.error(f"Error generating images: {e}")

# Matching Chart for Conic Types
st.markdown("""
### ↺ Conic Section Matching Activity
Match the conic section type with its equation and shape. Use the dropdowns to select and test your understanding. Visual learners should use the color-coded shape descriptions above as a reference.
""")

col1, col2, col3 = st.columns(3)
with col1:
    conic_type = st.selectbox("🔹 Select Conic Type", ["Circle", "Ellipse", "Parabola", "Hyperbola"])
with col2:
    equation = st.selectbox("🏢 Match Equation", [
        "(x - h)² + (y - k)² = r²",
        "(x - h)² / a² + (y - k)² / b² = 1",
        "(y - k)² = 4p(x - h)",
        "(y - k)² / a² - (x - h)² / b² = 1"
    ])
with col3:
    sketch = st.selectbox("📈 Match Shape Description", [
        "Red circle centered at (h,k)",
        "Blue stretched oval across axes",
        "Yellow curved V shape",
        "Green mirrored arcs (open sideways)"
    ])

# Feedback
if st.button("🔎 Check Match"):
    correct = (conic_type == "Circle" and equation == "(x - h)² + (y - k)² = r²" and sketch.startswith("Red")) or \
              (conic_type == "Ellipse" and equation == "(x - h)² / a² + (y - k)² / b² = 1" and "oval" in sketch.lower()) or \
              (conic_type == "Parabola" and "4p" in equation and "V shape" in sketch) or \
              (conic_type == "Hyperbola" and "mirrored" in sketch.lower() and "-" in equation)
    if correct:
        st.success("✅ Correct Match!")
    else:
        st.error("❌ Try Again — Mismatch Detected")

# Standards Dropdown
st.markdown("""
### 🏷️ Standards Reference
""")
st.selectbox("Select Standard Framework", ["Common Core", "Texas TEKS", "Massachusetts MA-FRAME"])

# Interactive Quiz Section
st.markdown("""
### 🎮 Quick Quiz
Test your understanding of conic sections with this interactive quiz!
""")

# Question 1
st.markdown("**Question 1:** What conic section results from a vertical slice through the cone's axis?")
q1_answer = st.radio(
    "Select your answer:",
    ["Ellipse", "Hyperbola", "Parabola", "Circle"],
    key="q1"
)

# Question 2
st.markdown("**Question 2:** Which of the following best models a satellite dish?")
q2_answer = st.radio(
    "Select your answer:",
    ["Circle", "Ellipse", "Parabola", "Hyperbola"],
    key="q2"
)

# Question 3
st.markdown("**Question 3:** What happens as the plane becomes parallel to a cone's slant?")
q3_answer = st.radio(
    "Select your answer:",
    ["A hyperbola appears", "A parabola forms", "The cone disappears"],
    key="q3"
)

# Submit button and scoring
if st.button("📊 Submit Quiz"):
    score = 0
    total_questions = 3
    
    # Check answers
    if q1_answer == "Hyperbola":
        score += 1
        st.success("✅ Question 1: Correct! A vertical slice through the axis creates a hyperbola.")
    else:
        st.error(f"❌ Question 1: Incorrect. You selected {q1_answer}, but the correct answer is Hyperbola.")
    
    if q2_answer == "Parabola":
        score += 1
        st.success("✅ Question 2: Correct! Satellite dishes use parabolic shapes to focus signals.")
    else:
        st.error(f"❌ Question 2: Incorrect. You selected {q2_answer}, but the correct answer is Parabola.")
    
    if q3_answer == "A parabola forms":
        score += 1
        st.success("✅ Question 3: Correct! When the plane is parallel to the cone's slant, a parabola forms.")
    else:
        st.error(f"❌ Question 3: Incorrect. You selected {q3_answer}, but the correct answer is 'A parabola forms'.")
    
    # Display final score
    percentage = (score / total_questions) * 100
    if percentage >= 80:
        st.balloons()
        st.success(f"🎉 Excellent work! You scored {score}/{total_questions} ({percentage:.0f}%)")
    elif percentage >= 60:
        st.info(f"👍 Good job! You scored {score}/{total_questions} ({percentage:.0f}%) - Review the materials and try again!")
    else:
        st.warning(f"📚 You scored {score}/{total_questions} ({percentage:.0f}%) - Consider reviewing the conic sections material above.")

# Reset button
if st.button("🔄 Reset Quiz"):
    # Clear the session state for quiz answers
    for key in ['q1', 'q2', 'q3']:
        if key in st.session_state:
            del st.session_state[key]
    st.success("Quiz reset! Please refresh the page or scroll up to take the quiz again.")

# Resources and Practice
st.markdown("""
### 📄 Practice and Resources
- [IXL Skill G.10 – Identify conic sections](https://www.ixl.com/math/algebra-2/identify-conic-sections)
- [Khan Academy – Conic Sections](https://www.khanacademy.org/math/geometry/geo-conic-sections)
- [GeoGebra Interactive Conic Tools](https://www.geogebra.org/m/edcuz7sa)
- [NASA – Real-world uses of parabolas](https://spaceplace.nasa.gov/real-world-math/en/)
- [YouTube: Conic Sections by The Organic Chemistry Tutor](https://www.youtube.com/watch?v=GUVFwUu8dO0)
- [Saylor: Visual Conic Sections Reference](https://saylordotorg.github.io/text_intermediate-algebra/s11-conic-sections.html)

---

<center>Built by Xavier Honablue M.Ed for CognitiveCloud.ai</center>
""")

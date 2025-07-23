# app.py
import streamlit as st
import streamlit.components.v1 as components

# Page config
st.set_page_config(
    page_title="Advanced Conic Sections",
    layout="wide",
    initial_sidebar_state="collapsed"
)

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

# Learning Objectives
st.markdown("""
### 🔍 Learning Objectives
- Understand the geometric construction of conic sections
- Explore the relationship between slicing angles and conic shapes
- Connect mathematical theory to real-world applications

**Standards Alignment:**
- HSG.GPE.A.2 – Derive the equation of a parabola given a focus and directrix
- HSG.GPE.A.1 – Derive the equation of a circle given its center and radius
""")

# Visual Aid Chart
st.markdown("""
### 🔹 Visual Aid: Match Shapes, Equations, and Descriptions
| Conic Type | Standard Equation | Visual Description |
|------------|-------------------|---------------------|
| Circle     | (x - h)² + (y - k)² = r² | 🄴 Red circle centered at (h,k) |
| Ellipse    | (x - h)² / a² + (y - k)² / b² = 1 | 🔵 Blue stretched oval across axes |
| Parabola   | (y - k)² = 4p(x - h) | 🟡 Yellow curved V shape |
| Hyperbola  | (y - k)² / a² - (x - h)² / b² = 1 | 🟢 Green mirrored arcs (open sideways) |

💡 Use this chart as your key reference when making selections in the matching activity below.
""")

# Matching Chart for Conic Types
st.markdown("""
### ↺ Conic Section Matching Activity
Match the conic section type with its equation and shape. Use the dropdowns to select and test your understanding. Visual learners should use the color-coded shape descriptions above as a reference.
""")

col1, col2, col3 = st.columns(3)
with col1:
    conic_type = st.selectbox("🔵 Select Conic Type", ["Circle", "Ellipse", "Parabola", "Hyperbola"])
with col2:
    equation = st.selectbox("🧲 Match Equation", [
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

# Quiz
st.markdown("""
### 🎮 Quick Quiz
1. What conic section results from a vertical slice through the cone’s axis?
   - [ ] Ellipse
   - [x] Hyperbola
   - [ ] Parabola
   - [ ] Circle

2. Which of the following best models a satellite dish?
   - [ ] Circle
   - [ ] Ellipse
   - [x] Parabola
   - [ ] Hyperbola

3. What happens as the plane becomes parallel to a cone’s slant?
   - [ ] A hyperbola appears
   - [x] A parabola forms
   - [ ] The cone disappears
""")

# Resources and Practice
st.markdown("""
### 📄 Practice and Resources
- [IXL Skill G.10 – Identify conic sections](https://www.ixl.com/math/algebra-2/identify-conic-sections)
- [Khan Academy – Conic Sections](https://www.khanacademy.org/math/geometry/geo-conic-sections)
- [GeoGebra Interactive Conic Tools](https://www.geogebra.org/m/edcuz7sa)
- [NASA – Real-world uses of parabolas](https://spaceplace.nasa.gov/real-world-math/en/)
- [YouTube: Conic Sections by The Organic Chemistry Tutor](https://www.youtube.com/watch?v=GUVFwUu8dO0)

---
<center>Built by Xavier Honablue M.Ed for CognitiveCloud.ai</center>
""")

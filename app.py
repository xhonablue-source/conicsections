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

# Matching Chart for Conic Types
st.markdown("""
### 🔁 Conic Section Matching Activity
Match the conic section type with its equation and shape. Use the dropdowns to select and test your understanding. Visual learners should use the color-coded shape descriptions.
""")

col1, col2, col3 = st.columns(3)
with col1:
    conic_type = st.selectbox("🔵 Select Conic Type", ["Circle", "Ellipse", "Parabola", "Hyperbola"])
with col2:
    equation = st.selectbox("🧮 Match Equation", [
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
              (conic_type == "Ellipse" and "ellipse" not in equation and "oval" in sketch.lower()) or \
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

# 3D Visualizer Embed
st.components.v1.html("""
<!DOCTYPE html>
<html>
<head>
  <meta charset=\"UTF-8\">
  <script src=\"https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js\"></script>
  <script src=\"https://cdnjs.cloudflare.com/ajax/libs/dat-gui/0.7.9/dat.gui.min.js\"></script>
  <style>
    html, body { margin: 0; overflow: hidden; background: black; }
    #three-container { width: 100vw; height: 80vh; }
  </style>
</head>
<body>
  <div id=\"three-container\"></div>
  <script>
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(75, window.innerWidth/window.innerHeight, 0.1, 1000);
    const renderer = new THREE.WebGLRenderer({antialias: true});
    renderer.setSize(window.innerWidth, window.innerHeight);
    document.getElementById(\"three-container\").appendChild(renderer.domElement);

    camera.position.set(0, 5, 10);

    const light = new THREE.DirectionalLight(0xffffff, 1);
    light.position.set(5, 10, 7.5);
    scene.add(light);
    scene.add(new THREE.AmbientLight(0x404040));

    const coneGeometry = new THREE.ConeGeometry(2, 6, 64, 64, true);
    coneGeometry.translate(0, -3, 0);
    const coneMaterial = new THREE.MeshPhongMaterial({ color: 0x156289, side: THREE.DoubleSide, wireframe: true });
    const cone = new THREE.Mesh(coneGeometry, coneMaterial);
    scene.add(cone);

    const planeGeometry = new THREE.PlaneGeometry(6, 6);
    const planeMaterial = new THREE.MeshBasicMaterial({ color: 0xffff00, side: THREE.DoubleSide, transparent: true, opacity: 0.4 });
    const plane = new THREE.Mesh(planeGeometry, planeMaterial);
    plane.rotation.x = Math.PI / 2;
    scene.add(plane);

    let guiParams = { planeRotationX: 90, planePositionY: 0 };
    const gui = new dat.GUI();
    gui.add(guiParams, 'planeRotationX', 0, 180).name(\"Plane Angle (°)\").onChange(updatePlane);
    gui.add(guiParams, 'planePositionY', -3, 3).name(\"Plane Height\").onChange(updatePlane);

    function updatePlane() {
      plane.rotation.x = THREE.MathUtils.degToRad(guiParams.planeRotationX);
      plane.position.y = guiParams.planePositionY;
    }

    function animate() {
      requestAnimationFrame(animate);
      renderer.render(scene, camera);
    }
    animate();
  </script>
</body>
</html>
""", height=700)

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

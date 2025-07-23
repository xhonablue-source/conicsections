import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Advanced Conic Sections", layout="wide")

st.markdown("""
    <div style='text-align:center; padding: 1rem; background: linear-gradient(to right, #1f4037, #99f2c8); color:black'>
        <h1>🌐 Advanced Conic Sections</h1>
        <h4><em>From 2D Mathematical Theory to 3D Real-World Applications</em></h4>
    </div>
""", unsafe_allow_html=True)

st.markdown("""
<div style='background-color:#111; padding: 1.5rem; color: white; font-size: 1.1rem'>
  This interactive visualization demonstrates how conic sections (circle, ellipse, parabola, hyperbola)
  emerge from the intersection of a plane with a double-napped cone. Use the controls to change the angle
  and position of the slicing plane. This mimics real-world applications such as satellite dish design (parabola),
  planetary orbits (ellipse), and navigation systems (hyperbola).
</div>
""", unsafe_allow_html=True)

# Inject the Three.js scene
components.html("""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <style>
    body { margin: 0; overflow: hidden; }
    canvas { display: block; }
  </style>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/dat-gui/0.7.9/dat.gui.min.js"></script>
</head>
<body>
<script>
let scene, camera, renderer, cone, plane, guiParams;

function init() {
  scene = new THREE.Scene();
  scene.background = new THREE.Color(0x000000);

  camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
  camera.position.set(0, 5, 10);

  renderer = new THREE.WebGLRenderer({ antialias: true });
  renderer.setSize(window.innerWidth, window.innerHeight);
  document.body.appendChild(renderer.domElement);

  const light = new THREE.DirectionalLight(0xffffff, 1);
  light.position.set(5, 10, 7.5);
  scene.add(light);
  scene.add(new THREE.AmbientLight(0x404040));

  const coneGeometry = new THREE.ConeGeometry(2, 6, 64, 64, true);
  coneGeometry.translate(0, -3, 0);
  const coneMaterial = new THREE.MeshPhongMaterial({ color: 0x156289, side: THREE.DoubleSide, wireframe: true });
  cone = new THREE.Mesh(coneGeometry, coneMaterial);
  scene.add(cone);

  const planeGeometry = new THREE.PlaneGeometry(6, 6);
  const planeMaterial = new THREE.MeshBasicMaterial({ color: 0xffff00, side: THREE.DoubleSide, transparent: true, opacity: 0.4 });
  plane = new THREE.Mesh(planeGeometry, planeMaterial);
  plane.rotation.x = Math.PI / 2;
  scene.add(plane);

  guiParams = { planeRotationX: 90, planePositionY: 0 };
  const gui = new dat.GUI();
  gui.add(guiParams, 'planeRotationX', 0, 180).name("Plane Angle (°)").onChange(updatePlane);
  gui.add(guiParams, 'planePositionY', -3, 3).name("Plane Height").onChange(updatePlane);

  updatePlane();
  animate();
}

function updatePlane() {
  plane.rotation.x = THREE.MathUtils.degToRad(guiParams.planeRotationX);
  plane.position.y = guiParams.planePositionY;
}

function animate() {
  requestAnimationFrame(animate);
  renderer.render(scene, camera);
}

window.addEventListener('resize', () => {
  camera.aspect = window.innerWidth / window.innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(window.innerWidth, window.innerHeight);
});

init();
</script>
</body>
</html>
""", height=700)

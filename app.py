<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Advanced Conic Sections: From 2D Theory to 3D Reality</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/dat-gui/0.7.9/dat.gui.min.js"></script>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: #333;
            line-height: 1.6;
        }
        
        .header {
            background: rgba(0, 0, 0, 0.9);
            color: white;
            padding: 20px;
            text-align: center;
            position: relative;
            overflow: hidden;
        }
        
        .header::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><defs><radialGradient id="grad1" cx="50%" cy="50%" r="50%"><stop offset="0%" style="stop-color:rgb(255,255,255);stop-opacity:0.1" /><stop offset="100%" style="stop-color:rgb(255,255,255);stop-opacity:0" /></radialGradient></defs><circle cx="50" cy="50" r="40" fill="url(%23grad1)" /></svg>') center/200px 200px;
            opacity: 0.1;
        }
        
        .header h1 {
            font-size: 2.5em;
            margin-bottom: 10px;
            position: relative;
            z-index: 1;
        }
        
        .header .subtitle {
            font-size: 1.2em;
            opacity: 0.9;
            position: relative;
            z-index: 1;
        }
        
        .developer-credit {
            background: rgba(255, 255, 255, 0.1);
            padding: 10px;
            margin: 20px;
            border-radius: 10px;
            text-align: center;
            color: white;
        }
        
        .container {
            max-width: 1400px;
            margin: 0 auto;
            padding: 20px;
        }
        
        .section {
            background: rgba(255, 255, 255, 0.95);
            margin: 20px 0;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
            backdrop-filter: blur(10px);
        }
        
        .conic-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 20px;
            margin: 20px 0;
        }
        
        .conic-card {
            background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 50%, #fecfef 100%);
            padding: 20px;
            border-radius: 15px;
            text-align: center;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            position: relative;
            overflow: hidden;
        }
        
        .conic-card:nth-child(1) {
            background: linear-gradient(135deg, #ff9a9e 0%, #fad0c4 100%);
        }
        
        .conic-card:nth-child(2) {
            background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
        }
        
        .conic-card:nth-child(3) {
            background: linear-gradient(135deg, #fbc2eb 0%, #a6c1ee 100%);
        }
        
        .conic-card:nth-child(4) {
            background: linear-gradient(135deg, #fdbb2d 0%, #22c1c3 100%);
        }
        
        .conic-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
        }
        
        .conic-visual {
            width: 200px;
            height: 200px;
            margin: 0 auto 15px;
            border-radius: 10px;
            background: rgba(255, 255, 255, 0.3);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 3em;
        }
        
        .equation {
            background: rgba(0, 0, 0, 0.8);
            color: white;
            padding: 15px;
            border-radius: 10px;
            font-family: 'Courier New', monospace;
            font-size: 1.1em;
            margin: 15px 0;
        }
        
        .three-container {
            width: 100%;
            height: 500px;
            border-radius: 15px;
            overflow: hidden;
            margin: 20px 0;
            position: relative;
        }
        
        .controls {
            background: rgba(0, 0, 0, 0.1);
            padding: 20px;
            border-radius: 10px;
            margin: 20px 0;
        }
        
        .control-group {
            margin: 15px 0;
        }
        
        .control-group label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        
        .slider {
            width: 100%;
            height: 6px;
            border-radius: 3px;
            background: #ddd;
            outline: none;
            -webkit-appearance: none;
        }
        
        .slider::-webkit-slider-thumb {
            appearance: none;
            width: 20px;
            height: 20px;
            border-radius: 50%;
            background: #667eea;
            cursor: pointer;
        }
        
        .tabs {
            display: flex;
            flex-wrap: wrap;
            margin-bottom: 20px;
        }
        
        .tab {
            padding: 15px 25px;
            background: rgba(255, 255, 255, 0.7);
            border: none;
            border-radius: 10px 10px 0 0;
            cursor: pointer;
            margin-right: 5px;
            font-weight: bold;
            transition: all 0.3s ease;
        }
        
        .tab.active {
            background: rgba(255, 255, 255, 1);
            box-shadow: 0 -5px 15px rgba(0, 0, 0, 0.1);
        }
        
        .tab-content {
            display: none;
            background: rgba(255, 255, 255, 1);
            padding: 30px;
            border-radius: 0 15px 15px 15px;
        }
        
        .tab-content.active {
            display: block;
        }
        
        .real-world-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin: 20px 0;
        }
        
        .application-card {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 25px;
            border-radius: 15px;
            transition: transform 0.3s ease;
        }
        
        .application-card:hover {
            transform: scale(1.05);
        }
        
        .application-icon {
            font-size: 3em;
            margin-bottom: 15px;
        }
        
        .dimension-comparison {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 30px;
            margin: 30px 0;
        }
        
        .dimension-box {
            padding: 25px;
            border-radius: 15px;
            text-align: center;
        }
        
        .dimension-2d {
            background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%);
        }
        
        .dimension-3d {
            background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
        }
        
        .assumption-box {
            background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
            padding: 25px;
            border-radius: 15px;
            margin: 20px 0;
            border-left: 5px solid #ff6b6b;
        }
        
        .interactive-demo {
            background: rgba(0, 0, 0, 0.05);
            padding: 25px;
            border-radius: 15px;
            margin: 20px 0;
        }
        
        @keyframes float {
            0%, 100% { transform: translateY(0px) rotate(0deg); opacity: 1; }
            50% { transform: translateY(-20px) rotate(180deg); opacity: 0.5; }
        }
        
        .conic-card, .application-card {
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }
        
        .tab {
            transition: all 0.3s ease;
        }
        
        .tab:hover {
            background: rgba(255, 255, 255, 0.9);
            transform: translateY(-2px);
        }
        
        .slider:hover {
            transform: scaleY(1.5);
        }
        
        .three-container {
            box-shadow: inset 0 0 50px rgba(0,0,0,0.3);
        }
        
        .section {
            position: relative;
            overflow: hidden;
        }
        
        .section::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.1), transparent);
            transition: left 0.5s;
        }
        
        .section:hover::before {
            left: 100%;
        }
        
        @media (max-width: 768px) {
            .header h1 {
                font-size: 2em;
            }
            
            .dimension-comparison {
                grid-template-columns: 1fr;
            }
            
            .tabs {
                flex-direction: column;
            }
            
            .tab {
                border-radius: 10px;
                margin-bottom: 5px;
            }
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>🌐 Advanced Conic Sections</h1>
        <div class="subtitle">From 2D Mathematical Theory to 3D Real-World Applications</div>
    </div>
    
    <div class="developer-credit">
        <strong>Developed by Xavier Honablue M.Ed</strong><br>
        Advanced Mathematical Visualization & Real-World Applications
    </div>
    
    <div class="container">
        <!-- Introduction Section -->
        <div class="section">
            <h2>🔍 Understanding the Dimensional Bridge</h2>
            <div class="assumption-box">
                <h3>⚠️ Critical Mathematical Assumption</h3>
                <p><strong>When we study conic sections in mathematics, we make a fundamental assumption:</strong> We work in a 2D planar coordinate system. This means we're looking at "slices" or cross-sections of 3D objects projected onto a flat plane.</p>
                <p><strong>Real-world implication:</strong> Every circle, ellipse, parabola, and hyperbola you see in nature is actually part of a 3D structure. Understanding this relationship is crucial for applications in engineering, architecture, and space technology.</p>
            </div>
            
            <div class="dimension-comparison">
                <div class="dimension-box dimension-2d">
                    <h3>📐 2D Mathematical Model</h3>
                    <p><strong>What we study:</strong></p>
                    <ul style="text-align: left;">
                        <li>Equations on coordinate planes</li>
                        <li>X-Y relationships</li>
                        <li>Graphical representations</li>
                        <li>Algebraic solutions</li>
                    </ul>
                    <p><em>Perfect for: Analysis, calculations, predictions</em></p>
                </div>
                
                <div class="dimension-box dimension-3d">
                    <h3>🌍 3D Real-World Reality</h3>
                    <p><strong>What actually exists:</strong></p>
                    <ul style="text-align: left;">
                        <li>Volumetric shapes</li>
                        <li>X-Y-Z spatial relationships</li>
                        <li>Physical structures</li>
                        <li>Engineering applications</li>
                    </ul>
                    <p><em>Perfect for: Construction, manufacturing, design</em></p>
                </div>
            </div>
        </div>

        <!-- Classic Conic Sections -->
        <div class="section">
            <h2>📊 The Four Fundamental Conic Sections</h2>
            <div class="conic-grid">
                <div class="conic-card">
                    <div class="conic-visual">⭕</div>
                    <h3>Circle</h3>
                    <div class="equation">(x - h)² + (y - k)² = r²</div>
                    <p><strong>2D Definition:</strong> All points equidistant from center</p>
                    <p><strong>3D Reality:</strong> Cross-section of cylinder or sphere</p>
                </div>
                
                <div class="conic-card">
                    <div class="conic-visual">🥚</div>
                    <h3>Ellipse</h3>
                    <div class="equation">x²/a² + y²/b² = 1</div>
                    <p><strong>2D Definition:</strong> Sum of distances to two foci is constant</p>
                    <p><strong>3D Reality:</strong> Cross-section of cone or ellipsoid</p>
                </div>
                
                <div class="conic-card">
                    <div class="conic-visual">📡</div>
                    <h3>Parabola</h3>
                    <div class="equation">y = ax² + bx + c</div>
                    <p><strong>2D Definition:</strong> Equidistant from focus and directrix</p>
                    <p><strong>3D Reality:</strong> Cross-section of paraboloid surface</p>
                </div>
                
                <div class="conic-card">
                    <div class="conic-visual">〰️</div>
                    <h3>Hyperbola</h3>
                    <div class="equation">x²/a² - y²/b² = 1</div>
                    <p><strong>2D Definition:</strong> Difference of distances to foci is constant</p>
                    <p><strong>3D Reality:</strong> Cross-section of hyperboloid</p>
                </div>
            </div>
        </div>

        <!-- Interactive 3D Visualization -->
        <div class="section">
            <h2>🎮 Interactive 3D Cone Slicing</h2>
            <p>Manipulate the cutting plane to see how different angles create different conic sections:</p>
            
            <div class="controls">
                <div class="control-group">
                    <label for="planeAngle">Cutting Plane Angle:</label>
                    <input type="range" id="planeAngle" class="slider" min="0" max="90" value="45">
                    <span id="angleValue">45°</span>
                </div>
                
                <div class="control-group">
                    <label for="planePosition">Plane Position:</label>
                    <input type="range" id="planePosition" class="slider" min="-2" max="2" step="0.1" value="0">
                    <span id="positionValue">0</span>
                </div>
                
                <div class="control-group">
                    <label>Current Conic Section: <span id="conicType">Ellipse</span></label>
                </div>
            </div>
            
            <div class="three-container" id="threeContainer"></div>
        </div>

        <!-- Real-World Applications -->
        <div class="section">
            <h2>🌟 Real-World Applications: From Theory to Technology</h2>
            
            <div class="tabs">
                <button class="tab active" onclick="showTab('aerospace')">🚀 Aerospace</button>
                <button class="tab" onclick="showTab('architecture')">🏗️ Architecture</button>
                <button class="tab" onclick="showTab('entertainment')">🎭 Entertainment</button>
                <button class="tab" onclick="showTab('technology')">💻 Technology</button>
            </div>

            <div id="aerospace" class="tab-content active">
                <h3>🛰️ Northrop Grumman & Aerospace Applications</h3>
                <div class="real-world-grid">
                    <div class="application-card">
                        <div class="application-icon">🛰️</div>
                        <h4>Satellite Orbits</h4>
                        <p><strong>Elliptical Paths:</strong> Satellites follow elliptical orbits with Earth at one focus. Northrop Grumman designs spacecraft that must calculate precise orbital mechanics using ellipse equations.</p>
                        <p><strong>3D Reality:</strong> The 2D ellipse we study becomes a 3D orbital path through space.</p>
                    </div>
                    
                    <div class="application-card">
                        <div class="application-icon">📡</div>
                        <h4>Radar & Communication</h4>
                        <p><strong>Parabolic Reflectors:</strong> Satellite dishes and radar systems use parabolic surfaces to focus electromagnetic signals.</p>
                        <p><strong>3D Reality:</strong> The 2D parabola becomes a 3D paraboloid surface that concentrates signals at the focal point.</p>
                    </div>
                    
                    <div class="application-card">
                        <div class="application-icon">🚀</div>
                        <h4>Trajectory Planning</h4>
                        <p><strong>Hyperbolic Escape Paths:</strong> Spacecraft leaving Earth's gravitational influence follow hyperbolic trajectories.</p>
                        <p><strong>3D Reality:</strong> The 2D hyperbola represents one plane of a 3D escape trajectory through space.</p>
                    </div>
                </div>
            </div>

            <div id="architecture" class="tab-content">
                <h3>🏛️ Architectural Marvels</h3>
                <div class="real-world-grid">
                    <div class="application-card">
                        <div class="application-icon">🏟️</div>
                        <h4>Stadium Design</h4>
                        <p><strong>Elliptical Structures:</strong> Many stadiums use elliptical designs for optimal sight lines and acoustics.</p>
                        <p><strong>3D Reality:</strong> The 2D ellipse becomes a 3D ellipsoid or cylindrical structure.</p>
                    </div>
                    
                    <div class="application-card">
                        <div class="application-icon">🌉</div>
                        <h4>Bridge Construction</h4>
                        <p><strong>Parabolic Cables:</strong> Suspension bridge cables form parabolic curves under uniform load.</p>
                        <p><strong>3D Reality:</strong> The 2D parabola extends in 3D space as a curved surface supporting the bridge deck.</p>
                    </div>
                    
                    <div class="application-card">
                        <div class="application-icon">❄️</div>
                        <h4>Cooling Towers</h4>
                        <p><strong>Hyperbolic Design:</strong> Nuclear cooling towers use hyperbolic shapes for structural efficiency.</p>
                        <p><strong>3D Reality:</strong> The 2D hyperbola rotates to create a 3D hyperboloid surface.</p>
                    </div>
                </div>
            </div>

            <div id="entertainment" class="tab-content">
                <h3>🎪 Las Vegas Sphere & Entertainment Technology</h3>
                <div class="application-card" style="margin-bottom: 20px;">
                    <div class="application-icon">🌐</div>
                    <h4>The Las Vegas Sphere: A Mathematical Marvel</h4>
                    <p><strong>Spherical Geometry:</strong> The Sphere is a perfect example of how circular cross-sections (conic sections) create 3D spherical surfaces.</p>
                    <p><strong>Mathematical Connection:</strong></p>
                    <ul style="text-align: left; margin: 15px 0;">
                        <li><strong>2D Circles:</strong> Every horizontal slice through the Sphere creates a perfect circle</li>
                        <li><strong>3D Reality:</strong> Thousands of these circular cross-sections stack to form the complete sphere</li>
                        <li><strong>Display Technology:</strong> The LED display maps 2D conic section equations onto the 3D spherical surface</li>
                    </ul>
                </div>
                
                <div class="real-world-grid">
                    <div class="application-card">
                        <div class="application-icon">🎬</div>
                        <h4>Projection Mapping</h4>
                        <p><strong>Mathematical Transformation:</strong> Converting 2D images to fit the 3D spherical surface requires understanding how circles map onto sphere surfaces.</p>
                    </div>
                    
                    <div class="application-card">
                        <div class="application-icon">🔊</div>
                        <h4>Acoustic Design</h4>
                        <p><strong>Sound Reflection:</strong> The spherical shape creates unique acoustic properties based on circular and elliptical sound reflection patterns.</p>
                    </div>
                    
                    <div class="application-card">
                        <div class="application-icon">🎮</div>
                        <h4>Immersive Experiences</h4>
                        <p><strong>360° Visuals:</strong> The sphere's geometry allows for true 360-degree immersive experiences using spherical coordinate mathematics.</p>
                    </div>
                </div>
            </div>

            <div id="technology" class="tab-content">
                <h3>💻 Modern Technology Applications</h3>
                <div class="real-world-grid">
                    <div class="application-card">
                        <div class="application-icon">📱</div>
                        <h4>GPS Navigation</h4>
                        <p><strong>Hyperbolic Positioning:</strong> GPS uses hyperbolic curves to triangulate position based on time differences from satellites.</p>
                        <p><strong>3D Reality:</strong> The 2D hyperbolas become 3D hyperboloid surfaces intersecting to determine location.</p>
                    </div>
                    
                    <div class="application-card">
                        <div class="application-icon">🔬</div>
                        <h4>Medical Imaging</h4>
                        <p><strong>Elliptical Scans:</strong> MRI and CT scanners use elliptical paths to capture 3D images of the human body.</p>
                        <p><strong>3D Reality:</strong> Multiple 2D elliptical slices combine to create 3D volumetric medical images.</p>
                    </div>
                    
                    <div class="application-card">
                        <div class="application-icon">🎯</div>
                        <h4>Targeting Systems</h4>
                        <p><strong>Parabolic Trajectories:</strong> Military and civilian targeting systems calculate parabolic paths for projectiles.</p>
                        <p><strong>3D Reality:</strong> The 2D parabola represents one plane of a 3D ballistic trajectory.</p>
                    </div>
                </div>
            </div>
        </div>

        <!-- 3D Transition Explanation -->
        <div class="section">
            <h2>🔄 From 2D Theory to 3D Reality: The Mathematical Bridge</h2>
            
            <div class="interactive-demo">
                <h3>🧮 Understanding the Transformation</h3>
                <p>Now that you understand the 2D mathematical foundations, let's explore how these concepts extend into 3D space:</p>
                
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin: 20px 0;">
                    <div style="background: rgba(255, 255, 255, 0.8); padding: 20px; border-radius: 10px;">
                        <h4>🔴 Circle → Sphere</h4>
                        <p><strong>2D:</strong> (x - h)² + (y - k)² = r²</p>
                        <p><strong>3D:</strong> (x - h)² + (y - k)² + (z - l)² = r²</p>
                        <p><em>Application:</em> Las Vegas Sphere's geometry</p>
                    </div>
                    
                    <div style="background: rgba(255, 255, 255, 0.8); padding: 20px; border-radius: 10px;">
                        <h4>🟡 Ellipse → Ellipsoid</h4>
                        <p><strong>2D:</strong> x²/a² + y²/b² = 1</p>
                        <p><strong>3D:</strong> x²/a² + y²/b² + z²/c² = 1</p>
                        <p><em>Application:</em> Satellite orbits in 3D space</p>
                    </div>
                    
                    <div style="background: rgba(255, 255, 255, 0.8); padding: 20px; border-radius: 10px;">
                        <h4>🔵 Parabola → Paraboloid</h4>
                        <p><strong>2D:</strong> y = ax² + bx + c</p>
                        <p><strong>3D:</strong> z = a(x² + y²) (rotation)</p>
                        <p><em>Application:</em> Satellite dish surfaces</p>
                    </div>
                    
                    <div style="background: rgba(255, 255, 255, 0.8); padding: 20px; border-radius: 10px;">
                        <h4>🟣 Hyperbola → Hyperboloid</h4>
                        <p><strong>2D:</strong> x²/a² - y²/b² = 1</p>
                        <p><strong>3D:</strong> x²/a² + y²/b² - z²/c² = 1</p>
                        <p><em>Application:</em> Cooling tower structures</p>
                    </div>
                </div>
            </div>
            
            <div class="assumption-box">
                <h3>🎯 Key Insight: Why Start with 2D?</h3>
                <p><strong>Educational Strategy:</strong> We study 2D conic sections first because:</p>
                <ul>
                    <li><strong>Simplicity:</strong> Easier to visualize and calculate</li>
                    <li><strong>Foundation:</strong> Essential understanding for 3D applications</li>
                    <li><strong>Practicality:</strong> Many real-world problems can be solved using 2D cross-sections</li>
                    <li><strong>Analysis:</strong> 3D problems often break down into multiple 2D problems</li>
                </ul>
                <p><strong>Real-World Bridge:</strong> Once you master 2D conic sections, you can understand how engineers at companies like Northrop Grumman use these principles to design complex 3D structures and systems.</p>
            </div>
        </div>

        <!-- Interactive Problem Solving -->
        <div class="section">
            <h2>🧪 Interactive Problem Solving</h2>
            
            <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 25px; border-radius: 15px; margin: 20px 0;">
                <h3>🚀 Challenge: Design a Satellite Dish</h3>
                <p>You're working for a telecommunications company and need to design a parabolic satellite dish:</p>
                
                <div class="controls">
                    <div class="control-group">
                        <label for="dishDiameter">Dish Diameter (meters):</label>
                        <input type="range" id="dishDiameter" class="slider" min="1" max="10" step="0.5" value="3">
                        <span id="diameterValue">3 m</span>
                    </div>
                    
                    <div class="control-group">
                        <label for="focalLength">Focal Length (meters):</label>
                        <input type="range" id="focalLength" class="slider" min="0.5" max="5" step="0.1" value="1.5">
                        <span id="focalValue">1.5 m</span>
                    </div>
                    
                    <div style="background: rgba(255, 255, 255, 0.1); padding: 15px; border-radius: 10px; margin: 10px 0;">
                        <p><strong>Dish Equation:</strong> <span id="dishEquation">x² = 4(1.5)y</span></p>
                        <p><strong>Efficiency Rating:</strong> <span id="efficiency">Good</span></p>
                        <p><strong>Beam Width:</strong> <span id="beamWidth">24°</span></p>
                    </div>
                </div>
            </div>
        </div>

        <!-- Advanced Visualization Section -->
        <div class="section">
            <h2>🎨 Advanced 3D Visualization Gallery</h2>
            
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(400px, 1fr)); gap: 20px;">
                <div style="background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%); padding: 25px; border-radius: 15px;">
                    <h3>🌐 Las Vegas Sphere Technical Specs</h3>
                    <div style="background: rgba(255, 255, 255, 0.9); color: #333; padding: 20px; border-radius: 10px; margin: 15px 0;">
                        <p><strong>Diameter:</strong> 516 feet (157 meters)</p>
                        <p><strong>Height:</strong> 366 feet (112 meters)</p>
                        <p><strong>LED Panels:</strong> 1.2 million programmable pucks</p>
                        <p><strong>Mathematical Principle:</strong> Perfect sphere = infinite circular cross-sections</p>
                        <p><strong>Equation:</strong> x² + y² + z² = r² where r ≈ 258 feet</p>
                    </div>
                    <p><em>Each LED pixel represents a point on the spherical surface, demonstrating how 2D circular equations combine to create 3D spherical reality.</em></p>
                </div>
                
                <div style="background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%); padding: 25px; border-radius: 15px;">
                    <h3>🛰️ Northrop Grumman Applications</h3>
                    <div style="background: rgba(255, 255, 255, 0.9); color: #333; padding: 20px; border-radius: 10px; margin: 15px 0;">
                        <p><strong>James Webb Space Telescope:</strong></p>
                        <p>• Primary mirror: 18 hexagonal segments</p>
                        <p>• Each segment: Parabolic surface</p>
                        <p>• Combined: Single parabolic reflector</p>
                        <p><strong>Mathematical Challenge:</strong> Aligning multiple 2D parabolic surfaces to create one perfect 3D paraboloid</p>
                    </div>
                    <p><em>This demonstrates how understanding 2D conic sections is essential for designing complex 3D optical systems.</em></p>
                </div>
            </div>
        </div>

        <!-- Interactive 3D Model Comparison -->
        <div class="section">
            <h2>🔍 2D vs 3D: Interactive Comparison</h2>
            
            <div class="tabs">
                <button class="tab active" onclick="showComparison('circles')">Circles → Spheres</button>
                <button class="tab" onclick="showComparison('parabolas')">Parabolas → Paraboloids</button>
                <button class="tab" onclick="showComparison('ellipses')">Ellipses → Ellipsoids</button>
                <button class="tab" onclick="showComparison('hyperbolas')">Hyperbolas → Hyperboloids</button>
            </div>

            <div id="circles-comparison" class="tab-content active">
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 30px;">
                    <div style="background: rgba(255, 255, 255, 0.8); padding: 20px; border-radius: 15px;">
                        <h4>🔴 2D Circle</h4>
                        <div style="width: 200px; height: 200px; border: 4px solid #ff6b6b; border-radius: 50%; margin: 20px auto; display: flex; align-items: center; justify-content: center; background: rgba(255, 107, 107, 0.1);">
                            <span style="font-size: 0.9em; text-align: center;">x² + y² = r²<br><small>Flat circle on plane</small></span>
                        </div>
                        <p><strong>Properties:</strong></p>
                        <ul>
                            <li>2 dimensions (x, y)</li>
                            <li>Single radius value</li>
                            <li>Area = πr²</li>
                            <li>Circumference = 2πr</li>
                        </ul>
                    </div>
                    
                    <div style="background: rgba(255, 255, 255, 0.8); padding: 20px; border-radius: 15px;">
                        <h4>🌐 3D Sphere (Las Vegas Sphere)</h4>
                        <div style="width: 200px; height: 200px; background: radial-gradient(circle at 30% 30%, #87CEEB, #4682B4, #191970); border-radius: 50%; margin: 20px auto; display: flex; align-items: center; justify-content: center; color: white; box-shadow: inset -20px -20px 50px rgba(0,0,0,0.3);">
                            <span style="font-size: 0.9em; text-align: center;">x² + y² + z² = r²<br><small>3D spherical surface</small></span>
                        </div>
                        <p><strong>Properties:</strong></p>
                        <ul>
                            <li>3 dimensions (x, y, z)</li>
                            <li>Single radius value</li>
                            <li>Volume = (4/3)πr³</li>
                            <li>Surface Area = 4πr²</li>
                        </ul>
                        <p><em>The Las Vegas Sphere uses this geometry for 360° immersive displays.</em></p>
                    </div>
                </div>
            </div>

            <div id="parabolas-comparison" class="tab-content">
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 30px;">
                    <div style="background: rgba(255, 255, 255, 0.8); padding: 20px; border-radius: 15px;">
                        <h4>📡 2D Parabola</h4>
                        <div style="width: 200px; height: 200px; margin: 20px auto; position: relative; background: rgba(255, 193, 7, 0.1); border-radius: 10px; display: flex; align-items: center; justify-content: center;">
                            <svg width="180" height="180" viewBox="0 0 180 180">
                                <path d="M 20 160 Q 90 20 160 160" stroke="#FFC107" stroke-width="4" fill="none"/>
                                <circle cx="90" cy="60" r="3" fill="#FF5722"/>
                                <text x="95" y="65" font-size="10" fill="#333">Focus</text>
                                <text x="70" y="175" font-size="12" fill="#333">y = ax²</text>
                            </svg>
                        </div>
                        <p><strong>Properties:</strong></p>
                        <ul>
                            <li>2 dimensions (x, y)</li>
                            <li>Single focus point</li>
                            <li>Opens up/down or left/right</li>
                            <li>Used in satellite dish cross-sections</li>
                        </ul>
                    </div>
                    
                    <div style="background: rgba(255, 255, 255, 0.8); padding: 20px; border-radius: 15px;">
                        <h4>🛰️ 3D Paraboloid (Satellite Dish)</h4>
                        <div style="width: 200px; height: 200px; margin: 20px auto; background: radial-gradient(ellipse at center bottom, #E3F2FD 0%, #1976D2 70%, #0D47A1 100%); border-radius: 50% 50% 50% 50% / 60% 60% 40% 40%; display: flex; align-items: center; justify-content: center; color: white; position: relative;">
                            <span style="font-size: 0.9em; text-align: center;">z = a(x² + y²)<br><small>3D dish surface</small></span>
                            <div style="position: absolute; top: 50%; left: 50%; width: 4px; height: 4px; background: #FF5722; border-radius: 50%; transform: translate(-50%, -50%);"></div>
                        </div>
                        <p><strong>Properties:</strong></p>
                        <ul>
                            <li>3 dimensions (x, y, z)</li>
                            <li>Rotational symmetry</li>
                            <li>Focus point for signal collection</li>
                            <li>Used by Northrop Grumman in communications</li>
                        </ul>
                        <p><em>Rotating the 2D parabola creates the 3D satellite dish surface.</em></p>
                    </div>
                </div>
            </div>

            <div id="ellipses-comparison" class="tab-content">
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 30px;">
                    <div style="background: rgba(255, 255, 255, 0.8); padding: 20px; border-radius: 15px;">
                        <h4>🥚 2D Ellipse</h4>
                        <div style="width: 200px; height: 200px; margin: 20px auto; display: flex; align-items: center; justify-content: center; background: rgba(76, 175, 80, 0.1); border-radius: 15px;">
                            <svg width="180" height="180" viewBox="0 0 180 180">
                                <ellipse cx="90" cy="90" rx="70" ry="40" stroke="#4CAF50" stroke-width="4" fill="none"/>
                                <circle cx="65" cy="90" r="3" fill="#FF5722"/>
                                <circle cx="115" cy="90" r="3" fill="#FF5722"/>
                                <text x="45" y="105" font-size="8" fill="#333">F1</text>
                                <text x="120" y="105" font-size="8" fill="#333">F2</text>
                                <text x="60" y="150" font-size="12" fill="#333">x²/a² + y²/b² = 1</text>
                            </svg>
                        </div>
                        <p><strong>Properties:</strong></p>
                        <ul>
                            <li>2 dimensions (x, y)</li>
                            <li>Two focus points</li>
                            <li>Semi-major and semi-minor axes</li>
                            <li>Orbital mechanics calculations</li>
                        </ul>
                    </div>
                    
                    <div style="background: rgba(255, 255, 255, 0.8); padding: 20px; border-radius: 15px;">
                        <h4>🌍 3D Ellipsoid (Earth's Shape)</h4>
                        <div style="width: 200px; height: 200px; margin: 20px auto; background: radial-gradient(ellipse at 30% 30%, #81C784, #4CAF50, #2E7D32); border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; transform: scaleY(0.8); box-shadow: inset -15px -15px 30px rgba(0,0,0,0.3);">
                            <span style="font-size: 0.9em; text-align: center; transform: scaleY(1.25);">x²/a² + y²/b² + z²/c² = 1<br><small>3D ellipsoidal surface</small></span>
                        </div>
                        <p><strong>Properties:</strong></p>
                        <ul>
                            <li>3 dimensions (x, y, z)</li>
                            <li>Three semi-axes (a, b, c)</li>
                            <li>Earth is an oblate ellipsoid</li>
                            <li>GPS systems account for this shape</li>
                        </ul>
                        <p><em>Satellite orbits are elliptical paths around Earth's ellipsoidal shape.</em></p>
                    </div>
                </div>
            </div>

            <div id="hyperbolas-comparison" class="tab-content">
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 30px;">
                    <div style="background: rgba(255, 255, 255, 0.8); padding: 20px; border-radius: 15px;">
                        <h4>〰️ 2D Hyperbola</h4>
                        <div style="width: 200px; height: 200px; margin: 20px auto; display: flex; align-items: center; justify-content: center; background: rgba(156, 39, 176, 0.1); border-radius: 15px;">
                            <svg width="180" height="180" viewBox="0 0 180 180">
                                <path d="M 20 20 Q 60 90 20 160" stroke="#9C27B0" stroke-width="3" fill="none"/>
                                <path d="M 160 20 Q 120 90 160 160" stroke="#9C27B0" stroke-width="3" fill="none"/>
                                <line x1="20" y1="20" x2="160" y2="160" stroke="#ccc" stroke-width="1" stroke-dasharray="5,5"/>
                                <line x1="160" y1="20" x2="20" y2="160" stroke="#ccc" stroke-width="1" stroke-dasharray="5,5"/>
                                <text x="50" y="175" font-size="12" fill="#333">x²/a² - y²/b² = 1</text>
                            </svg>
                        </div>
                        <p><strong>Properties:</strong></p>
                        <ul>
                            <li>2 dimensions (x, y)</li>
                            <li>Two branches</li>
                            <li>Asymptotic lines</li>
                            <li>GPS positioning calculations</li>
                        </ul>
                    </div>
                    
                    <div style="background: rgba(255, 255, 255, 0.8); padding: 20px; border-radius: 15px;">
                        <h4>🏭 3D Hyperboloid (Cooling Tower)</h4>
                        <div style="width: 200px; height: 200px; margin: 20px auto; background: linear-gradient(to bottom, #E1BEE7 0%, #9C27B0 50%, #4A148C 100%); border-radius: 40% 40% 60% 60% / 20% 20% 80% 80%; display: flex; align-items: center; justify-content: center; color: white; position: relative;">
                            <span style="font-size: 0.9em; text-align: center;">x²/a² + y²/b² - z²/c² = 1<br><small>3D hyperboloid surface</small></span>
                        </div>
                        <p><strong>Properties:</strong></p>
                        <ul>
                            <li>3 dimensions (x, y, z)</li>
                            <li>Saddle-shaped surface</li>
                            <li>Structural efficiency</li>
                            <li>Nuclear plant cooling towers</li>
                        </ul>
                        <p><em>The hyperbolic profile provides maximum strength with minimum material.</em></p>
                    </div>
                </div>
            </div>
        </div>

        <!-- Mathematical Proofs Section -->
        <div class="section">
            <h2>🧮 Mathematical Connections: Why This Matters</h2>
            
            <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 30px; border-radius: 15px;">
                <h3>🎯 The Engineering Reality</h3>
                <p><strong>When you work at companies like Northrop Grumman, you need to understand both 2D and 3D applications:</strong></p>
                
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; margin: 20px 0;">
                    <div style="background: rgba(255, 255, 255, 0.1); padding: 20px; border-radius: 10px;">
                        <h4>📐 Design Phase</h4>
                        <p>Engineers start with 2D conic section equations to model cross-sections and analyze specific planes of 3D objects.</p>
                    </div>
                    
                    <div style="background: rgba(255, 255, 255, 0.1); padding: 20px; border-radius: 10px;">
                        <h4>🔧 Manufacturing</h4>
                        <p>3D objects are often manufactured by combining or rotating 2D profiles. Understanding the math ensures precision.</p>
                    </div>
                    
                    <div style="background: rgba(255, 255, 255, 0.1); padding: 20px; border-radius: 10px;">
                        <h4>📊 Analysis</h4>
                        <p>Complex 3D problems are solved by breaking them down into multiple 2D conic section problems.</p>
                    </div>
                    
                    <div style="background: rgba(255, 255, 255, 0.1); padding: 20px; border-radius: 10px;">
                        <h4>🚀 Optimization</h4>
                        <p>Performance improvements often come from perfecting the 2D mathematical models that define 3D structures.</p>
                    </div>
                </div>
            </div>
        </div>

        <!-- Final Challenge Section -->
        <div class="section">
            <h2>🏆 Master Challenge: Design Your Own Application</h2>
            
            <div style="background: rgba(255, 255, 255, 0.95); padding: 30px; border-radius: 15px; border: 3px solid #667eea;">
                <h3>🎯 Choose Your Mission</h3>
                <p>Select a real-world application and design it using conic sections:</p>
                
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px; margin: 20px 0;">
                    <button onclick="selectMission('satellite')" style="padding: 20px; border: 2px solid #667eea; border-radius: 10px; background: white; cursor: pointer; transition: all 0.3s ease;">
                        🛰️ Design a Satellite Dish
                    </button>
                    <button onclick="selectMission('bridge')" style="padding: 20px; border: 2px solid #667eea; border-radius: 10px; background: white; cursor: pointer; transition: all 0.3s ease;">
                        🌉 Plan a Suspension Bridge
                    </button>
                    <button onclick="selectMission('tower')" style="padding: 20px; border: 2px solid #667eea; border-radius: 10px; background: white; cursor: pointer; transition: all 0.3s ease;">
                        🏭 Build a Cooling Tower
                    </button>
                    <button onclick="selectMission('sphere')" style="padding: 20px; border: 2px solid #667eea; border-radius: 10px; background: white; cursor: pointer; transition: all 0.3s ease;">
                        🌐 Create an Entertainment Sphere
                    </button>
                </div>
                
                <div id="missionDetails" style="margin-top: 20px; padding: 20px; background: rgba(102, 126, 234, 0.1); border-radius: 10px; display: none;">
                    <p id="missionDescription"></p>
                    <div id="missionControls"></div>
                    <div id="missionResults" style="margin-top: 15px; font-weight: bold;"></div>
                </div>
            </div>
        </div>

        <!-- Conclusion -->
        <div class="section">
            <h2>🎓 Mastery Achieved: From Theory to Innovation</h2>
            
            <div style="background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%); padding: 30px; border-radius: 15px; text-align: center;">
                <h3>🌟 Congratulations! You Now Understand:</h3>
                
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; margin: 30px 0;">
                    <div style="background: rgba(255, 255, 255, 0.8); padding: 20px; border-radius: 10px;">
                        <h4>📐 Mathematical Foundation</h4>
                        <p>The 2D equations that define circles, ellipses, parabolas, and hyperbolas</p>
                    </div>
                    
                    <div style="background: rgba(255, 255, 255, 0.8); padding: 20px; border-radius: 10px;">
                        <h4>🌐 3D Reality</h4>
                        <p>How these 2D concepts extend into real-world 3D applications</p>
                    </div>
                    
                    <div style="background: rgba(255, 255, 255, 0.8); padding: 20px; border-radius: 10px;">
                        <h4>🚀 Industry Applications</h4>
                        <p>Real examples from aerospace, entertainment, and technology sectors</p>
                    </div>
                    
                    <div style="background: rgba(255, 255, 255, 0.8); padding: 20px; border-radius: 10px;">
                        <h4>🔬 Problem-Solving Skills</h4>
                        <p>How to bridge mathematical theory with engineering practice</p>
                    </div>
                </div>
                
                <p style="font-size: 1.2em; margin-top: 20px;"><strong>You're now ready to think like an engineer at companies like Northrop Grumman, where mathematics meets cutting-edge technology!</strong></p>
            </div>
        </div>

        <!-- Footer -->
        <div style="text-align: center; padding: 30px; color: rgba(255, 255, 255, 0.8);">
            <p><strong>Advanced Mathematical Visualization by Xavier Honablue M.Ed</strong></p>
            <p>Bridging the gap between mathematical theory and real-world engineering applications</p>
        </div>
    </div>

    <script>
        // Three.js 3D Visualization
        let scene, camera, renderer, cone, plane;
        
        function initThreeJS() {
            const container = document.getElementById('threeContainer');
            
            scene = new THREE.Scene();
            scene.background = new THREE.Color(0x222222);
            
            camera = new THREE.PerspectiveCamera(75, container.clientWidth / container.clientHeight, 0.1, 1000);
            camera.position.set(5, 5, 5);
            camera.lookAt(0, 0, 0);
            
            renderer = new THREE.WebGLRenderer({ antialias: true });
            renderer.setSize(container.clientWidth, container.clientHeight);
            renderer.shadowMap.enabled = true;
            renderer.shadowMap.type = THREE.PCFSoftShadowMap;
            container.appendChild(renderer.domElement);
            
            // Create cone geometry
            const coneGeometry = new THREE.ConeGeometry(2, 4, 32);
            const coneMaterial = new THREE.MeshPhongMaterial({ 
                color: 0x4a90e2, 
                transparent: true, 
                opacity: 0.7,
                wireframe: false
            });
            cone = new THREE.Mesh(coneGeometry, coneMaterial);
            scene.add(cone);
            
            // Create cutting plane
            const planeGeometry = new THREE.PlaneGeometry(6, 6);
            const planeMaterial = new THREE.MeshPhongMaterial({ 
                color: 0xff6b6b, 
                transparent: true, 
                opacity: 0.5,
                side: THREE.DoubleSide
            });
            plane = new THREE.Mesh(planeGeometry, planeMaterial);
            scene.add(plane);
            
            // Add lights
            const ambientLight = new THREE.AmbientLight(0x404040, 0.6);
            scene.add(ambientLight);
            
            const directionalLight = new THREE.DirectionalLight(0xffffff, 0.8);
            directionalLight.position.set(5, 5, 5);
            directionalLight.castShadow = true;
            scene.add(directionalLight);
            
            // Add grid
            const gridHelper = new THREE.GridHelper(10, 10);
            scene.add(gridHelper);
            
            animate();
        }
        
        function animate() {
            requestAnimationFrame(animate);
            
            // Rotate cone slowly
            cone.rotation.y += 0.005;
            
            renderer.render(scene, camera);
        }
        
        function updateConeSlice() {
            const angleSlider = document.getElementById('planeAngle');
            const positionSlider = document.getElementById('planePosition');
            const angleValue = document.getElementById('angleValue');
            const positionValue = document.getElementById('positionValue');
            const conicType = document.getElementById('conicType');
            
            if (!angleSlider || !plane) return;
            
            const angle = parseFloat(angleSlider.value);
            const position = parseFloat(positionSlider.value);
            
            angleValue.textContent = angle + '°';
            positionValue.textContent = position;
            
            // Update plane rotation and position
            plane.rotation.x = (angle * Math.PI) / 180;
            plane.position.y = position;
            
            // Determine conic type based on angle
            let type = '';
            if (angle < 15) {
                type = 'Circle';
            } else if (angle < 45) {
                type = 'Ellipse';
            } else if (angle < 75) {
                type = 'Parabola';
            } else {
                type = 'Hyperbola';
            }
            
            conicType.textContent = type;
        }
        
        // Tab functionality
        function showTab(tabName) {
            // Hide all tab contents
            const contents = document.querySelectorAll('.tab-content');
            contents.forEach(content => content.classList.remove('active'));
            
            // Remove active class from all tabs
            const tabs = document.querySelectorAll('.tab');
            tabs.forEach(tab => tab.classList.remove('active'));
            
            // Show selected tab content
            document.getElementById(tabName).classList.add('active');
            
            // Add active class to clicked tab
            event.target.classList.add('active');
        }
        
        // Comparison functionality
        function showComparison(type) {
            // Hide all comparison contents
            const contents = document.querySelectorAll('[id$="-comparison"]');
            contents.forEach(content => content.style.display = 'none');
            
            // Show selected comparison
            document.getElementById(type + '-comparison').style.display = 'block';
        }
        
        // Satellite dish calculator
        function updateDishCalculations() {
            const diameter = parseFloat(document.getElementById('dishDiameter').value);
            const focal = parseFloat(document.getElementById('focalLength').value);
            
            document.getElementById('diameterValue').textContent = diameter + ' m';
            document.getElementById('focalValue').textContent = focal + ' m';
            
            // Calculate dish equation
            const equation = `x² = ${(4 * focal).toFixed(1)}y`;
            document.getElementById('dishEquation').textContent = equation;
            
            // Calculate efficiency (simplified)
            const fOverD = focal / diameter;
            let efficiency = '';
            if (fOverD < 0.3) efficiency = 'Poor';
            else if (fOverD < 0.5) efficiency = 'Good';
            else if (fOverD < 0.7) efficiency = 'Very Good';
            else efficiency = 'Excellent';
            
            document.getElementById('efficiency').textContent = efficiency;
            
            // Calculate beam width (simplified formula)
            const beamWidth = (70 / diameter).toFixed(1);
            document.getElementById('beamWidth').textContent = beamWidth + '°';
        }
        
        // Mission selection
        function selectMission(mission) {
            const details = document.getElementById('missionDetails');
            const description = document.getElementById('missionDescription');
            const controls = document.getElementById('missionControls');
            const results = document.getElementById('missionResults');
            
            details.style.display = 'block';
            
            switch(mission) {
                case 'satellite':
                    description.textContent = '🛰️ Design a parabolic satellite dish for optimal signal reception. Adjust parameters to maximize efficiency.';
                    controls.innerHTML = `
                        <label>Dish Diameter: <input type="range" min="2" max="12" value="6" oninput="updateMissionResults('satellite', this.value)"> <span id="satDiameter">6m</span></label><br>
                        <label>Focal Length: <input type="range" min="1" max="6" step="0.5" value="3" oninput="updateMissionResults('satellite', this.value, 'focal')"> <span id="satFocal">3m</span></label>
                    `;
                    break;
                case 'bridge':
                    description.textContent = '🌉 Design a suspension bridge with parabolic cables. Balance span length with structural requirements.';
                    controls.innerHTML = `
                        <label>Bridge Span: <input type="range" min="100" max="2000" step="50" value="800" oninput="updateMissionResults('bridge', this.value)"> <span id="bridgeSpan">800m</span></label><br>
                        <label>Cable Sag: <input type="range" min="20" max="200" step="10" value="100" oninput="updateMissionResults('bridge', this.value, 'sag')"> <span id="bridgeSag">100m</span></label>
                    `;
                    break;
                case 'tower':
                    description.textContent = '🏭 Design a hyperbolic cooling tower for maximum efficiency and structural strength.';
                    controls.innerHTML = `
                        <label>Tower Height: <input type="range" min="50" max="200" step="10" value="120" oninput="updateMissionResults('tower', this.value)"> <span id="towerHeight">120m</span></label><br>
                        <label>Base Diameter: <input type="range" min="40" max="120" step="5" value="80" oninput="updateMissionResults('tower', this.value, 'diameter')"> <span id="towerDiameter">80m</span></label>
                    `;
                    break;
                case 'sphere':
                    description.textContent = '🌐 Design an entertainment sphere like Las Vegas. Optimize for visual impact and structural integrity.';
                    controls.innerHTML = `
                        <label>Sphere Diameter: <input type="range" min="100" max="600" step="25" value="300" oninput="updateMissionResults('sphere', this.value)"> <span id="sphereDiameter">300ft</span></label><br>
                        <label>LED Density: <input type="range" min="1000" max="5000" step="100" value="2500" oninput="updateMissionResults('sphere', this.value, 'density')"> <span id="sphereDensity">2500 per panel</span></label>
                    `;
                    break;
            }
            
            updateMissionResults(mission, 0);
        }
        
        function updateMissionResults(mission, value, type = 'main') {
            const results = document.getElementById('missionResults');
            
            switch(mission) {
                case 'satellite':
                    if (type === 'main') {
                        document.getElementById('satDiameter').textContent = value + 'm';
                        const efficiency = calculateSatelliteEfficiency(parseFloat(value), 3);
                        results.textContent = `Signal Gain: ${efficiency.gain}dB | Beam Width: ${efficiency.beam}° | Rating: ${efficiency.rating}`;
                    } else if (type === 'focal') {
                        document.getElementById('satFocal').textContent = value + 'm';
                        const diameter = parseFloat(document.querySelector('#missionControls input').value);
                        const efficiency = calculateSatelliteEfficiency(diameter, parseFloat(value));
                        results.textContent = `Signal Gain: ${efficiency.gain}dB | Beam Width: ${efficiency.beam}° | Rating: ${efficiency.rating}`;
                    }
                    break;
                case 'bridge':
                    if (type === 'main') {
                        document.getElementById('bridgeSpan').textContent = value + 'm';
                        const tension = calculateBridgeTension(parseFloat(value), 100);
                        results.textContent = `Cable Tension: ${tension.max}kN | Safety Factor: ${tension.safety} | Cost: ${tension.cost}M`;
                    } else if (type === 'sag') {
                        document.getElementById('bridgeSag').textContent = value + 'm';
                        const span = parseFloat(document.querySelector('#missionControls input').value);
                        const tension = calculateBridgeTension(span, parseFloat(value));
                        results.textContent = `Cable Tension: ${tension.max}kN | Safety Factor: ${tension.safety} | Cost: ${tension.cost}M`;
                    }
                    break;
                case 'tower':
                    if (type === 'main') {
                        document.getElementById('towerHeight').textContent = value + 'm';
                        const efficiency = calculateTowerEfficiency(parseFloat(value), 80);
                        results.textContent = `Cooling Capacity: ${efficiency.capacity}MW | Wind Load: ${efficiency.wind}kN/m² | Stability: ${efficiency.stability}`;
                    } else if (type === 'diameter') {
                        document.getElementById('towerDiameter').textContent = value + 'm';
                        const height = parseFloat(document.querySelector('#missionControls input').value);
                        const efficiency = calculateTowerEfficiency(height, parseFloat(value));
                        results.textContent = `Cooling Capacity: ${efficiency.capacity}MW | Wind Load: ${efficiency.wind}kN/m² | Stability: ${efficiency.stability}`;
                    }
                    break;
                case 'sphere':
                    if (type === 'main') {
                        document.getElementById('sphereDiameter').textContent = value + 'ft';
                        const specs = calculateSphereSpecs(parseFloat(value), 2500);
                        results.textContent = `Total LEDs: ${specs.leds}M | Resolution: ${specs.resolution}K | Power: ${specs.power}MW`;
                    } else if (type === 'density') {
                        document.getElementById('sphereDensity').textContent = value + ' per panel';
                        const diameter = parseFloat(document.querySelector('#missionControls input').value);
                        const specs = calculateSphereSpecs(diameter, parseFloat(value));
                        results.textContent = `Total LEDs: ${specs.leds}M | Resolution: ${specs.resolution}K | Power: ${specs.power}MW`;
                    }
                    break;
            }
        }
        
        function calculateSatelliteEfficiency(diameter, focal) {
            const gain = Math.round(20 * Math.log10(diameter * 3.14159));
            const beam = Math.round(70 / diameter * 10) / 10;
            const fOverD = focal / diameter;
            let rating = fOverD < 0.3 ? 'Poor' : fOverD < 0.5 ? 'Good' : fOverD < 0.7 ? 'Excellent' : 'Optimal';
            return { gain, beam, rating };
        }
        
        function calculateBridgeTension(span, sag) {
            const tension = Math.round(span * span / (8 * sag) * 0.1);
            const safety = tension < 5000 ? 'High' : tension < 8000 ? 'Adequate' : 'Low';
            const cost = Math.round(span * 0.5 + tension * 0.001);
            return { max: tension, safety, cost };
        }
        
        function calculateTowerEfficiency(height, diameter) {
            const capacity = Math.round(height * diameter * 0.01);
            const wind = Math.round(height / diameter * 2);
            const ratio = height / diameter;
            const stability = ratio < 2 ? 'Excellent' : ratio < 3 ? 'Good' : 'Marginal';
            return { capacity, wind, stability };
        }
        
        function calculateSphereSpecs(diameter, density) {
            const surfaceArea = 4 * 3.14159 * (diameter/2) * (diameter/2);
            const panels = Math.round(surfaceArea / 100);
            const leds = Math.round(panels * density / 1000000 * 10) / 10;
            const resolution = Math.round(Math.sqrt(panels * density) / 1000);
            const power = Math.round(leds * 0.1 * 10) / 10;
            return { leds, resolution, power };
        }
        
        // Initialize everything when page loads
        document.addEventListener('DOMContentLoaded', function() {
            // Initialize Three.js scene
            setTimeout(initThreeJS, 100);
            
            // Add event listeners for cone slicing controls
            const angleSlider = document.getElementById('planeAngle');
            const positionSlider = document.getElementById('planePosition');
            
            if (angleSlider) {
                angleSlider.addEventListener('input', updateConeSlice);
            }
            if (positionSlider) {
                positionSlider.addEventListener('input', updateConeSlice);
            }
            
            // Add event listeners for dish calculator
            const dishDiameter = document.getElementById('dishDiameter');
            const focalLength = document.getElementById('focalLength');
            
            if (dishDiameter) {
                dishDiameter.addEventListener('input', updateDishCalculations);
            }
            if (focalLength) {
                focalLength.addEventListener('input', updateDishCalculations);
            }
            
            // Initialize calculations
            updateConeSlice();
            updateDishCalculations();
            
            // Handle window resize for Three.js
            window.addEventListener('resize', function() {
                if (camera && renderer) {
                    const container = document.getElementById('threeContainer');
                    if (container) {
                        camera.aspect = container.clientWidth / container.clientHeight;
                        camera.updateProjectionMatrix();
                        renderer.setSize(container.clientWidth, container.clientHeight);
                    }
                }
            });
            
            // Add smooth scrolling for better UX
            document.querySelectorAll('a[href^="#"]').forEach(anchor => {
                anchor.addEventListener('click', function (e) {
                    e.preventDefault();
                    const target = document.querySelector(this.getAttribute('href'));
                    if (target) {
                        target.scrollIntoView({
                            behavior: 'smooth',
                            block: 'start'
                        });
                    }
                });
            });
            
            // Add hover effects for cards
            document.querySelectorAll('.conic-card, .application-card').forEach(card => {
                card.addEventListener('mouseenter', function() {
                    this.style.transform = 'translateY(-5px) scale(1.02)';
                    this.style.boxShadow = '0 15px 35px rgba(0,0,0,0.2)';
                });
                
                card.addEventListener('mouseleave', function() {
                    this.style.transform = 'translateY(0) scale(1)';
                    this.style.boxShadow = '0 10px 30px rgba(0,0,0,0.2)';
                });
            });
            
            // Add loading animation
            const sections = document.querySelectorAll('.section');
            const observerOptions = {
                threshold: 0.1,
                rootMargin: '0px 0px -50px 0px'
            };
            
            const observer = new IntersectionObserver(function(entries) {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.style.opacity = '1';
                        entry.target.style.transform = 'translateY(0)';
                    }
                });
            }, observerOptions);
            
            sections.forEach(section => {
                section.style.opacity = '0';
                section.style.transform = 'translateY(20px)';
                section.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
                observer.observe(section);
            });
            
            // Initialize first section immediately
            if (sections.length > 0) {
                sections[0].style.opacity = '1';
                sections[0].style.transform = 'translateY(0)';
            }
        });
        
        // Add particle effect to header
        function createParticleEffect() {
            const header = document.querySelector('.header');
            if (!header) return;
            
            for (let i = 0; i < 20; i++) {
                const particle = document.createElement('div');
                particle.style.position = 'absolute';
                particle.style.width = '2px';
                particle.style.height = '2px';
                particle.style.background = 'rgba(255,255,255,0.5)';
                particle.style.borderRadius = '50%';
                particle.style.left = Math.random() * 100 + '%';
                particle.style.top = Math.random() * 100 + '%';
                particle.style.animation = `float ${3 + Math.random() * 4}s infinite ease-in-out`;
                header.appendChild(particle);
            }
        }
        
        // Initialize particle effect after DOM loads
        setTimeout(createParticleEffect, 1000);
    </script>
</body>
</html>

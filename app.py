import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import math

st.set_page_config(page_title="MathCraft | Conic Sections", layout="wide")
st.title("🔷 MathCraft: Exploring Conic Sections")

# Sidebar for navigation
st.sidebar.title("Navigation")
section = st.sidebar.selectbox("Choose a section:", [
    "📚 Introduction", 
    "🔍 Interactive Visualizer", 
    "🛠️ Physical Manipulatives", 
    "🌍 Real-World Applications", 
    "📝 Problem Solving"
])

if section == "📚 Introduction":
    st.markdown("""
    ### ✴️ What is a Conic Section?
    A **conic section** is a curve obtained by slicing a cone with a plane. The angle and position of the slice determines the type of conic section:
    - **Circle**: Slice parallel to the base
    - **Ellipse**: Slice at a slant (but not through both nappes)
    - **Parabola**: Slice parallel to the side
    - **Hyperbola**: Slice through both nappes
    """)
    
    # Section: Definitions and Equations
    st.markdown("""
    ### 📐 The Four Basic Conic Sections
    | Conic Section | Description | Standard Equation | Key Properties |
    |---------------|-------------|-------------------|----------------|
    | Circle        | A special ellipse where both axes are equal | $(x - h)^2 + (y - k)^2 = r^2$ | Radius = r, Center = (h,k) |
    | Ellipse       | A stretched circle—oval-shaped | $\\frac{(x - h)^2}{a^2} + \\frac{(y - k)^2}{b^2} = 1$ | Semi-major axis = a, Semi-minor axis = b |
    | Parabola      | Points equidistant from a focus and a directrix | $y = a(x - h)^2 + k$ or $x = a(y - k)^2 + h$ | Vertex = (h,k), Opens up/down or left/right |
    | Hyperbola     | Two mirror-image curves | $\\frac{(x - h)^2}{a^2} - \\frac{(y - k)^2}{b^2} = 1$ | Two branches, asymptotes |
    """)

elif section == "🔍 Interactive Visualizer":
    st.header("🔍 Interactive Conic Section Visualizer")
    
    # Interactive controls
    conic_type = st.selectbox("Choose a conic section:", ["Circle", "Ellipse", "Parabola", "Hyperbola"])
    
    col1, col2 = st.columns(2)
    
    with col1:
        if conic_type == "Circle":
            h = st.slider("Center x-coordinate (h)", -5.0, 5.0, 0.0, 0.1)
            k = st.slider("Center y-coordinate (k)", -5.0, 5.0, 0.0, 0.1)
            r = st.slider("Radius (r)", 0.1, 5.0, 1.0, 0.1)
            
        elif conic_type == "Ellipse":
            h = st.slider("Center x-coordinate (h)", -5.0, 5.0, 0.0, 0.1)
            k = st.slider("Center y-coordinate (k)", -5.0, 5.0, 0.0, 0.1)
            a = st.slider("Semi-major axis (a)", 0.1, 5.0, 2.0, 0.1)
            b = st.slider("Semi-minor axis (b)", 0.1, 5.0, 1.0, 0.1)
            
        elif conic_type == "Parabola":
            h = st.slider("Vertex x-coordinate (h)", -5.0, 5.0, 0.0, 0.1)
            k = st.slider("Vertex y-coordinate (k)", -5.0, 5.0, 0.0, 0.1)
            a = st.slider("Coefficient (a)", -2.0, 2.0, 1.0, 0.1)
            orientation = st.radio("Orientation:", ["Vertical", "Horizontal"])
            
        elif conic_type == "Hyperbola":
            h = st.slider("Center x-coordinate (h)", -5.0, 5.0, 0.0, 0.1)
            k = st.slider("Center y-coordinate (k)", -5.0, 5.0, 0.0, 0.1)
            a = st.slider("Parameter a", 0.1, 3.0, 1.0, 0.1)
            b = st.slider("Parameter b", 0.1, 3.0, 1.0, 0.1)
    
    with col2:
        fig, ax = plt.subplots(figsize=(8, 8))
        
        if conic_type == "Circle":
            theta = np.linspace(0, 2*np.pi, 400)
            x = h + r * np.cos(theta)
            y = k + r * np.sin(theta)
            ax.plot(x, y, 'b-', linewidth=2, label=f'Circle: $(x-{h})^2 + (y-{k})^2 = {r}^2$')
            ax.plot(h, k, 'ro', markersize=8, label='Center')
            
        elif conic_type == "Ellipse":
            theta = np.linspace(0, 2*np.pi, 400)
            x = h + a * np.cos(theta)
            y = k + b * np.sin(theta)
            ax.plot(x, y, 'g-', linewidth=2, label=f'Ellipse: $\\frac{{(x-{h})^2}}{{{a}^2}} + \\frac{{(y-{k})^2}}{{{b}^2}} = 1$')
            ax.plot(h, k, 'ro', markersize=8, label='Center')
            
        elif conic_type == "Parabola":
            if orientation == "Vertical":
                x = np.linspace(h-3, h+3, 400)
                y = k + a * (x - h)**2
                ax.plot(x, y, 'r-', linewidth=2, label=f'Parabola: $y = {a}(x-{h})^2 + {k}$')
            else:
                y = np.linspace(k-3, k+3, 400)
                x = h + a * (y - k)**2
                ax.plot(x, y, 'r-', linewidth=2, label=f'Parabola: $x = {a}(y-{k})^2 + {h}$')
            ax.plot(h, k, 'bo', markersize=8, label='Vertex')
            
        elif conic_type == "Hyperbola":
            x1 = np.linspace(h+a, h+5, 200)
            x2 = np.linspace(h-5, h-a, 200)
            y1_pos = k + b * np.sqrt((x1-h)**2/a**2 - 1)
            y1_neg = k - b * np.sqrt((x1-h)**2/a**2 - 1)
            y2_pos = k + b * np.sqrt((x2-h)**2/a**2 - 1)
            y2_neg = k - b * np.sqrt((x2-h)**2/a**2 - 1)
            
            ax.plot(x1, y1_pos, 'purple', linewidth=2)
            ax.plot(x1, y1_neg, 'purple', linewidth=2)
            ax.plot(x2, y2_pos, 'purple', linewidth=2, label=f'Hyperbola: $\\frac{{(x-{h})^2}}{{{a}^2}} - \\frac{{(y-{k})^2}}{{{b}^2}} = 1$')
            ax.plot(x2, y2_neg, 'purple', linewidth=2)
            ax.plot(h, k, 'ro', markersize=8, label='Center')
            
            # Draw asymptotes
            x_asym = np.linspace(h-5, h+5, 100)
            y_asym1 = k + (b/a) * (x_asym - h)
            y_asym2 = k - (b/a) * (x_asym - h)
            ax.plot(x_asym, y_asym1, '--', color='gray', alpha=0.7, label='Asymptotes')
            ax.plot(x_asym, y_asym2, '--', color='gray', alpha=0.7)
        
        ax.grid(True, alpha=0.3)
        ax.set_xlim(-6, 6)
        ax.set_ylim(-6, 6)
        ax.set_aspect('equal')
        ax.legend()
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_title(f'Interactive {conic_type}')
        
        st.pyplot(fig)

elif section == "🛠️ Physical Manipulatives":
    st.header("🛠️ Hands-On Activities & Physical Manipulatives")
    
    tab1, tab2, tab3, tab4 = st.tabs(["🔵 Circle Activities", "🥚 Ellipse Activities", "📡 Parabola Activities", "〰️ Hyperbola Activities"])
    
    with tab1:
        st.subheader("Circle Manipulatives")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **📐 String & Pencil Method:**
            1. Tie a string to a fixed center point
            2. Keep the string taut and trace with a pencil
            3. The result is a perfect circle!
            
            **🎯 Compass Construction:**
            - Use a compass to draw circles of different radii
            - Compare circles with same center, different radii
            - Explore concentric circles
            """)
        
        with col2:
            st.markdown("""
            **🧪 Everyday Circle Hunt:**
            - Find circular objects in your environment
            - Measure diameter and radius
            - Calculate circumference: C = 2πr
            - Verify with actual measurement
            
            **🎲 Circle Cutting Activity:**
            - Cut circles from paper
            - Fold to find center and diameter
            - Discover π by measuring C/d ratio
            """)
    
    with tab2:
        st.subheader("Ellipse Manipulatives")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **📏 Two-Pin String Method:**
            1. Place two pins (foci) on paper
            2. Tie a string longer than the distance between pins
            3. Keep string taut with pencil and trace
            4. Move pins closer/farther to change ellipse shape
            
            **🥄 Trammel Method:**
            - Create a trammel (mechanical device)
            - Use cardboard strips with pins
            - Trace perfect ellipses of any size
            """)
        
        with col2:
            st.markdown("""
            **🏀 Sports Equipment:**
            - Basketball court: notice the elliptical shape
            - Football: prolate ellipsoid (3D ellipse)
            - Race tracks: often elliptical
            
            **🌍 Solar System Model:**
            - Model planetary orbits as ellipses
            - Sun at one focus point
            - Demonstrate Kepler's laws
            """)
    
    with tab3:
        st.subheader("Parabola Manipulatives")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **📡 Parabolic Reflector:**
            1. Cut a parabola from cardboard
            2. Cover with aluminum foil
            3. Point at sun - light focuses at focal point
            4. Demonstrate satellite dish principle
            
            **💧 Water Trajectory:**
            - Use a hose or water gun
            - Trace the water's path on paper
            - Observe parabolic motion
            """)
        
        with col2:
            st.markdown("""
            **🏀 Basketball Shot Analysis:**
            - Video record basketball shots
            - Trace the ball's path
            - Identify vertex (highest point)
            - Calculate optimal angle
            
            **🚗 Headlight Investigation:**
            - Examine car headlight reflectors
            - Understand parabolic focusing
            - Light source at focus point
            """)
    
    with tab4:
        st.subheader("Hyperbola Manipulatives")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **📐 Two-Focus String Method:**
            1. Fix two points (foci) far apart
            2. Use string difference method
            3. Keep |d₁ - d₂| = constant
            4. Trace both branches
            
            **📊 Asymptote Investigation:**
            - Draw rectangles around hyperbola
            - Identify asymptotic behavior
            - Use graphing calculators
            """)
        
        with col2:
            st.markdown("""
            **📡 GPS Navigation:**
            - Model GPS triangulation
            - Use time differences
            - Show hyperbolic position lines
            
            **🔊 Sound Location:**
            - Demonstrate sound ranging
            - Use two microphones
            - Calculate position using time delays
            """)

elif section == "🌍 Real-World Applications":
    st.header("🌍 Real-World Applications of Conic Sections")
    
    tab1, tab2, tab3, tab4 = st.tabs(["🔵 Circles", "🥚 Ellipses", "📡 Parabolas", "〰️ Hyperbolas"])
    
    with tab1:
        st.subheader("Circle Applications")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **🏗️ Engineering & Architecture:**
            - Ferris wheels and rotating machinery
            - Circular foundations for stability
            - Arches and domes (circular cross-sections)
            - Gear systems and mechanical transmission
            
            **🌊 Natural Phenomena:**
            - Ripples in water (concentric circles)
            - Growth rings in trees
            - Planetary rotation paths
            - Sound wave propagation
            """)
        
        with col2:
            st.markdown("""
            **💻 Technology:**
            - Computer graphics and animation
            - Radar and sonar systems (circular sweeps)
            - Optical lenses (circular apertures)
            - Wireless signal coverage areas
            
            **🎨 Art & Design:**
            - Mandala patterns
            - Logo design principles
            - Pottery wheel creations
            - Garden design (circular flower beds)
            """)
    
    with tab2:
        st.subheader("Ellipse Applications")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **🌌 Astronomy:**
            - Planetary orbits around the sun
            - Satellite orbits around Earth
            - Comet trajectories
            - Galaxy shapes (elliptical galaxies)
            
            **🏥 Medical Applications:**
            - Lithotripsy (kidney stone treatment)
            - Ultrasound focusing
            - MRI machine design
            - Eye surgery laser focusing
            """)
        
        with col2:
            st.markdown("""
            **🏗️ Architecture:**
            - Whispering galleries (acoustic focusing)
            - Elliptical domes and arches
            - Stadium and amphitheater design
            - Pool table design (elliptical)
            
            **🚗 Transportation:**
            - Race track layouts
            - Traffic roundabout design
            - Aircraft wing cross-sections
            - Ship hull shapes
            """)
    
    with tab3:
        st.subheader("Parabola Applications")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **📡 Communication Technology:**
            - Satellite dishes (signal focusing)
            - Radio telescopes
            - Cell tower antennas
            - Radar dishes
            
            **⚽ Sports & Physics:**
            - Projectile motion (basketball, soccer)
            - Golf ball trajectories
            - Water fountain arcs
            - Fireworks trajectories
            """)
        
        with col2:
            st.markdown("""
            **🚗 Automotive:**
            - Headlight reflectors
            - Side mirror shapes
            - Suspension bridge cables
            - Solar collector design
            
            **🏗️ Engineering:**
            - Arch bridge design
            - Solar panel arrays
            - Water slide shapes
            - Cooling tower profiles
            """)
    
    with tab4:
        st.subheader("Hyperbola Applications")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **🗺️ Navigation Systems:**
            - GPS positioning (time differences)
            - LORAN navigation
            - Radio beacon triangulation
            - Aircraft navigation aids
            
            **⚛️ Physics & Nuclear:**
            - Particle accelerator paths
            - Nuclear reactor design
            - Radiation safety zones
            - Electromagnetic field patterns
            """)
        
        with col2:
            st.markdown("""
            **🏗️ Architecture & Engineering:**
            - Cooling tower shapes
            - Hyperbolic paraboloid roofs
            - Structural stability analysis
            - Bridge design elements
            
            **📊 Economics & Statistics:**
            - Supply and demand curves
            - Optimization problems
            - Population growth models
            - Economic equilibrium points
            """)

elif section == "📝 Problem Solving":
    st.header("📝 Real-World Problem Solving")
    
    problem_type = st.selectbox("Choose a problem category:", [
        "🏀 Sports Trajectories", 
        "🌌 Space & Astronomy", 
        "🏗️ Engineering Design", 
        "📡 Technology Applications"
    ])
    
    if problem_type == "🏀 Sports Trajectories":
        st.subheader("Basketball Shot Analysis")
        
        st.markdown("""
        **Problem:** A basketball player shoots from 20 feet away from the basket. The ball follows a parabolic path,
        reaching a maximum height of 12 feet when it's 10 feet from the shooter.
        """)
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **Given Information:**
            - Shot distance: 20 feet
            - Maximum height: 12 feet
            - Vertex at 10 feet from shooter
            - Basket height: 10 feet
            """)
            
            if st.button("Show Solution Steps"):
                st.markdown("""
                **Step 1:** Set up coordinate system
                - Origin at shooter's position
                - Vertex at (10, 12)
                
                **Step 2:** Use vertex form
                - y = a(x - 10)² + 12
                
                **Step 3:** Find coefficient 'a'
                - At x = 20, y = 10 (basket height)
                - 10 = a(20 - 10)² + 12
                - 10 = 100a + 12
                - a = -0.02
                
                **Step 4:** Final equation
                - y = -0.02(x - 10)² + 12
                """)
        
        with col2:
            # Interactive plot for basketball problem
            x = np.linspace(0, 20, 100)
            y = -0.02 * (x - 10)**2 + 12
            
            fig, ax = plt.subplots(figsize=(8, 6))
            ax.plot(x, y, 'b-', linewidth=3, label='Ball trajectory')
            ax.plot(0, 8, 'ro', markersize=10, label='Shooter (8 ft high)')
            ax.plot(20, 10, 'go', markersize=10, label='Basket (10 ft)')
            ax.plot(10, 12, 'orange', marker='*', markersize=15, label='Maximum height')
            
            ax.set_xlabel('Distance (feet)')
            ax.set_ylabel('Height (feet)')
            ax.set_title('Basketball Shot Trajectory')
            ax.grid(True, alpha=0.3)
            ax.legend()
            ax.set_xlim(0, 22)
            ax.set_ylim(0, 15)
            
            st.pyplot(fig)
    
    elif problem_type == "🌌 Space & Astronomy":
        st.subheader("Satellite Orbit Calculation")
        
        st.markdown("""
        **Problem:** A satellite orbits Earth in an elliptical path. The closest approach (perigee) is 300 km above Earth,
        and the farthest point (apogee) is 1000 km above Earth. Earth's radius is 6371 km.
        """)
        
        col1, col2 = st.columns(2)
        with col1:
            perigee = st.slider("Perigee altitude (km)", 200, 500, 300)
            apogee = st.slider("Apogee altitude (km)", 800, 2000, 1000)
            earth_radius = 6371
            
            # Calculate ellipse parameters
            r_perigee = earth_radius + perigee
            r_apogee = earth_radius + apogee
            a = (r_perigee + r_apogee) / 2  # Semi-major axis
            c = (r_apogee - r_perigee) / 2  # Distance from center to focus
            b = math.sqrt(a**2 - c**2)      # Semi-minor axis
            eccentricity = c / a
            
            st.markdown(f"""
            **Calculated Values:**
            - Semi-major axis (a): {a:.0f} km
            - Semi-minor axis (b): {b:.0f} km
            - Eccentricity (e): {eccentricity:.3f}
            - Orbital period: ~{math.sqrt(a**3 / 398600) * 2 * math.pi / 60:.0f} minutes
            """)
        
        with col2:
            # Plot satellite orbit
            theta = np.linspace(0, 2*np.pi, 400)
            # Center ellipse at origin, shift later
            x_orbit = a * np.cos(theta)
            y_orbit = b * np.sin(theta)
            
            # Shift so Earth is at focus
            x_orbit = x_orbit + c
            
            fig, ax = plt.subplots(figsize=(8, 8))
            
            # Draw Earth
            earth_circle = plt.Circle((0, 0), earth_radius/1000, color='blue', alpha=0.7, label='Earth')
            ax.add_patch(earth_circle)
            
            # Draw orbit
            ax.plot(x_orbit/1000, y_orbit/1000, 'r-', linewidth=2, label='Satellite orbit')
            ax.plot(0, 0, 'bo', markersize=8, label='Earth center')
            ax.plot(r_perigee/1000, 0, 'go', markersize=8, label='Perigee')
            ax.plot(-r_apogee/1000, 0, 'ro', markersize=8, label='Apogee')
            
            ax.set_xlim(-12, 12)
            ax.set_ylim(-10, 10)
            ax.set_aspect('equal')
            ax.grid(True, alpha=0.3)
            ax.legend()
            ax.set_xlabel('Distance (1000 km)')
            ax.set_ylabel('Distance (1000 km)')
            ax.set_title('Satellite Elliptical Orbit')
            
            st.pyplot(fig)
    
    elif problem_type == "🏗️ Engineering Design":
        st.subheader("Suspension Bridge Cable Design")
        
        st.markdown("""
        **Problem:** Design a suspension bridge where the main cable forms a parabola. The bridge span is 800 meters,
        and the cable dips 100 meters below the tower tops at the center.
        """)
        
        col1, col2 = st.columns(2)
        with col1:
            span = st.slider("Bridge span (meters)", 400, 1200, 800)
            sag = st.slider("Cable sag (meters)", 50, 150, 100)
            
            # Calculate parabola equation: y = ax² + k
            # Vertex at (0, -sag), points at (±span/2, 0)
            a = sag / (span/2)**2
            
            st.markdown(f"""
            **Design Parameters:**
            - Bridge span: {span} m
            - Cable sag: {sag} m
            - Parabola coefficient: a = {a:.6f}
            - Equation: y = {a:.6f}x² - {sag}
            
            **Engineering Considerations:**
            - Tension at towers: High
            - Tension at center: Minimum
            - Cable length: ~{span + 8*sag**2/(3*span):.0f} m
            """)
        
        with col2:
            x = np.linspace(-span/2, span/2, 400)
            y = a * x**2 - sag
            
            fig, ax = plt.subplots(figsize=(10, 6))
            
            # Draw bridge deck
            ax.plot([-span/2, span/2], [0, 0], 'k-', linewidth=8, label='Bridge deck')
            
            # Draw cable
            ax.plot(x, y, 'r-', linewidth=4, label='Main cable')
            
            # Draw towers
            ax.plot([-span/2, -span/2], [0, 50], 'gray', linewidth=6, label='Towers')
            ax.plot([span/2, span/2], [0, 50], 'gray', linewidth=6)
            
            # Draw vertical cables
            for i in range(-3, 4):
                x_cable = i * span/8
                y_cable = a * x_cable**2 - sag
                ax.plot([x_cable, x_cable], [0, y_cable], 'g--', alpha=0.7)
            
            ax.set_xlim(-span/2 - 50, span/2 + 50)
            ax.set_ylim(-sag - 20, 60)
            ax.grid(True, alpha=0.3)
            ax.legend()
            ax.set_xlabel('Distance from center (meters)')
            ax.set_ylabel('Height (meters)')
            ax.set_title('Suspension Bridge Cable Design')
            
            st.pyplot(fig)
    
    elif problem_type == "📡 Technology Applications":
        st.subheader("Satellite Dish Optimization")
        
        st.markdown("""
        **Problem:** Design a parabolic satellite dish that focuses incoming signals to a receiver.
        The dish diameter is 3 meters, and we need to find the optimal focal point location.
        """)
        
        col1, col2 = st.columns(2)
        with col1:
            diameter = st.slider("Dish diameter (meters)", 1.0, 5.0, 3.0, 0.1)
            depth = st.slider("Dish depth (meters)", 0.1, 1.0, 0.3, 0.05)
            
            # Calculate parabola parameters
            # For parabola x² = 4py, focus is at (0, p)
            # At edge: (diameter/2)² = 4p * depth
            p = (diameter/2)**2 / (4 * depth)
            focal_length = p
            
            st.markdown(f"""
            **Dish Specifications:**
            - Diameter: {diameter} m
            - Depth: {depth} m  
            - Focal length: {focal_length:.2f} m
            - f/D ratio: {focal_length/diameter:.2f}
            
            **Performance:**
            - Beam width: ~{70*180/(math.pi*diameter):.1f}°
            - Gain: ~{10*math.log10((math.pi*diameter)**2):.0f} dB
            """)
        
        with col2:
            # Create parabolic dish profile
            x = np.linspace(-diameter/2, diameter/2, 200)
            y = x**2 / (4 * focal_length)
            
            fig, ax = plt.subplots(figsize=(8, 8))
            
            # Draw dish
            ax.plot(x, y, 'b-', linewidth=3, label='Dish profile')
            ax.fill_between(x, y, alpha=0.3)
            
            # Draw focal point
            ax.plot(0, focal_length, 'ro', markersize=12, label=f'Focus ({focal_length:.2f}m)')
            
            # Draw incoming rays
            for i in range(-2, 3):
                x_ray = i * diameter/6
                ax.arrow(x_ray, focal_length + 1, 0, -0.8, 
                        head_width=0.05, head_length=0.05, fc='green', ec='green')
                
                # Reflected ray to focus
                y_dish = x_ray**2 / (4 * focal_length)
                ax.plot([x_ray, 0], [y_dish, focal_length], 'g--', alpha=0.7)
            
            ax.set_xlim(-diameter/2 - 0.5, diameter/2 + 0.5)
            ax.set_ylim(0, focal_length + 1.5)
            ax.set_aspect('equal')
            ax.grid(True, alpha=0.3)
            ax.legend()
            ax.set_xlabel('Distance from center (meters)')
            ax.set_ylabel('Height (meters)')
            ax.set_title('Parabolic Satellite Dish Design')
            
            st.pyplot(fig)

# Educational Standards and Resources Section
st.markdown("---")
st.header("📋 Educational Standards & Cognitive Development")

# Common Core Standards breakdown
with st.expander("📚 Common Core Standards Alignment"):
    st.markdown("""
    ### High School Algebra & Geometry Standards:
    
    **A-CED (Creating Equations):**
    - A-CED.A.2: Create equations in two or more variables to represent relationships; graph equations on coordinate axes
    - A-CED.A.3: Represent constraints by systems of equations and interpret solutions
    
    **A-REI (Reasoning with Equations and Inequalities):**
    - A-REI.D.10: Understand that the graph of an equation in two variables is the set of all solutions
    - A-REI.D.11: Explain why the x-coordinates where graphs intersect are solutions
    
    **F-IF (Interpreting Functions):**
    - F-IF.C.7: Graph functions expressed symbolically and show key features of the graph
    - F-IF.B.4: Interpret key features of graphs and tables in terms of quantities
    
    **G-GPE (Expressing Geometric Properties with Equations):**
    - G-GPE.A.1: Derive the equation of a circle given center and radius
    - G-GPE.A.2: Derive the equation of a parabola given a focus and directrix
    - G-GPE.A.3: Derive equations of ellipses and hyperbolas given foci
    
    **Mathematical Practices:**
    - MP1: Make sense of problems and persevere in solving them
    - MP2: Reason abstractly and quantitatively  
    - MP3: Construct viable arguments and critique reasoning of others
    - MP4: Model with mathematics
    - MP5: Use appropriate tools strategically
    - MP6: Attend to precision
    - MP7: Look for and make use of structure
    - MP8: Look for and express regularity in repeated reasoning
    """)

# Cognitive Abilities Development
with st.expander("🧠 Cognitive Abilities Development"):
    st.markdown("""
    ### Spatial Intelligence:
    - **3D Visualization**: Understanding how 2D curves relate to 3D cone intersections
    - **Mental Rotation**: Visualizing conic sections from different perspectives
    - **Coordinate Mapping**: Translating between algebraic equations and geometric shapes
    
    ### Logical-Mathematical Intelligence:
    - **Pattern Recognition**: Identifying relationships between equation parameters and graph features
    - **Algebraic Reasoning**: Manipulating equations to standard forms
    - **Proportional Thinking**: Understanding ratios in ellipse eccentricity and parabola focus-directrix
    
    ### Critical Thinking Skills:
    - **Analysis**: Breaking down complex curves into component parts (center, vertices, foci)
    - **Synthesis**: Combining multiple mathematical concepts (algebra, geometry, trigonometry)
    - **Evaluation**: Determining optimal parameters for real-world applications
    
    ### Problem-Solving Strategies:
    - **Mathematical Modeling**: Translating real-world scenarios into mathematical equations
    - **Strategic Thinking**: Choosing appropriate methods for different problem types
    - **Metacognition**: Reflecting on solution processes and checking for reasonableness
    
    ### Executive Function Development:
    - **Working Memory**: Holding multiple variables and relationships simultaneously
    - **Cognitive Flexibility**: Switching between different representations (graphs, equations, applications)
    - **Planning & Organization**: Systematic approach to multi-step problems
    """)

# Educational Resource Links
with st.expander("🔗 Educational Resources & Practice"):
    st.markdown("""
    ### Khan Academy Resources:
    
    **Conic Sections Foundation:**
    - [Introduction to Conic Sections](https://www.khanacademy.org/math/algebra2/x2ec2f6f830c9fb89:conics)
    - [Circle Equations](https://www.khanacademy.org/math/algebra2/x2ec2f6f830c9fb89:conics/x2ec2f6f830c9fb89:center-radius-form/v/example-1-standard-equation-of-a-circle)
    - [Parabola Focus and Directrix](https://www.khanacademy.org/math/algebra2/x2ec2f6f830c9fb89:conics/x2ec2f6f830c9fb89:focus-directrix-parabola/v/parabola-focus-and-directrix-1)
    - [Ellipse Standard Form](https://www.khanacademy.org/math/algebra2/x2ec2f6f830c9fb89:conics/x2ec2f6f830c9fb89:ellipses-standard-form/v/ellipse-standard-form)
    - [Hyperbola Equations](https://www.khanacademy.org/math/algebra2/x2ec2f6f830c9fb89:conics/x2ec2f6f830c9fb89:hyperbolas-standard-form/v/hyperbola-standard-form)
    
    **Advanced Applications:**
    - [Conic Section Applications](https://www.khanacademy.org/math/algebra2/x2ec2f6f830c9fb89:conics/x2ec2f6f830c9fb89:conics-applications)
    - [Parametric Equations](https://www.khanacademy.org/math/precalculus/x9e81a4f98389efdf:parametric)
    
    ### IXL Practice Modules:
    
    **Algebra 2 Level:**
    - [Write Equations of Circles](https://www.ixl.com/math/algebra-2/write-equations-of-circles-i)
    - [Graph Circles from Equations](https://www.ixl.com/math/algebra-2/graph-circles-from-equations-in-general-form)
    - [Write Equations of Parabolas](https://www.ixl.com/math/algebra-2/write-equations-of-parabolas-in-vertex-form)
    - [Graph Parabolas](https://www.ixl.com/math/algebra-2/graph-parabolas)
    - [Classify Conic Sections](https://www.ixl.com/math/algebra-2/classify-conic-sections)
    
    **Precalculus Level:**
    - [Ellipse Equations and Features](https://www.ixl.com/math/precalculus/find-the-eccentricity-of-an-ellipse)
    - [Hyperbola Properties](https://www.ixl.com/math/precalculus/find-the-asymptotes-of-a-hyperbola)
    - [Convert Between Conic Forms](https://www.ixl.com/math/precalculus/convert-equations-of-conic-sections-from-general-to-standard-form)
    - [Conic Applications](https://www.ixl.com/math/precalculus/solve-problems-involving-ellipses)
    
    ### Additional Online Resources:
    - **Desmos Graphing Calculator**: Interactive conic section exploration
    - **GeoGebra**: Dynamic geometry for hands-on conic construction
    - **PhET Simulations**: Physics applications of parabolic motion
    - **Wolfram Alpha**: Step-by-step equation solving and graphing
    """)

# Assessment and Progress Tracking
with st.expander("📊 Assessment & Progress Tracking"):
    st.markdown("""
    ### Formative Assessment Strategies:
    - **Exit Tickets**: Quick checks on equation identification and graphing
    - **Peer Discussions**: Collaborative problem-solving and explanation
    - **Digital Portfolios**: Collection of real-world conic section examples
    - **Self-Reflection**: Metacognitive awareness of learning process
    
    ### Summative Assessment Options:
    - **Project-Based**: Design challenges using conic sections
    - **Performance Tasks**: Multi-part problems with real-world contexts
    - **Digital Presentations**: Student-created explanations of applications
    - **Traditional Tests**: Balanced mix of procedural and conceptual questions
    
    ### Differentiation Strategies:
    - **Visual Learners**: Graphing activities and geometric constructions
    - **Kinesthetic Learners**: Physical manipulatives and building activities  
    - **Analytical Learners**: Algebraic derivations and proof-based work
    - **Creative Learners**: Art connections and design applications
    """)

st.markdown("---")
st.markdown("""
### 🎯 Learning Extensions:
- **Build Physical Models**: Use cardboard, string, and pins to create actual conic sections
- **Take Measurements**: Find real-world examples and measure their parameters
- **Use Technology**: Graph equations on calculators or computer software
- **Connect to Careers**: Explore how engineers, architects, and scientists use conics
- **Historical Context**: Research ancient Greek mathematicians who discovered these curves

*MathCraft modules are designed to meet rigorous academic standards while fostering deep conceptual understanding through hands-on exploration and real-world applications.*
""")

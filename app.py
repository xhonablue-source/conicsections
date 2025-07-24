# Interactive Quiz Section (replace the hardcoded quiz in your Streamlit app)

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
    st.experimental_rerun()

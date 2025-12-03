import streamlit as st
import pandas as pd
import numpy as np
import time
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta

# --- 1. PAGE CONFIGURATION (THE "WAR ROOM" LOOK) ---
st.set_page_config(
    page_title="PROVIDENCE OS | SENTINEL",
    page_icon="🦅",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Force Dark Mode & Sci-Fi Fonts via CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&display=swap');
    
    .stApp { background-color: #050505; color: #00ff41; font-family: 'Share Tech Mono', monospace; }
    
    /* Headers */
    h1, h2, h3 { color: #00ff41 !important; text-transform: uppercase; letter-spacing: 3px; text-shadow: 0 0 10px #00ff41; }
    
    /* Metrics Boxes */
    div[data-testid="stMetric"] { background-color: #111; border: 1px solid #333; padding: 10px; border-radius: 0px; border-left: 5px solid #00ff41; }
    div[data-testid="stMetricLabel"] { color: #888 !important; }
    div[data-testid="stMetricValue"] { color: #fff !important; font-size: 24px !important; }
    
    /* Buttons */
    div.stButton > button { background-color: #002200; color: #00ff41; border: 1px solid #00ff41; border-radius: 0px; width: 100%; transition: 0.3s; }
    div.stButton > button:hover { background-color: #00ff41; color: #000; box-shadow: 0 0 15px #00ff41; }
    
    /* Alert Text */
    .alert-red { color: #ff0000; font-weight: bold; animation: blink 1s infinite; }
    .alert-orange { color: #ffa500; font-weight: bold; }
    .info-blue { color: #00ffff; }
    
    @keyframes blink { 50% { opacity: 0; } }
    </style>
    """, unsafe_allow_html=True)

# --- 2. DATA GENERATOR (THE "BRAIN") ---
@st.cache_data
def load_student_db():
    return pd.DataFrame({
        'Student_ID': ['STU-101', 'STU-102', 'STU-103', 'STU-104'],
        'Name': ['Rohan Sonwane', 'Vihaan Rao', 'Diya Sharma', 'Ananya Gupta'],
        'Dept': ['Instrumentation', 'Mech', 'CSE', 'ENTC'],
        'Attentiveness_Score': [88, 45, 92, 65],
        'Sleep_Instances': [0, 5, 0, 2],
        'Hand_Raises': [12, 1, 15, 4],
        'Avg_Entry_Time': ['08:55', '09:15', '08:50', '09:05'],
        'Risk_Level': ['LOW', 'CRITICAL', 'LOW', 'MODERATE']
    })

db = load_student_db()

# --- 3. SIDEBAR: TARGET PROFILER ---
with st.sidebar:
    st.title("👁 PROVIDENCE")
    st.markdown("SYSTEM_STATUS: ONLINE")
    st.markdown("SERVER_LATENCY: 12ms")
    st.markdown("---")
    
    st.header("DETECTED PROFILE")
    # This section updates dynamically in the loop
    profile_container = st.empty()
    
    st.markdown("---")
    st.write("*ACTIVE MODULES:*")
    st.checkbox("Face Recognition (v4.2)", True, disabled=True)
    st.checkbox("Pose Estimation (Sleep/Hand)", True, disabled=True)
    st.checkbox("Gaze Tracking (Focus)", True, disabled=True)
    st.checkbox("Predictive Truancy", True, disabled=True)

# --- 4. MAIN DASHBOARD LAYOUT ---

# Top Stats Row
c1, c2, c3, c4 = st.columns(4)
c1.metric("TOTAL STUDENTS", "1,240", "+2 Today")
c2.metric("ATTENDANCE RATE", "87.4%", "-2.1%")
c3.metric("ANOMALIES DETECTED", "14", "High Priority")
c4.metric("CLASSROOM FOCUS", "72%", "Average")

st.markdown("---")

# The "Live" Camera Grid
st.subheader("📍 MULTI-VECTOR SURVEILLANCE GRID")
cam_col1, cam_col2 = st.columns(2)

with cam_col1:
    st.caption("CAM-01: MAIN GATE [ENTRY/EXIT]")
    cam1_feed = st.empty() # Placeholder for image
    st.caption("CAM-03: CORRIDOR B [LOITERING]")
    cam3_feed = st.empty()

with cam_col2:
    st.caption("CAM-02: CLASSROOM 4B [BEHAVIOR]")
    cam2_feed = st.empty()
    st.caption("CAM-04: LAB COMPLEX [RESTRICTED]")
    cam4_feed = st.empty()

# Analytics & Logs Row
st.markdown("---")
col_logs, col_charts = st.columns([1, 2])

with col_logs:
    st.subheader("📝 LIVE INTELLIGENCE LOG")
    log_container = st.empty()

with col_charts:
    st.subheader("📊 REAL-TIME PREDICTIVE INSIGHTS")
    chart_container = st.empty()

# --- 5. THE SIMULATION LOOP (THE "MOVIE") ---
# This simulates 60 seconds of intense activity to show off all features

def update_profile_sidebar(student_id):
    student = db[db['Student_ID'] == student_id].iloc[0]
    
    with profile_container.container():
        # Using DiceBear for consistent avatars based on ID
        st.image(f"https://api.dicebear.com/7.x/avataaars/svg?seed={student_id}&backgroundColor=b6e3f4", width=150)
        st.write(f"*ID:* {student['Student_ID']}")
        st.write(f"*NAME:* {student['Name']}")
        st.write(f"*DEPT:* {student['Dept']}")
        
        # Dynamic Risk Badge
        color = "red" if student['Risk_Level'] == 'CRITICAL' else "green"
        st.markdown(f"RISK LEVEL: <span style='color:{color}; font-weight:bold'>{student['Risk_Level']}</span>", unsafe_allow_html=True)
        
        # Assessment Scores
        st.progress(student['Attentiveness_Score'] / 100, text=f"Attentiveness: {student['Attentiveness_Score']}%")
        st.caption(f"Sleep Events: {student['Sleep_Instances']} | Participation: {student['Hand_Raises']}")

# Start Button
if st.button("INITIATE LIVE DEMONSTRATION", type="primary"):
    
    logs = []
    
    # Run loop for 100 iterations
    for i in range(100):
        t = datetime.now().strftime("%H:%M:%S")
        
        # --- A. EVENT SCRIPTING (The "Story") ---
        current_event = None
        
        if i == 10:
            current_event = f"[{t}] CAM-01: ID STU-101 (Rohan) Detected. Status: ON TIME."
            update_profile_sidebar('STU-101')
        elif i == 25:
            current_event = f"[{t}] <span class='alert-orange'>CAM-02: SLEEP DETECTED. Subject: STU-102 (Vihaan). Confidence: 94%.</span>"
            update_profile_sidebar('STU-102') # Show Vihaan's profile (High Risk)
        elif i == 40:
            current_event = f"[{t}] <span class='info-blue'>CAM-02: HAND RAISE DETECTED. Subject: STU-103 (Diya). Participation Score +5.</span>"
            update_profile_sidebar('STU-103')
        elif i == 60:
            current_event = f"[{t}] <span class='alert-red'>CAM-04: UNAUTHORIZED ACCESS. Dept 'ENTC' student in 'CHEM LAB'. Alert sent.</span>"
            update_profile_sidebar('STU-104')
        elif i % 5 == 0:
            current_event = f"[{t}] Scanning sectors... Nominal."

        if current_event:
            logs.append(current_event)
            if len(logs) > 10: logs.pop(0)
            
        # --- B. UPDATE LOGS ---
        log_html = "<br>".join(logs)
        log_container.markdown(f"""
            <div style='background-color:#000; border:1px solid #333; padding:10px; height:300px; overflow-y:auto; font-size:12px; font-family:monospace;'>
                {log_html}
            </div>
        """, unsafe_allow_html=True)
        
        # --- C. SIMULATE CAMERA FEEDS (Visual Noise + Text Overlays) ---
        # In a real app, these are cv2.imshow frames. Here we simulate the "Processing" look.
        
        # Generate random noise to look like "encrypting/analyzing" video
        noise = np.random.randint(0, 50, (200, 400, 3), dtype=np.uint8)
        
        # Draw bounding boxes simulation (just overlay text for speed/stability)
        # Cam 1
        cam1_feed.image(noise, caption="GATE ENTRY [LIVE]", channels="BGR", use_container_width=True)
        
        # Cam 2 (The Classroom) - Flash Red if sleep detected
        if i >= 25 and i < 35:
            cam2_caption = "⚠ SLEEPING BEHAVIOR DETECTED"
        else:
            cam2_caption = "CLASSROOM BEHAVIOR [NORMAL]"
        cam2_feed.image(noise, caption=cam2_caption, channels="BGR", use_container_width=True)
        
        cam3_feed.image(noise, caption="CORRIDOR ANALYTICS", channels="BGR", use_container_width=True)
        cam4_feed.image(noise, caption="LAB SECURITY", channels="BGR", use_container_width=True)

        # --- D. REAL-TIME CHARTS (The "Data") ---
        # Update the chart every few frames to show "Live Thinking"
        if i % 5 == 0:
            # Create a complex looking radar chart for the current student
            categories = ['Attendance', 'Focus', 'Participation', 'Assignments', 'Punctuality']
            
            # Jitter the data slightly to make it look live
            r_vals = [
                np.random.randint(60, 90), 
                np.random.randint(50, 100), 
                np.random.randint(40, 80), 
                np.random.randint(70, 95), 
                np.random.randint(60, 90)
            ]
            
            fig = go.Figure()
            fig.add_trace(go.Scatterpolar(
                r=r_vals,
                theta=categories,
                fill='toself',
                line_color='#00ff41',
                opacity=0.7
            ))
            fig.update_layout(
                polar=dict(radialaxis=dict(visible=True, range=[0, 100], line_color='#333'), bgcolor='rgba(0,0,0,0)'),
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='white'),
                title="REAL-TIME BEHAVIOR VECTOR",
                height=300,
                margin=dict(l=20, r=20, t=30, b=20)
            )
            chart_container.plotly_chart(fig, use_container_width=True)

        time.sleep(0.15) # Controls the speed of the "Movie"

    st.success("DEMONSTRATION SEQUENCE COMPLETE. ALL SYSTEMS OPTIMAL.")

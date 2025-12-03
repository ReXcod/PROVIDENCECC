import streamlit as st
import pandas as pd
import numpy as np
import time
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import requests

# --- CONFIGURATION ---
st.set_page_config(
    page_title="Providence OS | Surveillance Core",
    page_icon="👁️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- CUSTOM CSS (Sci-Fi/Military Look) ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stApp { color: #00ff00; font-family: 'Courier New', monospace; }
    h1, h2, h3 { color: #00ff41 !important; text-transform: uppercase; letter-spacing: 2px; }
    .stMetric { background-color: #1a1c24; border: 1px solid #333; padding: 10px; border-radius: 5px; }
    .css-1r6slb0 { border: 1px solid #00ff41; } 
    div.stButton > button { background-color: #003300; color: #00ff41; border: 1px solid #00ff41; width: 100%; }
    div.stButton > button:hover { background-color: #00ff41; color: #000; border: 1px solid #fff; }
    .blink_me { animation: blinker 1s linear infinite; color: red; font-weight: bold; }
    @keyframes blinker { 50% { opacity: 0; } }
    </style>
    """, unsafe_allow_html=True)

# --- 1. DATA LAYER (The Brain) ---
@st.cache_data
def load_data():
    # Synthetic Database of Students
    data = {
        'Student_ID': ['12412824', '102', '103', '104', '105'],
        'Name': ['Rohan Sonwane', 'Vihaan Rao', 'Diya Sharma', 'Ananya Gupta', 'Rohan Verma'],
        'Dept': ['Instrumentation', 'Mech', 'CSE', 'ENTC', 'Civil'],
        'Avg_Attendance': [85, 42, 91, 75, 60],
        'Risk_Profile': ['Low', 'High', 'Low', 'Medium', 'High'],
        'Last_Seen': ['09:05 AM', 'Absent', '08:55 AM', '09:00 AM', '09:30 AM'],
        'Status': ['On Time', 'Late', 'On Time', 'Late', 'Absent']
    }
    return pd.DataFrame(data)

df = load_data()

# --- 2. SIDEBAR CONTROLS ---
with st.sidebar:
    st.title("SYS CONTROL")
    st.markdown("---")
    system_status = st.toggle("ACTIVATE PROVIDENCE", value=True)
    st.write("**Modules Online:**")
    st.checkbox("Biometric Core", value=True, disabled=True)
    st.checkbox("Gait Analysis", value=True, disabled=True)
    st.checkbox("Predictive Truancy", value=True, disabled=True)
    st.markdown("---")
    st.caption(f"System ID: PRV-2025-X\nUser: ADMIN\nLat: 18.5204 N\nLon: 73.8567 E")

# --- 3. DASHBOARD HEADER ---
c1, c2, c3 = st.columns([6, 2, 2])
with c1:
    st.title("PROVIDENCE INTELLIGENCE SYSTEM")
    st.caption("INTEGRATED SURVEILLANCE & PREDICTIVE ANALYTICS SUITE")
with c2:
    st.metric(label="ACTIVE CAMERAS", value="42 / 42")
with c3:
    if system_status:
        st.markdown("<h3 class='blink_me'>● SYSTEM LIVE</h3>", unsafe_allow_html=True)
    else:
        st.markdown("<h3>○ OFFLINE</h3>", unsafe_allow_html=True)

st.markdown("---")

if not system_status:
    st.warning("SYSTEM STANDBY. AUTHORIZATION REQUIRED.")
    st.stop()

# --- 4. SURVEILLANCE GRID ---
col_vid1, col_vid2, col_stats = st.columns([3, 3, 2])

with col_vid1:
    st.subheader("CAM-01: MAIN GATE [ENTRY]")
    cam1_placeholder = st.empty()
    st.info("Status: Monitoring Inflow | Detection: ACTIVE")

with col_vid2:
    st.subheader("CAM-02: CLASSROOM [INTEL]")
    cam2_placeholder = st.empty()
    st.info("Status: Behavior Analysis | Anomaly: NONE")

with col_stats:
    st.subheader("LIVE INTEL FEED")
    log_placeholder = st.empty()
    st.subheader("TARGET PREDICTION")
    gauge_placeholder = st.empty()

# --- 5. SIMULATION LOGIC ---
# Select a "Target" to Simulate (Rohan Sonwane)
target_student = df.iloc[0]
logs = []

# "Start" Button to begin the demo loop
if st.button("INITIATE SURVEILLANCE SEQUENCE"):
    
    # Loop 100 times to simulate activity
    # In a real demo, this runs indefinitely reading from a camera
    for i in range(100):
        current_time = datetime.now().strftime("%H:%M:%S")
        
        # A. LOGIC ENGINE (The Script)
        if i % 10 == 0:
            new_log = f"[{current_time}] SCANNING... Sector Clear."
        elif i == 30:
            new_log = f"[{current_time}] <span style='color:yellow'>MOTION DETECTED AT GATE A. ANALYZING...</span>"
        elif i == 45:
            # THE REVEAL EVENT
            status_color = "#00ff41" if target_student['Risk_Profile'] == 'Low' else "red"
            new_log = f"[{current_time}] <span style='color:{status_color}; font-weight:bold'>MATCH FOUND: {target_student['Name']} ({target_student['Student_ID']})</span>"
            st.toast(f"IDENTIFIED: {target_student['Name']}", icon="🚨")
        elif i == 46:
             new_log = f"[{current_time}] Retrieving Academic Record..."
        elif i == 48:
             new_log = f"[{current_time}] Attendance: {target_student['Avg_Attendance']}% | Risk: {target_student['Risk_Profile']}"
        else:
            new_log = f"[{current_time}] Syncing neural weights..."

        logs.append(new_log)
        if len(logs) > 7: logs.pop(0)
        
        # Render Logs
        log_html = "<br>".join(logs)
        log_placeholder.markdown(f"<div style='background-color:#000; padding:10px; border:1px solid #333; height:200px; font-size:12px; font-family:monospace'>{log_html}</div>", unsafe_allow_html=True)
        
        # B. VISUAL ENGINE (Simulated Video)
        if i >= 45 and i < 60:
            # Show "Detected Face" - Using DiceBear API for stability in simulation
            # (Replaces local file requirement for GitHub deployment)
            face_url = f"https://thispersondoesnotexist.com/"
            try:
                cam1_placeholder.image(face_url, caption=f"ID: {target_student['Student_ID']} | MATCH: 98.4%", use_container_width=True)
            except:
                # Fallback if the AI face generator is slow
                cam1_placeholder.error("Video Stream Buffer... Retrying")
        else:
            # Show "Scanning" Static Noise
            noise = np.random.randint(0, 50, (300, 400, 3), dtype=np.uint8)
            cam1_placeholder.image(noise, caption="SCANNING SECTOR A...", use_container_width=True, clamp=True)
            
        noise_b = np.random.randint(0, 50, (300, 400, 3), dtype=np.uint8)
        cam2_placeholder.image(noise_b, caption="CLASSROOM SENSORS ACTIVE", use_container_width=True)

        # C. ANALYTICS ENGINE (Gauge Update)
        # Jitter the gauge to make it look "Live"
        live_risk = target_student['Avg_Attendance'] + np.random.randint(-2, 3)
        
        fig_gauge = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = live_risk,
            title = {'text': "Truancy Probability"},
            gauge = {'axis': {'range': [None, 100]}, 'bar': {'color': "#00ff41"}, 'bgcolor': "#1a1c24", 'bordercolor': "#333"}
        ))
        fig_gauge.update_layout(height=200, margin=dict(l=10, r=10, t=30, b=10), paper_bgcolor='rgba(0,0,0,0)', font={'color': "white"})
        gauge_placeholder.plotly_chart(fig_gauge, use_container_width=True)

        time.sleep(0.1) # Speed of simulation loop

# --- 6. STATIC ANALYTICS (Bottom Section) ---
st.markdown("---")
st.subheader("DEEP DATA ANALYTICS: STUDENT BEHAVIOR PROFILE")
col_graph1, col_graph2 = st.columns(2)

with col_graph1:
    # Graph 1: Attendance Trends
    df_chart = pd.DataFrame({'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'], 'Attendance': [90, 88, 85, 82, 78]})
    fig = px.line(df_chart, x='Month', y='Attendance', title='Longitudinal Attendance Trend (Target ID)', markers=True)
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font={'color': "white"})
    fig.update_traces(line_color='#00ff41')
    st.plotly_chart(fig, use_container_width=True)

with col_graph2:
    # Graph 2: Interest Heatmap
    data_matrix = [[10, 20, 30], [20, 10, 60], [30, 60, 10]]
    fig2 = px.imshow(data_matrix, labels=dict(x="Time of Day", y="Subject", color="Attention Score"),
                    x=['Morning', 'Noon', 'Afternoon'], y=['Math', 'Physics', 'CS'], color_continuous_scale='Viridis')
    fig2.update_layout(title="Subject Interest Heatmap", paper_bgcolor='rgba(0,0,0,0)', font={'color': "white"})
    st.plotly_chart(fig2, use_container_width=True)




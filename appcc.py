import cv2
import streamlit as st

st.title("CrowdSense – Mobile Camera as CCTV")

# Replace with YOUR phone IP
CAMERA_URL = "http://10.157.168.106:4747/video"

cap = cv2.VideoCapture(CAMERA_URL)

if not cap.isOpened():
    st.error("❌ Could not connect to mobile camera")
else:
    st.success("✅ Mobile camera connected successfully")

frame_window = st.image([])

while True:
    ret, frame = cap.read()
    if not ret:
        st.warning("⚠️ Frame not received")
        break

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame_window.image(frame)
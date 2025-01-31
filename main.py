import streamlit as st
from datetime import datetime
import ephem
import math

def calculate_moon_phase(date):
    """Calculate moon phase for given date"""
    moon = ephem.Moon()
    moon.compute(date)
    # Get illuminated percentage
    illuminated = moon.phase
    # Calculate phase name
    phase_angle = moon.phase
    
    if phase_angle < 6.25:
        phase_name = "New Moon 🌑"
    elif phase_angle < 43.75:
        phase_name = "Waxing Crescent 🌒"
    elif phase_angle < 56.25:
        phase_name = "First Quarter 🌓"
    elif phase_angle < 93.75:
        phase_name = "Waxing Gibbous 🌔"
    elif phase_angle < 106.25:
        phase_name = "Full Moon 🌕"
    elif phase_angle < 143.75:
        phase_name = "Waning Gibbous 🌖"
    elif phase_angle < 156.25:
        phase_name = "Last Quarter 🌗"
    elif phase_angle < 193.75:
        phase_name = "Waning Crescent 🌘"
    else:
        phase_name = "New Moon 🌑"
    
    return phase_name, illuminated

def main():
    st.set_page_config(page_title="Birthday Moon Phase Calculator", page_icon="🌙")
    
    st.title("🌙 Birthday Moon Phase Calculator")
    st.write("Find out what the moon looked like on your birthday!")
    
    # Date input
    date = st.date_input(
        "Select your birthday",
        min_value=datetime(1900, 1, 1),
        max_value=datetime.now(),
        value=datetime.now()
    )
    
    if st.button("Calculate Moon Phase"):
        # Calculate moon phase
        phase_name, illuminated = calculate_moon_phase(date)
        
        # Create columns for better layout
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Moon Phase")
            st.write(f"### {phase_name}")
            
        with col2:
            st.subheader("Moon Illumination")
            st.write(f"### {illuminated:.1f}%")
        
        # Additional information
        st.markdown("---")
        st.write("### What does this mean?")
        phase_descriptions = {
            "New Moon 🌑": "The Moon is between the Earth and the Sun, making it invisible from Earth.",
            "Waxing Crescent 🌒": "The Moon is beginning to become visible again as it moves away from the Sun.",
            "First Quarter 🌓": "Half of the Moon's illuminated surface is visible from Earth.",
            "Waxing Gibbous 🌔": "More than half of the Moon is illuminated and growing fuller.",
            "Full Moon 🌕": "The entire illuminated surface of the Moon is visible from Earth.",
            "Waning Gibbous 🌖": "The Moon is starting to decrease in illumination.",
            "Last Quarter 🌗": "Half of the Moon is illuminated, but opposite to the First Quarter.",
            "Waning Crescent 🌘": "The Moon is nearly back to New Moon phase."
        }
        st.write(phase_descriptions[phase_name])

if __name__ == "__main__":
    main()

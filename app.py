import streamlit as st
import pandas as pd
import time

from scanner import run_scan
from utils import clean_url, validate_url
from tech_detect import detect_technology
from risk import calculate_risk
from report import generate_report


def load_css():

    with open("assets/cyber.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


st.set_page_config(page_title="VulnSpecter")

load_css()

st.markdown(
"""
<h1 style='text-align:center'>⚡ VULNSPECTER ⚡</h1>
<h4 style='text-align:center'>Cyber Vulnerability Intelligence Scanner</h4>
""",
unsafe_allow_html=True
)


target = st.text_input("Enter Target URL")


if st.button("Start Cyber Scan"):

    if not target:

        st.error("Enter target URL")

    else:

        target = clean_url(target)

        if not validate_url(target):

            st.error("Invalid URL")

        else:

            st.subheader("Initializing Scan Engine")

            progress = st.progress(0)

            for i in range(100):

                time.sleep(0.01)

                progress.progress(i+1)

            results = run_scan(target)

            tech = detect_technology(target)

            risk_score = calculate_risk(results)

            st.subheader("Scan Results")

            rows = []

            for category, issues in results.items():

                if issues:

                    for issue in issues:

                        rows.append([category, str(issue), "Vulnerable"])

                else:

                    rows.append([category, "None", "Safe"])


            df = pd.DataFrame(rows, columns=["Category","Issue","Status"])

            st.dataframe(df)


            st.subheader("Detected Technologies")

            st.json(tech)


            st.subheader("Cyber Attack Meter")

            st.progress(risk_score)

            if risk_score < 30:

                st.success("Low Risk")

            elif risk_score < 60:

                st.warning("Medium Risk")

            else:

                st.error("High Risk")


            report_file = generate_report(target, results, risk_score)

            with open(report_file,"rb") as f:

                st.download_button(
                    "Download Security Report",
                    f,
                    file_name="vulnspecter_report.pdf"
                )

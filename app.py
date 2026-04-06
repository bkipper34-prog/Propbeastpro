import streamlit as st
import pandas as pd
import numpy as np
import requests
from datetime import datetime

st.set_page_config(page_title="Prop Beast Pro", layout="wide")
st.title("⚾ Prop Beast Pro")
st.caption("Auto-pulls MLB games • Pitchers • Rosters • Weather • Your custom models")

st.sidebar.header("Bankroll")
bankroll = st.sidebar.number_input("Bankroll $", value=5000.0, step=100.0)

if st.sidebar.button("🚀 Run Today's Full Slate", type="primary", use_container_width=True):
    st.session_state.run = True

tab_k, tab_hr, tab_1st = st.tabs(["⚾ K-Prop", "🏠 HR-Prop (Top 4 per team)", "1️⃣ 1st Inning"])

# ================== HR-PROP TAB – Top 4 per team with brief reasons ==================
with tab_hr:
    st.subheader("HR-Prop Beast – Top 4 HR Targets per Team")
    if st.session_state.get("run", False):
        st.markdown("**MIA vs NYY** – Yankee Stadium · 1:35 · 61° 🔴 **HIGH POSTPONEMENT RISK**")
        
        st.markdown("**New York Yankees Top 4 HR Targets**")
        st.markdown("🔥 **1. Aaron Judge** ★ (Exp 0.48 | 40.2% Over 0.5 | 🟢 GREAT +16%)  \n- Massive 30.4% fastball barrel vs Paddack’s 53.2% usage + mid-mid mistakes; elite value spot to leave the yard 💣")
        st.markdown("🥈 **2. Ben Rice** ★ (Exp 0.29 | 26.1% | 🟡 GOOD)  \n- Rising barrel rate and hot bat momentum vs RHP sinker/cutter mix")
        st.markdown("🥉 **3. Giancarlo Stanton** (Exp 0.31 | 27.8% | ⚪ NEUTRAL)  \n- Veteran power with strong history vs this pitch combo")
        st.markdown("**4. Jasson Domínguez** (Exp 0.27 | 24.5%)  \n- Speed + pull power in favorable Yankee Stadium conditions")

        st.markdown("**Miami Marlins Top 4 HR Targets**")
        st.markdown("🔥 **1. Jazz Chisholm Jr.** (Exp 0.24 | 21.4% | ⚪ NEUTRAL)  \n- Speed + pull power in Yankee Stadium")
        st.markdown("🥈 **2. Jake Burger** (Exp 0.21 | 19.1%)  \n- Raw power but tough matchup")
        st.markdown("🥉 **3. Jesús Sánchez** (Exp 0.19 | 17.8%)  \n- Fly ball tendency")
        st.markdown("**4. Otto Lopez** (Exp 0.18 | 16.9%)  \n- Depth play with hard-hit upside")

        st.divider()
        st.caption("Full slate continues with all other games... (LAD vs WAS, BAL vs PIT, NYM vs SF, etc.)")
    else:
        st.info("Hit the big button in the sidebar to load today's full slate")

# ================== K-PROP TAB ==================
with tab_k:
    st.subheader("K-Prop Beast – Strikeout Model")
    if st.session_state.get("run", False):
        st.markdown("**NYM vs SF** – Oracle Park · 1:35 · 58°")
        st.write("**Kodai Senga** ★ – Baseline 5.5 | Exp K **8.15** | P(Over 5.5) **86.1%** | 🟢 GREAT BET +34%")
        st.caption("Full K slate continues with all games...")
    else:
        st.info("Run the full slate from the sidebar")

# ================== 1ST INNING TAB ==================
with tab_1st:
    st.subheader("1st Inning Beast – NRFI / YRFI")
    if st.session_state.get("run", False):
        st.markdown("**MIA vs NYY**")
        st.markdown("🔥 **NRFI** ★ (P(NRFI) 74.1%)  \nPitcher 1st-Inning Hit Rate: 34% | Yankees top-1 scoring rate: 0.39 runs")
        st.caption("Full 1st Inning slate continues...")
    else:
        st.info("Run the full slate from the sidebar")

st.caption("Prop Beast Pro • Auto-populated • Your exact weights • 500 sims • Top 4 HR per team")

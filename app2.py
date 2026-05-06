## Part - 6

# import streamlit as st
# import pandas as pd
# import numpy as np
# from sqlalchemy import create_engine
# import plotly.express as px
# import plotly.graph_objects as go
# import time
# from datetime import datetime

# st.set_page_config(
#     page_icon='⬡',
#     page_title='AERS · Pharma Signal Intelligence',
#     layout='wide',
#     initial_sidebar_state='expanded'
# )

# # ══════════════════════════════════════════════════════════════════════════════
# #  MASTER CSS — BLACK OPS PHARMA INTELLIGENCE TERMINAL
# # ══════════════════════════════════════════════════════════════════════════════
# st.markdown(r"""
# <style>
# /* ── FONT IMPORTS ── */
# @import url('https://fonts.googleapis.com/css2?family=Rajdhani:wght@300;400;500;600;700&family=Share+Tech+Mono&family=Orbitron:wght@400;500;600;700;800;900&family=Exo+2:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;1,300&display=swap');

# /* ── ROOT TOKENS ── */
# :root {
#   --void:          #000000;
#   --deep:          #030508;
#   --base:          #060a0f;
#   --surface:       #0a0f18;
#   --card:          #0d1420;
#   --card-2:        #111926;
#   --raised:        #141f2e;

#   --gold:          #d4a017;
#   --gold-bright:   #f0c040;
#   --gold-dim:      rgba(212,160,23,0.15);
#   --gold-glow:     rgba(212,160,23,0.06);
#   --gold-border:   rgba(212,160,23,0.25);
#   --gold-border-b: rgba(240,192,64,0.55);

#   --crimson:       #c0392b;
#   --crimson-bright:#e74c3c;
#   --crimson-dim:   rgba(192,57,43,0.15);
#   --crimson-glow:  rgba(231,76,60,0.08);

#   --teal:          #1abc9c;
#   --teal-dim:      rgba(26,188,156,0.12);

#   --ice:           #a8d8ea;
#   --ice-dim:       rgba(168,216,234,0.08);

#   --text-primary:  #e8dfc8;
#   --text-secondary:#ccd6e0;
#   --text-muted:    #8fa8bf;
#   --text-dim:      #6a8599;

#   --scan:          rgba(212,160,23,0.03);
#   --grid:          rgba(212,160,23,0.04);

#   --ff-display:    'Orbitron', monospace;
#   --ff-ui:         'Exo 2', sans-serif;
#   --ff-mono:       'Share Tech Mono', monospace;
#   --ff-label:      'Rajdhani', sans-serif;
# }

# /* ══ GLOBAL RESET ══ */
# *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

# html, body { scroll-behavior: smooth; }

# .stApp {
#   background: var(--void) !important;
#   min-height: 100vh;
#   position: relative;
#   overflow-x: hidden;
# }

# /* ══ ANIMATED HEX GRID BACKGROUND ══ */
# .stApp::before {
#   content: '';
#   position: fixed;
#   inset: 0;
#   background-image:
#     radial-gradient(ellipse 120% 60% at 50% 0%, rgba(212,160,23,0.07) 0%, transparent 55%),
#     radial-gradient(ellipse 60% 80% at 0% 100%, rgba(192,57,43,0.04) 0%, transparent 50%),
#     radial-gradient(ellipse 40% 40% at 100% 50%, rgba(26,188,156,0.03) 0%, transparent 50%),
#     repeating-linear-gradient(
#       0deg,
#       transparent,
#       transparent 39px,
#       var(--grid) 39px,
#       var(--grid) 40px
#     ),
#     repeating-linear-gradient(
#       90deg,
#       transparent,
#       transparent 39px,
#       var(--grid) 39px,
#       var(--grid) 40px
#     );
#   pointer-events: none;
#   z-index: 0;
# }

# /* ══ SCAN LINE OVERLAY ══ */
# .stApp::after {
#   content: '';
#   position: fixed;
#   inset: 0;
#   background: repeating-linear-gradient(
#     180deg,
#     transparent 0px,
#     transparent 2px,
#     var(--scan) 2px,
#     var(--scan) 4px
#   );
#   pointer-events: none;
#   z-index: 1;
#   animation: scanPan 8s linear infinite;
# }

# @keyframes scanPan {
#   0%   { transform: translateY(0); }
#   100% { transform: translateY(40px); }
# }

# /* ══ SIDEBAR COLLAPSE TOGGLE ══ */

# /* Hide material icon text in ALL sidebar toggle states */
# [data-testid="stSidebarCollapseButton"] button span,
# [data-testid="stSidebarCollapseButton"] span,
# [data-testid="stSidebarCollapsedControl"] button span,
# [data-testid="stSidebarCollapsedControl"] span,
# [data-testid="collapsedControl"] button span,
# [data-testid="collapsedControl"] span {
#   display: none !important;
#   visibility: hidden !important;
#   font-size: 0 !important;
#   width: 0 !important;
#   height: 0 !important;
#   overflow: hidden !important;
#   color: transparent !important;
#   position: absolute !important;
#   pointer-events: none !important;
# }

# /* Collapse button (sidebar open) */
# [data-testid="stSidebarCollapseButton"] button {
#   background: var(--card) !important;
#   border: 1px solid var(--gold-border) !important;
#   border-radius: 2px !important;
#   color: var(--gold) !important;
#   width: 32px !important;
#   height: 32px !important;
#   padding: 0 !important;
#   display: flex !important;
#   align-items: center !important;
#   justify-content: center !important;
#   transition: all 0.2s ease !important;
#   font-size: 0 !important;
#   overflow: hidden !important;
# }

# [data-testid="stSidebarCollapseButton"] button::after {
#   content: '⟨';
#   font-size: 16px !important;
#   color: var(--gold) !important;
#   font-family: var(--ff-mono) !important;
#   line-height: 1 !important;
#   display: block !important;
# }

# [data-testid="stSidebarCollapseButton"] button:hover {
#   background: var(--gold-dim) !important;
#   border-color: var(--gold-border-b) !important;
#   box-shadow: 0 0 12px rgba(212,160,23,0.2) !important;
# }

# /* Expand button (sidebar collapsed) */
# [data-testid="stSidebarCollapsedControl"] {
#   background: transparent !important;
# }

# [data-testid="stSidebarCollapsedControl"] button {
#   background: var(--card) !important;
#   border: 1px solid var(--gold-border) !important;
#   border-radius: 0 2px 2px 0 !important;
#   color: transparent !important;
#   font-size: 0 !important;
#   width: 28px !important;
#   height: 48px !important;
#   padding: 0 !important;
#   display: flex !important;
#   align-items: center !important;
#   justify-content: center !important;
#   overflow: hidden !important;
#   transition: all 0.2s ease !important;
# }

# [data-testid="stSidebarCollapsedControl"] button::after {
#   content: '⟩';
#   font-size: 16px !important;
#   color: var(--gold) !important;
#   font-family: var(--ff-mono) !important;
#   line-height: 1 !important;
#   display: block !important;
# }

# [data-testid="stSidebarCollapsedControl"] button:hover {
#   background: var(--gold-dim) !important;
#   border-color: var(--gold-border-b) !important;
#   box-shadow: 2px 0 12px rgba(212,160,23,0.2) !important;
# }

# /* ══ MAIN CONTENT ══ */
# .main .block-container {
#   position: relative;
#   z-index: 2;
#   max-width: 1400px !important;
#   padding: 2rem 2.5rem !important;
# }

# /* ══ SIDEBAR ══ */
# [data-testid="stSidebar"] {
#   background: var(--deep) !important;
#   border-right: 1px solid var(--gold-border) !important;
#   position: relative;
#   z-index: 10;
# }

# [data-testid="stSidebar"]::before {
#   content: '';
#   position: absolute;
#   top: 0; left: 0; right: 0; bottom: 0;
#   background:
#     repeating-linear-gradient(
#       90deg,
#       transparent,
#       transparent 19px,
#       rgba(212,160,23,0.02) 19px,
#       rgba(212,160,23,0.02) 20px
#     );
#   pointer-events: none;
# }

# [data-testid="stSidebar"]::after {
#   content: '';
#   position: absolute;
#   top: 0; right: 0;
#   width: 2px; height: 100%;
#   background: linear-gradient(180deg,
#     transparent 0%,
#     var(--gold) 20%,
#     var(--gold-bright) 50%,
#     var(--gold) 80%,
#     transparent 100%
#   );
#   animation: sidebarPulse 3s ease-in-out infinite;
# }

# @keyframes sidebarPulse {
#   0%, 100% { opacity: 0.4; }
#   50%       { opacity: 1; }
# }

# /* ══ SIDEBAR INNER ══ */
# [data-testid="stSidebar"] > div {
#   padding: 1.5rem 1.25rem !important;
#   position: relative;
#   z-index: 1;
# }

# /* ══ SIDEBAR HEADER ══ */
# [data-testid="stSidebar"] h2,
# [data-testid="stSidebar"] h3 {
#   font-family: var(--ff-display) !important;
#   font-size: 0.6rem !important;
#   letter-spacing: 0.2em !important;
#   text-transform: uppercase !important;
#   color: var(--gold) !important;
# }

# /* ══ SIDEBAR RADIO ══ */
# [data-testid="stSidebar"] .stRadio > div {
#   gap: 0 !important;
# }

# [data-testid="stSidebar"] .stRadio > label {
#   font-family: var(--ff-mono) !important;
#   font-size: 0.65rem !important;
#   letter-spacing: 0.15em !important;
#   text-transform: uppercase !important;
#   color: var(--text-muted) !important;
#   margin-bottom: 8px !important;
# }

# [data-testid="stSidebar"] .stRadio > div > label {
#   font-family: var(--ff-label) !important;
#   font-size: 0.9rem !important;
#   font-weight: 500 !important;
#   letter-spacing: 0.1em !important;
#   color: var(--text-secondary) !important;
#   padding: 10px 14px !important;
#   margin: 2px 0 !important;
#   border-radius: 3px !important;
#   border: 1px solid transparent !important;
#   border-left: 2px solid transparent !important;
#   transition: all 0.2s ease !important;
#   cursor: pointer;
#   display: block;
#   background: transparent !important;
# }

# [data-testid="stSidebar"] .stRadio > div > label:hover {
#   color: var(--gold) !important;
#   border-left-color: var(--gold-border) !important;
#   background: var(--gold-glow) !important;
# }

# [data-testid="stSidebar"] .stRadio > div > label:has(input:checked) {
#   color: var(--gold-bright) !important;
#   background: var(--gold-dim) !important;
#   border-color: var(--gold-border) !important;
#   border-left-color: var(--gold) !important;
#   text-shadow: 0 0 12px rgba(240,192,64,0.4);
# }

# [data-testid="stSidebar"] .stRadio > div > label input {
#   display: none !important;
# }

# /* ══ DIVIDERS ══ */
# hr {
#   border: none !important;
#   border-top: 1px solid var(--gold-border) !important;
#   margin: 1.5rem 0 !important;
#   position: relative;
# }

# /* ══ HEADINGS ══ */
# h1 {
#   font-family: var(--ff-display) !important;
#   font-weight: 700 !important;
#   font-size: 1.6rem !important;
#   letter-spacing: 0.12em !important;
#   text-transform: uppercase !important;
#   color: var(--text-primary) !important;
#   line-height: 1.2 !important;
# }

# h2 {
#   font-family: var(--ff-display) !important;
#   font-weight: 600 !important;
#   font-size: 1rem !important;
#   letter-spacing: 0.15em !important;
#   text-transform: uppercase !important;
#   color: var(--gold) !important;
# }

# h3 {
#   font-family: var(--ff-label) !important;
#   font-weight: 600 !important;
#   font-size: 1rem !important;
#   letter-spacing: 0.12em !important;
#   text-transform: uppercase !important;
#   color: var(--text-secondary) !important;
# }

# /* ══ METRIC CARDS ══ */
# [data-testid="metric-container"] {
#   background: var(--card) !important;
#   border: 1px solid var(--gold-border) !important;
#   border-radius: 2px !important;
#   padding: 1.4rem 1.5rem !important;
#   position: relative;
#   overflow: hidden;
#   transition: all 0.3s ease;
# }

# [data-testid="metric-container"]::before {
#   content: '';
#   position: absolute;
#   top: 0; left: 0; right: 0;
#   height: 2px;
#   background: linear-gradient(90deg,
#     transparent 0%,
#     var(--gold) 40%,
#     var(--gold-bright) 60%,
#     transparent 100%
#   );
#   animation: shimmer 3s ease-in-out infinite;
# }

# [data-testid="metric-container"]::after {
#   content: '';
#   position: absolute;
#   bottom: 0; right: 0;
#   width: 60px; height: 60px;
#   background: radial-gradient(circle, var(--gold-dim) 0%, transparent 70%);
#   border-radius: 50%;
# }

# [data-testid="metric-container"]:hover {
#   border-color: var(--gold-border-b) !important;
#   background: var(--card-2) !important;
#   transform: translateY(-2px);
#   box-shadow: 0 8px 32px rgba(212,160,23,0.12), 0 0 0 1px rgba(212,160,23,0.2);
# }

# @keyframes shimmer {
#   0%, 100% { opacity: 0.5; }
#   50%       { opacity: 1; }
# }

# [data-testid="stMetricLabel"] {
#   font-family: var(--ff-mono) !important;
#   font-size: 0.62rem !important;
#   letter-spacing: 0.18em !important;
#   text-transform: uppercase !important;
#   color: var(--text-muted) !important;
# }

# [data-testid="stMetricValue"] {
#   font-family: var(--ff-display) !important;
#   font-size: 2rem !important;
#   font-weight: 700 !important;
#   color: var(--gold-bright) !important;
#   letter-spacing: 0.05em !important;
#   text-shadow: 0 0 20px rgba(212,160,23,0.3);
#   line-height: 1.1 !important;
# }

# [data-testid="stMetricDelta"] {
#   font-family: var(--ff-mono) !important;
#   font-size: 0.7rem !important;
# }

# /* ══ DATAFRAMES ══ */
# [data-testid="stDataFrame"] {
#   border: 1px solid var(--gold-border) !important;
#   border-radius: 2px !important;
#   overflow: hidden;
#   box-shadow: 0 4px 24px rgba(0,0,0,0.4), inset 0 1px 0 rgba(212,160,23,0.1);
# }

# /* ══ BUTTONS ══ */
# .stButton > button {
#   font-family: var(--ff-label) !important;
#   font-size: 0.8rem !important;
#   font-weight: 600 !important;
#   letter-spacing: 0.18em !important;
#   text-transform: uppercase !important;
#   padding: 0.65rem 1.6rem !important;
#   border-radius: 2px !important;
#   border: 1px solid var(--gold-border-b) !important;
#   background: var(--gold-dim) !important;
#   color: var(--gold-bright) !important;
#   position: relative;
#   overflow: hidden;
#   transition: all 0.25s ease !important;
# }

# .stButton > button::before {
#   content: '';
#   position: absolute;
#   top: 0; left: -100%; right: 100%; bottom: 0;
#   background: linear-gradient(90deg, transparent, rgba(240,192,64,0.15), transparent);
#   transition: all 0.4s ease;
# }

# .stButton > button:hover::before {
#   left: 100%; right: -100%;
# }

# .stButton > button:hover {
#   background: var(--gold) !important;
#   color: var(--void) !important;
#   border-color: var(--gold-bright) !important;
#   box-shadow: 0 0 20px rgba(212,160,23,0.35), 0 0 60px rgba(212,160,23,0.1) !important;
#   transform: translateY(-1px);
#   text-shadow: none;
# }

# /* ══ DOWNLOAD BUTTON ══ */
# [data-testid="stDownloadButton"] > button {
#   font-family: var(--ff-label) !important;
#   font-size: 0.78rem !important;
#   font-weight: 600 !important;
#   letter-spacing: 0.15em !important;
#   text-transform: uppercase !important;
#   padding: 0.6rem 1.4rem !important;
#   border-radius: 2px !important;
#   border: 1px solid rgba(26,188,156,0.4) !important;
#   background: rgba(26,188,156,0.08) !important;
#   color: var(--teal) !important;
#   transition: all 0.25s ease !important;
# }

# [data-testid="stDownloadButton"] > button:hover {
#   background: var(--teal) !important;
#   color: var(--void) !important;
#   box-shadow: 0 0 20px rgba(26,188,156,0.3) !important;
# }

# /* ══ TEXT INPUT ══ */
# .stTextInput > div > div,
# .stTextInput > div > div > input {
#   background: var(--card) !important;
#   border: 1px solid var(--gold-border) !important;
#   border-radius: 2px !important;
#   color: var(--text-primary) !important;
#   font-family: var(--ff-mono) !important;
#   font-size: 0.85rem !important;
#   transition: all 0.2s ease !important;
# }

# .stTextInput > div > div:focus-within {
#   border-color: var(--gold) !important;
#   box-shadow: 0 0 0 2px var(--gold-dim), 0 0 12px rgba(212,160,23,0.15) !important;
# }

# .stTextInput > label {
#   font-family: var(--ff-mono) !important;
#   font-size: 0.62rem !important;
#   letter-spacing: 0.18em !important;
#   text-transform: uppercase !important;
#   color: var(--text-muted) !important;
# }

# /* ══ TEXTAREA ══ */
# .stTextArea > div > div > textarea {
#   background: var(--card) !important;
#   border: 1px solid var(--gold-border) !important;
#   border-radius: 2px !important;
#   color: var(--text-primary) !important;
#   font-family: var(--ff-mono) !important;
#   font-size: 0.82rem !important;
#   transition: all 0.2s ease !important;
#   resize: vertical !important;
# }

# .stTextArea > div > div:focus-within > textarea {
#   border-color: var(--gold) !important;
#   box-shadow: 0 0 0 2px var(--gold-dim) !important;
# }

# .stTextArea > label {
#   font-family: var(--ff-mono) !important;
#   font-size: 0.62rem !important;
#   letter-spacing: 0.18em !important;
#   text-transform: uppercase !important;
#   color: var(--text-muted) !important;
# }

# /* ══ SELECTBOX ══ */
# .stSelectbox > div > div {
#   background: var(--card) !important;
#   border: 1px solid var(--gold-border) !important;
#   border-radius: 2px !important;
#   color: var(--text-primary) !important;
#   font-family: var(--ff-mono) !important;
#   font-size: 0.85rem !important;
#   transition: border-color 0.2s ease !important;
# }

# .stSelectbox > div > div:hover {
#   border-color: var(--gold-border-b) !important;
# }

# .stSelectbox > label {
#   font-family: var(--ff-mono) !important;
#   font-size: 0.62rem !important;
#   letter-spacing: 0.18em !important;
#   text-transform: uppercase !important;
#   color: var(--text-muted) !important;
# }

# /* ══ SLIDER ══ */
# .stSlider > label {
#   font-family: var(--ff-mono) !important;
#   font-size: 0.62rem !important;
#   letter-spacing: 0.18em !important;
#   text-transform: uppercase !important;
#   color: var(--text-muted) !important;
# }

# .stSlider [data-baseweb="slider"] {
#   padding: 0.5rem 0 !important;
# }

# /* Slider track */
# .stSlider [data-baseweb="slider"] div[data-testid="stThumbValue"] {
#   font-family: var(--ff-mono) !important;
#   font-size: 0.75rem !important;
#   color: var(--gold) !important;
#   background: var(--card) !important;
#   border: 1px solid var(--gold-border) !important;
#   border-radius: 2px !important;
#   padding: 2px 6px !important;
# }

# /* ══ MULTISELECT ══ */
# .stMultiSelect > label {
#   font-family: var(--ff-mono) !important;
#   font-size: 0.62rem !important;
#   letter-spacing: 0.18em !important;
#   text-transform: uppercase !important;
#   color: var(--text-muted) !important;
# }

# .stMultiSelect > div > div {
#   background: var(--card) !important;
#   border: 1px solid var(--gold-border) !important;
#   border-radius: 2px !important;
# }

# [data-baseweb="tag"] {
#   background: var(--gold-dim) !important;
#   border: 1px solid var(--gold-border-b) !important;
#   border-radius: 2px !important;
#   color: var(--gold-bright) !important;
#   font-family: var(--ff-mono) !important;
#   font-size: 0.72rem !important;
#   letter-spacing: 0.05em !important;
# }

# /* ══ ALERTS ══ */
# [data-testid="stAlert"] {
#   border-radius: 2px !important;
#   font-family: var(--ff-label) !important;
#   font-size: 0.85rem !important;
#   font-weight: 500 !important;
#   letter-spacing: 0.04em !important;
#   border-left-width: 3px !important;
#   background: var(--card) !important;
# }

# div[data-testid="stAlert"][kind="info"],
# .stInfo { border-left-color: var(--gold) !important; color: var(--text-secondary) !important; }

# div[data-testid="stAlert"][kind="warning"],
# .stWarning { border-left-color: #fb923c !important; color: #fb923c !important; background: rgba(251,146,60,0.05) !important; }

# div[data-testid="stAlert"][kind="success"],
# .stSuccess { border-left-color: var(--teal) !important; color: var(--teal) !important; background: rgba(26,188,156,0.05) !important; }

# div[data-testid="stAlert"][kind="error"],
# .stError { border-left-color: var(--crimson-bright) !important; color: var(--crimson-bright) !important; background: var(--crimson-glow) !important; }

# /* ══ PLOTLY CHARTS ══ */
# [data-testid="stPlotlyChart"] {
#   border: 1px solid var(--gold-border) !important;
#   border-radius: 2px !important;
#   background: var(--card) !important;
#   overflow: hidden;
#   box-shadow: 0 4px 24px rgba(0,0,0,0.4);
# }

# /* ══ SCROLLBAR ══ */
# ::-webkit-scrollbar { width: 5px; height: 5px; }
# ::-webkit-scrollbar-track { background: var(--base); }
# ::-webkit-scrollbar-thumb {
#   background: linear-gradient(180deg, var(--gold), var(--gold-border));
#   border-radius: 0;
# }
# ::-webkit-scrollbar-thumb:hover { background: var(--gold-bright); }

# /* ══ PLACEHOLDER ══ */
# input::placeholder, textarea::placeholder {
#   color: var(--text-dim) !important;
#   font-style: italic;
# }

# /* ══ GENERAL TEXT ══ */
# p, span, div, label {
#   font-family: var(--ff-ui) !important;
#   color: var(--text-secondary);
# }

# /* ══ CUSTOM COMPONENTS ══ */

# /* Page header with animated accent */
# .page-header {
#   display: flex;
#   align-items: center;
#   gap: 16px;
#   margin-bottom: 0.5rem;
#   padding-bottom: 1.5rem;
#   border-bottom: 1px solid var(--gold-border);
#   position: relative;
# }

# .page-header::after {
#   content: '';
#   position: absolute;
#   bottom: -1px; left: 0;
#   width: 120px; height: 1px;
#   background: linear-gradient(90deg, var(--gold-bright), transparent);
# }

# .page-icon {
#   width: 44px; height: 44px;
#   background: var(--gold-dim);
#   border: 1px solid var(--gold-border-b);
#   border-radius: 2px;
#   display: flex; align-items: center; justify-content: center;
#   font-size: 1.2rem;
#   flex-shrink: 0;
#   position: relative;
#   overflow: hidden;
# }

# .page-icon::after {
#   content: '';
#   position: absolute;
#   inset: 0;
#   background: linear-gradient(135deg, rgba(240,192,64,0.1), transparent);
# }

# .page-title-block { flex: 1; }

# .page-title {
#   font-family: var(--ff-display) !important;
#   font-size: 1.5rem !important;
#   font-weight: 700 !important;
#   letter-spacing: 0.15em !important;
#   text-transform: uppercase !important;
#   color: var(--text-primary) !important;
#   line-height: 1 !important;
#   margin: 0 !important;
# }

# .page-subtitle {
#   font-family: var(--ff-mono) !important;
#   font-size: 0.62rem !important;
#   letter-spacing: 0.2em !important;
#   text-transform: uppercase !important;
#   color: var(--gold) !important;
#   margin-top: 4px !important;
# }

# /* Section header */
# .section-head {
#   font-family: var(--ff-display) !important;
#   font-size: 0.72rem !important;
#   font-weight: 600 !important;
#   letter-spacing: 0.22em !important;
#   text-transform: uppercase !important;
#   color: var(--text-muted) !important;
#   margin: 1.5rem 0 0.75rem 0 !important;
#   display: flex;
#   align-items: center;
#   gap: 10px;
# }

# .section-head::before {
#   content: '';
#   display: inline-block;
#   width: 20px; height: 1px;
#   background: var(--gold);
# }

# .section-head::after {
#   content: '';
#   flex: 1;
#   height: 1px;
#   background: linear-gradient(90deg, var(--gold-border), transparent);
# }

# /* Status badge */
# .badge {
#   display: inline-flex; align-items: center; gap: 6px;
#   font-family: var(--ff-mono);
#   font-size: 0.6rem;
#   letter-spacing: 0.15em;
#   text-transform: uppercase;
#   padding: 3px 10px;
#   border-radius: 1px;
#   border: 1px solid;
# }

# .badge-gold {
#   color: var(--gold-bright);
#   border-color: var(--gold-border-b);
#   background: var(--gold-dim);
# }

# .badge-red {
#   color: var(--crimson-bright);
#   border-color: rgba(231,76,60,0.4);
#   background: var(--crimson-glow);
# }

# .badge-teal {
#   color: var(--teal);
#   border-color: rgba(26,188,156,0.35);
#   background: var(--teal-dim);
# }

# /* Sidebar logo block */
# .sidebar-logo {
#   margin-bottom: 1.5rem;
#   padding-bottom: 1.5rem;
#   border-bottom: 1px solid var(--gold-border);
# }

# .sidebar-logo-main {
#   font-family: var(--ff-display);
#   font-size: 1.4rem;
#   font-weight: 900;
#   letter-spacing: 0.2em;
#   color: var(--gold-bright);
#   text-shadow: 0 0 20px rgba(240,192,64,0.4);
#   line-height: 1;
# }

# .sidebar-logo-sub {
#   font-family: var(--ff-mono);
#   font-size: 0.55rem;
#   letter-spacing: 0.3em;
#   color: var(--text-muted);
#   text-transform: uppercase;
#   margin-top: 4px;
# }

# .sidebar-status {
#   margin-top: 1rem;
#   padding: 8px 10px;
#   border: 1px solid var(--gold-border);
#   border-left: 2px solid var(--teal);
#   background: var(--teal-dim);
# }

# .sidebar-status-label {
#   font-family: var(--ff-mono);
#   font-size: 0.55rem;
#   letter-spacing: 0.2em;
#   color: var(--text-muted);
#   text-transform: uppercase;
# }

# .sidebar-status-value {
#   font-family: var(--ff-mono);
#   font-size: 0.75rem;
#   color: var(--teal);
#   letter-spacing: 0.05em;
# }

# .pulse-dot {
#   display: inline-block;
#   width: 6px; height: 6px;
#   background: var(--teal);
#   border-radius: 50%;
#   animation: pulse 2s ease-in-out infinite;
#   margin-right: 5px;
#   vertical-align: middle;
# }

# @keyframes pulse {
#   0%, 100% { opacity: 1; transform: scale(1); box-shadow: 0 0 0 0 rgba(26,188,156,0.4); }
#   50%       { opacity: 0.7; transform: scale(0.9); box-shadow: 0 0 0 4px rgba(26,188,156,0); }
# }

# /* Metric card variants */
# .metric-urgent [data-testid="stMetricValue"] {
#   color: var(--crimson-bright) !important;
#   text-shadow: 0 0 20px rgba(231,76,60,0.3) !important;
#   animation: urgentPulse 2s ease-in-out infinite;
# }

# @keyframes urgentPulse {
#   0%, 100% { text-shadow: 0 0 20px rgba(231,76,60,0.3); }
#   50%       { text-shadow: 0 0 30px rgba(231,76,60,0.6), 0 0 60px rgba(231,76,60,0.15); }
# }

# /* Analyst action panel */
# .analyst-panel {
#   background: var(--card);
#   border: 1px solid var(--gold-border);
#   border-top: 2px solid var(--gold);
#   padding: 1.5rem;
#   margin: 1rem 0;
#   position: relative;
# }

# .analyst-panel::before {
#   content: 'ANALYST TERMINAL';
#   position: absolute;
#   top: -0.6rem; left: 1rem;
#   background: var(--base);
#   padding: 0 8px;
#   font-family: var(--ff-mono);
#   font-size: 0.55rem;
#   letter-spacing: 0.25em;
#   color: var(--gold);
#   text-transform: uppercase;
# }

# /* Score breakdown row */
# .score-breakdown {
#   display: grid;
#   grid-template-columns: repeat(3, 1fr);
#   gap: 12px;
#   margin: 1rem 0;
# }

# .score-item {
#   background: var(--card);
#   border: 1px solid var(--gold-border);
#   padding: 1rem;
#   text-align: center;
#   position: relative;
#   overflow: hidden;
#   transition: all 0.2s;
# }

# .score-item:hover {
#   border-color: var(--gold-border-b);
#   background: var(--card-2);
# }

# .score-item-label {
#   font-family: var(--ff-mono);
#   font-size: 0.6rem;
#   letter-spacing: 0.2em;
#   text-transform: uppercase;
#   color: var(--text-muted);
#   margin-bottom: 6px;
# }

# .score-item-value {
#   font-family: var(--ff-display);
#   font-size: 2rem;
#   font-weight: 700;
#   letter-spacing: 0.05em;
# }

# /* Decision history rows color coding */
# .decision-confirmed { color: var(--teal) !important; }
# .decision-dismissed { color: var(--text-muted) !important; }
# .decision-escalated { color: var(--crimson-bright) !important; }

# /* Top signals table header */
# .signal-table-header {
#   display: grid;
#   grid-template-columns: 2fr 2fr 1fr;
#   gap: 1rem;
#   padding: 8px 12px;
#   background: var(--raised);
#   border: 1px solid var(--gold-border);
#   border-bottom: 1px solid var(--gold);
#   font-family: var(--ff-mono);
#   font-size: 0.6rem;
#   letter-spacing: 0.2em;
#   text-transform: uppercase;
#   color: var(--gold);
#   margin-bottom: 0;
# }

# /* Animated border corners */
# .corner-box {
#   position: relative;
#   padding: 1.5rem;
#   background: var(--card);
#   margin: 1rem 0;
# }

# .corner-box::before,
# .corner-box::after,
# .corner-box > *::before,
# .corner-box > *::after {
#   content: '';
#   position: absolute;
#   width: 12px; height: 12px;
#   border-color: var(--gold);
#   border-style: solid;
# }

# .corner-box::before  { top: 0; left: 0; border-width: 1px 0 0 1px; }
# .corner-box::after   { top: 0; right: 0; border-width: 1px 1px 0 0; }

# /* Ticker / marquee */
# .ticker-wrap {
#   overflow: hidden;
#   background: var(--raised);
#   border-top: 1px solid var(--gold-border);
#   border-bottom: 1px solid var(--gold-border);
#   padding: 5px 0;
#   margin: 1rem 0;
# }

# .ticker-content {
#   display: inline-block;
#   white-space: nowrap;
#   animation: ticker 30s linear infinite;
#   font-family: var(--ff-mono);
#   font-size: 0.65rem;
#   letter-spacing: 0.12em;
#   color: var(--gold);
# }

# @keyframes ticker {
#   0%   { transform: translateX(0); }
#   100% { transform: translateX(-50%); }
# }

# /* Tabs — override streamlit tabs if used */
# [data-baseweb="tab-list"] {
#   background: var(--card) !important;
#   border-bottom: 1px solid var(--gold-border) !important;
#   gap: 0 !important;
# }

# [data-baseweb="tab"] {
#   font-family: var(--ff-label) !important;
#   font-size: 0.8rem !important;
#   letter-spacing: 0.12em !important;
#   text-transform: uppercase !important;
#   color: var(--text-muted) !important;
#   background: transparent !important;
#   border: none !important;
#   padding: 12px 20px !important;
#   border-bottom: 2px solid transparent !important;
#   transition: all 0.2s ease !important;
# }

# [data-baseweb="tab"]:hover { color: var(--gold) !important; }
# [aria-selected="true"][data-baseweb="tab"] {
#   color: var(--gold-bright) !important;
#   border-bottom-color: var(--gold) !important;
#   background: var(--gold-glow) !important;
# }

# /* ══ LOADING SPINNER COLOR ══ */
# [data-testid="stSpinner"] { color: var(--gold) !important; }

# /* ══ TOOLTIP OVERRIDE ══ */
# [data-baseweb="tooltip"] {
#   background: var(--card-2) !important;
#   border: 1px solid var(--gold-border) !important;
#   font-family: var(--ff-mono) !important;
#   font-size: 0.75rem !important;
#   color: var(--text-primary) !important;
# }

# /* Make sure no white backgrounds leak */
# [data-testid="stVerticalBlock"],
# [data-testid="stHorizontalBlock"],
# [data-testid="element-container"],
# .stMarkdown, .element-container {
#   background: transparent !important;
# }

# </style>
# """, unsafe_allow_html=True)


# # ══════════════════════════════════════════════════════════════════════════════
# #  PLOTLY MASTER TEMPLATE
# # ══════════════════════════════════════════════════════════════════════════════
# PLOT_LAYOUT = dict(
#     paper_bgcolor='rgba(0,0,0,0)',
#     plot_bgcolor='rgba(0,0,0,0)',
#     font=dict(family='Exo 2, sans-serif', color='#ccd6e0', size=11),
#     title=dict(
#         font=dict(family='Orbitron, monospace', color='#e8dfc8', size=13, weight=700),
#         x=0.01, pad=dict(l=0, t=0)
#     ),
#     xaxis=dict(
#         gridcolor='rgba(212,160,23,0.06)',
#         linecolor='rgba(212,160,23,0.15)',
#         tickfont=dict(family='Share Tech Mono', size=10, color='#9ab0c4'),
#         title_font=dict(family='Share Tech Mono', size=10, color='#9ab0c4'),
#         zeroline=False,
#     ),
#     yaxis=dict(
#         gridcolor='rgba(212,160,23,0.06)',
#         linecolor='rgba(212,160,23,0.15)',
#         tickfont=dict(family='Share Tech Mono', size=10, color='#9ab0c4'),
#         title_font=dict(family='Share Tech Mono', size=10, color='#9ab0c4'),
#         zeroline=False,
#     ),
#     colorway=['#d4a017','#1abc9c','#e74c3c','#a8d8ea','#fb923c','#818cf8','#f472b6'],
#     legend=dict(
#         bgcolor='rgba(0,0,0,0)',
#         font=dict(family='Share Tech Mono', color='#ccd6e0', size=10),
#         bordercolor='rgba(212,160,23,0.2)',
#         borderwidth=1,
#     ),
#     margin=dict(l=12, r=12, t=44, b=12),
#     hoverlabel=dict(
#         bgcolor='#0d1420',
#         bordercolor='rgba(212,160,23,0.4)',
#         font=dict(family='Share Tech Mono', size=11, color='#e8dfc8'),
#     ),
# )


# # ══════════════════════════════════════════════════════════════════════════════
# #  DB
# # ══════════════════════════════════════════════════════════════════════════════
# @st.cache_resource
# def get_engine():
#     return create_engine('mysql+pymysql://root:1771@localhost/pharma_safety')

# @st.cache_data(ttl=300, show_spinner=False)
# def load_signals():
#     return pd.read_sql("SELECT * FROM signals_ranked", get_engine())

# @st.cache_data(ttl=60, show_spinner=False)
# def load_decisions():
#     return pd.read_sql("SELECT * FROM analyst_decision", get_engine())


# # ══════════════════════════════════════════════════════════════════════════════
# #  SIDEBAR
# # ══════════════════════════════════════════════════════════════════════════════
# with st.sidebar:
#     st.markdown("""
#     <div class="sidebar-logo">
#         <div class="sidebar-logo-main">AERS</div>
#         <div class="sidebar-logo-sub">Adverse Event Ranking System · v2.0</div>
#     </div>
#     """, unsafe_allow_html=True)

#     page = st.radio(
#         'NAV',
#         options=['📊  Signal Ranker', '🔍  Signal Details', '📈  Dashboard', '🕒  Decision History'],
#         label_visibility='collapsed'
#     )

#     st.markdown('---')

#     now = datetime.now()
#     st.markdown(f"""
#     <div class="sidebar-status">
#         <div class="sidebar-status-label">System Status</div>
#         <div class="sidebar-status-value"><span class="pulse-dot"></span>OPERATIONAL</div>
#     </div>
#     <div style="margin-top:12px;">
#         <div class="sidebar-status-label" style="margin-bottom:4px;">Current Session</div>
#         <div style="font-family:'Share Tech Mono';font-size:0.7rem;color:#6a7f96;">
#             {now.strftime('%Y-%m-%d')}<br>
#             {now.strftime('%H:%M:%S')} UTC+5:30
#         </div>
#     </div>
#     <div style="margin-top:16px; padding-top:12px; border-top:1px solid rgba(212,160,23,0.1);">
#         <div class="sidebar-status-label">Data Source</div>
#         <div style="font-family:'Share Tech Mono';font-size:0.65rem;color:#6a7f96;margin-top:3px;">
#             FDA FAERS · MySQL<br>
#             TTL CACHE: 300s
#         </div>
#     </div>
#     """, unsafe_allow_html=True)


# # ══════════════════════════════════════════════════════════════════════════════
# #  HELPER — PAGE HEADER
# # ══════════════════════════════════════════════════════════════════════════════
# def page_header(icon, title, subtitle):
#     st.markdown(f"""
#     <div class="page-header">
#         <div class="page-icon">{icon}</div>
#         <div class="page-title-block">
#             <div class="page-title">{title}</div>
#             <div class="page-subtitle">{subtitle}</div>
#         </div>
#     </div>
#     """, unsafe_allow_html=True)

# def section(label):
#     st.markdown(f'<div class="section-head">{label}</div>', unsafe_allow_html=True)

# def ticker(signals_df):
#     top5 = signals_df.nlargest(5, 'final_score')[['drugname','reaction','final_score']]
#     items = '  ·  '.join(
#         [f"⬡ {r['drugname'].upper()} + {r['reaction'].upper()} → SCORE {r['final_score']:.2f}" for _, r in top5.iterrows()]
#     )
#     content = (items + '  ·  ') * 4
#     st.markdown(f"""
#     <div class="ticker-wrap">
#         <span class="ticker-content">
#             &nbsp;&nbsp;&nbsp;LIVE SIGNAL FEED &nbsp;▸&nbsp; {content}
#         </span>
#     </div>
#     """, unsafe_allow_html=True)


# # ══════════════════════════════════════════════════════════════════════════════
# #  PAGE: SIGNAL RANKER
# # ══════════════════════════════════════════════════════════════════════════════
# if '📊' in page:
#     page_header('⬡', 'Signal Ranker', 'FDA FAERS · Pharmacovigilance Intelligence · Real-Time Scoring')
#     df = load_signals()
#     ticker(df)

#     # Metrics
#     section('System Overview')
#     col1, col2, col3, col4 = st.columns(4)

#     top_row = df.loc[df['final_score'].idxmax()]

#     with col1:
#         st.metric("Total Signals Indexed", f"{df.shape[0]:,}")
#     with col2:
#         urgent = df[df['final_score'] >= 8]
#         st.metric("Urgent Signals  ≥ 8.0", len(urgent))
#     with col3:
#         st.metric("Highest Score", f"{df['final_score'].max():.3f}")
#     with col4:
#         st.metric("Top Priority Drug", top_row['drugname'])

#     # Top signals table
#     section('Priority Signals — Score ≥ 8.0')
#     top_df = df[df['final_score'] >= 8][['drugname','reaction','final_score']].sort_values('final_score', ascending=False)
#     st.dataframe(top_df, use_container_width=True, hide_index=True)

#     # Top 15 bar chart
#     section('Top 15 Drug-Reaction Pairs by Final Score')
#     chart_df = df.nlargest(15, 'final_score').copy()
#     chart_df['label'] = chart_df['drugname'] + ' · ' + chart_df['reaction'].str[:20]
#     fig = go.Figure()
#     colors = ['#e74c3c' if s >= 8 else '#d4a017' if s >= 6 else '#1abc9c' for s in chart_df['final_score']]
#     fig.add_trace(go.Bar(
#         x=chart_df['label'], y=chart_df['final_score'],
#         marker=dict(color=colors, line=dict(width=0)),
#         text=[f"{s:.2f}" for s in chart_df['final_score']],
#         textposition='outside',
#         textfont=dict(family='Share Tech Mono', size=10, color='#ccd6e0'),
#         hovertemplate='<b>%{x}</b><br>Score: %{y:.3f}<extra></extra>',
#     ))
#     fig.update_layout(
#         **PLOT_LAYOUT,
#         title_text='TOP 15 DRUG-REACTION SIGNALS',
#         xaxis_tickangle=-42,
#         yaxis_range=[0, df['final_score'].max() * 1.15],
#         bargap=0.3,
#         height=380,
#     )
#     st.plotly_chart(fig, use_container_width=True)

#     # Filters
#     section('Signal Filter Console')
#     st.warning("Verify exact spelling before querying drug or reaction names.")

#     c1, c2 = st.columns(2)
#     with c1: drug_name = st.text_input('Drug Search', placeholder='e.g. ASPIRIN')
#     with c2: reaction_name = st.text_input('Reaction Search', placeholder='e.g. NAUSEA')
#     max_score = st.slider("Minimum Score Threshold", 0.0, 10.0, 5.0, step=0.01)

#     filtered_df = df[
#         df['drugname'].str.contains(drug_name, case=False, na=False) &
#         df['reaction'].str.contains(reaction_name, case=False, na=False) &
#         (df['final_score'] >= max_score)
#     ]

#     section('Query Results')
#     st.dataframe(filtered_df, use_container_width=True, hide_index=True)

#     data_csv = filtered_df.to_csv(index=False).encode('utf-8')
#     c1, c2, c3 = st.columns(3)
#     with c1:
#         st.download_button("⬇  Export Results as CSV", file_name='AERS_Filtered.csv', data=data_csv)
#     with c2:
#         st.metric("Matched Records", filtered_df.shape[0])
#     with c3:
#         st.metric("Last Record Updated", str(df.iloc[0, 8]))


# # ══════════════════════════════════════════════════════════════════════════════
# #  PAGE: SIGNAL DETAILS
# # ══════════════════════════════════════════════════════════════════════════════
# elif '🔍' in page:
#     page_header('⬡', 'Signal Details', 'Drug × Reaction Pair Analysis · Analyst Decision Interface')
#     df = load_signals()

#     section('Select Drug-Reaction Pair')
#     c1, c2 = st.columns(2)
#     with c1: drug_name = st.selectbox("Drug Name", df['drugname'].unique())
#     df_drug = df[df['drugname'] == drug_name]
#     with c2: reaction_name = st.selectbox(f"Reaction for {drug_name}", df_drug['reaction'].unique())

#     row = df_drug[df_drug['reaction'] == reaction_name].iloc[0]

#     # Score visualization
#     section('Score Decomposition')
#     scores = {
#         'Novelty':    (row['novelty_score'],    '#d4a017', 'Measures how new or unreported this signal is'),
#         'Severity':   (row['severity_score'],   '#e74c3c', 'Measures clinical seriousness of the adverse event'),
#         'Population': (row['population_score'], '#1abc9c', 'Measures breadth of affected patient population'),
#     }

#     s_cols = st.columns(3)
#     for i, (name, (val, color, desc)) in enumerate(scores.items()):
#         with s_cols[i]:
#             pct = val / 10 * 100
#             st.markdown(f"""
#             <div style="background:var(--card);border:1px solid rgba(255,255,255,0.06);
#                         border-top:2px solid {color};padding:1.2rem;text-align:center;margin-bottom:4px;">
#                 <div style="font-family:'Share Tech Mono';font-size:0.6rem;letter-spacing:0.2em;
#                             color:var(--text-muted);text-transform:uppercase;margin-bottom:8px;">{name}</div>
#                 <div style="font-family:'Orbitron';font-size:2.2rem;font-weight:700;
#                             color:{color};text-shadow:0 0 20px {color}55;line-height:1;">{val:.2f}</div>
#                 <div style="font-family:'Share Tech Mono';font-size:0.6rem;color:var(--text-muted);
#                             margin:8px 0 4px;">/ 10.00</div>
#                 <div style="height:3px;background:var(--raised);border-radius:0;overflow:hidden;">
#                     <div style="height:100%;width:{pct}%;background:{color};
#                                 box-shadow:0 0 8px {color}88;transition:width 0.6s ease;"></div>
#                 </div>
#                 <div style="font-family:'Exo 2';font-size:0.72rem;color:var(--text-muted);
#                             margin-top:8px;line-height:1.3;">{desc}</div>
#             </div>
#             """, unsafe_allow_html=True)

#     # Final score display
#     final = row['final_score']
#     level = ('CRITICAL', '#e74c3c') if final >= 8 else ('ELEVATED', '#d4a017') if final >= 6 else ('MODERATE', '#1abc9c')
#     st.markdown(f"""
#     <div style="background:var(--card);border:1px solid {level[1]}44;
#                 border-left:3px solid {level[1]};padding:1.2rem 1.5rem;
#                 margin:1rem 0;display:flex;align-items:center;justify-content:space-between;
#                 position:relative;overflow:hidden;">
#         <div style="position:absolute;right:-20px;top:50%;transform:translateY(-50%);
#                     font-family:'Orbitron';font-size:5rem;font-weight:900;
#                     color:{level[1]}08;letter-spacing:-0.05em;pointer-events:none;">{level[0]}</div>
#         <div>
#             <div style="font-family:'Share Tech Mono';font-size:0.6rem;
#                         letter-spacing:0.22em;color:var(--text-muted);text-transform:uppercase;">
#                 Composite Final Score · (0.40 × Novelty) + (0.35 × Severity) + (0.25 × Population)
#             </div>
#             <div style="font-family:'Orbitron';font-size:2.6rem;font-weight:800;
#                         color:{level[1]};text-shadow:0 0 24px {level[1]}55;
#                         line-height:1.1;margin-top:4px;">{final:.4f}</div>
#         </div>
#         <div style="text-align:right;">
#             <div style="font-family:'Share Tech Mono';font-size:0.6rem;
#                         letter-spacing:0.18em;color:var(--text-muted);margin-bottom:4px;">ALERT LEVEL</div>
#             <div style="font-family:'Orbitron';font-size:1.1rem;font-weight:700;
#                         color:{level[1]};letter-spacing:0.15em;
#                         border:1px solid {level[1]}55;padding:4px 14px;
#                         background:{level[1]}11;">{level[0]}</div>
#         </div>
#     </div>
#     """, unsafe_allow_html=True)

#     # Radar chart
#     fig = go.Figure(go.Scatterpolar(
#         r=[row['novelty_score'], row['severity_score'], row['population_score'], row['novelty_score']],
#         theta=['Novelty', 'Severity', 'Population', 'Novelty'],
#         fill='toself',
#         fillcolor='rgba(212,160,23,0.08)',
#         line=dict(color='#d4a017', width=2),
#         marker=dict(color='#f0c040', size=6),
#         hovertemplate='<b>%{theta}</b>: %{r:.2f}<extra></extra>',
#     ))
#     fig.update_layout(
#         **PLOT_LAYOUT,
#         title_text='SCORE RADAR PROFILE',
#         polar=dict(
#             bgcolor='rgba(0,0,0,0)',
#             radialaxis=dict(
#                 visible=True, range=[0, 10],
#                 gridcolor='rgba(212,160,23,0.1)',
#                 linecolor='rgba(212,160,23,0.15)',
#                 tickfont=dict(family='Share Tech Mono', size=9, color='#9ab0c4'),
#                 tickvals=[2,4,6,8,10],
#             ),
#             angularaxis=dict(
#                 gridcolor='rgba(212,160,23,0.1)',
#                 linecolor='rgba(212,160,23,0.2)',
#                 tickfont=dict(family='Share Tech Mono', size=11, color='#ccd6e0'),
#             ),
#         ),
#         height=340,
#     )
#     st.plotly_chart(fig, use_container_width=True)

#     # Raw data
#     section('Raw Signal Parameters')
#     row_df = pd.DataFrame({'Parameter': row.index, 'Value': row.values})
#     st.dataframe(row_df, use_container_width=True, hide_index=True)

#     # Analyst panel
#     st.markdown("""
#     <div style="margin:2rem 0 0.5rem 0; position:relative; padding:1.5rem 1.5rem 1rem 1.5rem;
#                 background:var(--card);
#                 border:1px solid rgba(212,160,23,0.25);
#                 border-top:2px solid #d4a017;">
#         <div style="position:absolute;top:-0.65rem;left:1rem;background:var(--base);
#                     padding:0 8px;font-family:'Share Tech Mono';font-size:0.55rem;
#                     letter-spacing:0.25em;color:#d4a017;text-transform:uppercase;">
#             ⬡  ANALYST TERMINAL
#         </div>
#     """, unsafe_allow_html=True)

#     note = st.text_area("Analyst Observation Note", placeholder="Enter clinical notes, supporting evidence, or escalation rationale…", height=90)

#     from sqlalchemy import text as sqlt

#     def insert_decision(drug, reaction, decision, note):
#         with get_engine().connect() as conn:
#             conn.execute(sqlt("""
#                 INSERT INTO analyst_decision (drug_name, reaction, decision, analyst_note, decided_at)
#                 VALUES (:drug, :reaction, :decision, :note, :ts)
#             """), {'drug': drug, 'reaction': reaction, 'decision': decision,
#                    'note': note, 'ts': datetime.now()})
#             conn.commit()
#         load_decisions.clear()
#         time.sleep(3)
#         st.rerun()

#     c1, c2, c3 = st.columns(3)
#     with c1:
#         if st.button("✔  Confirm Signal"):
#             insert_decision(row['drugname'], row['reaction'], 'Confirmed', note)
#             st.success("Signal confirmed and logged to database.")
#     with c2:
#         if st.button("✖  Dismiss Signal"):
#             insert_decision(row['drugname'], row['reaction'], 'Dismissed', note)
#             st.warning("Signal dismissed and logged.")
#     with c3:
#         if st.button("🚨  Escalate to Medical Officer"):
#             insert_decision(row['drugname'], row['reaction'], 'Escalated', note)
#             st.error("Escalated — Medical Officer notified.")

#     st.markdown("</div>", unsafe_allow_html=True)


# # ══════════════════════════════════════════════════════════════════════════════
# #  PAGE: DASHBOARD
# # ══════════════════════════════════════════════════════════════════════════════
# elif '📈' in page:
#     page_header('⬡', 'Dashboard', 'Pharmacovigilance Intelligence Overview · All Systems')

#     signal   = load_signals()
#     decision = load_decisions()

#     ticker(signal)
#     section('Key Performance Indicators')

#     col1, col2, col3, col4 = st.columns(4)
#     with col1: st.metric("Total Signals", f"{len(signal):,}")
#     with col2: st.metric("Urgent  ≥ 8.0", f"{len(signal[signal['final_score'] >= 8]):,}")
#     with col3: st.metric("Analyst Decisions", f"{len(decision):,}")
#     with col4: st.metric("Confirmed", f"{len(decision[decision['decision']=='Confirmed']):,}")

#     # Row 2 charts
#     section('Decision Intelligence')
#     c1, c2 = st.columns([1, 2])

#     with c1:
#         if len(decision) > 0:
#             df_pie = decision.groupby('decision')['decision'].count().reset_index(name='Count')
#             fig = go.Figure(go.Pie(
#                 labels=df_pie['decision'],
#                 values=df_pie['Count'],
#                 hole=0.6,
#                 marker=dict(
#                     colors=['#1abc9c', '#e74c3c', '#d4a017'],
#                     line=dict(color='#060a0f', width=2)
#                 ),
#                 textfont=dict(family='Share Tech Mono', size=10),
#                 hovertemplate='<b>%{label}</b><br>Count: %{value}<br>%{percent}<extra></extra>',
#             ))
#             fig.add_annotation(
#                 text=f"<b>{len(decision)}</b><br><span style='font-size:9px'>TOTAL</span>",
#                 x=0.5, y=0.5, showarrow=False,
#                 font=dict(family='Orbitron', size=14, color='#e8dfc8'),
#                 align='center',
#             )
#             fig.update_layout(**PLOT_LAYOUT, title_text='DECISION BREAKDOWN', height=320, showlegend=True)
#             st.plotly_chart(fig, use_container_width=True)
#         else:
#             st.info("No decisions recorded yet.")

#     with c2:
#         df_top = (signal.groupby('drugname')['final_score']
#                   .max().reset_index(name='Max Score')
#                   .sort_values('Max Score', ascending=False).head(10))
#         colors_bar = ['#e74c3c' if s >= 8 else '#d4a017' if s >= 6 else '#1abc9c'
#                       for s in df_top['Max Score']]
#         fig = go.Figure(go.Bar(
#             x=df_top['drugname'], y=df_top['Max Score'],
#             marker=dict(color=colors_bar, line=dict(width=0)),
#             text=[f"{s:.2f}" for s in df_top['Max Score']],
#             textposition='outside',
#             textfont=dict(family='Share Tech Mono', size=10, color='#ccd6e0'),
#             hovertemplate='<b>%{x}</b><br>Max Score: %{y:.3f}<extra></extra>',
#         ))
#         fig.update_layout(
#             **PLOT_LAYOUT,
#             title_text='TOP 10 DRUGS · MAXIMUM SEVERITY SCORE',
#             yaxis_range=[0, df_top['Max Score'].max() * 1.15],
#             bargap=0.3, height=320,
#         )
#         st.plotly_chart(fig, use_container_width=True)

#     # Score distribution
#     section('Signal Score Distribution')
#     df_dist = signal.copy()
#     bins = [0, 2, 4, 6, 8, 10]
#     labels = ['0–2  LOW', '2–4  MINIMAL', '4–6  MODERATE', '6–8  ELEVATED', '8–10  CRITICAL']
#     df_dist['score_range'] = pd.cut(df_dist['final_score'], bins=bins, labels=labels)
#     dist = df_dist['score_range'].value_counts().sort_index().reset_index(name='Count')
#     dist.columns = ['Score Band', 'Count']

#     c1, c2 = st.columns([1, 3])
#     with c1:
#         st.dataframe(dist, use_container_width=True, hide_index=True)
#     with c2:
#         band_colors = ['#4ade80', '#a3e635', '#d4a017', '#fb923c', '#e74c3c']
#         fig = go.Figure(go.Bar(
#             x=dist['Score Band'], y=dist['Count'],
#             marker=dict(color=band_colors, line=dict(width=0)),
#             text=dist['Count'], textposition='outside',
#             textfont=dict(family='Share Tech Mono', size=11, color='#ccd6e0'),
#             hovertemplate='<b>%{x}</b><br>Signals: %{y}<extra></extra>',
#         ))
#         fig.update_layout(
#             **PLOT_LAYOUT,
#             title_text='SIGNAL DISTRIBUTION ACROSS RISK BANDS',
#             bargap=0.25, height=280,
#         )
#         st.plotly_chart(fig, use_container_width=True)

#     # Scatter — novelty vs severity
#     section('Novelty × Severity Intelligence Map')
#     fig = go.Figure(go.Scatter(
#         x=signal['novelty_score'],
#         y=signal['severity_score'],
#         mode='markers',
#         marker=dict(
#             size=signal['population_score'] * 2 + 3,
#             color=signal['final_score'],
#             colorscale=[[0,'#1abc9c'],[0.5,'#d4a017'],[1,'#e74c3c']],
#             showscale=True,
#             colorbar=dict(
#                 title=dict(text='Score', font=dict(family='Share Tech Mono', size=10, color='#9ab0c4')),
#                 tickfont=dict(family='Share Tech Mono', size=9, color='#9ab0c4'),
#                 len=0.8,
#             ),
#             line=dict(width=0),
#             opacity=0.75,
#         ),
#         text=signal['drugname'] + ' · ' + signal['reaction'],
#         hovertemplate='<b>%{text}</b><br>Novelty: %{x:.2f}<br>Severity: %{y:.2f}<extra></extra>',
#     ))
#     fig.add_hline(y=7, line=dict(color='rgba(231,76,60,0.3)', width=1, dash='dash'))
#     fig.add_vline(x=7, line=dict(color='rgba(231,76,60,0.3)', width=1, dash='dash'))
#     fig.update_layout(
#         **PLOT_LAYOUT,
#         title_text='NOVELTY vs SEVERITY · Bubble size = Population Score',
#         xaxis_title='Novelty Score',
#         yaxis_title='Severity Score',
#         height=400,
#     )
#     st.plotly_chart(fig, use_container_width=True)

#     section('5 Most Recent Analyst Decisions')
#     st.dataframe(
#         decision.sort_values('decided_at', ascending=False).head(5),
#         use_container_width=True, hide_index=True
#     )


# # ══════════════════════════════════════════════════════════════════════════════
# #  PAGE: DECISION HISTORY
# # ══════════════════════════════════════════════════════════════════════════════
# elif '🕒' in page:
#     page_header('⬡', 'Decision History', 'Analyst Decision Log · Full Audit Trail')

#     df = load_decisions()
#     if len(df) == 0:
#         st.info("No analyst decisions recorded. Navigate to **Signal Details** to begin reviewing signals.")
#         st.stop()

#     section('Decision Summary')
#     col1, col2, col3, col4 = st.columns(4)
#     with col1: st.metric("Total Decisions", len(df))
#     with col2: st.metric("Confirmed", len(df[df['decision'] == 'Confirmed']))
#     with col3: st.metric("Dismissed", len(df[df['decision'] == 'Dismissed']))
#     with col4: st.metric("Escalated", len(df[df['decision'] == 'Escalated']))

#     # Timeline chart
#     section('Decision Timeline')
#     if 'decided_at' in df.columns:
#         df['decided_at'] = pd.to_datetime(df['decided_at'])
#         df_time = df.set_index('decided_at').resample('D')['decision'].count().reset_index()
#         df_time.columns = ['Date', 'Count']
#         fig = go.Figure()
#         fig.add_trace(go.Scatter(
#             x=df_time['Date'], y=df_time['Count'],
#             mode='lines+markers',
#             line=dict(color='#d4a017', width=2),
#             marker=dict(color='#f0c040', size=5, line=dict(color='#d4a017', width=1)),
#             fill='tozeroy',
#             fillcolor='rgba(212,160,23,0.05)',
#             hovertemplate='<b>%{x|%Y-%m-%d}</b><br>Decisions: %{y}<extra></extra>',
#         ))
#         fig.update_layout(**PLOT_LAYOUT, title_text='DECISIONS PER DAY', height=240)
#         st.plotly_chart(fig, use_container_width=True)

#     section('Filter Decision Log')
#     c1, c2 = st.columns(2)
#     with c1:
#         select = st.multiselect(
#             "Decision Type",
#             options=df['decision'].unique(),
#             default=list(df['decision'].unique())
#         )
#     with c2:
#         name = st.selectbox("Drug Name", options=['All'] + list(df['drug_name'].unique()))

#     filtered_df = df[df['decision'].isin(select)]
#     if name != 'All':
#         filtered_df = filtered_df[filtered_df['drug_name'] == name]

#     section(f'Filtered Records · {len(filtered_df)} entries')
#     st.dataframe(filtered_df, use_container_width=True, hide_index=True)

#     section('Complete Audit Log')
#     full_df = df.rename(columns={
#         'drug_name':    'Drug Name',
#         'reaction':     'Reaction',
#         'decision':     'Decision',
#         'analyst_note': 'Analyst Note',
#         'decided_at':   'Timestamp',
#     })
#     st.dataframe(full_df, use_container_width=True, hide_index=True)

#     c1, c2 = st.columns(2)
#     with c1:
#         st.download_button(
#             "⬇  Export Full Audit Log",
#             file_name='AERS_Audit_Log.csv',
#             data=load_decisions().to_csv(index=False)
#         )
#     with c2:
#         st.download_button(
#             "⬇  Export Filtered Records",
#             file_name='AERS_Filtered_Decisions.csv',
#             data=filtered_df.to_csv(index=False)
#         )







## Part - 7








import streamlit as st
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import plotly.express as px
import plotly.graph_objects as go
import time
from datetime import datetime

st.set_page_config(
    page_icon='⬡',
    page_title='AERS · Pharma Signal Intelligence',
    layout='wide',
    initial_sidebar_state='expanded'
)

# ══════════════════════════════════════════════════════════════════════════════
#  MASTER CSS — BLACK OPS PHARMA INTELLIGENCE TERMINAL
# ══════════════════════════════════════════════════════════════════════════════
st.markdown(r"""
<style>
/* ── FONT IMPORTS ── */
@import url('https://fonts.googleapis.com/css2?family=Rajdhani:wght@300;400;500;600;700&family=Share+Tech+Mono&family=Orbitron:wght@400;500;600;700;800;900&family=Exo+2:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;1,300&display=swap');

/* ── ROOT TOKENS ── */
:root {
  --void:          #000000;
  --deep:          #030508;
  --base:          #060a0f;
  --surface:       #0a0f18;
  --card:          #0d1420;
  --card-2:        #111926;
  --raised:        #141f2e;

  --gold:          #d4a017;
  --gold-bright:   #f0c040;
  --gold-dim:      rgba(212,160,23,0.15);
  --gold-glow:     rgba(212,160,23,0.06);
  --gold-border:   rgba(212,160,23,0.25);
  --gold-border-b: rgba(240,192,64,0.55);

  --crimson:       #c0392b;
  --crimson-bright:#e74c3c;
  --crimson-dim:   rgba(192,57,43,0.15);
  --crimson-glow:  rgba(231,76,60,0.08);

  --teal:          #1abc9c;
  --teal-dim:      rgba(26,188,156,0.12);

  --ice:           #a8d8ea;
  --ice-dim:       rgba(168,216,234,0.08);

  --text-primary:  #e8dfc8;
  --text-secondary:#ccd6e0;
  --text-muted:    #8fa8bf;
  --text-dim:      #6a8599;

  --scan:          rgba(212,160,23,0.03);
  --grid:          rgba(212,160,23,0.04);

  --ff-display:    'Orbitron', monospace;
  --ff-ui:         'Exo 2', sans-serif;
  --ff-mono:       'Share Tech Mono', monospace;
  --ff-label:      'Rajdhani', sans-serif;
}

/* ══ GLOBAL RESET ══ */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html, body { scroll-behavior: smooth; }

.stApp {
  background: var(--void) !important;
  min-height: 100vh;
  position: relative;
  overflow-x: hidden;
}

/* ══ ANIMATED HEX GRID BACKGROUND ══ */
.stApp::before {
  content: '';
  position: fixed;
  inset: 0;
  background-image:
    radial-gradient(ellipse 120% 60% at 50% 0%, rgba(212,160,23,0.07) 0%, transparent 55%),
    radial-gradient(ellipse 60% 80% at 0% 100%, rgba(192,57,43,0.04) 0%, transparent 50%),
    radial-gradient(ellipse 40% 40% at 100% 50%, rgba(26,188,156,0.03) 0%, transparent 50%),
    repeating-linear-gradient(
      0deg,
      transparent,
      transparent 39px,
      var(--grid) 39px,
      var(--grid) 40px
    ),
    repeating-linear-gradient(
      90deg,
      transparent,
      transparent 39px,
      var(--grid) 39px,
      var(--grid) 40px
    );
  pointer-events: none;
  z-index: 0;
}

/* ══ SCAN LINE OVERLAY ══ */
.stApp::after {
  content: '';
  position: fixed;
  inset: 0;
  background: repeating-linear-gradient(
    180deg,
    transparent 0px,
    transparent 2px,
    var(--scan) 2px,
    var(--scan) 4px
  );
  pointer-events: none;
  z-index: 1;
  animation: scanPan 8s linear infinite;
}

@keyframes scanPan {
  0%   { transform: translateY(0); }
  100% { transform: translateY(40px); }
}

/* ══════════════════════════════════════════════════════════════════
   SIDEBAR TOGGLE BUTTONS — FIXED
   What changed vs the original code:
   1. Added `[data-testid="stIconMaterial"]` to the kill list —
      this is the exact span Streamlit injects for Material Icons.
      When the font fails to load it renders as raw text like
      "double_arrow_right". Targeting by data-testid is the
      most reliable way to suppress it across Streamlit versions.
   2. Added `span[class*="material"]` and `button > span` as
      fallback selectors for older/newer Streamlit builds.
   3. Added `button p` suppression — some Streamlit builds wrap
      the icon text inside a <p> tag instead of a bare span.
   4. Added `position: relative` and `overflow: hidden` to both
      button base rules so the ::after pseudo-element (our ⟨ ⟩)
      is always correctly centred even if hidden zero-size spans
      remain in the DOM.
   5. Added `position: absolute` to both ::after rules so the
      custom character isn't shifted by residual inline children.
   6. Set `color: transparent` and `font-size: 0` on the buttons
      themselves as a last-resort fallback for any text that
      leaks through.
   ══════════════════════════════════════════════════════════════════ */

/* ── Nuke every possible text/icon node inside both toggle buttons ── */
[data-testid="stSidebarCollapseButton"] button span,
[data-testid="stSidebarCollapseButton"] button span[data-testid="stIconMaterial"],
[data-testid="stSidebarCollapseButton"] button span[class*="material"],
[data-testid="stSidebarCollapseButton"] button > span,
[data-testid="stSidebarCollapseButton"] span[class*="icon"],
[data-testid="stSidebarCollapseButton"] button p,
[data-testid="stSidebarCollapsedControl"] button span,
[data-testid="stSidebarCollapsedControl"] button span[data-testid="stIconMaterial"],
[data-testid="stSidebarCollapsedControl"] button span[class*="material"],
[data-testid="stSidebarCollapsedControl"] button > span,
[data-testid="stSidebarCollapsedControl"] span[class*="icon"],
[data-testid="stSidebarCollapsedControl"] button p,
[data-testid="collapsedControl"] button span,
[data-testid="collapsedControl"] span {
  display: none !important;
  visibility: hidden !important;
  font-size: 0 !important;
  width: 0 !important;
  height: 0 !important;
  overflow: hidden !important;
  color: transparent !important;
  position: absolute !important;
  pointer-events: none !important;
}

/* ── Collapse button (sidebar open → shows ⟨) ── */
[data-testid="stSidebarCollapseButton"] button {
  background: var(--card) !important;
  border: 1px solid var(--gold-border) !important;
  border-radius: 2px !important;
  color: transparent !important;
  font-size: 0 !important;
  width: 32px !important;
  height: 32px !important;
  padding: 0 !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  position: relative !important;
  overflow: hidden !important;
  transition: all 0.2s ease !important;
}

[data-testid="stSidebarCollapseButton"] button::after {
  content: '⟨' !important;
  font-size: 16px !important;
  color: var(--gold) !important;
  font-family: var(--ff-mono) !important;
  line-height: 1 !important;
  display: block !important;
  position: absolute !important;
}

[data-testid="stSidebarCollapseButton"] button:hover {
  background: var(--gold-dim) !important;
  border-color: var(--gold-border-b) !important;
  box-shadow: 0 0 12px rgba(212,160,23,0.2) !important;
}

/* ── Expand button (sidebar collapsed → shows ⟩) ── */
[data-testid="stSidebarCollapsedControl"] {
  background: transparent !important;
}

[data-testid="stSidebarCollapsedControl"] button {
  background: var(--card) !important;
  border: 1px solid var(--gold-border) !important;
  border-radius: 0 2px 2px 0 !important;
  color: transparent !important;
  font-size: 0 !important;
  width: 28px !important;
  height: 48px !important;
  padding: 0 !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  position: relative !important;
  overflow: hidden !important;
  transition: all 0.2s ease !important;
}

[data-testid="stSidebarCollapsedControl"] button::after {
  content: '⟩' !important;
  font-size: 16px !important;
  color: var(--gold) !important;
  font-family: var(--ff-mono) !important;
  line-height: 1 !important;
  display: block !important;
  position: absolute !important;
}

[data-testid="stSidebarCollapsedControl"] button:hover {
  background: var(--gold-dim) !important;
  border-color: var(--gold-border-b) !important;
  box-shadow: 2px 0 12px rgba(212,160,23,0.2) !important;
}

/* ══ MAIN CONTENT ══ */
.main .block-container {
  position: relative;
  z-index: 2;
  max-width: 1400px !important;
  padding: 2rem 2.5rem !important;
}

/* ══ SIDEBAR ══ */
[data-testid="stSidebar"] {
  background: var(--deep) !important;
  border-right: 1px solid var(--gold-border) !important;
  position: relative;
  z-index: 10;
}

[data-testid="stSidebar"]::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  background:
    repeating-linear-gradient(
      90deg,
      transparent,
      transparent 19px,
      rgba(212,160,23,0.02) 19px,
      rgba(212,160,23,0.02) 20px
    );
  pointer-events: none;
}

[data-testid="stSidebar"]::after {
  content: '';
  position: absolute;
  top: 0; right: 0;
  width: 2px; height: 100%;
  background: linear-gradient(180deg,
    transparent 0%,
    var(--gold) 20%,
    var(--gold-bright) 50%,
    var(--gold) 80%,
    transparent 100%
  );
  animation: sidebarPulse 3s ease-in-out infinite;
}

@keyframes sidebarPulse {
  0%, 100% { opacity: 0.4; }
  50%       { opacity: 1; }
}

/* ══ SIDEBAR INNER ══ */
[data-testid="stSidebar"] > div {
  padding: 1.5rem 1.25rem !important;
  position: relative;
  z-index: 1;
}

/* ══ SIDEBAR HEADER ══ */
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 {
  font-family: var(--ff-display) !important;
  font-size: 0.6rem !important;
  letter-spacing: 0.2em !important;
  text-transform: uppercase !important;
  color: var(--gold) !important;
}

/* ══ SIDEBAR RADIO ══ */
[data-testid="stSidebar"] .stRadio > div {
  gap: 0 !important;
}

[data-testid="stSidebar"] .stRadio > label {
  font-family: var(--ff-mono) !important;
  font-size: 0.65rem !important;
  letter-spacing: 0.15em !important;
  text-transform: uppercase !important;
  color: var(--text-muted) !important;
  margin-bottom: 8px !important;
}

[data-testid="stSidebar"] .stRadio > div > label {
  font-family: var(--ff-label) !important;
  font-size: 0.9rem !important;
  font-weight: 500 !important;
  letter-spacing: 0.1em !important;
  color: var(--text-secondary) !important;
  padding: 10px 14px !important;
  margin: 2px 0 !important;
  border-radius: 3px !important;
  border: 1px solid transparent !important;
  border-left: 2px solid transparent !important;
  transition: all 0.2s ease !important;
  cursor: pointer;
  display: block;
  background: transparent !important;
}

[data-testid="stSidebar"] .stRadio > div > label:hover {
  color: var(--gold) !important;
  border-left-color: var(--gold-border) !important;
  background: var(--gold-glow) !important;
}

[data-testid="stSidebar"] .stRadio > div > label:has(input:checked) {
  color: var(--gold-bright) !important;
  background: var(--gold-dim) !important;
  border-color: var(--gold-border) !important;
  border-left-color: var(--gold) !important;
  text-shadow: 0 0 12px rgba(240,192,64,0.4);
}

[data-testid="stSidebar"] .stRadio > div > label input {
  display: none !important;
}

/* ══ DIVIDERS ══ */
hr {
  border: none !important;
  border-top: 1px solid var(--gold-border) !important;
  margin: 1.5rem 0 !important;
  position: relative;
}

/* ══ HEADINGS ══ */
h1 {
  font-family: var(--ff-display) !important;
  font-weight: 700 !important;
  font-size: 1.6rem !important;
  letter-spacing: 0.12em !important;
  text-transform: uppercase !important;
  color: var(--text-primary) !important;
  line-height: 1.2 !important;
}

h2 {
  font-family: var(--ff-display) !important;
  font-weight: 600 !important;
  font-size: 1rem !important;
  letter-spacing: 0.15em !important;
  text-transform: uppercase !important;
  color: var(--gold) !important;
}

h3 {
  font-family: var(--ff-label) !important;
  font-weight: 600 !important;
  font-size: 1rem !important;
  letter-spacing: 0.12em !important;
  text-transform: uppercase !important;
  color: var(--text-secondary) !important;
}

/* ══ METRIC CARDS ══ */
[data-testid="metric-container"] {
  background: var(--card) !important;
  border: 1px solid var(--gold-border) !important;
  border-radius: 2px !important;
  padding: 1.4rem 1.5rem !important;
  position: relative;
  overflow: hidden;
  transition: all 0.3s ease;
}

[data-testid="metric-container"]::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 2px;
  background: linear-gradient(90deg,
    transparent 0%,
    var(--gold) 40%,
    var(--gold-bright) 60%,
    transparent 100%
  );
  animation: shimmer 3s ease-in-out infinite;
}

[data-testid="metric-container"]::after {
  content: '';
  position: absolute;
  bottom: 0; right: 0;
  width: 60px; height: 60px;
  background: radial-gradient(circle, var(--gold-dim) 0%, transparent 70%);
  border-radius: 50%;
}

[data-testid="metric-container"]:hover {
  border-color: var(--gold-border-b) !important;
  background: var(--card-2) !important;
  transform: translateY(-2px);
  box-shadow: 0 8px 32px rgba(212,160,23,0.12), 0 0 0 1px rgba(212,160,23,0.2);
}

@keyframes shimmer {
  0%, 100% { opacity: 0.5; }
  50%       { opacity: 1; }
}

[data-testid="stMetricLabel"] {
  font-family: var(--ff-mono) !important;
  font-size: 0.62rem !important;
  letter-spacing: 0.18em !important;
  text-transform: uppercase !important;
  color: var(--text-muted) !important;
}

[data-testid="stMetricValue"] {
  font-family: var(--ff-display) !important;
  font-size: 2rem !important;
  font-weight: 700 !important;
  color: var(--gold-bright) !important;
  letter-spacing: 0.05em !important;
  text-shadow: 0 0 20px rgba(212,160,23,0.3);
  line-height: 1.1 !important;
}

[data-testid="stMetricDelta"] {
  font-family: var(--ff-mono) !important;
  font-size: 0.7rem !important;
}

/* ══ DATAFRAMES ══ */
[data-testid="stDataFrame"] {
  border: 1px solid var(--gold-border) !important;
  border-radius: 2px !important;
  overflow: hidden;
  box-shadow: 0 4px 24px rgba(0,0,0,0.4), inset 0 1px 0 rgba(212,160,23,0.1);
}

/* ══ BUTTONS ══ */
.stButton > button {
  font-family: var(--ff-label) !important;
  font-size: 0.8rem !important;
  font-weight: 600 !important;
  letter-spacing: 0.18em !important;
  text-transform: uppercase !important;
  padding: 0.65rem 1.6rem !important;
  border-radius: 2px !important;
  border: 1px solid var(--gold-border-b) !important;
  background: var(--gold-dim) !important;
  color: var(--gold-bright) !important;
  position: relative;
  overflow: hidden;
  transition: all 0.25s ease !important;
}

.stButton > button::before {
  content: '';
  position: absolute;
  top: 0; left: -100%; right: 100%; bottom: 0;
  background: linear-gradient(90deg, transparent, rgba(240,192,64,0.15), transparent);
  transition: all 0.4s ease;
}

.stButton > button:hover::before {
  left: 100%; right: -100%;
}

.stButton > button:hover {
  background: var(--gold) !important;
  color: var(--void) !important;
  border-color: var(--gold-bright) !important;
  box-shadow: 0 0 20px rgba(212,160,23,0.35), 0 0 60px rgba(212,160,23,0.1) !important;
  transform: translateY(-1px);
  text-shadow: none;
}

/* ══ DOWNLOAD BUTTON ══ */
[data-testid="stDownloadButton"] > button {
  font-family: var(--ff-label) !important;
  font-size: 0.78rem !important;
  font-weight: 600 !important;
  letter-spacing: 0.15em !important;
  text-transform: uppercase !important;
  padding: 0.6rem 1.4rem !important;
  border-radius: 2px !important;
  border: 1px solid rgba(26,188,156,0.4) !important;
  background: rgba(26,188,156,0.08) !important;
  color: var(--teal) !important;
  transition: all 0.25s ease !important;
}

[data-testid="stDownloadButton"] > button:hover {
  background: var(--teal) !important;
  color: var(--void) !important;
  box-shadow: 0 0 20px rgba(26,188,156,0.3) !important;
}

/* ══ TEXT INPUT ══ */
.stTextInput > div > div,
.stTextInput > div > div > input {
  background: var(--card) !important;
  border: 1px solid var(--gold-border) !important;
  border-radius: 2px !important;
  color: var(--text-primary) !important;
  font-family: var(--ff-mono) !important;
  font-size: 0.85rem !important;
  transition: all 0.2s ease !important;
}

.stTextInput > div > div:focus-within {
  border-color: var(--gold) !important;
  box-shadow: 0 0 0 2px var(--gold-dim), 0 0 12px rgba(212,160,23,0.15) !important;
}

.stTextInput > label {
  font-family: var(--ff-mono) !important;
  font-size: 0.62rem !important;
  letter-spacing: 0.18em !important;
  text-transform: uppercase !important;
  color: var(--text-muted) !important;
}

/* ══ TEXTAREA ══ */
.stTextArea > div > div > textarea {
  background: var(--card) !important;
  border: 1px solid var(--gold-border) !important;
  border-radius: 2px !important;
  color: var(--text-primary) !important;
  font-family: var(--ff-mono) !important;
  font-size: 0.82rem !important;
  transition: all 0.2s ease !important;
  resize: vertical !important;
}

.stTextArea > div > div:focus-within > textarea {
  border-color: var(--gold) !important;
  box-shadow: 0 0 0 2px var(--gold-dim) !important;
}

.stTextArea > label {
  font-family: var(--ff-mono) !important;
  font-size: 0.62rem !important;
  letter-spacing: 0.18em !important;
  text-transform: uppercase !important;
  color: var(--text-muted) !important;
}

/* ══ SELECTBOX ══ */
.stSelectbox > div > div {
  background: var(--card) !important;
  border: 1px solid var(--gold-border) !important;
  border-radius: 2px !important;
  color: var(--text-primary) !important;
  font-family: var(--ff-mono) !important;
  font-size: 0.85rem !important;
  transition: border-color 0.2s ease !important;
}

.stSelectbox > div > div:hover {
  border-color: var(--gold-border-b) !important;
}

.stSelectbox > label {
  font-family: var(--ff-mono) !important;
  font-size: 0.62rem !important;
  letter-spacing: 0.18em !important;
  text-transform: uppercase !important;
  color: var(--text-muted) !important;
}

/* ══ SLIDER ══ */
.stSlider > label {
  font-family: var(--ff-mono) !important;
  font-size: 0.62rem !important;
  letter-spacing: 0.18em !important;
  text-transform: uppercase !important;
  color: var(--text-muted) !important;
}

.stSlider [data-baseweb="slider"] {
  padding: 0.5rem 0 !important;
}

.stSlider [data-baseweb="slider"] div[data-testid="stThumbValue"] {
  font-family: var(--ff-mono) !important;
  font-size: 0.75rem !important;
  color: var(--gold) !important;
  background: var(--card) !important;
  border: 1px solid var(--gold-border) !important;
  border-radius: 2px !important;
  padding: 2px 6px !important;
}

/* ══ MULTISELECT ══ */
.stMultiSelect > label {
  font-family: var(--ff-mono) !important;
  font-size: 0.62rem !important;
  letter-spacing: 0.18em !important;
  text-transform: uppercase !important;
  color: var(--text-muted) !important;
}

.stMultiSelect > div > div {
  background: var(--card) !important;
  border: 1px solid var(--gold-border) !important;
  border-radius: 2px !important;
}

[data-baseweb="tag"] {
  background: var(--gold-dim) !important;
  border: 1px solid var(--gold-border-b) !important;
  border-radius: 2px !important;
  color: var(--gold-bright) !important;
  font-family: var(--ff-mono) !important;
  font-size: 0.72rem !important;
  letter-spacing: 0.05em !important;
}

/* ══ ALERTS ══ */
[data-testid="stAlert"] {
  border-radius: 2px !important;
  font-family: var(--ff-label) !important;
  font-size: 0.85rem !important;
  font-weight: 500 !important;
  letter-spacing: 0.04em !important;
  border-left-width: 3px !important;
  background: var(--card) !important;
}

div[data-testid="stAlert"][kind="info"],
.stInfo { border-left-color: var(--gold) !important; color: var(--text-secondary) !important; }

div[data-testid="stAlert"][kind="warning"],
.stWarning { border-left-color: #fb923c !important; color: #fb923c !important; background: rgba(251,146,60,0.05) !important; }

div[data-testid="stAlert"][kind="success"],
.stSuccess { border-left-color: var(--teal) !important; color: var(--teal) !important; background: rgba(26,188,156,0.05) !important; }

div[data-testid="stAlert"][kind="error"],
.stError { border-left-color: var(--crimson-bright) !important; color: var(--crimson-bright) !important; background: var(--crimson-glow) !important; }

/* ══ PLOTLY CHARTS ══ */
[data-testid="stPlotlyChart"] {
  border: 1px solid var(--gold-border) !important;
  border-radius: 2px !important;
  background: var(--card) !important;
  overflow: hidden;
  box-shadow: 0 4px 24px rgba(0,0,0,0.4);
}

/* ══ SCROLLBAR ══ */
::-webkit-scrollbar { width: 5px; height: 5px; }
::-webkit-scrollbar-track { background: var(--base); }
::-webkit-scrollbar-thumb {
  background: linear-gradient(180deg, var(--gold), var(--gold-border));
  border-radius: 0;
}
::-webkit-scrollbar-thumb:hover { background: var(--gold-bright); }

/* ══ PLACEHOLDER ══ */
input::placeholder, textarea::placeholder {
  color: var(--text-dim) !important;
  font-style: italic;
}

/* ══ GENERAL TEXT ══ */
p, span, div, label {
  font-family: var(--ff-ui) !important;
  color: var(--text-secondary);
}

/* ══ CUSTOM COMPONENTS ══ */

.page-header {
  display: flex;
  align-items: center;
  gap: 16px;
  margin-bottom: 0.5rem;
  padding-bottom: 1.5rem;
  border-bottom: 1px solid var(--gold-border);
  position: relative;
}

.page-header::after {
  content: '';
  position: absolute;
  bottom: -1px; left: 0;
  width: 120px; height: 1px;
  background: linear-gradient(90deg, var(--gold-bright), transparent);
}

.page-icon {
  width: 44px; height: 44px;
  background: var(--gold-dim);
  border: 1px solid var(--gold-border-b);
  border-radius: 2px;
  display: flex; align-items: center; justify-content: center;
  font-size: 1.2rem;
  flex-shrink: 0;
  position: relative;
  overflow: hidden;
}

.page-icon::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(135deg, rgba(240,192,64,0.1), transparent);
}

.page-title-block { flex: 1; }

.page-title {
  font-family: var(--ff-display) !important;
  font-size: 1.5rem !important;
  font-weight: 700 !important;
  letter-spacing: 0.15em !important;
  text-transform: uppercase !important;
  color: var(--text-primary) !important;
  line-height: 1 !important;
  margin: 0 !important;
}

.page-subtitle {
  font-family: var(--ff-mono) !important;
  font-size: 0.62rem !important;
  letter-spacing: 0.2em !important;
  text-transform: uppercase !important;
  color: var(--gold) !important;
  margin-top: 4px !important;
}

.section-head {
  font-family: var(--ff-display) !important;
  font-size: 0.72rem !important;
  font-weight: 600 !important;
  letter-spacing: 0.22em !important;
  text-transform: uppercase !important;
  color: var(--text-muted) !important;
  margin: 1.5rem 0 0.75rem 0 !important;
  display: flex;
  align-items: center;
  gap: 10px;
}

.section-head::before {
  content: '';
  display: inline-block;
  width: 20px; height: 1px;
  background: var(--gold);
}

.section-head::after {
  content: '';
  flex: 1;
  height: 1px;
  background: linear-gradient(90deg, var(--gold-border), transparent);
}

.badge {
  display: inline-flex; align-items: center; gap: 6px;
  font-family: var(--ff-mono);
  font-size: 0.6rem;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  padding: 3px 10px;
  border-radius: 1px;
  border: 1px solid;
}

.badge-gold  { color: var(--gold-bright); border-color: var(--gold-border-b); background: var(--gold-dim); }
.badge-red   { color: var(--crimson-bright); border-color: rgba(231,76,60,0.4); background: var(--crimson-glow); }
.badge-teal  { color: var(--teal); border-color: rgba(26,188,156,0.35); background: var(--teal-dim); }

.sidebar-logo {
  margin-bottom: 1.5rem;
  padding-bottom: 1.5rem;
  border-bottom: 1px solid var(--gold-border);
}

.sidebar-logo-main {
  font-family: var(--ff-display);
  font-size: 1.4rem;
  font-weight: 900;
  letter-spacing: 0.2em;
  color: var(--gold-bright);
  text-shadow: 0 0 20px rgba(240,192,64,0.4);
  line-height: 1;
}

.sidebar-logo-sub {
  font-family: var(--ff-mono);
  font-size: 0.55rem;
  letter-spacing: 0.3em;
  color: var(--text-muted);
  text-transform: uppercase;
  margin-top: 4px;
}

.sidebar-status {
  margin-top: 1rem;
  padding: 8px 10px;
  border: 1px solid var(--gold-border);
  border-left: 2px solid var(--teal);
  background: var(--teal-dim);
}

.sidebar-status-label {
  font-family: var(--ff-mono);
  font-size: 0.55rem;
  letter-spacing: 0.2em;
  color: var(--text-muted);
  text-transform: uppercase;
}

.sidebar-status-value {
  font-family: var(--ff-mono);
  font-size: 0.75rem;
  color: var(--teal);
  letter-spacing: 0.05em;
}

.pulse-dot {
  display: inline-block;
  width: 6px; height: 6px;
  background: var(--teal);
  border-radius: 50%;
  animation: pulse 2s ease-in-out infinite;
  margin-right: 5px;
  vertical-align: middle;
}

@keyframes pulse {
  0%, 100% { opacity: 1; transform: scale(1); box-shadow: 0 0 0 0 rgba(26,188,156,0.4); }
  50%       { opacity: 0.7; transform: scale(0.9); box-shadow: 0 0 0 4px rgba(26,188,156,0); }
}

.metric-urgent [data-testid="stMetricValue"] {
  color: var(--crimson-bright) !important;
  text-shadow: 0 0 20px rgba(231,76,60,0.3) !important;
  animation: urgentPulse 2s ease-in-out infinite;
}

@keyframes urgentPulse {
  0%, 100% { text-shadow: 0 0 20px rgba(231,76,60,0.3); }
  50%       { text-shadow: 0 0 30px rgba(231,76,60,0.6), 0 0 60px rgba(231,76,60,0.15); }
}

.analyst-panel {
  background: var(--card);
  border: 1px solid var(--gold-border);
  border-top: 2px solid var(--gold);
  padding: 1.5rem;
  margin: 1rem 0;
  position: relative;
}

.analyst-panel::before {
  content: 'ANALYST TERMINAL';
  position: absolute;
  top: -0.6rem; left: 1rem;
  background: var(--base);
  padding: 0 8px;
  font-family: var(--ff-mono);
  font-size: 0.55rem;
  letter-spacing: 0.25em;
  color: var(--gold);
  text-transform: uppercase;
}

.score-breakdown {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 12px;
  margin: 1rem 0;
}

.score-item {
  background: var(--card);
  border: 1px solid var(--gold-border);
  padding: 1rem;
  text-align: center;
  position: relative;
  overflow: hidden;
  transition: all 0.2s;
}

.score-item:hover {
  border-color: var(--gold-border-b);
  background: var(--card-2);
}

.score-item-label {
  font-family: var(--ff-mono);
  font-size: 0.6rem;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--text-muted);
  margin-bottom: 6px;
}

.score-item-value {
  font-family: var(--ff-display);
  font-size: 2rem;
  font-weight: 700;
  letter-spacing: 0.05em;
}

.decision-confirmed { color: var(--teal) !important; }
.decision-dismissed { color: var(--text-muted) !important; }
.decision-escalated { color: var(--crimson-bright) !important; }

.signal-table-header {
  display: grid;
  grid-template-columns: 2fr 2fr 1fr;
  gap: 1rem;
  padding: 8px 12px;
  background: var(--raised);
  border: 1px solid var(--gold-border);
  border-bottom: 1px solid var(--gold);
  font-family: var(--ff-mono);
  font-size: 0.6rem;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--gold);
  margin-bottom: 0;
}

.corner-box {
  position: relative;
  padding: 1.5rem;
  background: var(--card);
  margin: 1rem 0;
}

.corner-box::before,
.corner-box::after,
.corner-box > *::before,
.corner-box > *::after {
  content: '';
  position: absolute;
  width: 12px; height: 12px;
  border-color: var(--gold);
  border-style: solid;
}

.corner-box::before  { top: 0; left: 0; border-width: 1px 0 0 1px; }
.corner-box::after   { top: 0; right: 0; border-width: 1px 1px 0 0; }

.ticker-wrap {
  overflow: hidden;
  background: var(--raised);
  border-top: 1px solid var(--gold-border);
  border-bottom: 1px solid var(--gold-border);
  padding: 5px 0;
  margin: 1rem 0;
}

.ticker-content {
  display: inline-block;
  white-space: nowrap;
  animation: ticker 30s linear infinite;
  font-family: var(--ff-mono);
  font-size: 0.65rem;
  letter-spacing: 0.12em;
  color: var(--gold);
}

@keyframes ticker {
  0%   { transform: translateX(0); }
  100% { transform: translateX(-50%); }
}

[data-baseweb="tab-list"] {
  background: var(--card) !important;
  border-bottom: 1px solid var(--gold-border) !important;
  gap: 0 !important;
}

[data-baseweb="tab"] {
  font-family: var(--ff-label) !important;
  font-size: 0.8rem !important;
  letter-spacing: 0.12em !important;
  text-transform: uppercase !important;
  color: var(--text-muted) !important;
  background: transparent !important;
  border: none !important;
  padding: 12px 20px !important;
  border-bottom: 2px solid transparent !important;
  transition: all 0.2s ease !important;
}

[data-baseweb="tab"]:hover { color: var(--gold) !important; }
[aria-selected="true"][data-baseweb="tab"] {
  color: var(--gold-bright) !important;
  border-bottom-color: var(--gold) !important;
  background: var(--gold-glow) !important;
}

[data-testid="stSpinner"] { color: var(--gold) !important; }

[data-baseweb="tooltip"] {
  background: var(--card-2) !important;
  border: 1px solid var(--gold-border) !important;
  font-family: var(--ff-mono) !important;
  font-size: 0.75rem !important;
  color: var(--text-primary) !important;
}

[data-testid="stVerticalBlock"],
[data-testid="stHorizontalBlock"],
[data-testid="element-container"],
.stMarkdown, .element-container {
  background: transparent !important;
}

</style>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
#  PLOTLY MASTER TEMPLATE
# ══════════════════════════════════════════════════════════════════════════════
PLOT_LAYOUT = dict(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    font=dict(family='Exo 2, sans-serif', color='#ccd6e0', size=11),
    title=dict(
        font=dict(family='Orbitron, monospace', color='#e8dfc8', size=13, weight=700),
        x=0.01, pad=dict(l=0, t=0)
    ),
    xaxis=dict(
        gridcolor='rgba(212,160,23,0.06)',
        linecolor='rgba(212,160,23,0.15)',
        tickfont=dict(family='Share Tech Mono', size=10, color='#9ab0c4'),
        title_font=dict(family='Share Tech Mono', size=10, color='#9ab0c4'),
        zeroline=False,
    ),
    yaxis=dict(
        gridcolor='rgba(212,160,23,0.06)',
        linecolor='rgba(212,160,23,0.15)',
        tickfont=dict(family='Share Tech Mono', size=10, color='#9ab0c4'),
        title_font=dict(family='Share Tech Mono', size=10, color='#9ab0c4'),
        zeroline=False,
    ),
    colorway=['#d4a017','#1abc9c','#e74c3c','#a8d8ea','#fb923c','#818cf8','#f472b6'],
    legend=dict(
        bgcolor='rgba(0,0,0,0)',
        font=dict(family='Share Tech Mono', color='#ccd6e0', size=10),
        bordercolor='rgba(212,160,23,0.2)',
        borderwidth=1,
    ),
    margin=dict(l=12, r=12, t=44, b=12),
    hoverlabel=dict(
        bgcolor='#0d1420',
        bordercolor='rgba(212,160,23,0.4)',
        font=dict(family='Share Tech Mono', size=11, color='#e8dfc8'),
    ),
)


# ══════════════════════════════════════════════════════════════════════════════
#  DB
# ══════════════════════════════════════════════════════════════════════════════
@st.cache_resource
def get_engine():
    return create_engine('mysql+pymysql://root:1771@localhost/pharma_safety')

@st.cache_data(ttl=300, show_spinner=False)
def load_signals():
    return pd.read_sql("SELECT * FROM signals_ranked", get_engine())

@st.cache_data(ttl=60, show_spinner=False)
def load_decisions():
    return pd.read_sql("SELECT * FROM analyst_decision", get_engine())


# ══════════════════════════════════════════════════════════════════════════════
#  SIDEBAR
# ══════════════════════════════════════════════════════════════════════════════
with st.sidebar:
    st.markdown("""
    <div class="sidebar-logo">
        <div class="sidebar-logo-main">AERS</div>
        <div class="sidebar-logo-sub">Adverse Event Ranking System · v2.0</div>
    </div>
    """, unsafe_allow_html=True)

    page = st.radio(
        'NAV',
        options=['📊  Signal Ranker', '🔍  Signal Details', '📈  Dashboard', '🕒  Decision History'],
        label_visibility='collapsed'
    )

    st.markdown('---')

    now = datetime.now()
    st.markdown(f"""
    <div class="sidebar-status">
        <div class="sidebar-status-label">System Status</div>
        <div class="sidebar-status-value"><span class="pulse-dot"></span>OPERATIONAL</div>
    </div>
    <div style="margin-top:12px;">
        <div class="sidebar-status-label" style="margin-bottom:4px;">Current Session</div>
        <div style="font-family:'Share Tech Mono';font-size:0.7rem;color:#6a7f96;">
            {now.strftime('%Y-%m-%d')}<br>
            {now.strftime('%H:%M:%S')} UTC+5:30
        </div>
    </div>
    <div style="margin-top:16px; padding-top:12px; border-top:1px solid rgba(212,160,23,0.1);">
        <div class="sidebar-status-label">Data Source</div>
        <div style="font-family:'Share Tech Mono';font-size:0.65rem;color:#6a7f96;margin-top:3px;">
            FDA FAERS · MySQL<br>
            TTL CACHE: 300s
        </div>
    </div>
    """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
#  HELPER — PAGE HEADER
# ══════════════════════════════════════════════════════════════════════════════
def page_header(icon, title, subtitle):
    st.markdown(f"""
    <div class="page-header">
        <div class="page-icon">{icon}</div>
        <div class="page-title-block">
            <div class="page-title">{title}</div>
            <div class="page-subtitle">{subtitle}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def section(label):
    st.markdown(f'<div class="section-head">{label}</div>', unsafe_allow_html=True)

def ticker(signals_df):
    top5 = signals_df.nlargest(5, 'final_score')[['drugname','reaction','final_score']]
    items = '  ·  '.join(
        [f"⬡ {r['drugname'].upper()} + {r['reaction'].upper()} → SCORE {r['final_score']:.2f}" for _, r in top5.iterrows()]
    )
    content = (items + '  ·  ') * 4
    st.markdown(f"""
    <div class="ticker-wrap">
        <span class="ticker-content">
            &nbsp;&nbsp;&nbsp;LIVE SIGNAL FEED &nbsp;▸&nbsp; {content}
        </span>
    </div>
    """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
#  PAGE: SIGNAL RANKER
# ══════════════════════════════════════════════════════════════════════════════
if '📊' in page:
    page_header('⬡', 'Signal Ranker', 'FDA FAERS · Pharmacovigilance Intelligence · Real-Time Scoring')
    df = load_signals()
    ticker(df)

    section('System Overview')
    col1, col2, col3, col4 = st.columns(4)

    top_row = df.loc[df['final_score'].idxmax()]

    with col1:
        st.metric("Total Signals Indexed", f"{df.shape[0]:,}")
    with col2:
        urgent = df[df['final_score'] >= 8]
        st.metric("Urgent Signals  ≥ 8.0", len(urgent))
    with col3:
        st.metric("Highest Score", f"{df['final_score'].max():.3f}")
    with col4:
        st.metric("Top Priority Drug", top_row['drugname'])

    section('Priority Signals — Score ≥ 8.0')
    top_df = df[df['final_score'] >= 8][['drugname','reaction','final_score']].sort_values('final_score', ascending=False)
    st.dataframe(top_df, use_container_width=True, hide_index=True)

    section('Top 15 Drug-Reaction Pairs by Final Score')
    chart_df = df.nlargest(15, 'final_score').copy()
    chart_df['label'] = chart_df['drugname'] + ' · ' + chart_df['reaction'].str[:20]
    fig = go.Figure()
    colors = ['#e74c3c' if s >= 8 else '#d4a017' if s >= 6 else '#1abc9c' for s in chart_df['final_score']]
    fig.add_trace(go.Bar(
        x=chart_df['label'], y=chart_df['final_score'],
        marker=dict(color=colors, line=dict(width=0)),
        text=[f"{s:.2f}" for s in chart_df['final_score']],
        textposition='outside',
        textfont=dict(family='Share Tech Mono', size=10, color='#ccd6e0'),
        hovertemplate='<b>%{x}</b><br>Score: %{y:.3f}<extra></extra>',
    ))
    fig.update_layout(
        **PLOT_LAYOUT,
        title_text='TOP 15 DRUG-REACTION SIGNALS',
        xaxis_tickangle=-42,
        yaxis_range=[0, df['final_score'].max() * 1.15],
        bargap=0.3,
        height=380,
    )
    st.plotly_chart(fig, use_container_width=True)

    section('Signal Filter Console')
    st.warning("Verify exact spelling before querying drug or reaction names.")

    c1, c2 = st.columns(2)
    with c1: drug_name = st.text_input('Drug Search', placeholder='e.g. ASPIRIN')
    with c2: reaction_name = st.text_input('Reaction Search', placeholder='e.g. NAUSEA')
    max_score = st.slider("Minimum Score Threshold", 0.0, 10.0, 5.0, step=0.01)

    filtered_df = df[
        df['drugname'].str.contains(drug_name, case=False, na=False) &
        df['reaction'].str.contains(reaction_name, case=False, na=False) &
        (df['final_score'] >= max_score)
    ]

    section('Query Results')
    st.dataframe(filtered_df, use_container_width=True, hide_index=True)

    data_csv = filtered_df.to_csv(index=False).encode('utf-8')
    c1, c2, c3 = st.columns(3)
    with c1:
        st.download_button("⬇  Export Results as CSV", file_name='AERS_Filtered.csv', data=data_csv)
    with c2:
        st.metric("Matched Records", filtered_df.shape[0])
    with c3:
        st.metric("Last Record Updated", str(df.iloc[0, 8]))


# ══════════════════════════════════════════════════════════════════════════════
#  PAGE: SIGNAL DETAILS
# ══════════════════════════════════════════════════════════════════════════════
elif '🔍' in page:
    page_header('⬡', 'Signal Details', 'Drug × Reaction Pair Analysis · Analyst Decision Interface')
    df = load_signals()

    section('Select Drug-Reaction Pair')
    c1, c2 = st.columns(2)
    with c1: drug_name = st.selectbox("Drug Name", df['drugname'].unique())
    df_drug = df[df['drugname'] == drug_name]
    with c2: reaction_name = st.selectbox(f"Reaction for {drug_name}", df_drug['reaction'].unique())

    row = df_drug[df_drug['reaction'] == reaction_name].iloc[0]

    section('Score Decomposition')
    scores = {
        'Novelty':    (row['novelty_score'],    '#d4a017', 'Measures how new or unreported this signal is'),
        'Severity':   (row['severity_score'],   '#e74c3c', 'Measures clinical seriousness of the adverse event'),
        'Population': (row['population_score'], '#1abc9c', 'Measures breadth of affected patient population'),
    }

    s_cols = st.columns(3)
    for i, (name, (val, color, desc)) in enumerate(scores.items()):
        with s_cols[i]:
            pct = val / 10 * 100
            st.markdown(f"""
            <div style="background:var(--card);border:1px solid rgba(255,255,255,0.06);
                        border-top:2px solid {color};padding:1.2rem;text-align:center;margin-bottom:4px;">
                <div style="font-family:'Share Tech Mono';font-size:0.6rem;letter-spacing:0.2em;
                            color:var(--text-muted);text-transform:uppercase;margin-bottom:8px;">{name}</div>
                <div style="font-family:'Orbitron';font-size:2.2rem;font-weight:700;
                            color:{color};text-shadow:0 0 20px {color}55;line-height:1;">{val:.2f}</div>
                <div style="font-family:'Share Tech Mono';font-size:0.6rem;color:var(--text-muted);
                            margin:8px 0 4px;">/ 10.00</div>
                <div style="height:3px;background:var(--raised);border-radius:0;overflow:hidden;">
                    <div style="height:100%;width:{pct}%;background:{color};
                                box-shadow:0 0 8px {color}88;transition:width 0.6s ease;"></div>
                </div>
                <div style="font-family:'Exo 2';font-size:0.72rem;color:var(--text-muted);
                            margin-top:8px;line-height:1.3;">{desc}</div>
            </div>
            """, unsafe_allow_html=True)

    final = row['final_score']
    level = ('CRITICAL', '#e74c3c') if final >= 8 else ('ELEVATED', '#d4a017') if final >= 6 else ('MODERATE', '#1abc9c')
    st.markdown(f"""
    <div style="background:var(--card);border:1px solid {level[1]}44;
                border-left:3px solid {level[1]};padding:1.2rem 1.5rem;
                margin:1rem 0;display:flex;align-items:center;justify-content:space-between;
                position:relative;overflow:hidden;">
        <div style="position:absolute;right:-20px;top:50%;transform:translateY(-50%);
                    font-family:'Orbitron';font-size:5rem;font-weight:900;
                    color:{level[1]}08;letter-spacing:-0.05em;pointer-events:none;">{level[0]}</div>
        <div>
            <div style="font-family:'Share Tech Mono';font-size:0.6rem;
                        letter-spacing:0.22em;color:var(--text-muted);text-transform:uppercase;">
                Composite Final Score · (0.40 × Novelty) + (0.35 × Severity) + (0.25 × Population)
            </div>
            <div style="font-family:'Orbitron';font-size:2.6rem;font-weight:800;
                        color:{level[1]};text-shadow:0 0 24px {level[1]}55;
                        line-height:1.1;margin-top:4px;">{final:.4f}</div>
        </div>
        <div style="text-align:right;">
            <div style="font-family:'Share Tech Mono';font-size:0.6rem;
                        letter-spacing:0.18em;color:var(--text-muted);margin-bottom:4px;">ALERT LEVEL</div>
            <div style="font-family:'Orbitron';font-size:1.1rem;font-weight:700;
                        color:{level[1]};letter-spacing:0.15em;
                        border:1px solid {level[1]}55;padding:4px 14px;
                        background:{level[1]}11;">{level[0]}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    fig = go.Figure(go.Scatterpolar(
        r=[row['novelty_score'], row['severity_score'], row['population_score'], row['novelty_score']],
        theta=['Novelty', 'Severity', 'Population', 'Novelty'],
        fill='toself',
        fillcolor='rgba(212,160,23,0.08)',
        line=dict(color='#d4a017', width=2),
        marker=dict(color='#f0c040', size=6),
        hovertemplate='<b>%{theta}</b>: %{r:.2f}<extra></extra>',
    ))
    fig.update_layout(
        **PLOT_LAYOUT,
        title_text='SCORE RADAR PROFILE',
        polar=dict(
            bgcolor='rgba(0,0,0,0)',
            radialaxis=dict(
                visible=True, range=[0, 10],
                gridcolor='rgba(212,160,23,0.1)',
                linecolor='rgba(212,160,23,0.15)',
                tickfont=dict(family='Share Tech Mono', size=9, color='#9ab0c4'),
                tickvals=[2,4,6,8,10],
            ),
            angularaxis=dict(
                gridcolor='rgba(212,160,23,0.1)',
                linecolor='rgba(212,160,23,0.2)',
                tickfont=dict(family='Share Tech Mono', size=11, color='#ccd6e0'),
            ),
        ),
        height=340,
    )
    st.plotly_chart(fig, use_container_width=True)

    section('Raw Signal Parameters')
    row_df = pd.DataFrame({'Parameter': row.index, 'Value': row.values})
    st.dataframe(row_df, use_container_width=True, hide_index=True)

    st.markdown("""
    <div style="margin:2rem 0 0.5rem 0; position:relative; padding:1.5rem 1.5rem 1rem 1.5rem;
                background:var(--card);
                border:1px solid rgba(212,160,23,0.25);
                border-top:2px solid #d4a017;">
        <div style="position:absolute;top:-0.65rem;left:1rem;background:var(--base);
                    padding:0 8px;font-family:'Share Tech Mono';font-size:0.55rem;
                    letter-spacing:0.25em;color:#d4a017;text-transform:uppercase;">
            ⬡  ANALYST TERMINAL
        </div>
    """, unsafe_allow_html=True)

    note = st.text_area("Analyst Observation Note", placeholder="Enter clinical notes, supporting evidence, or escalation rationale…", height=90)

    from sqlalchemy import text as sqlt

    def insert_decision(drug, reaction, decision, note):
        with get_engine().connect() as conn:
            conn.execute(sqlt("""
                INSERT INTO analyst_decision (drug_name, reaction, decision, analyst_note, decided_at)
                VALUES (:drug, :reaction, :decision, :note, :ts)
            """), {'drug': drug, 'reaction': reaction, 'decision': decision,
                   'note': note, 'ts': datetime.now()})
            conn.commit()
        load_decisions.clear()
        time.sleep(3)
        st.rerun()

    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("✔  Confirm Signal"):
            insert_decision(row['drugname'], row['reaction'], 'Confirmed', note)
            st.success("Signal confirmed and logged to database.")
    with c2:
        if st.button("✖  Dismiss Signal"):
            insert_decision(row['drugname'], row['reaction'], 'Dismissed', note)
            st.warning("Signal dismissed and logged.")
    with c3:
        if st.button("🚨  Escalate to Medical Officer"):
            insert_decision(row['drugname'], row['reaction'], 'Escalated', note)
            st.error("Escalated — Medical Officer notified.")

    st.markdown("</div>", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
#  PAGE: DASHBOARD
# ══════════════════════════════════════════════════════════════════════════════
elif '📈' in page:
    page_header('⬡', 'Dashboard', 'Pharmacovigilance Intelligence Overview · All Systems')

    signal   = load_signals()
    decision = load_decisions()

    ticker(signal)
    section('Key Performance Indicators')

    col1, col2, col3, col4 = st.columns(4)
    with col1: st.metric("Total Signals", f"{len(signal):,}")
    with col2: st.metric("Urgent  ≥ 8.0", f"{len(signal[signal['final_score'] >= 8]):,}")
    with col3: st.metric("Analyst Decisions", f"{len(decision):,}")
    with col4: st.metric("Confirmed", f"{len(decision[decision['decision']=='Confirmed']):,}")

    section('Decision Intelligence')
    c1, c2 = st.columns([1, 2])

    with c1:
        if len(decision) > 0:
            df_pie = decision.groupby('decision')['decision'].count().reset_index(name='Count')
            fig = go.Figure(go.Pie(
                labels=df_pie['decision'],
                values=df_pie['Count'],
                hole=0.6,
                marker=dict(
                    colors=['#1abc9c', '#e74c3c', '#d4a017'],
                    line=dict(color='#060a0f', width=2)
                ),
                textfont=dict(family='Share Tech Mono', size=10),
                hovertemplate='<b>%{label}</b><br>Count: %{value}<br>%{percent}<extra></extra>',
            ))
            fig.add_annotation(
                text=f"<b>{len(decision)}</b><br><span style='font-size:9px'>TOTAL</span>",
                x=0.5, y=0.5, showarrow=False,
                font=dict(family='Orbitron', size=14, color='#e8dfc8'),
                align='center',
            )
            fig.update_layout(**PLOT_LAYOUT, title_text='DECISION BREAKDOWN', height=320, showlegend=True)
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No decisions recorded yet.")

    with c2:
        df_top = (signal.groupby('drugname')['final_score']
                  .max().reset_index(name='Max Score')
                  .sort_values('Max Score', ascending=False).head(10))
        colors_bar = ['#e74c3c' if s >= 8 else '#d4a017' if s >= 6 else '#1abc9c'
                      for s in df_top['Max Score']]
        fig = go.Figure(go.Bar(
            x=df_top['drugname'], y=df_top['Max Score'],
            marker=dict(color=colors_bar, line=dict(width=0)),
            text=[f"{s:.2f}" for s in df_top['Max Score']],
            textposition='outside',
            textfont=dict(family='Share Tech Mono', size=10, color='#ccd6e0'),
            hovertemplate='<b>%{x}</b><br>Max Score: %{y:.3f}<extra></extra>',
        ))
        fig.update_layout(
            **PLOT_LAYOUT,
            title_text='TOP 10 DRUGS · MAXIMUM SEVERITY SCORE',
            yaxis_range=[0, df_top['Max Score'].max() * 1.15],
            bargap=0.3, height=320,
        )
        st.plotly_chart(fig, use_container_width=True)

    section('Signal Score Distribution')
    df_dist = signal.copy()
    bins = [0, 2, 4, 6, 8, 10]
    labels = ['0–2  LOW', '2–4  MINIMAL', '4–6  MODERATE', '6–8  ELEVATED', '8–10  CRITICAL']
    df_dist['score_range'] = pd.cut(df_dist['final_score'], bins=bins, labels=labels)
    dist = df_dist['score_range'].value_counts().sort_index().reset_index(name='Count')
    dist.columns = ['Score Band', 'Count']

    c1, c2 = st.columns([1, 3])
    with c1:
        st.dataframe(dist, use_container_width=True, hide_index=True)
    with c2:
        band_colors = ['#4ade80', '#a3e635', '#d4a017', '#fb923c', '#e74c3c']
        fig = go.Figure(go.Bar(
            x=dist['Score Band'], y=dist['Count'],
            marker=dict(color=band_colors, line=dict(width=0)),
            text=dist['Count'], textposition='outside',
            textfont=dict(family='Share Tech Mono', size=11, color='#ccd6e0'),
            hovertemplate='<b>%{x}</b><br>Signals: %{y}<extra></extra>',
        ))
        fig.update_layout(
            **PLOT_LAYOUT,
            title_text='SIGNAL DISTRIBUTION ACROSS RISK BANDS',
            bargap=0.25, height=280,
        )
        st.plotly_chart(fig, use_container_width=True)

    section('Novelty × Severity Intelligence Map')
    fig = go.Figure(go.Scatter(
        x=signal['novelty_score'],
        y=signal['severity_score'],
        mode='markers',
        marker=dict(
            size=signal['population_score'] * 2 + 3,
            color=signal['final_score'],
            colorscale=[[0,'#1abc9c'],[0.5,'#d4a017'],[1,'#e74c3c']],
            showscale=True,
            colorbar=dict(
                title=dict(text='Score', font=dict(family='Share Tech Mono', size=10, color='#9ab0c4')),
                tickfont=dict(family='Share Tech Mono', size=9, color='#9ab0c4'),
                len=0.8,
            ),
            line=dict(width=0),
            opacity=0.75,
        ),
        text=signal['drugname'] + ' · ' + signal['reaction'],
        hovertemplate='<b>%{text}</b><br>Novelty: %{x:.2f}<br>Severity: %{y:.2f}<extra></extra>',
    ))
    fig.add_hline(y=7, line=dict(color='rgba(231,76,60,0.3)', width=1, dash='dash'))
    fig.add_vline(x=7, line=dict(color='rgba(231,76,60,0.3)', width=1, dash='dash'))
    fig.update_layout(
        **PLOT_LAYOUT,
        title_text='NOVELTY vs SEVERITY · Bubble size = Population Score',
        xaxis_title='Novelty Score',
        yaxis_title='Severity Score',
        height=400,
    )
    st.plotly_chart(fig, use_container_width=True)

    section('5 Most Recent Analyst Decisions')
    st.dataframe(
        decision.sort_values('decided_at', ascending=False).head(5),
        use_container_width=True, hide_index=True
    )


# ══════════════════════════════════════════════════════════════════════════════
#  PAGE: DECISION HISTORY
# ══════════════════════════════════════════════════════════════════════════════
elif '🕒' in page:
    page_header('⬡', 'Decision History', 'Analyst Decision Log · Full Audit Trail')

    df = load_decisions()
    if len(df) == 0:
        st.info("No analyst decisions recorded. Navigate to **Signal Details** to begin reviewing signals.")
        st.stop()

    section('Decision Summary')
    col1, col2, col3, col4 = st.columns(4)
    with col1: st.metric("Total Decisions", len(df))
    with col2: st.metric("Confirmed", len(df[df['decision'] == 'Confirmed']))
    with col3: st.metric("Dismissed", len(df[df['decision'] == 'Dismissed']))
    with col4: st.metric("Escalated", len(df[df['decision'] == 'Escalated']))

    section('Decision Timeline')
    if 'decided_at' in df.columns:
        df['decided_at'] = pd.to_datetime(df['decided_at'])
        df_time = df.set_index('decided_at').resample('D')['decision'].count().reset_index()
        df_time.columns = ['Date', 'Count']
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=df_time['Date'], y=df_time['Count'],
            mode='lines+markers',
            line=dict(color='#d4a017', width=2),
            marker=dict(color='#f0c040', size=5, line=dict(color='#d4a017', width=1)),
            fill='tozeroy',
            fillcolor='rgba(212,160,23,0.05)',
            hovertemplate='<b>%{x|%Y-%m-%d}</b><br>Decisions: %{y}<extra></extra>',
        ))
        fig.update_layout(**PLOT_LAYOUT, title_text='DECISIONS PER DAY', height=240)
        st.plotly_chart(fig, use_container_width=True)

    section('Filter Decision Log')
    c1, c2 = st.columns(2)
    with c1:
        select = st.multiselect(
            "Decision Type",
            options=df['decision'].unique(),
            default=list(df['decision'].unique())
        )
    with c2:
        name = st.selectbox("Drug Name", options=['All'] + list(df['drug_name'].unique()))

    filtered_df = df[df['decision'].isin(select)]
    if name != 'All':
        filtered_df = filtered_df[filtered_df['drug_name'] == name]

    section(f'Filtered Records · {len(filtered_df)} entries')
    st.dataframe(filtered_df, use_container_width=True, hide_index=True)

    section('Complete Audit Log')
    full_df = df.rename(columns={
        'drug_name':    'Drug Name',
        'reaction':     'Reaction',
        'decision':     'Decision',
        'analyst_note': 'Analyst Note',
        'decided_at':   'Timestamp',
    })
    st.dataframe(full_df, use_container_width=True, hide_index=True)

    c1, c2 = st.columns(2)
    with c1:
        st.download_button(
            "⬇  Export Full Audit Log",
            file_name='AERS_Audit_Log.csv',
            data=load_decisions().to_csv(index=False)
        )
    with c2:
        st.download_button(
            "⬇  Export Filtered Records",
            file_name='AERS_Filtered_Decisions.csv',
            data=filtered_df.to_csv(index=False)
        )


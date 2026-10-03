import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(page_title="A Rose for You", page_icon="🌹")

st.markdown(
    """
    <style>
    [data-testid="stAppViewContainer"] {
        background: radial-gradient(circle at top, #3b1027, #09060c 70%);
        color: #fff5fa;
    }
    .title {
        color: #ffd7e8;
        font: 4rem Georgia, serif;
        text-align: center;
        text-shadow: 0 0 18px #ff5c99;
    }
    .subtitle { color: #f7b7d1; text-align: center; }
    .stButton > button {
        display: block; margin: auto; border-radius: 999px;
        background: #8e174f; color: white; border: 1px solid #ff8ab8;
    }
    </style>
    <h1 class="title">A Rose for You</h1>
    <p class="subtitle">A Python-powered rose, now live in your browser.</p>
    """,
    unsafe_allow_html=True,
)

components.html(
    """
    <style>
    html, body { margin: 0; background: transparent; overflow: hidden; }
    .scene { height: 520px; display: grid; place-items: center; }
    .rose { position: relative; width: 280px; height: 460px; }
    .flower { position: absolute; top: 35px; left: 50%; width: 180px; height: 180px;
      transform: translateX(-50%); animation: float 4s ease-in-out infinite; }
    .petal { position: absolute; width: 95px; height: 130px; border-radius: 75% 25% 70% 30%;
      background: linear-gradient(135deg, #ff8fb8, #b30d54 62%, #5d0630);
      box-shadow: inset -10px -14px 18px #46001e, 0 0 14px #ff3c82; }
    .p1 { left: 15px; top: 40px; transform: rotate(-48deg); }
    .p2 { left: 65px; top: 25px; transform: rotate(8deg); }
    .p3 { left: 92px; top: 58px; transform: rotate(55deg); }
    .p4 { left: 48px; top: 72px; transform: rotate(180deg) scale(.9); }
    .p5 { left: 20px; top: 75px; transform: rotate(235deg) scale(.78); }
    .center { position: absolute; left: 75px; top: 70px; width: 55px; height: 55px;
      border-radius: 50%; background: radial-gradient(circle at 35% 30%, #ffb6d2, #c41660 55%, #62052f); }
    .stem { position: absolute; left: 136px; top: 185px; width: 10px; height: 250px;
      border-radius: 10px; background: linear-gradient(90deg, #174f2c, #4bb35d, #123a22); }
    .leaf { position: absolute; width: 92px; height: 42px; border-radius: 100% 0;
      background: linear-gradient(135deg, #75d873, #176530 65%, #0b321d); }
    .left { left: 45px; top: 285px; transform: rotate(-28deg); }
    .right { left: 143px; top: 340px; transform: rotate(155deg); }
    @keyframes float { 0%,100% { transform: translateX(-50%) rotate(-2deg); }
      50% { transform: translateX(-50%) rotate(2deg) translateY(-8px); } }
    </style>
    <div class="scene"><div class="rose"><div class="flower">
      <div class="petal p1"></div><div class="petal p2"></div><div class="petal p3"></div>
      <div class="petal p4"></div><div class="petal p5"></div><div class="center"></div>
    </div><div class="stem"></div><div class="leaf left"></div><div class="leaf right"></div>
    </div></div>
    """,
    height=540,
    scrolling=False,
)

if st.button("Make it bloom"):
    st.balloons()
    st.success("A rose is blooming for you! 🌹")

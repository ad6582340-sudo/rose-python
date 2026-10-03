import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(
    page_title="A Rose for You",
    page_icon="🌹",
    layout="centered",
)

st.markdown(
    """
    <style>
    [data-testid="stAppViewContainer"] {
        background: radial-gradient(circle at top, #3b1027 0%, #160b18 55%, #09060c 100%);
        color: #fff5fa;
    }

    [data-testid="stHeader"] {
        background: transparent;
    }

    .rose-title {
        text-align: center;
        color: #ffd7e8;
        font-family: Georgia, serif;
        font-size: clamp(2rem, 7vw, 4rem);
        margin: 1rem 0 0;
        text-shadow: 0 0 18px rgba(255, 92, 153, 0.65);
    }

    .rose-subtitle {
        color: #f7b7d1;
        font-size: 1.1rem;
        text-align: center;
        margin-bottom: 0;
    }

    .stButton > button {
        display: block;
        margin: 0 auto;
        border: 1px solid #ff8ab8;
        border-radius: 999px;
        background: #8e174f;
        color: white;
        padding: 0.55rem 1.5rem;
    }
    </style>
    <h1 class="rose-title">A Rose for You</h1>
    <p class="rose-subtitle">A little Python-powered animation, now live in your browser.</p>
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
        box-shadow: inset -10px -14px 18px rgba(70, 0, 30, .45), 0 0 14px rgba(255, 60, 130, .3);
        transform-origin: 75% 90%; }
      .p1 { left: 15px; top: 40px; transform: rotate(-48deg); }
      .p2 { left: 65px; top: 25px; transform: rotate(8deg); }
      .p3 { left: 92px; top: 58px; transform: rotate(55deg); }
      .p4 { left: 48px; top: 72px; transform: rotate(180deg) scale(.9); }
      .p5 { left: 20px; top: 75px; transform: rotate(235deg) scale(.78); }
      .center { position: absolute; left: 75px; top: 70px; width: 55px; height: 55px;
        border-radius: 50%; background: radial-gradient(circle at 35% 30%, #ffb6d2, #c41660 55%, #62052f); z-index: 2; }
      .stem { position: absolute; left: 136px; top: 185px; width: 10px; height: 250px;
        border-radius: 10px; background: linear-gradient(90deg, #174f2c, #4bb35d, #123a22);
        transform: rotate(3deg); }
      .leaf { position: absolute; width: 92px; height: 42px; border-radius: 100% 0 100% 0;
        background: linear-gradient(135deg, #75d873, #176530 65%, #0b321d); }
      .leaf-left { left: 45px; top: 285px; transform: rotate(-28deg); }
      .leaf-right { left: 143px; top: 340px; transform: rotate(155deg); }
      .ground { position: absolute; left: 30px; bottom: 20px; width: 220px; height: 24px;
        border-radius: 50%; background: rgba(255, 76, 143, .2); filter: blur(9px); }
      @keyframes float { 0%, 100% { transform: translateX(-50%) rotate(-2deg); }
        50% { transform: translateX(-50%) rotate(2deg) translateY(-8px); } }
    </style>
    <div class="scene">
      <div class="rose">
        <div class="flower">
          <div class="petal p1"></div><div class="petal p2"></div><div class="petal p3"></div>
          <div class="petal p4"></div><div class="petal p5"></div><div class="center"></div>
        </div>
        <div class="stem"></div><div class="leaf leaf-left"></div><div class="leaf leaf-right"></div>
        <div class="ground"></div>
      </div>
    </div>
    """,
    height=540,
    scrolling=False,
)

if st.button("Make it bloom"):
    st.balloons()
    st.success("A rose is blooming for you! 🌹")

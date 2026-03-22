#!/usr/bin/env python3
"""
Methodology Decision-Support Tool
Based on primary simulation + literature review
"""

import streamlit as st
import plotly.graph_objects as go
import math

# Page config
st.set_page_config(
    page_title="Methodology Decision Tool",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    :root {
        --primary-color: #1e3a5f;
        --accent-color: #3b82f6;
        --success-color: #10b981;
        --warning-color: #f59e0b;
    }
    
    .main {
        background-color: #f4f6f9;
    }
    
    .stMetric {
        background-color: white;
        padding: 1rem;
        border-radius: 0.5rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }
    
    .recommendation-badge {
        padding: 1rem;
        border-radius: 0.75rem;
        text-align: center;
        font-size: 1.5rem;
        font-weight: bold;
        color: white;
    }
    
    .recommendation-agile {
        background-color: #3b82f6;
    }
    
    .recommendation-waterfall {
        background-color: #1e3a5f;
    }
    
    .recommendation-hybrid {
        background-color: #f59e0b;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.title("📊 Methodology Decision-Support Tool")
st.subheader("Agile vs Waterfall vs Hybrid — Based on Primary Simulation + Literature")

# Sidebar inputs
st.sidebar.header("Project Characteristics")

volatility = st.sidebar.slider(
    "Requirements Volatility",
    min_value=1,
    max_value=10,
    value=5,
    help="1 = Fully fixed requirements | 10 = Highly volatile"
)

regulatory = st.sidebar.selectbox(
    "Regulatory Intensity",
    ["None", "Low", "High"],
    help="Compliance requirements (HIPAA, SOX, etc.)"
)

team_size = st.sidebar.selectbox(
    "Team Size",
    ["Solo", "Small (2-5)", "Large (6+)"],
    help="Number of developers"
)

distribution = st.sidebar.selectbox(
    "Team Distribution",
    ["Co-located", "Hybrid", "Remote"],
    help="Physical location of team members"
)

project_type = st.sidebar.selectbox(
    "Project Type",
    ["Fixed-scope", "Cloud-native", "AI-integrated", "Mixed"],
    help="Nature of the project"
)

timeline = st.sidebar.slider(
    "Timeline Pressure",
    min_value=1,
    max_value=10,
    value=5,
    help="1 = Flexible | 10 = Extremely tight"
)

# Analyze button
if st.sidebar.button("🔍 Analyse", use_container_width=True):
    # Calculate scores
    agile_score = 0
    waterfall_score = 0
    
    # Factor 1: Requirements Volatility
    agile_score += volatility * 7
    waterfall_score += (10 - volatility) * 7
    
    # Factor 2: Regulatory Intensity
    if regulatory == "Low":
        waterfall_score += 10
    elif regulatory == "High":
        waterfall_score += 25
        agile_score -= 15
    
    # Factor 3: Team Size
    if team_size in ["Solo", "Small (2-5)"]:
        agile_score += 10
    elif team_size == "Large (6+)":
        waterfall_score += 15
    
    # Factor 4: Team Distribution
    if distribution == "Hybrid":
        agile_score -= 5
        waterfall_score += 5
    elif distribution == "Remote":
        agile_score -= 10
        waterfall_score += 10
    
    # Factor 5: Project Type
    if project_type == "Fixed-scope":
        waterfall_score += 15
    elif project_type in ["Cloud-native", "AI-integrated"]:
        agile_score += 20
    elif project_type == "Mixed":
        agile_score += 10
    
    # Factor 6: Timeline Pressure
    agile_score += timeline * 4
    if timeline > 7:
        waterfall_score -= 10
    
    # Hybrid score
    hybrid_score = (agile_score + waterfall_score) / 2 + 10
    
    # Cap scores
    agile_score = min(100, max(0, agile_score))
    waterfall_score = min(100, max(0, waterfall_score))
    hybrid_score = min(100, max(0, hybrid_score))
    
    # Determine winner
    scores = {
        "Agile": agile_score,
        "Waterfall": waterfall_score,
        "Hybrid": hybrid_score
    }
    winner = max(scores, key=scores.get)
    winner_score = scores[winner]
    
    # Calculate confidence
    sorted_scores = sorted(scores.values(), reverse=True)
    confidence_diff = sorted_scores[0] - sorted_scores[1]
    
    if confidence_diff >= 20:
        confidence = "High"
        confidence_color = "#10b981"
    elif confidence_diff >= 10:
        confidence = "Medium"
        confidence_color = "#f59e0b"
    else:
        confidence = "Low"
        confidence_color = "#ef4444"
    
    # Display results
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.header("Recommendation")
        
        # Recommendation badge
        if winner == "Agile":
            badge_class = "recommendation-agile"
            emoji = "⚡"
        elif winner == "Waterfall":
            badge_class = "recommendation-waterfall"
            emoji = "📋"
        else:
            badge_class = "recommendation-hybrid"
            emoji = "⚙️"
        
        st.markdown(f"""
        <div class="recommendation-badge {badge_class}">
            {emoji} {winner.upper()}
        </div>
        """, unsafe_allow_html=True)
        
        # Confidence
        st.markdown(f"""
        <div style="text-align: center; margin-top: 1rem; padding: 0.75rem; background-color: {confidence_color}; color: white; border-radius: 0.5rem; font-weight: bold;">
            Confidence: {confidence}
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.metric("Agile Score", f"{agile_score:.0f}/100")
        st.metric("Waterfall Score", f"{waterfall_score:.0f}/100")
        st.metric("Hybrid Score", f"{hybrid_score:.0f}/100")
    
    # Explanation
    st.markdown("---")
    st.subheader("Why This Recommendation?")
    
    explanation_parts = []
    
    if volatility >= 7:
        explanation_parts.append(f"• **High volatility ({volatility}/10)** favors Agile's iterative approach")
    elif volatility <= 3:
        explanation_parts.append(f"• **Low volatility ({volatility}/10)** favors Waterfall's upfront planning")
    
    if regulatory == "High":
        explanation_parts.append("• **High regulatory intensity** requires Waterfall's formal documentation and change control")
    elif regulatory == "None":
        explanation_parts.append("• **No regulatory requirements** enables Agile's flexibility")
    
    if team_size == "Large (6+)":
        explanation_parts.append("• **Large team** benefits from Waterfall's upfront planning to reduce coordination overhead")
    elif team_size in ["Solo", "Small (2-5)"]:
        explanation_parts.append("• **Small team** enables Agile's iterative development with easy communication")
    
    if distribution == "Remote":
        explanation_parts.append("• **Distributed team** benefits from Waterfall's documentation to reduce communication needs")
    elif distribution == "Co-located":
        explanation_parts.append("• **Co-located team** enables Agile's frequent collaboration")
    
    if project_type in ["Cloud-native", "AI-integrated"]:
        explanation_parts.append(f"• **{project_type} project** benefits from Agile's iterative approach and continuous deployment")
    elif project_type == "Fixed-scope":
        explanation_parts.append("• **Fixed-scope project** benefits from Waterfall's upfront planning")
    
    if timeline >= 8:
        explanation_parts.append(f"• **Tight timeline ({timeline}/10)** favors Agile's incremental delivery")
    elif timeline <= 3:
        explanation_parts.append(f"• **Flexible timeline ({timeline}/10)** allows Waterfall's comprehensive planning")
    
    for part in explanation_parts:
        st.markdown(part)
    
    # Radar chart
    st.markdown("---")
    st.subheader("Score Breakdown")
    
    # Create radar chart
    categories = ["Agile", "Waterfall", "Hybrid"]
    values = [agile_score, waterfall_score, hybrid_score]
    
    fig = go.Figure(data=go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        name='Scores',
        line=dict(color='#3b82f6'),
        fillcolor='rgba(59, 130, 246, 0.3)'
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100],
                tickfont=dict(size=10)
            )
        ),
        showlegend=False,
        height=500,
        margin=dict(l=80, r=80, t=80, b=80)
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Score table
    st.subheader("Detailed Scores")
    
    score_data = {
        "Methodology": ["Agile", "Waterfall", "Hybrid"],
        "Score": [f"{agile_score:.0f}", f"{waterfall_score:.0f}", f"{hybrid_score:.0f}"],
        "Recommendation": [
            "✓ Recommended" if winner == "Agile" else "",
            "✓ Recommended" if winner == "Waterfall" else "",
            "✓ Recommended" if winner == "Hybrid" else ""
        ]
    }
    
    st.table(score_data)
    
    # Disclaimer
    st.markdown("---")
    st.markdown("""
    <div style="background-color: #f0f4f9; padding: 1rem; border-radius: 0.5rem; font-size: 0.85rem; color: #64748b;">
    <strong>Disclaimer:</strong> This tool is based on a primary simulation of a small-scale task management application. 
    Recommendations should be considered alongside organizational maturity, team experience, and project-specific constraints. 
    For enterprise projects, consult with project management professionals and stakeholders.
    </div>
    """, unsafe_allow_html=True)

else:
    # Initial state
    st.info("👈 Configure project characteristics in the sidebar and click **Analyse** to get a recommendation.")
    
    st.markdown("---")
    st.subheader("About This Tool")
    
    st.markdown("""
    This decision-support tool recommends Agile, Waterfall, or Hybrid methodologies based on six key project characteristics:
    
    1. **Requirements Volatility** — How much requirements are expected to change
    2. **Regulatory Intensity** — Compliance and audit requirements
    3. **Team Size** — Number of developers
    4. **Team Distribution** — Physical location of team members
    5. **Project Type** — Nature of the project (fixed-scope, cloud-native, AI-integrated, mixed)
    6. **Timeline Pressure** — How tight the delivery deadline is
    
    The scoring algorithm is based on:
    - **Primary simulation:** Controlled comparison of Waterfall vs Agile on identical scope
    - **Literature review:** Standish CHAOS Report, Digital.ai State of Agile, PMI Pulse of the Profession
    - **Industry best practices:** Lessons learned from methodology adoption across organizations
    
    **Key Findings from Simulation:**
    - Agile superior in change management (8 hrs rework vs 5 hrs, but zero schedule impact)
    - Agile superior in early defect detection (7 defects found and fixed vs 0 in testing phase)
    - Waterfall superior in upfront planning (10 hrs documentation provided clarity)
    - Both methodologies achieved 100% feature delivery
    """)
    
    st.markdown("---")
    st.subheader("Methodology Characteristics")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        ### ⚡ Agile
        
        **Best for:**
        - Evolving requirements
        - Startups & innovation
        - Cloud-native projects
        - Small co-located teams
        
        **Strengths:**
        - Flexible to changes
        - Early delivery
        - Continuous feedback
        - Early defect detection
        
        **Risks:**
        - Requires strong communication
        - May conflict with compliance
        - Needs experienced team
        """)
    
    with col2:
        st.markdown("""
        ### 📋 Waterfall
        
        **Best for:**
        - Fixed-scope projects
        - Regulated industries
        - Large distributed teams
        - Stable requirements
        
        **Strengths:**
        - Predictable process
        - Comprehensive documentation
        - Formal change control
        - Clear milestones
        
        **Risks:**
        - Inflexible to changes
        - Delayed delivery
        - Late defect discovery
        - High rework cost
        """)
    
    with col3:
        st.markdown("""
        ### ⚙️ Hybrid
        
        **Best for:**
        - Mixed characteristics
        - Moderate volatility
        - Some regulatory requirements
        - Transitioning organizations
        
        **Strengths:**
        - Balances planning & flexibility
        - Reduces risk
        - Adapts to context
        - Combines best of both
        
        **Risks:**
        - More complex to manage
        - Requires discipline
        - May satisfy neither extreme
        """)

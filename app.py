import streamlit as st
import pandas as pd
import plotly.express as px

from src.analyzer import analyze_complaint
from src.batch_analyzer import process_batch
from src.database import (
    create_database,
    save_complaint,
    get_complaints
)


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="IntelliResolve",
    page_icon="◆",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    /* =========================
       MAIN APPLICATION
       ========================= */

    .stApp {
        background-color: #f4f6fa;
    }

    .block-container {
        max-width: 1450px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }


    /* =========================
       SIDEBAR
       ========================= */

    section[data-testid="stSidebar"] {
        background-color: #0f172a;
    }

    section[data-testid="stSidebar"] * {
        color: #e5e7eb;
    }

    .brand {
        font-size: 27px;
        font-weight: 800;
        color: #ffffff;
        margin-bottom: 5px;
    }

    .brand-subtitle {
        font-size: 13px;
        color: #94a3b8;
        margin-bottom: 30px;
    }

    .sidebar-heading {
        color: #cbd5e1;
        font-size: 16px;
        font-weight: 700;
        margin-top: 18px;
        margin-bottom: 12px;
    }

    .system-card {
        background-color: #1e293b;
        border: 1px solid #334155;
        border-radius: 12px;
        padding: 16px;
        margin-top: 15px;
    }

    .system-label {
        color: #94a3b8;
        font-size: 11px;
        font-weight: 600;
        margin-top: 10px;
    }

    .system-value {
        color: #f8fafc;
        font-size: 14px;
        font-weight: 600;
        margin-top: 3px;
    }


    /* =========================
       HEADINGS
       ========================= */

    .main-title {
        color: #111827;
        font-size: 38px;
        font-weight: 800;
        margin-bottom: 5px;
    }

    .main-subtitle {
        color: #64748b;
        font-size: 15px;
        margin-bottom: 20px;
    }


    /* =========================
       STATUS
       ========================= */

    .online-badge {
        display: inline-block;
        background-color: #dcfce7;
        color: #047857;
        padding: 7px 13px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 700;
        margin-bottom: 22px;
    }


    /* =========================
       KPI CARDS
       ========================= */

    .kpi-card {
        background-color: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 14px;
        padding: 20px;
        min-height: 115px;
        box-shadow: 0 2px 7px rgba(15, 23, 42, 0.04);
    }

    .kpi-label {
        color: #64748b;
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 0.5px;
    }

    .kpi-value {
        color: #111827;
        font-size: 28px;
        font-weight: 800;
        margin-top: 9px;
    }

    .kpi-description {
        color: #94a3b8;
        font-size: 11px;
        margin-top: 3px;
    }


    /* =========================
       CARDS
       ========================= */

    .card {
        background-color: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 14px;
        padding: 22px;
        margin-bottom: 18px;
        box-shadow: 0 2px 7px rgba(15, 23, 42, 0.04);
    }

    .card-title {
        color: #172033;
        font-size: 19px;
        font-weight: 750;
        margin-bottom: 6px;
    }

    .card-description {
        color: #64748b;
        font-size: 13px;
        margin-bottom: 12px;
    }


    /* =========================
       RESULT BOX
       ========================= */

    .result-box {
        background-color: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 14px;
        padding: 22px;
        margin-top: 18px;
    }

    .result-title {
        color: #172033;
        font-size: 18px;
        font-weight: 750;
        margin-bottom: 10px;
    }


    /* =========================
       AI BOX
       ========================= */

    .ai-box {
        background: linear-gradient(
            135deg,
            #eef4ff,
            #f8faff
        );
        border: 1px solid #dbe5ff;
        border-radius: 14px;
        padding: 24px;
        margin-top: 20px;
    }

    .ai-title {
        color: #1e3a8a;
        font-size: 19px;
        font-weight: 750;
        margin-bottom: 12px;
    }


    /* =========================
       BUTTONS
       ========================= */

    .stButton > button {
        border-radius: 9px;
        font-weight: 700;
        min-height: 44px;
    }


    /* =========================
       FOOTER
       ========================= */

    .footer {
        text-align: center;
        color: #94a3b8;
        font-size: 11px;
        margin-top: 45px;
        padding-bottom: 20px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# DATABASE INITIALIZATION
# ============================================================

create_database()


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        '<div class="brand">◇ IntelliResolve</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="brand-subtitle">'
        'Customer Complaint Intelligence'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-heading">Navigation</div>',
        unsafe_allow_html=True
    )

    page = st.radio(
        "",
        [
            "Analyze Complaint",
            "Batch Analysis",
            "Complaint History",
            "Analytics"
        ],
        label_visibility="collapsed"
    )

    st.divider()

    st.markdown(
        '<div class="sidebar-heading">System</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="system-card">

            <div class="system-label">
                AI ENGINE
            </div>

            <div class="system-value">
                Gemini
            </div>


            <div class="system-label">
                NLP ENGINE
            </div>

            <div class="system-value">
                TF-IDF + VADER
            </div>


            <div class="system-label">
                DATABASE
            </div>

            <div class="system-value">
                SQLite
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# LOAD DATABASE RECORDS
# ============================================================

try:

    records = get_complaints()

except Exception:

    records = []


# ============================================================
# ANALYZE COMPLAINT
# ============================================================

if page == "Analyze Complaint":

    st.markdown(
        '<div class="main-title">'
        'Customer Complaint Analysis'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="main-subtitle">'
        'Analyze customer complaints using NLP and Generative AI.'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="online-badge">'
        '● AI SYSTEM ONLINE'
        '</div>',
        unsafe_allow_html=True
    )


    # --------------------------------------------------------
    # KPI CALCULATIONS
    # --------------------------------------------------------

    total_complaints = len(records)

    negative_cases = 0
    high_priority_cases = 0

    for record in records:

        # Database structure:
        # 0 = id
        # 1 = complaint
        # 2 = category
        # 3 = sentiment
        # 4 = sentiment_score
        # 5 = priority
        # 6 = keywords
        # 7 = llm_analysis
        # 8 = created_at

        if len(record) > 3:

            if record[3] == "Negative":
                negative_cases += 1

        if len(record) > 5:

            if record[5] in ["High", "Critical"]:
                high_priority_cases += 1


    # --------------------------------------------------------
    # KPI CARDS
    # --------------------------------------------------------

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        st.markdown(
            f"""
            <div class="kpi-card">

                <div class="kpi-label">
                    TOTAL COMPLAINTS
                </div>

                <div class="kpi-value">
                    {total_complaints}
                </div>

                <div class="kpi-description">
                    Analyzed by system
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    with c2:

        st.markdown(
            f"""
            <div class="kpi-card">

                <div class="kpi-label">
                    NEGATIVE CASES
                </div>

                <div class="kpi-value">
                    {negative_cases}
                </div>

                <div class="kpi-description">
                    Require attention
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    with c3:

        st.markdown(
            f"""
            <div class="kpi-card">

                <div class="kpi-label">
                    HIGH PRIORITY
                </div>

                <div class="kpi-value">
                    {high_priority_cases}
                </div>

                <div class="kpi-description">
                    Urgent complaints
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    with c4:

        st.markdown(
            """
            <div class="kpi-card">

                <div class="kpi-label">
                    AI ENGINE
                </div>

                <div class="kpi-value">
                    Active
                </div>

                <div class="kpi-description">
                    Gemini + NLP
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    st.write("")


    # --------------------------------------------------------
    # INPUT CARD
    # --------------------------------------------------------

    st.markdown(
        """
        <div class="card">

            <div class="card-title">
                Analyze a New Complaint
            </div>

            <div class="card-description">
                Enter the customer's message below.
                IntelliResolve will classify, prioritize,
                extract keywords and generate an AI-assisted
                resolution.
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


    complaint = st.text_area(
        "Customer complaint",
        height=170,
        placeholder=(
            "Example: My package has been delayed for five "
            "days and the tracking information has not been "
            "updated. Customer support has not responded."
        ),
        label_visibility="collapsed"
    )


    analyze_button = st.button(
        "Analyze Complaint →",
        type="primary",
        use_container_width=True
    )


    # --------------------------------------------------------
    # RUN ANALYSIS
    # --------------------------------------------------------

    if analyze_button:

        if not complaint.strip():

            st.warning(
                "Please enter a customer complaint."
            )

        else:

            with st.spinner(
                "Analyzing complaint with NLP and Gemini AI..."
            ):

                try:

                    result = analyze_complaint(
                        complaint.strip()
                    )


                    # Save using our existing database API
                    save_complaint(
                        result,
                        complaint.strip()
                    )


                    st.success(
                        "Analysis completed successfully."
                    )


                    # ------------------------------------------------
                    # RESULT METRICS
                    # ------------------------------------------------

                    r1, r2, r3 = st.columns(3)


                    with r1:

                        st.metric(
                            "Category",
                            result["category"]
                        )


                    with r2:

                        st.metric(
                            "Sentiment",
                            result["sentiment"]["sentiment"]
                        )


                    with r3:

                        st.metric(
                            "Priority",
                            result["urgency"]["priority"]
                        )


                    # ------------------------------------------------
                    # SENTIMENT SCORE
                    # ------------------------------------------------

                    score = result[
                        "sentiment"
                    ]["score"]


                    st.markdown(
                        '<div class="result-box">',
                        unsafe_allow_html=True
                    )


                    st.markdown(
                        '<div class="result-title">'
                        'Sentiment Analysis'
                        '</div>',
                        unsafe_allow_html=True
                    )


                    st.write(
                        f"VADER sentiment score: "
                        f"**{score:.3f}**"
                    )


                    st.progress(
                        min(
                            max(
                                (score + 1) / 2,
                                0
                            ),
                            1
                        )
                    )


                    st.markdown(
                        '</div>',
                        unsafe_allow_html=True
                    )


                    # ------------------------------------------------
                    # KEYWORDS
                    # ------------------------------------------------

                    st.markdown(
                        '<div class="result-box">',
                        unsafe_allow_html=True
                    )


                    st.markdown(
                        '<div class="result-title">'
                        '🔑 Detected Keywords'
                        '</div>',
                        unsafe_allow_html=True
                    )


                    if result["keywords"]:

                        st.write(
                            " • ".join(
                                result["keywords"]
                            )
                        )

                    else:

                        st.write(
                            "No significant keywords detected."
                        )


                    st.markdown(
                        '</div>',
                        unsafe_allow_html=True
                    )


                    # ------------------------------------------------
                    # URGENCY
                    # ------------------------------------------------

                    st.markdown(
                        '<div class="result-box">',
                        unsafe_allow_html=True
                    )


                    st.markdown(
                        '<div class="result-title">'
                        '⚠️ Priority Analysis'
                        '</div>',
                        unsafe_allow_html=True
                    )


                    triggers = result[
                        "urgency"
                    ]["triggers"]


                    if triggers:

                        st.write(
                            "Detected triggers: "
                            + ", ".join(triggers)
                        )

                    else:

                        st.write(
                            "No specific urgency triggers detected."
                        )


                    st.markdown(
                        '</div>',
                        unsafe_allow_html=True
                    )


                    # ------------------------------------------------
                    # GEMINI
                    # ------------------------------------------------

                    st.markdown(
                        """
                        <div class="ai-box">

                            <div class="ai-title">
                                ✦ Gemini AI Resolution Assistant
                            </div>

                        </div>
                        """,
                        unsafe_allow_html=True
                    )


                    st.markdown(
                        result["llm_analysis"]
                    )


                except Exception as error:

                    st.error(
                        f"Analysis failed: {error}"
                    )


# ============================================================
# BATCH ANALYSIS
# ============================================================

elif page == "Batch Analysis":

    st.markdown(
        '<div class="main-title">'
        'Batch Complaint Analysis'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="main-subtitle">'
        'Upload multiple customer complaints and analyze '
        'them automatically.'
        '</div>',
        unsafe_allow_html=True
    )


    st.markdown(
        """
        <div class="card">

            <div class="card-title">
                Upload Complaint Dataset
            </div>

            <div class="card-description">
                Your CSV must contain a column named
                <b>text</b> or <b>complaint</b>.
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


    uploaded_file = st.file_uploader(
        "Upload CSV",
        type=["csv"],
        label_visibility="collapsed"
    )


    if uploaded_file is not None:

        try:

            uploaded_df = pd.read_csv(
                uploaded_file
            )


            st.success(
                f"File uploaded successfully: "
                f"{len(uploaded_df)} complaints found."
            )


            st.markdown(
                "### Dataset Preview"
            )


            st.dataframe(
                uploaded_df.head(10),
                use_container_width=True,
                hide_index=True
            )


            # ------------------------------------------------
            # VALIDATE COLUMNS
            # ------------------------------------------------

            if (
                "text" not in uploaded_df.columns
                and
                "complaint" not in uploaded_df.columns
            ):

                st.error(
                    "Your CSV must contain a "
                    "'text' or 'complaint' column."
                )


            else:

                st.success(
                    "CSV format is valid. "
                    "Ready for analysis."
                )


                st.info(
                    "Each complaint will be processed through "
                    "the NLP pipeline and Gemini AI."
                )


                process_button = st.button(
                    "🚀 Analyze All Complaints",
                    type="primary",
                    use_container_width=True
                )


                if process_button:

                    with st.spinner(
                        "Processing complaints with NLP and Gemini AI..."
                    ):

                        try:

                            results_df = process_batch(
                                uploaded_df
                            )


                            st.session_state[
                                "batch_results"
                            ] = results_df


                            st.success(
                                "Batch analysis completed!"
                            )


                        except Exception as error:

                            st.error(
                                f"Batch analysis failed: {error}"
                            )


        except Exception as error:

            st.error(
                f"Could not read the CSV file: {error}"
            )


    # --------------------------------------------------------
    # DISPLAY BATCH RESULTS
    # --------------------------------------------------------

    if "batch_results" in st.session_state:

        results_df = st.session_state[
            "batch_results"
        ]


        st.divider()


        st.markdown(
            "### 📊 Analysis Results"
        )


        total_results = len(
            results_df
        )


        successful = (
            results_df["status"]
            .astype(str)
            .str.startswith("Success")
        ).sum()


        negative = (
            results_df["sentiment"]
            == "Negative"
        ).sum()


        high_priority = results_df[
            results_df["priority"].isin(
                ["High", "Critical"]
            )
        ].shape[0]


        # ------------------------------------------------
        # BATCH KPIs
        # ------------------------------------------------

        c1, c2, c3, c4 = st.columns(4)


        with c1:

            st.metric(
                "Processed",
                total_results
            )


        with c2:

            st.metric(
                "Successful",
                successful
            )


        with c3:

            st.metric(
                "Negative",
                negative
            )


        with c4:

            st.metric(
                "High Priority",
                high_priority
            )


        st.write("")


        # ------------------------------------------------
        # RESULTS TABLE
        # ------------------------------------------------

        st.dataframe(
            results_df,
            use_container_width=True,
            hide_index=True
        )


        # ------------------------------------------------
        # DOWNLOAD
        # ------------------------------------------------

        csv_results = results_df.to_csv(
            index=False
        )


        st.download_button(
            label="⬇ Download Analysis Results",
            data=csv_results,
            file_name="intelliresolve_batch_results.csv",
            mime="text/csv",
            type="primary"
        )


# ============================================================
# COMPLAINT HISTORY
# ============================================================

elif page == "Complaint History":

    st.markdown(
        '<div class="main-title">'
        'Complaint History'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="main-subtitle">'
        'Review previously analyzed customer complaints.'
        '</div>',
        unsafe_allow_html=True
    )


    if not records:

        st.info(
            "No complaints have been analyzed yet."
        )


    else:

        history_data = []


        for record in records:

            history_data.append(
                {
                    "ID": record[0],
                    "Complaint": record[1],
                    "Category": record[2],
                    "Sentiment": record[3],
                    "Sentiment Score": record[4],
                    "Priority": record[5],
                    "Keywords": record[6],
                    "Created": record[8]
                }
            )


        history_df = pd.DataFrame(
            history_data
        )


        st.dataframe(
            history_df,
            use_container_width=True,
            hide_index=True
        )


        # ------------------------------------------------
        # DOWNLOAD HISTORY
        # ------------------------------------------------

        csv_history = history_df.to_csv(
            index=False
        )


        st.download_button(
            "⬇ Download Complaint History",
            csv_history,
            "complaint_history.csv",
            "text/csv"
        )


# ============================================================
# ANALYTICS
# ============================================================

elif page == "Analytics":

    st.markdown(
        '<div class="main-title">'
        'Analytics Dashboard'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="main-subtitle">'
        'Monitor complaint patterns, sentiment and '
        'support priorities.'
        '</div>',
        unsafe_allow_html=True
    )


    if not records:

        st.info(
            "No complaint data is available yet. "
            "Analyze some complaints first."
        )


    else:

        analytics_data = []


        for record in records:

            analytics_data.append(
                {
                    "Category": record[2],
                    "Sentiment": record[3],
                    "Priority": record[5]
                }
            )


        df = pd.DataFrame(
            analytics_data
        )


        # ------------------------------------------------
        # KPI VALUES
        # ------------------------------------------------

        total = len(df)


        negative = (
            df["Sentiment"]
            == "Negative"
        ).sum()


        high_priority = df[
            df["Priority"].isin(
                ["High", "Critical"]
            )
        ].shape[0]


        top_category = (
            df["Category"]
            .value_counts()
            .idxmax()
        )


        # ------------------------------------------------
        # KPI CARDS
        # ------------------------------------------------

        c1, c2, c3, c4 = st.columns(4)


        with c1:

            st.markdown(
                f"""
                <div class="kpi-card">

                    <div class="kpi-label">
                        TOTAL COMPLAINTS
                    </div>

                    <div class="kpi-value">
                        {total}
                    </div>

                    <div class="kpi-description">
                        Cases analyzed
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )


        with c2:

            st.markdown(
                f"""
                <div class="kpi-card">

                    <div class="kpi-label">
                        NEGATIVE CASES
                    </div>

                    <div class="kpi-value">
                        {negative}
                    </div>

                    <div class="kpi-description">
                        Customer dissatisfaction
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )


        with c3:

            st.markdown(
                f"""
                <div class="kpi-card">

                    <div class="kpi-label">
                        HIGH PRIORITY
                    </div>

                    <div class="kpi-value">
                        {high_priority}
                    </div>

                    <div class="kpi-description">
                        High + Critical
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )


        with c4:

            st.markdown(
                f"""
                <div class="kpi-card">

                    <div class="kpi-label">
                        TOP CATEGORY
                    </div>

                    <div class="kpi-value"
                         style="font-size:20px;">
                        {top_category}
                    </div>

                    <div class="kpi-description">
                        Most frequent complaint
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )


        st.write("")


        # ------------------------------------------------
        # CATEGORY + SENTIMENT
        # ------------------------------------------------

        col1, col2 = st.columns(2)


        with col1:

            st.markdown(
                "### Complaints by Category"
            )


            category_counts = (
                df["Category"]
                .value_counts()
                .reset_index()
            )


            category_counts.columns = [
                "Category",
                "Count"
            ]


            fig_category = px.bar(
                category_counts,
                x="Category",
                y="Count",
                text="Count"
            )


            fig_category.update_layout(
                height=400,
                showlegend=False,
                xaxis_title="",
                yaxis_title="Complaints"
            )


            fig_category.update_traces(
                textposition="outside"
            )


            st.plotly_chart(
                fig_category,
                use_container_width=True
            )


        with col2:

            st.markdown(
                "### Customer Sentiment"
            )


            sentiment_counts = (
                df["Sentiment"]
                .value_counts()
                .reset_index()
            )


            sentiment_counts.columns = [
                "Sentiment",
                "Count"
            ]


            fig_sentiment = px.pie(
                sentiment_counts,
                names="Sentiment",
                values="Count",
                hole=0.55
            )


            fig_sentiment.update_layout(
                height=400
            )


            st.plotly_chart(
                fig_sentiment,
                use_container_width=True
            )


        # ------------------------------------------------
        # PRIORITY
        # ------------------------------------------------

        st.markdown(
            "### Priority Distribution"
        )


        priority_counts = (
            df["Priority"]
            .value_counts()
            .reset_index()
        )


        priority_counts.columns = [
            "Priority",
            "Count"
        ]


        fig_priority = px.bar(
            priority_counts,
            x="Priority",
            y="Count",
            text="Count"
        )


        fig_priority.update_layout(
            height=350,
            showlegend=False,
            xaxis_title="",
            yaxis_title="Complaints"
        )


        fig_priority.update_traces(
            textposition="outside"
        )


        st.plotly_chart(
            fig_priority,
            use_container_width=True
        )


        # ------------------------------------------------
        # CATEGORY VS SENTIMENT
        # ------------------------------------------------

        st.markdown(
            "### Category vs Sentiment"
        )


        category_sentiment = (
            df.groupby(
                ["Category", "Sentiment"]
            )
            .size()
            .reset_index(
                name="Count"
            )
        )


        fig_category_sentiment = px.bar(
            category_sentiment,
            x="Category",
            y="Count",
            color="Sentiment",
            barmode="group"
        )


        fig_category_sentiment.update_layout(
            height=420,
            xaxis_title="",
            yaxis_title="Complaints"
        )


        st.plotly_chart(
            fig_category_sentiment,
            use_container_width=True
        )


        # ------------------------------------------------
        # HIGH-RISK COMPLAINTS
        # ------------------------------------------------

        st.markdown(
            "### 🚨 High-Risk Complaints"
        )


        high_risk = df[
            df["Priority"].isin(
                ["High", "Critical"]
            )
        ]


        if high_risk.empty:

            st.success(
                "No high-risk complaints detected."
            )

        else:

            st.dataframe(
                high_risk,
                use_container_width=True,
                hide_index=True
            )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">
        IntelliResolve · AI-Powered Customer Complaint Intelligence
        <br>
        Hybrid NLP + Generative AI System
    </div>
    """,
    unsafe_allow_html=True
)
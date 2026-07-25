import streamlit as st

st.set_page_config(
    page_title="Campaign",
    page_icon="📢",
)

st.title("📢 Create Campaign")

st.caption(
    "Buat Campaign Meta Ads menggunakan Marketing API"
)

st.divider()

# ==========================
# BASIC INFORMATION
# ==========================

st.subheader("Basic Campaign Information")

campaign_name = st.text_input(
    "Campaign Name",
    placeholder="Contoh: Summer Sale 2026"
)

objective = st.selectbox(
    "Campaign Objective",
    [
        "Awareness",
        "Traffic",
        "Engagement",
        "Leads",
        "App Promotion",
        "Sales",
    ]
)

buying_type = st.selectbox(
    "Buying Type",
    [
        "AUCTION",
    ]
)

campaign_status = st.selectbox(
    "Campaign Status",
    [
        "ACTIVE",
        "PAUSED",
    ]
)

st.divider()

# ==========================
# BUDGET
# ==========================

st.subheader("Campaign Budget")

cbo = st.toggle(
    "Campaign Budget Optimization (CBO)",
    value=True,
)

budget_type = st.radio(
    "Budget Type",
    [
        "Daily",
        "Lifetime",
    ],
    horizontal=True,
)

budget = st.number_input(
    "Budget (Rp)",
    min_value=0,
    step=1000,
    value=100000,
)

st.divider()

# ==========================
# STRATEGY
# ==========================

st.subheader("Bid Strategy")

bid_strategy = st.selectbox(
    "Bid Strategy",
    [
        "LOWEST_COST_WITHOUT_CAP",
        "LOWEST_COST_WITH_BID_CAP",
        "COST_CAP",
    ]
)

special_category = st.selectbox(
    "Special Ad Category",
    [
        "NONE",
        "HOUSING",
        "EMPLOYMENT",
        "CREDIT",
    ]
)

st.divider()

col1, col2 = st.columns(2)

with col1:
    preview = st.button(
        "Preview Payload",
        use_container_width=True,
    )

with col2:
    create = st.button(
        "Create Campaign",
        type="primary",
        use_container_width=True,
    )

if preview:

    st.subheader("Preview")

    st.json(
        {
            "name": campaign_name,
            "objective": objective,
            "buying_type": buying_type,
            "status": campaign_status,
            "cbo": cbo,
            "budget_type": budget_type,
            "budget": budget,
            "bid_strategy": bid_strategy,
            "special_ad_category": special_category,
        }
    )

if create:

    errors = []

    if campaign_name.strip() == "":
        errors.append("Campaign Name wajib diisi.")

    if budget <= 0:
        errors.append("Budget harus lebih besar dari 0.")

    if len(errors) > 0:

        st.error("Periksa kembali data Campaign.")

        for error in errors:
            st.write(f"• {error}")

    else:

        st.success("✅ Validasi berhasil")

        st.info(
            "Tahap berikutnya Campaign akan dikirim ke Meta Marketing API."
    )
   

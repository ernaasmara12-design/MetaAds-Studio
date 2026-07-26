import streamlit as st

from meta_services.asset_service import AssetService


def render_identity(account_id):

    st.subheader("Identity")

    service = AssetService(account_id)
  
def get_pages(self):

    return self.account.get_ad_creative_previews()

def get_instagram_accounts(self):

    return [] 

    pages = {}
    instagram_accounts = {}

    try:
        for page in service.get_pages():
            pages[page["name"]] = page["id"]
    except Exception:
        pass

    try:
        for ig in service.get_instagram_accounts():
            instagram_accounts[ig["username"]] = ig["id"]
    except Exception:
        pass

    selected_page = st.selectbox(
        "Facebook Page",
        list(pages.keys()) if pages else ["Tidak ada Page"]
    )

    selected_ig = st.selectbox(
        "Instagram Account",
        list(instagram_accounts.keys()) if instagram_accounts else ["Tidak ada Instagram"]
    )

    return {
        "page_id": pages.get(selected_page),
        "instagram_actor_id": instagram_accounts.get(selected_ig),
    }

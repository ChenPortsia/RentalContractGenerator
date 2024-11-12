import streamlit as st
from time import sleep
from stqdm import stqdm
import pandas as pd

st.markdown("<h1 style='text-align: right;'>מחולל חוזי שכירות</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: right;'>הכנס פרטים כדי ליצור חוזה</h2>", unsafe_allow_html=True)
# Landlord details:
expander = st.expander("פרטי משכיר")
l, r = expander.columns(2)
r.markdown("<div style='text-align: right;'>שם מלא</div>", unsafe_allow_html=True)
l.markdown("<div style='text-align: right;'>ת\"ז</div>", unsafe_allow_html=True)
r.text_input("שם מלא", key="landlord_name", label_visibility="hidden")
l.text_input("ת\"ז", key="landlord_id", label_visibility="hidden")

r.markdown("<div style='text-align: right;'>טלפון נייד</div>", unsafe_allow_html=True)
l.markdown("<div style='text-align: right;'>אימייל</div>", unsafe_allow_html=True)
r.text_input("טלפון נייד", key="landlord_phone", label_visibility="hidden")
l.text_input("אימייל", key="landlord_email", label_visibility="hidden")
r.markdown("<div style='text-align: right;'>יישוב</div>", unsafe_allow_html=True)
l.markdown("<div style='text-align: right;'>רחוב</div>", unsafe_allow_html=True)
r.text_input("יישוב", key="landlord_city", label_visibility="hidden")
l.text_input("רחוב", key="landlord_street", label_visibility="hidden")

expander = st.expander("פרטי שוכר")
l, r = expander.columns(2)
r.markdown("<div style='text-align: right;'>שם מלא</div>", unsafe_allow_html=True)
l.markdown("<div style='text-align: right;'>ת\"ז</div>", unsafe_allow_html=True)
r.text_input("שם מלא", key="tenant_name", label_visibility="hidden")
l.text_input("ת\"ז", key="tenant_id", label_visibility="hidden")
r.markdown("<div style='text-align: right;'>טלפון נייד</div>", unsafe_allow_html=True)
l.markdown("<div style='text-align: right;'>אימייל</div>", unsafe_allow_html=True)
r.text_input("טלפון נייד", key="tenant_phone", label_visibility="hidden")
l.text_input("אימייל", key="tenant_email", label_visibility="hidden")

expander = st.expander("פרטי הנכס")
l, r = expander.columns(2)
r.markdown("<div style='text-align: right;'>יישוב</div>", unsafe_allow_html=True)
l.markdown("<div style='text-align: right;'>רחוב</div>", unsafe_allow_html=True)
r.text_input("יישוב", key="prop_city", label_visibility="hidden")
l.text_input("רחוב", key="prop_street", label_visibility="hidden")
a, b, c, d, e = expander.columns(5)
a.markdown("<div style='text-align: right;'>מספר בית</div>", unsafe_allow_html=True)
b.markdown("<div style='text-align: right;'>מספר דירה</div>", unsafe_allow_html=True)
c.markdown("<div style='text-align: right;'>מספר חדרים</div>", unsafe_allow_html=True)
d.markdown("<div style='text-align: right;'>קומה</div>", unsafe_allow_html=True)
e.markdown("<div style='text-align: right;'>מ\"ר הנכס</div>", unsafe_allow_html=True)
a.text_input("מספר בית", key="prop_num", label_visibility="hidden")
b.text_input("מספר דירה", key="prop_apt_num", label_visibility="hidden")
c.text_input("מספר חדרים", key="prop_rooms", label_visibility="hidden")
d.text_input("קומה", key="prop_level", label_visibility="hidden")
e.text_input("מ\"ר הנכס", key="prop_srm", label_visibility="hidden")

expander = st.expander("פרטי ההסכם")
a, b, c = expander.columns(3)
a.markdown("<div style='text-align: right;'>תחילת תקופת שכירות</div>", unsafe_allow_html=True)
b.markdown("<div style='text-align: right;'>סיום השכירות</div>", unsafe_allow_html=True)
c.markdown("<div style='text-align: right;'>תקופת שכירות</div>", unsafe_allow_html=True)
a.date_input("תחילת תקופת שכירות", key="rental_start_date", label_visibility="hidden")
b.date_input("סיום השכירות", key="rental_end_date", label_visibility="hidden")
rental_period = c.number_input("תקופת שכירות", 1, 12)
a.markdown("<div style='text-align: right;'>דמי שכירות</div>", unsafe_allow_html=True)
b.markdown("<div style='text-align: right;'>מועד התשלום</div>", unsafe_allow_html=True)
c.markdown("<div style='text-align: right;'>אופן התשלום</div>", unsafe_allow_html=True)
rental = a.number_input("דמי שכירות", 1, 1000000)
rental_date = b.number_input("מועד התשלום", 1, 31)
rental_method = c.selectbox('אופן התשלום',('המחאה', 'העברה בנקאית', 'מזומן'))

expander = st.expander("בטחונות")
a, b = expander.columns(2)
a.markdown("<div style='text-align: right;'>קנס יומי עבור איחור בפינוי דירה</div>", unsafe_allow_html=True)
b.markdown("<div style='text-align: right;'>גובהה צ’ק ביטחון</div>", unsafe_allow_html=True)
a.number_input("קנס יומי עבור איחור בפינוי דירה", key="sec_daily_violance_fee", label_visibility="hidden")
b.number_input("גובהה צ’ק ביטחון", key="sec_check", label_visibility="hidden")

expander = st.expander("פרטי ערב")
l, r = expander.columns(2)
r.markdown("<div style='text-align: right;'>שם מלא</div>", unsafe_allow_html=True)
l.markdown("<div style='text-align: right;'>ת\"ז</div>", unsafe_allow_html=True)
r.text_input("שם מלא", key="bail_name", label_visibility="hidden")
l.text_input("ת\"ז", key="bail_id", label_visibility="hidden")
r.markdown("<div style='text-align: right;'>טלפון נייד</div>", unsafe_allow_html=True)
l.markdown("<div style='text-align: right;'>אימייל</div>", unsafe_allow_html=True)
r.text_input("טלפון נייד", key="bail_phone", label_visibility="hidden")
l.text_input("אימייל", key="bail_email", label_visibility="hidden")
r.markdown("<div style='text-align: right;'>יישוב</div>", unsafe_allow_html=True)
l.markdown("<div style='text-align: right;'>רחוב</div>", unsafe_allow_html=True)
r.text_input("יישוב", key="bail_city", label_visibility="hidden")
l.text_input("רחוב", key="bail_street", label_visibility="hidden")

expander = st.expander("תנאים נוספים")
return_painted = expander.checkbox("החזרת דירה צבועה")
pats_not_allowed = expander.checkbox("איסור על בעלי חיים")
if expander.checkbox("תקופת התראה מוקדמת"):
    prior_notice = expander.number_input("תקופת התראה מוקדמת", 1, 12)
if expander.checkbox("אחר"):
    expander.markdown("<div style='text-align: right;'>:כתוב/י בצורה מטומצטת וברורה מה הסעיך הנוסף שתרצי/ה להוסיף</div>", unsafe_allow_html=True)
    expander.text_area("אחר", key="other", label_visibility="hidden")

# Load text from contract_form.txt

@st.cache_data
def populate_in_contract_form():
  with open('contract_form.txt', 'r', encoding='utf-8') as f:
    contract_form = f.read().format(
        landlord_name=st.session_state.landlord_name,
        landlord_id=st.session_state.landlord_id,
        landlord_phone=st.session_state.landlord_phone,
        landlord_email=st.session_state.landlord_email,
        landlord_city=st.session_state.landlord_city,
        landlord_street=st.session_state.landlord_street,
        tenant_name=st.session_state.tenant_name,
        tenant_id=st.session_state.tenant_id,
        tenant_phone=st.session_state.tenant_phone,
        tenant_email=st.session_state.tenant_email,
        prop_city=st.session_state.prop_city,
        prop_street=st.session_state.prop_street,
        prop_num=st.session_state.prop_num,
        prop_apt_num=st.session_state.prop_apt_num,
        prop_rooms=st.session_state.prop_rooms,
        prop_level=st.session_state.prop_level,
        prop_srm=st.session_state.prop_srm,
        rental_start_date=st.session_state.rental_start_date,
        rental_end_date=st.session_state.rental_end_date,
        rental_period=rental_period,
        rental=rental,
        rental_date=rental_date,
        rental_method=rental_method,
        sec_daily_violance_fee=st.session_state.sec_daily_violance_fee,
        sec_check=st.session_state.sec_check,
        bail_name=st.session_state.bail_name,
        bail_id=st.session_state.bail_id,
        bail_phone=st.session_state.bail_phone,
        bail_email=st.session_state.bail_email,
        bail_city=st.session_state.bail_city,
        bail_street=st.session_state.bail_street
    )
  return contract_form

contract = populate_in_contract_form()

if st.button('צור חוזה'):
  # st.write('טוען...')
  # for _ in stqdm(range(10)):
  #   sleep(0.5)
  st.write(contract)





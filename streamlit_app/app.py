import requests
import streamlit as st

url = 'http://127.0.0.1:8000/predict'

st.title('🏠 House Price Predictor')
st.markdown('___')

cities_dict = {
    'Auburn': 'Auburn',
    'Bellevue': 'Bellevue',
    'Black Diamond': 'Black Diamond',
    'Bothell': 'Bothell',
    'Carnation': 'Carnation',
    'Duvall': 'Duvall',
    'Enumclaw': 'Enumclaw',
    'Fall City': 'Fall City',
    'Federal Way': 'Federal Way',
    'Issaquah': 'Issaquah',
    'Kenmore': 'Kenmore',
    'Kent': 'Kent',
    'Kirkland': 'Kirkland',
    'Maple Valley': 'Maple Valley',
    'Medina': 'Medina',
    'Mercer Island': 'Mercer Island',
    'North Bend': 'North Bend',
    'Redmond': 'Redmond',
    'Renton': 'Renton',
    'Sammamish': 'Sammamish',
    'Seattle': 'Seattle',
    'Snoqualmie': 'Snoqualmie',
    'Vashon': 'Vashon',
    'Woodinville': 'Woodinville'
}

city = st.pills(
    'Choose a city in Washington',
    options=cities_dict.keys(),
    format_func=lambda option: cities_dict[option],
    selection_mode='single',
    key='city_selector',
)

st.markdown('---')

row1_col1, row1_col2, row1_col3 = st.columns(3)

with row1_col1:
    bedrooms = st.number_input(
        'Bedrooms (0 - 35)',
        min_value=0,
        max_value=35,
        value=0,
        step=1,
        key='bedrooms',
    )

with row1_col2:
    bathrooms = st.number_input(
        'Bathrooms (0.0 - 8.0)',
        min_value=0.0,
        max_value=8.0,
        value=0.0,
        step=0.25,
        key='bathrooms',
    )

with row1_col3:
    sqft_living = st.number_input(
        'Sq Ft (200 - 13500)',
        min_value=200,
        max_value=13500,
        value=200,
        step=100,
        key='sqft_living',
    )

row2_col1, row2_col2, row2_col3 = st.columns(3)

with row2_col1:
    floors = st.number_input(
        'Floors (1.0 - 4.0)',
        min_value=1.0,
        max_value=4.0,
        value=1.0,
        step=0.5,
        key='floors',
    )

with row2_col2:
    basement = st.selectbox(
        'Basement?',
        options=['Yes', 'No'],
        index=1,
        key='basement',
    )

with row2_col3:
    if basement == 'Yes':
        sqft_basement = st.number_input(
            'Basement Sq Ft',
            min_value=0,
            max_value=sqft_living,
            value=0,
            step=100,
            key='sqft_basement',
        )

    else:
        sqft_basement = 0

pct_basement = sqft_basement / sqft_living if sqft_living > 0 else 0.0

row3_col1, row3_col2, row3_col3, row3_col4 = st.columns(4)

with row3_col1:
    condition = st.selectbox(
        'House Condition',
        options=['Poor', 'Fair', 'Good', 'Very Good', 'Excellent'],
        index=2,  # Default to 'Good'
        key='condition',
    )

    condition_dict = {
        'Poor': 1,
        'Fair': 2,
        'Good': 3,
        'Very Good': 4,
        'Excellent': 5,
    }

    condition = condition_dict[condition]

with row3_col2:
    year_built = st.number_input(
        'Year Built (1900 - 2025)',
        min_value=1900,
        max_value=2025,
        value=1900,
        step=1,
        key='year_built',
    )

    house_age = 2025 - year_built

with row3_col3:
    was_renovated = st.selectbox(
        'Renovated?',
        options=['Yes', 'No'],
        index=1,
        key='was_renovated',
    )

    was_renovated_dict = {
        'Yes': 1,
        'No': 0,
    }

    was_renovated = was_renovated_dict[was_renovated]

with row3_col4:
    if was_renovated == 1:
        year_renovated = st.number_input(
            'Year Renovated',
            min_value=year_built,
            max_value=2025,
            value=year_built,
            step=1,
            key='year_renovated',
        )

        renovation_age = 2025 - year_renovated

    else:
        renovation_age = house_age

row4_col1, row4_col2, _, _ = st.columns(4)

with row4_col1:
    sqft_lot = st.radio(
        'Lot Size',
        options=['Sq Ft', 'Acres'],
        index=0,
        horizontal=True,
        key='sqft_lot_measure',
    )

with row4_col2:
    if sqft_lot == 'Sq Ft':
        sqft_lot = st.number_input(
            'Sq Ft',
            min_value=400,
            max_value=1_650_000,
            value=400,
            step=100,
            key='sqft_lot_sqft',
        )

    else:
        sqft_lot = st.number_input(
            'Acres',
            min_value=0.01,
            max_value=38.0,
            value=0.01,
            step=0.01,
            key='sqft_lot_acres',
        )

        sqft_lot = sqft_lot * 43560

st.markdown('---')

row5_col1, row5_col2 = st.columns(2)

with row5_col1:
    comps_sqft_living = st.radio(
        'Do you know Avg Sq Ft of the 15 closest houses?',
        options=['Yes', 'No'],
        horizontal=True,
        key='comps_sqft_living',
    )

with row5_col2:
    if comps_sqft_living == 'Yes':
        sqft_living15 = st.number_input(
            'Comps Avg Sq Ft',
            min_value=200,
            max_value=20_000,
            value=200,
            step=100,
            key='sqft_living15',
        )

    else:
        sqft_living15 = st.selectbox(
            'Comps Sq Ft (Compared to House)',
            options=['Much smaller', 'Slightly smaller', 'Same size', 'Slightly bigger', 'Much bigger'],
            index=2,
            key='sqft_living15',
        )

        sqft_living15_dict = {
            'Much smaller': (0.6 * sqft_living),
            'Slightly smaller': int(0.85 * sqft_living),
            'Same size': sqft_living,
            'Slightly bigger': int(1.15 * sqft_living),
            'Much bigger': int(1.4 * sqft_living),
        }

        sqft_living15 = sqft_living15_dict[sqft_living15]

row6_col1, row6_col2 = st.columns(2)

with row6_col1:
    comps_sqft_lot = st.radio(
        'Do you know Avg Lot Size of the 15 closest houses?',
        options=['Yes', 'No'],
        horizontal=True,
    )

with row6_col2:
    if comps_sqft_lot == 'No':
        sqft_lot15 = st.selectbox(
            'Average lot acreage (15 closest properties)',
            options=['Much smaller', 'Slightly smaller', 'Same size', 'Slightly bigger', 'Much bigger'],
            index=2,
        )

        sqft_lot15_dict = {
            'Much smaller': 0.6 * sqft_lot,
            'Slightly smaller': 0.85 * sqft_lot,
            'Same size': sqft_lot,
            'Slightly bigger': 1.15 * sqft_lot,
            'Much bigger': 1.4 * sqft_lot,
        }

        sqft_lot15 = sqft_lot15_dict[sqft_lot15]

row7_col1, row7_col2 = st.columns(2)

with row7_col1:
    if comps_sqft_lot == 'Yes':
        comps_lot_measure = st.radio(
            'Lot Size',
            options=['Sq Ft', 'Acres'],
            index=0,
            horizontal=True,
            key='comps_lot_measure',
        )

with row7_col2:
    if comps_sqft_lot == 'Yes':
        if comps_lot_measure == 'Sq Ft':
            sqft_lot15 = st.number_input(
                'Comps Avg Lot Sq Ft (15 closest houses)',
                min_value=400,
                max_value=1_650_000,
                value=400,
                step=100,
                key='sqft_lot15_sqft',
            )

        else:
            sqft_lot15 = st.number_input(
                'Comps Avg Lot Acres (15 closest houses)',
                min_value=0.01,
                max_value=38.0,
                value=0.01,
                step=0.01,
                key='sqft_lot15_acres',
            )

st.markdown('---')

payload = {
    'bedrooms': bedrooms,
    'bathrooms': bathrooms,
    'sqft_living': sqft_living,
    'sqft_lot': sqft_lot,
    'floors': floors,
    'condition': condition,
    'sqft_basement': sqft_basement,
    'pct_basement': pct_basement,
    'house_age': house_age,
    'renovation_age': renovation_age,
    'sqft_living15': sqft_living15,
    'sqft_lot15': sqft_lot15,
    'city': city,
    'was_renovated': was_renovated
}

if st.button('Predict 🏠 Price'):
    if any(val is None or val == '' for val in payload.values()):
        st.error('🚨 Please complete all fields before predicting.')

    else:
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                pred = data.get('predicted_price', None)

                if pred is not None:
                    st.success(f'${int(pred):,}')
                else:
                    st.error('🚨 Prediction not found in response.')
            
            else:
                st.error(f'API error: {response.status_code} - {response.text}')
                
        except Exception as e:
            st.error(f'Could not connect to API: {e}') 
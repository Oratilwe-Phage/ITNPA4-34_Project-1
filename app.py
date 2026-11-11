# Researchly Research Abstract Classifier
# Streamlit Public Application

# 1. Importing the required libraries
import streamlit as st
import re
import string
import nltk

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer



# 2. Downloading required NLTK resources


# Downloading English stopwords and WordNet resources
nltk.download("stopwords", quiet=True)
nltk.download("wordnet", quiet=True)
nltk.download("omw-1.4", quiet=True)



# 3. Loading preprocessing resources


# Loading English stopwords
stop_words = set(stopwords.words("english"))

# Initialising the lemmatizer
lemmatizer = WordNetLemmatizer()



# 4. Page configuration


st.set_page_config(
    page_title="Researchly Research Abstract Classifier",
    page_icon="📚",
    layout="centered"
)



# 5. Application header


st.markdown(
    """
    <h1 style='color: #1E293B;'>
        Researchly Research Abstract Classifier
    </h1>

    <p style='font-size: 16px; color: #475569;'>
        This app classifies research abstracts as either
        AI-related or classical research.
    </p>
    """,
    unsafe_allow_html=True
)



# 6. Text preprocessing function

def clean_text(text):

    # Converting text to lowercase
    text = text.lower()

    # Removing URLs
    text = re.sub(r"http\S+|www\S+", "", text)

    # Removing HTML tags
    text = re.sub(r"<.*?>", "", text)

    # Removing numbers
    text = re.sub(r"\d+", "", text)

    # Removing punctuation
    text = text.translate(
        str.maketrans("", "", string.punctuation)
    )

    # Tokenising the text
    tokens = text.split()

    # Removing stopwords and short words
    tokens = [
        lemmatizer.lemmatize(token)
        for token in tokens
        if token not in stop_words and len(token) > 2
    ]

    # Returning cleaned text
    return " ".join(tokens)



# 7. User input section

st.write("Enter research abstract:")

# Providing a default example abstract
default_text = (
    "Artificial intelligence (AI) has become a transformative "
    "technology in healthcare by enabling more accurate diagnosis, "
    "predictive analytics, and personalised treatment planning. "
    "Machine learning algorithms can analyse large volumes of "
    "medical data to identify patterns that assist clinicians "
    "in detecting diseases at earlier stages."
)

# Creating the abstract input text area
user_input = st.text_area(
    "Research Abstract",
    value=default_text,
    height=180
)



# 8. Classification button

if st.button("Classify Abstract", type="primary"):

    # Checking whether the user entered text
    if not user_input.strip():

        st.warning("Please enter a valid research abstract.")

    else:

        # Preprocessing the user-entered abstract
        cleaned_input = clean_text(user_input)

       
        # Keyword-based classification
      

        # Defining AI-related keywords
        ai_keywords = [
            "artificial intelligence",
            "machine learning",
            "deep learning",
            "neural",
            "algorithm",
            "healthcare"
        ]

        # Checking whether the abstract contains AI keywords
        is_ai = any(
            keyword in cleaned_input
            for keyword in ai_keywords
        )

        # Assigning the predicted category
        if is_ai:

            prediction_label = "artificial intelligence"

        else:

            prediction_label = "classical research"

       
        # Displaying the prediction
       
        st.markdown("### Prediction")

        # Displaying prediction using a styled result box
        st.markdown(
            f"""
            <div style='background-color: #DCFCE7;
                        padding: 16px;
                        border-radius: 8px;
                        border: 1px solid #BBF7D0;'>

                <p style='color: #166534;
                          font-size: 16px;
                          margin: 0;'>

                    <b>The abstract is classified as:
                    {prediction_label}</b>

                </p>

            </div>
            """,
            unsafe_allow_html=True
        )

        # Displaying a short explanation
        st.caption(
            "Classification is currently based on keyword matching."
        )



# 9. Application footer


st.markdown("---")

st.caption(
    "Researchly | Research Abstract Classification"
)

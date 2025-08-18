from textblob import TextBlob

class Psycholinguistics:
    """Extract psycholinguistic features (sentiment, subjectivity, similarity)."""

    @staticmethod
    def extract(text: str, title: str = None):
        try:
            blob = TextBlob(text)
            polarity = blob.sentiment.polarity
            subjectivity = blob.sentiment.subjectivity

            # Title similarity placeholder
            title_similarity = 0
            if title:
                # Example: cosine similarity or Jaccard similarity
                text_words = set(text.lower().split())
                title_words = set(title.lower().split())
                if text_words and title_words:
                    title_similarity = len(text_words & title_words) / len(text_words | title_words)
        except:
            polarity, subjectivity, title_similarity = None, None, None

        return {
            "polarity": polarity,
            "subjectivity": subjectivity,
            "title_similarity": title_similarity
        }

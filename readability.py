import textstat

class ReadabilityIndices:
    """Extract readability-related features from text."""

    @staticmethod
    def extract(text: str):
        try:
            gunning_fog = textstat.gunning_fog(text)
            smog = textstat.smog_index(text)
            ari = textstat.automated_readability_index(text)
        except:
            gunning_fog, smog, ari = None, None, None

        return {
            "gunning_fog": gunning_fog,
            "smog": smog,
            "ari": ari
        }

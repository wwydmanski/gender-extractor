from gender_extractor import GenderExtractor


def test_andrea():
    ext = GenderExtractor()
    assert ext.extract("Andrea")=='female'
    assert ext.extract("Andrea", "Italy")=='male'

if __name__=="__main__":
    test_andrea()
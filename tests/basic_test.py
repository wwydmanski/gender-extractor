from gender_extractor import GenderExtractor


def test_andrea():
    ext = GenderExtractor()
    assert ext.extract_gender("Andrea")=='female'
    assert ext.extract_gender("Andrea", "Italy")=='mostly male'


if __name__=="__main__":
    test_andrea()
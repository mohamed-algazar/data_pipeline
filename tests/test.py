from data_ingestion import create_db_engine, query_data, read_from_web_CSV

def test_web_csv():
    url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
    df = read_from_web_CSV(url)
    assert not df.empty

def test_database_query():
    engine = create_db_engine("sqlite:///Maji_Ndogo_farm_survey_small.db")
    sql = "SELECT name FROM sqlite_master WHERE type='table';"
    df = query_data(engine, sql)
    assert not df.empty

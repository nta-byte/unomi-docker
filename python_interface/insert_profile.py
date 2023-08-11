import requests
import pandas as pd
from tqdm import tqdm


def call_api(id, properties):
    r = requests.post('http://localhost:8182/cxs/profiles/',
                      auth=('karaf', 'karaf'),
                      json={
                          "itemId": id,
                          "itemType": "profile",
                          "version": None,
                          "properties": properties,
                          "systemProperties": {},
                          "segments": [],
                          "scores": {},
                          "mergedWith": None,
                          "consents": {}
                      })
    # print(r)
    # print(r.content)


def update_profile():
    df = pd.read_csv('../data/bq-results-20230225-063820-1677307502328.csv')
    print(df)
    for idx, row in tqdm(df.iterrows(), total=len(df)):
        # print(row.to_dict())
        r = {k: v for k, v in row.to_dict().items() if v == v}
        # print(r)
        call_api(r['DG_ID'], r)
        # break


if __name__ == '__main__':
    update_profile()

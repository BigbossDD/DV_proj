
import pandas as pd



def issues_to_csv(issues_dict, filename="issues_long.csv"):
    rows = []

    for issue_name, ids in issues_dict.items():
        for trip_id in ids:
            rows.append((trip_id, issue_name))

    df_out = pd.DataFrame(rows, columns=['trip_id', 'issue'])
    df_out.to_csv(filename, index=False)

    return df_out
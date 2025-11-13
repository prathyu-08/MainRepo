import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    duplicates = person.groupby('email').size()
    duplicates = duplicates[duplicates > 1].reset_index()
    duplicates.columns = ['Email', 'count']
    result = duplicates[['Email']]
    
    return result

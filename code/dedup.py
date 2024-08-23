import pandas as pd

# Read the combined CSV file
df = pd.read_csv("combined_output.csv")

print(f"Original number of rows: {len(df)}")

# Function to clean strings
def clean_string(s):
    if pd.isna(s):
        return s
    return s.lower().strip()

# Clean the 'title' and 'doi' columns
df['title_clean'] = df['title'].apply(clean_string)
df['doi_clean'] = df['doi'].apply(clean_string)

# De-duplicate based on title
title_duplicates = df[df.duplicated(subset='title_clean', keep=False)]
title_duplicate_count = len(title_duplicates)
df_title_deduped = df.drop_duplicates(subset='title_clean', keep='first')

print(f"Number of duplicates identified by title: {title_duplicate_count}")
print(f"Number of rows after title de-duplication: {len(df_title_deduped)}")

# De-duplicate based on DOI
doi_duplicates = df_title_deduped[df_title_deduped.duplicated(subset='doi_clean', keep=False)]
doi_duplicate_count = len(doi_duplicates)
df_final = df_title_deduped.drop_duplicates(subset='doi_clean', keep='first')

print(f"Number of duplicates identified by DOI: {doi_duplicate_count}")
print(f"Final number of rows after DOI de-duplication: {len(df_final)}")

# Remove the temporary cleaning columns
df_final = df_final.drop(columns=['title_clean', 'doi_clean'])

# Save the de-duplicated dataset
df_final.to_csv("deduplicated_output.csv", index=False)

print("De-duplicated dataset saved as 'deduplicated_output.csv'")

# Optional: Save duplicates to separate files for review
title_duplicates.to_csv("title_duplicates.csv", index=False)
doi_duplicates.to_csv("doi_duplicates.csv", index=False)

print("Duplicate entries saved in 'title_duplicates.csv' and 'doi_duplicates.csv' for review")
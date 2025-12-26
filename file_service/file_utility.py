

# Write DataFrame to CSV file
def save_cashflows_to_csv(df, filename):
    df.to_csv(filename, index = False)

def save_cashflows_to_csv(meta_df, df, filename):
    with open(filename, 'w', newline='') as f:
        meta_df.to_csv(f, index=False, header=False)
        f.write('\n')
        df.to_csv(f, index=False)
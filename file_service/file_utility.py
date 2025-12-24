

# Write DataFrame to CSV file
def save_cashflows_to_csv(df, filename):
    """Save the DataFrame to a CSV file."""
    df.to_csv(filename, index=False)
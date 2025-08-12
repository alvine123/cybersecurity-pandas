import pandas as pd

# Sample CSV: assume columns like 'timestamp', 'source_ip', 'destination_ip', 'bytes'
data = pd.read_csv('network_log.csv')
print("Top 5 Source IPs by Frequency:")
print(data['source_ip'].value_counts().head())


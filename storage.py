print("=== storage converter ===")
storage_gb = float(input("Enter storage in GB: "))
storage_mb = storage_gb * 1024
print("Storage in MB:", storage_mb)
print("Back to GB:", storage_mb / 1024, "GB")
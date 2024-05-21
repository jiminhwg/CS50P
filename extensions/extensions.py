file = input("File name: ")

if ".gif" in file.lower():
    print("image/gif")
elif ".jpg" in file.lower() or ".jpeg" in file.lower():
    print("image/jpeg")
elif ".png" in file.lower():
    print("image/png")
elif ".pdf" in file.lower():
    print("application/pdf")
elif ".txt" in file.lower():
    print("text/plain")
elif ".zip" in file.lower():
    print("application/zip")
else:
    print("application/octet-stream")
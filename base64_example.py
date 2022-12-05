# Base64 is a popular method to get binary data into ASCII characters, which is widely understood by the majority of networks and applications.
import base64


# Encode a string to base64

# Raw string
raw_string = "testing that <b>this gets</b> encoded to base64"
print(raw_string)

# Convert ASCII string into bytes
raw_bytes = raw_string.encode('utf-8')
print(raw_bytes)

# Base64 encode the bytes
base64_bytes = base64.b64encode(raw_bytes)
print(base64_bytes)

# Convert bytes into ASCII string
base64_string = base64_bytes.decode('utf-8')
print(base64_string)


# Decode a base64 string

# Base64 ASCII string
base64_string = base64_string
print(base64_string)

# Convert string into bytes
base64_bytes = base64_string.encode('utf-8')
print(base64_bytes)

# Decode the bytes
raw_bytes = base64.b64decode(base64_bytes)
print(raw_bytes)

# Convert bytes into string
raw_string = raw_bytes.decode('utf-8')
print(raw_string)

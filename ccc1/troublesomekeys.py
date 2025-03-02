keys = input()
output = input()

silly_key = ""
wrong_letter = ""
quiet_key = "-"

for i in range(len(keys)):
    if i < len(output) and keys[i] != output[i]:
        silly_key = keys[i]
        wrong_letter = output[i]
if keys[-1] != output[-1] and not keys.__contains__(output[-1]):
    silly_key = keys[-1]
    wrong_letter = output[-1]

keys_without_silly = keys.replace(silly_key, "")

for key in keys_without_silly:
    if key not in output:
        quiet_key = key
        break

print(f"{silly_key} {wrong_letter}")
print(quiet_key)

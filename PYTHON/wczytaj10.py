string = "1,2,3,4,5,6,7,8,9,10,11"
start = string.find("1")
end = string.find("11") + 1
print("Numer:", string.find("5", start, end))
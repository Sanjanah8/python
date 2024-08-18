text = "Hello, World!"
vowels = 'aeiouAEIOU'
count = sum(1 for char in text if char in vowels)
print("Vowels Count:", count)

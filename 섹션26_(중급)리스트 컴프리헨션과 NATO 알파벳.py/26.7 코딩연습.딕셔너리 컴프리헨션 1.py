sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above ๐

# Write your code below:
# split๋ฉ์๋๋ ๋ฌธ์์ด์ ๊ณต๋ฐฑ์ ๊ธฐ์ค์ผ๋ก ๋๋ ์ ๋ฆฌ์คํธ์ ๋ฃ๋๋ค.
result = {word :len(word) for word in sentence.split()}
print(result)
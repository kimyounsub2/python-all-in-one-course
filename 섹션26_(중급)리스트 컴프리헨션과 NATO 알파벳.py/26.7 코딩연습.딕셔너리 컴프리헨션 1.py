sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:
# split메소드는 문자열을 공백을 기준으로 나눠서 리스트에 넣는다.
result = {word :len(word) for word in sentence.split()}
print(result)
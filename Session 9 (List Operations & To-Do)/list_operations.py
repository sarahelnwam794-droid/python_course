
scores = [85, 92, 78, 95, 88]

print(f"All Scores: {scores}")


print(f"Total number of scores: {len(scores)}")

print(f"Sorted scores: {sorted(scores)}")

print(f"Sorted from high to low: {sorted(scores, reverse=True)}")

for score in scores:

    print(f"Student score is: {score}")


if 92 in scores:

    print("Great! The score 93 exists in the list.")

else:
    
    print("\nScore 93 not found.")
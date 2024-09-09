currentrating = float(input("Current rating: "))
averagerating = float(input("Average opponent rating: "))
rounds = int(input("Number of rounds: "))
pts = float(input("Points: "))
while pts - 0.5 != int(pts) and pts != int(pts):
    print("Enter a score that is (whole number + .5) or a whole number!")
    pts = float(input("Points: "))
if pts == rounds:
    pts -= 0.25
if pts == 0:
    pts += 0.25
def chessrating(rating, opponent, rounds):
    playera = rating / 400
    ratinga = pow(10, playera)
    opponentb = opponent / 400
    ratingb = pow(10, opponentb)
    expected = ratinga / (ratinga + ratingb)
    expected = expected * rounds
    return expected
def performance(opponent, rounds, points):
    rating = 0
    while True:
        playera = rating / 400
        ratinga = pow(10, playera)
        opponentb = opponent / 400
        ratingb = pow(10, opponentb)
        expected = ratinga / (ratinga + ratingb)
        expected = expected * rounds
        if points >= expected:
            rating += 1
        elif points < expected:
            rating -= 1
            playera = rating / 400
            ratinga = pow(10, playera)
            opponentb = opponent / 400
            ratingb = pow(10, opponentb)
            expected = ratinga / (ratinga + ratingb)
            expected = expected * rounds
            if points >= expected:
                break
    return rating
print(chessrating(currentrating, averagerating, rounds))
print(performance(averagerating, rounds, pts))
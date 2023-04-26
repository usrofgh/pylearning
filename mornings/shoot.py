def shoot(results: list) -> str:
    p1_count = 0
    p2_count = 0

    for round_ in results:
        p1_count += round_[0]["P1"].count("X") * (1 + int(round_[1]))
        p2_count += round_[0]["P2"].count("X") * (1 + int(round_[1]))
    
    if p1_count > p2_count:
        return "Pete Wins!"
    elif p1_count < p2_count:
        return "Phil Wins!"
    return "Draw!"

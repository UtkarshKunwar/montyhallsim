import argparse
import random


def runSim(prob=1, iteration=None, verbose=False):
    # Setup experiment
    doors = (1, 2, 3)
    prize_door = random.choice(doors)
    no_prize_door = [door for door in doors if door != prize_door]

    # Make door choice
    choice_door = random.choice(doors)

    # Host reveals a door
    reveal_door = [door for door in no_prize_door if door != choice_door][0]
    remaining_door = [door for door in doors if door not in (
        choice_door, reveal_door)][0]

    # Probability of switching

    if random.random() < prob:
        new_door = remaining_door
        switched = True
    else:
        new_door = choice_door
        switched = False

    if new_door == prize_door:
        result = "win"
    else:
        result = "lose"

    if verbose:
        print(f"[{iteration}] Prize {prize_door}, chose {choice_door}, revealed {reveal_door}, switched {switched}, result {result}")

    return result


def runAllSims(num_sims: int):
    wins = 0

    for i in range(num_sims):
        result = runSim(prob=args["switch_prob"],
                        iteration=i + 1, verbose=args["verbose"])

        if result == "win":
            wins += 1

    print(f"Total wins = {wins}")
    print(f"Probability of winning {wins/num_sims}")


def main(args):
    print(f"Running {args['num_sims']} simulations...")
    runAllSims(args['num_sims'])
    print(f"Finished running {args['num_sims']} simulations.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Monty Hall simulator.")
    parser.add_argument(
        "-n",
        "--num_sims",
        type=int,
        default=1000,
        help="Number of simulations to run.")
    parser.add_argument("-sp", "--switch_prob", type=float,
                        default=1.0, help="Probability of switching doors.")
    parser.add_argument("-v", "--verbose",
                        action="store_true", help="Verbose output.")
    args = vars(parser.parse_args())
    main(args)

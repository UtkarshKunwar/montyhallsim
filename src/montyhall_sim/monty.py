import argparse
import random
from typing import Any, Dict, Optional


class MontyHall:
    def __init__(self, choice_door: int = 1, switch_prob: float = 1.0) -> None:
        self.choice_door = choice_door
        self.switch_prob = switch_prob
        self.all_doors = (1, 2, 3)
        self._prize_door = random.choice(self.all_doors)
        self._no_prize_doors = [
            door for door in self.all_doors if door != self._prize_door
        ]

    @property
    def isPrizeDoor(self) -> bool:
        return self.choice_door == self._prize_door

    def revealDoor(self) -> None:
        self.reveal_door = [
            door for door in self._no_prize_doors if door != self.choice_door
        ][0]
        self.remaining_door = [
            door
            for door in self.all_doors
            if door not in (self.choice_door, self.reveal_door)
        ][0]

    def switchOrNot(self):
        if random.random() < self.switch_prob:
            self.choice_door = self.remaining_door
            self.switched = True
        else:
            self.switched = False

    def run(self) -> None:
        self.revealDoor()
        self.switchOrNot()
        self.victory = self.isPrizeDoor


def runSim(
    initial_door: int = 1,
    prob: float = 1,
    iteration: Optional[int] = None,
    verbose: bool = False,
):
    montyhall = MontyHall(choice_door=initial_door, switch_prob=prob)
    montyhall.run()

    result = "win" if montyhall.victory else "lose"

    if verbose:
        print(
            (f"[{iteration}] Prize {montyhall._prize_door},"),
            (" chose {montyhall.choice_door},"),
            (" revealed {montyhall.reveal_door}, switched {montyhall.switched},"),
            (" result {result}"),
        )

    return result


def runAllSims(args: Dict[str, Any]) -> None:
    wins = 0

    for i in range(args["num_sims"]):
        initial_door = (
            1 if args["door_choice"] == "constant" else random.choice((1, 2, 3))
        )
        result = runSim(
            initial_door=initial_door,
            prob=args["switch_prob"],
            iteration=i + 1,
            verbose=args["verbose"],
        )

        if result == "win":
            wins += 1

    print(f"Total wins = {wins}")
    print(f"Probability of winning {wins/args['num_sims']}")


def main(args: Dict[str, Any]) -> None:
    print(f"Running {args['num_sims']} simulations...")
    runAllSims(args)
    print(f"Finished running {args['num_sims']} simulations.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Monty Hall simulator.")
    parser.add_argument(
        "-n", "--num_sims", type=int, default=1000, help="Number of simulations to run."
    )
    parser.add_argument(
        "-sp",
        "--switch_prob",
        type=float,
        default=1.0,
        help="Probability of switching doors.",
    )
    parser.add_argument(
        "-dc",
        "--door_choice",
        type=str,
        choices=["random", "constant"],
        default="random",
        help="Strategy of door initial door selection.",
    )
    parser.add_argument("-v", "--verbose", action="store_true", help="Verbose output.")
    args = vars(parser.parse_args())
    main(args)

from montyhall_sim.monty import MontyHall, runAllSims, runSim


def test_reveal(montyhall):
    initial_door = montyhall.choice_door
    montyhall.revealDoor()
    assert montyhall.remaining_door != initial_door
    assert montyhall.remaining_door != montyhall.choice_door


def test_switch(montyhall):
    initial_door = montyhall.choice_door
    montyhall.switchOrNot()
    assert montyhall.choice_door != initial_door
    assert montyhall.choice_door == montyhall.remaining_door


def test_result():
    assert runSim(initial_door=1, prob=1, iteration=1, verbose=False) in ["win", "lose"]


def test_all():
    assert (
        runAllSims(
            args={
                "num_sims": 1,
                "door_choice": "constant",
                "switch_prob": 1.0,
                "verbose": False,
            }
        )
        is None
    )

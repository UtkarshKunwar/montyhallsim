import pytest
from montyhall_sim.monty import MontyHall


@pytest.fixture(scope="session")
def montyhall():
    mh = MontyHall(choice_door=1, switch_prob=1.0)
    return mh

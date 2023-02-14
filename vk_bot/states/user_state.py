from vkwave.bots.fsm import State, FiniteStateMachine

user_state_machine = FiniteStateMachine()


class UserState:
    section = State('section')

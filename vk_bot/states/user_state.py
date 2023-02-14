from vkwave.bots.fsm import State, FiniteStateMachine

user_state_machine: FiniteStateMachine = FiniteStateMachine()


class UserState:
    """
    Класс описывающий состояние пользователя.
    Нужен для более корректной работы при диалоге
    с пользователем.
    """
    section: State = State('section')

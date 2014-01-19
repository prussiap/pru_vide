from fluidity import StateMachine, state, transition

class UiStateMachine(StateMachine):

  initial_state = 'main_menu'

  state('main_menu')
  state('setting_setpoint')
  state('setting_preset')
  state('config')

  transition(from_='main_menu', event='set_setpoint', to='setting_setpoint')
  transition(from_='main_menu', event='set_preset', to='setting_preset')
  transition(from_='main_menu', event='set_config', to='setting_config')
  transition(from_=['setting_setpoint', 'setting_preset'],
    event='send_temperature', to='main_menu')
  transition(from_='config', event='config_finished', to='main_menu')

  transition(from_=['setting_setpoint', 'setting_preset', 'config'],
  event='cancel', to='main_menu')


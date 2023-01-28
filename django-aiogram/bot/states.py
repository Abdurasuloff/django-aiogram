from aiogram.dispatcher.filters.state import State, StatesGroup

class FeedbackState(StatesGroup):
      body = State()

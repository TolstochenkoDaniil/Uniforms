import { createStore } from 'vuex';
import Discipline from './modules/Discipline.store';
import Forms from './modules/Forms.store';
import auth from './modules/auth.store';

const store = createStore({
  modules: {
    Discipline,
    Forms,
    auth
  }
});

export default store;
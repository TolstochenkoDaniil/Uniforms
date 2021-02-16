import { createStore } from 'vuex';
import discipline from './modules/discipline.store';
import university from './modules/university.store';
import forms from './modules/forms.store';
import form from './modules/form.store';
import auth from './modules/auth.store';

const store = createStore({
  modules: {
    university,
    discipline,
    forms,
    form,
    auth,
  }
});

export default store;